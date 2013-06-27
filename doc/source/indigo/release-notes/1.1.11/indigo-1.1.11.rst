.. _indigo-1.1.11-release-notes:

#############
Indigo 1.1.11
#############

:Date: 26 June 2013

*******
Summary
*******
    
**New features and improvements**:

 * Fingerprints computation is 2-4 times faster
 * Restored source compatibility with MinGW compiler
 * :ref:`New IndigoObject methods for stereocenters: <indigo-1.1.11-stereocenters-methods>`: ``stereocenterGroup``, ``setStereocenterGroup``, ``markStereobonds``
 * :ref:`New option to specify atom colors individually via s-groups<indigo-1.1.11-atom-coloring>`: ``render-atom-color-property`` 
 * :ref:`New rendering option for bond width <indigo-1.1.11-bond-width>`: ``render-bond-line-width``
 * :ref:`New chirality validation method <indigo-1.1.11-chirality-validation>`: ``validateChirality`` [#fchiral]_
 * Indigo Java API uses Maven instead of Ant for building
 * :ref:`Maven repository for Indigo Java API packages <indigo-1.1.11-maven>`
 * New method that releases memory for the Indigo Object: ``dispose`` 
 * Indigo Java doesn't remove dll-modules in the temporary directory that results in a faster loading 
 * :ref:`CDXML file format export <indigo-1.1.11-cdxml>`
 * :ref:`New methods to read data from buffers <indigo-1.1.11-buffers>`: ``loadBuffer``, ``loadString``, ``iterateSDF``, ``iterateSmiles``, ``iterateCML``, ``iterateSmiles``
 * Indigo Python API binding works for Python 3
 * :ref:`New SGroup-related methods <indigo-1.1.11-sgroups>`: ``getGenericSGroup``, ``getMultipleGroup``, ``getRepeatingUnit``, ``data``
 
**Bugfixes**:

 * Memory leak in the ``grossFormula`` API method in case of exceptions during computation
 * Molfile substitution flag value was set to 4 instead of 6
 * ``render-bond-length`` option was ignored if ``render-image-size`` were set. Now ``render-bond-length`` 
   parameter specifies maximum bond length even if image size is specified
 * Either cis-trans flag was ignored in Molfile V3000 loader
 * Indigo options may be used from a previous Indigo instance when new Indigo instance is allocated
 * Transform ...
 * C# dll loader pull request...
 
*******
Details
*******

.. _indigo-1.1.11-maven:

========================
Maven Central Repository
========================

All the Indigo Java packages are uploaded to `The Central Respository <http://maven.org>`_.

======================   ===============
GroupId                  ArtifactId
======================   ===============
com.ggasoftware          indigo
com.ggasoftware.indigo   indigo-inchi
com.ggasoftware.indigo   indigo-renderer
======================   ===============

Just add a dependency to your Maven project to download Indigo Java API automatically::

    <dependencies>
        ...
        <dependency>
            <groupId>com.ggasoftware</groupId>
            <artifactId>indigo</artifactId>
            <version>1.1.11</version>
        </dependency>
        ...
    </dependencies>

======================
Core Indigo API module
======================
 
.. _indigo-1.1.11-stereocenters-methods:

---------------------
Stereocenters methods
---------------------

There are new ``stereocenterGroup`` and ``setStereocenterGroup`` method to get/set stereocenter group:
 
.. indigorenderer::
    :indigoobjecttype: code
    :indigoloadertype: code
    :downloads: data/stereogroups.mol

    # Load structure
    m = indigo.loadMoleculeFromFile('data/stereogroups.mol')
    indigo.setOption('render-comment', 'Before')
    indigoRenderer.renderToFile(m, 'result_1.png')
    
    for s in m.iterateStereocenters():
        print "atom index =", s.index(), "group =", s.stereocenterGroup()
        
    m.getAtom(1).changeStereocenterType(Indigo.OR)
    m.getAtom(1).setStereocenterGroup(1)
    m.getAtom(5).setStereocenterGroup(1)
    indigo.setOption('render-comment', 'Stereocenter groups and types were changed')
    indigoRenderer.renderToFile(m, 'result_2.png')
    
The ``markStereobonds`` method set up/down bond marks if a stereoconfiguration were changed manually, or if it should be reset:
    
.. indigorenderer::
    :indigoobjecttype: code
    :indigoloadertype: code
    :downloads: data/stereobonds.mol

    m = indigo.loadMoleculeFromFile('data/stereobonds.mol')
    indigo.setOption('render-comment', 'Before')
    indigoRenderer.renderToFile(m, 'result_1.png')
    
    m.markStereobonds()
    
    indigo.setOption('render-comment', 'After')
    indigoRenderer.renderToFile(m, 'result_2.png')


.. _indigo-1.1.11-chirality-validation:

--------------------
Chirality validation
--------------------

Molecule can have a chirality flag even if it not chiral. There is a new ``validateChirality`` that checks 
if a molecule matches to its mirror and clears chirality flag in this case [#fchiral]_.

.. indigorenderer::
    :indigoobjecttype: code
    :indigoloadertype: code

    m = indigo.loadMolecule("C[C@@H]1C[C@H](C)C[C@@H](C)C1")
    indigo.setOption('render-comment', 'Before')
    indigoRenderer.renderToFile(m, 'result_1.png')
    print("Before: " + m.smiles())
    
    m.validateChirality()
    
    indigo.setOption('render-comment', 'After')
    indigoRenderer.renderToFile(m, 'result_2.png')
    print("After:  " + m.smiles())

.. _indigo-1.1.11-sgroups:

--------------
SGroup methods
--------------
    
  * getGenericSGroup(int index), getMultipleGroup(int index), getRepeatingUnit(int index),
  * data() returns SGroup data information    
  
.. _indigo-1.1.11-buffers:

-------
Buffers
-------

.. _indigo-1.1.11-cdxml:

----------
CDX Export
----------
    
Chriality

Pages

Grid    

Test comments    
    
================
Rendering module
================

.. _indigo-1.1.11-atom-coloring:

-------------
Atom coloring
-------------

Indigo can use a specified color for each atom and interpolate these colors for bond rendering.

.. indigorenderer::
    :indigoobjecttype: code
    :indigoloadertype: code

    # Load structure
    m = indigo.loadMolecule('CC(=C)C1=C(C)C(C)=CC(O)=C1NCCCCC=O')
    
    # Add data sgroups with 'color' description
    m.addDataSGroup([0, 1, 2, 3], [], "color", "0.155, 0.55, 0.955")
    m.addDataSGroup([4, 5, 6, 16, 17, 18], [], "color", "0.955, 0.155, 0.155")
    
    indigo.setOption("render-atom-color-property", "color")
    indigo.setOption('render-coloring', False)
    indigoRenderer.renderToFile(m, 'result.png')

For a larger example see :ref:`indigo-example-atom-coloring`.

.. _indigo-1.1.11-bond-width:

---------------
Bond line width
---------------

.. indigorenderer::
    :indigoobjecttype: code
    :indigoloadertype: code

    m = indigo.loadMolecule('CC1=C(Cl)C=CC2=C1NS(=O)S2')
    
    # Default visualization
    indigo.setOption('render-comment', 'default')
    indigoRenderer.renderToFile(m, 'result_1.png')

    # Bonds are twice thicker
    indigo.setOption('render-bond-line-width', 2.0)
    indigo.setOption('render-comment', 'render-bond-line-width=2.0')
    indigoRenderer.renderToFile(m, 'result_2.png')
    
    # Bonds are twice thinner
    indigo.setOption('render-bond-line-width', 0.5)
    indigo.setOption('render-comment', 'render-bond-line-width=0.5')
    indigoRenderer.renderToFile(m, 'result_3.png')

.. rubric:: Footnotes

.. [#fchiral] Suggested by Marcin: https://groups.google.com/d/msg/indigo-general/A8VtF-51viw/E093AE-b-pwJ
