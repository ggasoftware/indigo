.. _mass:

==================================
Different Mass Computation Methods
==================================

On a small molecules the methods ``mostAbundantMass`` and ``monoisotopicMass`` returns the same results. But on a large molecules, 
or on a molecules with atoms that have more than one stable isotope (like Chlorine) these methods returns different results.

For example, let look at the structure with `ChemSpider ID = 370269 <http://www.chemspider.com/Chemical-Structure.370269.html>`_:

.. indigorenderer::
    :indigoobjecttype: code
    :indigoloadertype: code
    :nocode:

    m = indigo.loadMoleculeFromFile('data/csid-370269.mol')
    # Render the structure
    indigo.setOption("render-bond-length", 12.0)
    indigo.setOption("render-coloring", True)
    indigoRenderer.renderToFile(m, "result.png")
    
.. indigorenderer::
    :indigoobjecttype: code
    :indigoloadertype: code
    :downloads: data/csid-370269.mol
    :noimage:

    m = indigo.loadMoleculeFromFile('data/csid-370269.mol')
    
    print "Gross:", m.grossFormula(), "\n"
    
    print "molecularWeight = ", m.molecularWeight()
    print "mostAbundantMass =", m.mostAbundantMass()
    print "monoisotopicMass =", m.monoisotopicMass()

