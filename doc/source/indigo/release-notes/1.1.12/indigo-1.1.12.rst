.. _indigo-1.1.12-release-notes:

#############
Indigo 1.1.12
#############

:Date: 23 Dec 2013

*******
Summary
*******


**New features and improvements**:

* Bold bonds detection in the rendering procedure  (:ref:`details <indigo-1.1.12-bold-bonds>`)

* Transformation method do not change molecule layout for simple transformations.

* Timeout option works for layout and transformation methods [#f5]_

* Build process and dependencies update (:ref:`details <indigo-1.1.12-build>`)

* Smiles includes cis-trans marks in rings including in canonical smiles (:ref:`details <indigo-1.1.12-smiles-cis-trans>`)

* ``checkBadValance``, ``checkAmbiguousH`` methods try to find number of implicit hydrogens for aromatic molecules first. If molecule is aromatic then there is no need to dearomatize it first to check ambiguous hydrogens. See :optref:`unique-dearomatization` option that contains examples.

* cdxml format: text width estimation

* indigo-python: createSaver method to render or save into buffers (:ref:`details <indigo-1.1.12-saver>`)

* Rendering module supports multiline comments and titles. See :optref:`render-comment` and :optref:`render-grid-title-property` options.

* Linux distributive do not depend on GLIBC_2.14. Binary files can be used even on old versions of Linux.

* Multiline properties, empty properties are loaded from SDF file. ``rawData`` method includes properties too.

* SDF reader can read sdf.gz and files

**Bugfixes**:

* Various fixes in the transformation procedure [#f2]_
* Fixed canvas estimation in the rendering methods.
* Indigo finalization method could affect other Indigo instances as well in Java [#f1]_
* ``foldHydrogens`` method mark other bond if that bond were marked
* Fixed issues in deserialization method if molecule cis-trans configuration was invalid
* Substructure matcher matches N[C@H](O)S on C[C@@](N)(O)S
* Normalize method validates cis-trans after doing normalization
* Molfile with ISISHOST header are supported. Such molecules has empty molfile version.
* Layout did not respect cis-trans configuration in rare cases
* Memory leak in InChI to molecule conversion
* Monoisotpic mass computation fix [#f3]_
* SMARTS expressions can have multiple atom constraints for a single atom without explicit `and` operation. For example [!#1!#6]. [#f4]_
* Fixed ``collapse`` option value for ``render-superatom-mode`` option.
* Complete Python 3 compatibility

*******
Details
*******

.. _indigo-1.1.12-smiles-cis-trans:

======================
Smiles cis-trans flags
======================

Cis-trans bonds in rings are saved using SMILES extension with "c" and "t" fields.

.. indigorenderer::
    :indigoobjecttype: code
    :indigoloadertype: code

    m = indigo.loadMoleculeFromFile('data/macro.mol')

    indigoRenderer.renderToFile(m, "result.png")

    print(m.canonicalSmiles())

.. _indigo-1.1.12-bold-bonds:

==================================
Bold bonds detection and rendering
==================================

To depict Surgars Indigo can automatically detect where bold bond should be drawn:

.. indigorenderer::
    :indigoobjecttype: code
    :indigoloadertype: code
    :downloads: data/bold-bond2.mol

    m = indigo.loadMoleculeFromFile('data/bold-bond2.mol')

    indigo.setOption("render-comment", "With bold bonds")
    indigoRenderer.renderToFile(m, "result_1.png")

    indigo.setOption('render-bold-bond-detection', False)

    indigo.setOption("render-comment", "Original")
    indigoRenderer.renderToFile(m, "result_2.png")

.. _indigo-1.1.12-saver:

=============
Generic saver
=============

Python bindings has a new method `createSaver` that can be used to save chemical structures into buffers.

.. indigorenderer::
    :indigoobjecttype: code
    :indigoloadertype: code

    # Create molecules and set their names
    m1 = indigo.loadMolecule('[H][C@](C)(N)O')
    m1.setName("Molecule 1")
    m2 = indigo.loadMolecule('C1=CC=CC=C1')
    m2.setName("Molecule 2")

    # Create string stream and save molecules in SMILES format into it
    buffer = indigo.writeBuffer()
    # Instead of "smi" one can use "sdf", "cml", "rdf"
    saver = indigo.createSaver(buffer, "smi")
    saver.append(m1)
    saver.append(m2)

    print(buffer.toString())


.. _indigo-1.1.12-build:

=============
Build Process
=============


* Visual Studio 2013 and OS X Mavericks support added.
* Indigo-java: source and target compatibility versions set to Java 1.5.
* Third party libraries: Cairo updated to 1.126; Pixman updated to 0.30.2; Cairo can be built with cairo-gl, cairo-vg, cairo-egl and cairo-glesv2 support.

.. rubric:: Footnotes

.. [#f1] Bug report by Joos: https://groups.google.com/d/msg/indigo-bugs/Vdzp0B26KsA/DehJm2QhW34J
.. [#f2] Bug report by Ken: https://groups.google.com/d/msg/indigo-general/6B-LlLR0Ppw/fvI1RM7CzWUJ
.. [#f3] Bug report by Oliver Kohlbacher: https://groups.google.com/d/msg/indigo-general/h6p9QxMuI_Q/4x2TckxWProJ
.. [#f4] Bug report by Oleg: https://groups.google.com/d/msg/indigo-general/D3P-TbZBnL0/oJEOM82i1lwJ
.. [#f5] Feature request by Ken: https://groups.google.com/d/msg/indigo-general/wK4eDGiOzJc/kgwc0mAH89YJ