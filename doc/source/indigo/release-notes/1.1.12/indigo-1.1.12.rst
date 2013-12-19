.. _indigo-1.1.12-release-notes:

#############
Indigo 1.1.12
#############

:Date: 20 Nov 2013

*******
Summary
*******
    

**New features and improvements**:

* GLIBC_2.14 dependency excluded

* indigo: transformations: some bugs fixed, transform layout option added + simple transforms can be performed without  layout

* timeouts for layout and transformations

* :ref:`Bold bonds detection <indigo-1.1.12-bold-bonds>`

* :ref:`Build process and dependecies update <indigo-1.1.12-build>`

* :ref:`Smiles now includes cis-trans marks in rings including in canonical smiles <indigo-1.1.12-smiles-cis-trans>`

* Python 3 compatibility

* Transfromation calls layout only for complicated reactions

* indigo-core: new methods restoreUnambiguousHydrogens that tries to restore hydrogens if they can be determined (c1ccncc1). checkBadValance, CheckAmbiguousH and checkForConsistency methods calls restoreUnambiguousHydrogens first.

* cdxml format: text width estimation

* indigo-python: createSaver method to render or save into buffers

**Bugfixes**:

* indigo: transformations: some bugs fixed [cite...]
* SDF loader: multiline properties, empty properties, RawData includes properties too
* rendering: fixed canvas estimation
* indigo-java fix: Indigo finalization method could affect other Indigo instances as well
* SDF reader can read sdf.gz and files
* Fixed: foldHydrogens method mark other bond if that bond were marked
* Various fixes in transformations in reaction product enumeration (example for that?)
* Bug in deserialization if molecule cis-trans configuration was invalid
* substructure matcher: * indigo-core: allow to match N[C@H](O)S on C[C@@](N)(O)S
* indigo-api: normalize method validates cis-trans after doing normalization
* indigo-core: molfile loaded treats empty molfile version as V2000 because there were such file with  ISISHOST header [IND-597]

TODO:

    New methods:
        isMolecule

        Read other

    Examples:

        1. how to use C++ modules with Cmake

        2. Highlight matchings + align them

        3. Generic MCS with C++

*******
Details
*******

:ref:`Bold bonds detection <indigo-1.1.12-bold-bonds>`

.. _indigo-1.1.12-build:

=============
Build Process
=============

build process:
*  indigo can be build with external cairo-gl and cairo-vg libraries
* findCairo
* findPixman
* MinGW 
* cairo-egl and cairo-glesv2 support added
* cairo: linking with libegl and libglesv2
* cairo updated to 1.126; pixman updated to 0.30.2
* Visual Studio 2013 and OS X Mavericks support added
* indigo-java: source and target set to 1.5

.. _indigo-1.1.12-smiles-cis-trans:

======================
Smiles cis-trans flags
======================

.. _indigo-1.1.12-bold-bonds:

==================================
Bold bonds detection and rendering
==================================



