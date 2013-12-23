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

* Timeout option works for layout and transformation methods

* Build process and dependecies update (:ref:`details <indigo-1.1.12-build>`)

* Smiles includes cis-trans marks in rings including in canonical smiles (:ref:`details <indigo-1.1.12-smiles-cis-trans>`)

* Python 3 compatibility

* New method ``restoreUnambiguousHydrogens`` that tries to restore hydrogens if they can be determined. ``checkBadValance``, ``checkAmbiguousH`` and ``checkForConsistency`` methods calls ``restoreUnambiguousHydrogens`` first.

* cdxml format: text width estimation

* indigo-python: createSaver method to render or save into buffers (:ref:`details <indigo-1.1.12-saver>`)

* Structures rendering in grid can have multiline titles

* Linux distributive do not depent on GLIBC_2.14. Binary files can be used even on old versions of Linux.

* Multiline properties, empty properties are loaded from SDF file. ``rawData`` method includes properties too.

* SDF reader can read sdf.gz and files

**Bugfixes**:

* Various fixes in the transformation procedure.
* Fixed canvas estimation in the rendering methods.
* Indigo finalization method could affect other Indigo instances as well in Java
* ``foldHydrogens`` method mark other bond if that bond were marked
* Fixed issues in deserialization method if molecule cis-trans configuration was invalid
* Substructure matcher matchs N[C@H](O)S on C[C@@](N)(O)S
* Normalize method validates cis-trans after doing normalization
* Molfile with ISISHOST header are supported. Such molecules has empty molfile version.
* Layout did not respect cis-trans configuration in rare cases
* Memory leak in InChI to molecule conversion
* Monoisotpic mass computation fix
* SMARTS expressions can have multiple atom constraints for a single atom without explicit `and` operation. For example [!#1!#6].
* Fixed ``collapse`` option value for ``render-superatom-mode`` option.

*******
Details
*******

.. _indigo-1.1.12-smiles-cis-trans:

======================
Smiles cis-trans flags
======================

.. _indigo-1.1.12-bold-bonds:

==================================
Bold bonds detection and rendering
==================================

.. _indigo-1.1.12-saver:

=============
Generic saver
=============

.. _indigo-1.1.12-build:

=============
Build Process
=============

build process:

* indigo can be build with external cairo-gl and cairo-vg libraries
* findCairo
* findPixman
* MinGW 
* cairo-egl and cairo-glesv2 support added
* cairo: linking with libegl and libglesv2
* cairo updated to 1.126; pixman updated to 0.30.2
* Visual Studio 2013 and OS X Mavericks support added
* indigo-java: source and target set to 1.5
