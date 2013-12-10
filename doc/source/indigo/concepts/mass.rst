.. _mass:

==================================
Different Mass Computation Methods
==================================

There are three different methods to compute molecule mass in Indigo:

 * ``molecularWeight`` -- returns the molecular weight (molecular mass), i.e. the average mass of all the isotopic compositions for a given structure.
 * ``mostAbundantMass`` --  returns the "most abundant isotopes mass", i.e. the mass of a most common isotopic composition.
 * ``monoisotopicMass`` --  returns the monoisotopic mass, i.e. the mass of structure where the most abundant isotope is used for all atoms.

On a small molecules the methods ``mostAbundantMass`` and ``monoisotopicMass`` returns the same results. But on a large molecules,
or on a molecules with atoms that have more than one stable isotope (like Chlorine) these methods returns different results.

************
Real example
************

For example, let's look at the structure with `ChemSpider ID = 370269 <http://www.chemspider.com/Chemical-Structure.370269.html>`_:

.. indigorenderer::
    :indigoobjecttype: code
    :indigoloadertype: code
    :nocode:

    m = indigo.loadMoleculeFromFile('data/csid-370269.mol')
    # Render the structure
    indigo.setOption("render-bond-length", 12.0)
    indigo.setOption("render-coloring", True)
    indigoRenderer.renderToFile(m, "result.png")

The following code computed molecule formula and three difference masses:

.. indigorenderer::
    :indigoobjecttype: code
    :indigoloadertype: code
    :downloads: data/csid-370269.mol
    :noimage:

    m = indigo.loadMoleculeFromFile('data/csid-370269.mol')

    print "Molecule formula:", m.grossFormula(), "\n"

    print "molecularWeight = ", m.molecularWeight()
    print "mostAbundantMass =", m.mostAbundantMass()
    print "monoisotopicMass =", m.monoisotopicMass()

All three masses are different and this can be illustrated on the isotope distribution plot for this structure [#fiso]_.
Each peak on this plot corresponds to single isotopic composition:

.. indigorenderer::
    :indigoobjecttype: code
    :indigoloadertype: code
    :includecodefile: data/mass-spec-plot.py
    :format: png

Molecule masses are the following:

  * ``molecularWeight`` is the sum of the standard atomic weights of all the atoms (if isotope is not specified), and it is the same as the weighted sum of
    all the peak values multiplied by peak abundance.
  * ``mostAbundantMass`` corresponds to the highest peak.
  * ``monoisotopicMass`` corresponds to a peak with default atom isotopes

*****************
Synthetic example
*****************

Difference of these masses can be explained on another example with a structure with 1000 Carbon atoms (without Hydrogens).
There are two relevant carbon isotopes: 12C with 98.9% natural abundance, and 13C with 1.1%.

  * ``molecularWeight`` = 1000 * M\ :sub:`C`\
  * ``mostAbundantMass`` = 989 * M\ :sub:`12C`\ + 11 * M\ :sub:`13C` [#fmostab]_
  * ``monoisotopicMass``  = 1000 * M\ :sub:`12C`\

.. indigorenderer::
    :indigoobjecttype: code
    :indigoloadertype: code
    :nocode:
    :noimage:
    :nooutputtitle:

    m = indigo.createMolecule()
    for i in range(1000):
        m.addAtom("C")
    for i in range(1000):
        m.getAtom(i).addBond(m.getAtom((i + 1) % 1000), 2)

    print "molecularWeight = ", m.molecularWeight()
    print "mostAbundantMass =", m.mostAbundantMass()
    print "monoisotopicMass =", m.monoisotopicMass()

***********
Source data
***********

Natural abundance, standard atomic weight, and relative atomic masses are taken from the `NIST Atomic Weights and Isotopic Compositions Database <http://www.nist.gov/pml/data/comp.cfm>`_.

.. rubric:: Footnotes

.. [#fiso] Data is computed using the isotopes distribution online calculator `Isotope Distribution Calculator and Mass Spec Plotter service <http://www.sisweb.com/mstools/isotope.htm>`_ from Scientific Instruments Services
.. [#fmostab] If we pick 1000 random Carbon atoms that forms a structure, then with a high probability there will be 989 of :sup:`12`\C atoms, and 11 of :sup:`13`\C atoms
