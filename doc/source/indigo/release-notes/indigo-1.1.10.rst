.. _indigo-1.1.10-release-notes:

#############
Indigo 1.1.10
#############

Last commit:

    | Revision: 6de4d98cfede30fd848188e9358a0a906246cfc2
    | Author: Mikhail Rybalkin <rybalkin@ggasoftware.com>
    | Date: 4/26/2013 14:29:19
    | Message:
    | indigo-api: new methods: stereocenterGroup, setStereocenterGroup, markStereobonds

**********************
Core Indigo API module
**********************

=============================
New features and improvements
=============================

 * Fingerprints computation is 2-4 times faster
 * Restored source compatibility with MinGW compiler

======== 
Bugfixes
========

 * Memory leak in the `grossFormula` API method in case of exceptions during computation
 * Molfile substitution flag value was set to 4 instead of 6
 
=====================
Stereocenters methods
=====================

stereocenterGroup, setStereocenterGroup, markStereobonds 
 
.. indigorenderer::
    :indigoobjecttype: code
    :indigoloadertype: code

    # Load structure
    m = indigo.loadMoleculeFromFile('data/stereogroups.mol')
    print m.smiles()
    indigoRenderer.renderToFile(m, 'result_1.png')
    m2 = indigo.loadMolecule('C1=C(O)C=CN=C1CN')
    print m2.smiles()
    indigoRenderer.renderToFile(m2, 'result_2.png')
    m3 = indigo.loadMolecule('C1=CN(O)C=CN=C1CN')
    print m3.smiles()
    indigoRenderer.renderToFile(m3, 'result_3.png')

 
****************
Rendering module
****************

========
Bugfixes
========

 * `render-bond-length` were disabled if `render-image-size` were set. Now `render-bond-length` 
   parameter specifies maximum bond length even if image size is specified


=============
Atom coloring
=============

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

===============
Bond line width
===============

.. indigorenderer::
    :indigoobjecttype: code
    :indigoloadertype: code

    m = indigo.loadMolecule('CC1=C(Cl)C=CC2=C1NS(=O)S2')
    
    # Default visualization
    indigo.setOption('render-comment', 'default')
    indigoRenderer.renderToFile(m, 'result.png')

    # Bonds are twice thicker
    indigo.setOption('render-bond-line-width', 2.0)
    indigo.setOption('render-comment', 'render-bond-line-width=2.0')
    indigoRenderer.renderToFile(m, 'result.png')
    
    # Bonds are twice thinner
    indigo.setOption('render-bond-line-width', 0.5)
    indigo.setOption('render-comment', 'render-bond-line-width=0.5')
    indigoRenderer.renderToFile(m, 'result.png')

