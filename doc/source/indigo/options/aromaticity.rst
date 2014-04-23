###################
Aromaticity options
###################

.. indigo_option::
    :name: aromaticity-model
    :type: enum
    :default: basic
    :short: Aromaticity model

    Aromaticity model used in aromatization and dearomatization procedures. Supported values:

    **basic**:
        External double bond for aromatic rings are not allowed

    **generic**
        External double bond are allowed


.. indigorenderer::
    :indigoobjecttype: code
    :indigoloadertype: code

    m = indigo.loadMolecule('O=c1[nH]c(nc2c1CSCC2)c1ccc(cc1)C(F)(F)F')

    indigo.setOption("render-comment", "Aromatized")
    indigoRenderer.renderToFile(m, "result_1.png")

    indigo.setOption("aromaticity-model", "basic")
    m.dearomatize()
    indigo.setOption("render-comment", "Dearomatized (basic)")
    indigoRenderer.renderToFile(m, "result_2.png")

    indigo.setOption("aromaticity-model", "generic")
    m.dearomatize()
    indigo.setOption("render-comment", "Dearomatized (generic)")
    indigoRenderer.renderToFile(m, "result_3.png")

    

.. indigo_option::
    :name: dearomatize-verification
    :type: boolean
    :default: true
    :short: Verify dearomatization method

    In the dearomatization method Indigo enumerates possible single/double bonds configurations and checks that such configuration is aromatic. If there are no valid dearomatization for a given aromatic system, then Indigo leaves such aromatic system unchanged. With this option disabled Indigo dearomatizes such aromatic system, but without guarantee that this dearomatization is correct. It can be used to convert antiaromatic rings:

.. indigorenderer::
    :indigoobjecttype: code
    :indigoloadertype: code

    m = indigo.loadMolecule('c1ccccccc1')

    indigo.setOption("render-comment", "Original\nstructure")
    indigoRenderer.renderToFile(m, "result_1.png")

    m.dearomatize()
    indigo.setOption("render-comment", "Dearomatized with\nverification")
    indigoRenderer.renderToFile(m, "result_2.png")

    indigo.setOption("dearomatize-verification", False)
    m.dearomatize()
    indigo.setOption("render-comment", "Dearomatized without\nverification")
    indigoRenderer.renderToFile(m, "result_3.png")


.. indigo_option::
    :name: unique-dearomatization
    :type: boolean
    :default: false
    :short: Find dearomatization if all possible configurations uniquely define hydrogens.

    Molfile format doesn't store information about hydrogens in aromatic rings and this leads to a situation when two different (tautomers) structure has the same aromatization.

    .. code::
        :hidden:
        :name: code-unique-dearomatization

        m1 = indigo.loadMoleculeFromFile('data/ambiguous_arom1.mol')
        m2 = indigo.loadMoleculeFromFile('data/ambiguous_arom2.mol')

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code
        :includecode: code-unique-dearomatization
        :nocode:

        indigo.setOption("render-comment", "(A)")
        indigoRenderer.renderToFile(m1, "result_1.png")
        indigo.setOption("render-comment", "(B)")
        indigoRenderer.renderToFile(m2, "result_2.png")

    Molecules (A) and (B) are different, and aromatic forms are the following:

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code
        :includecode: code-unique-dearomatization
        :nocode:

        m1.aromatize()
        m2.aromatize()

        indigo.setOption("render-comment", "(A)")
        indigoRenderer.renderToFile(m1, "result_1.png")
        indigo.setOption("render-comment", "(B)")
        indigoRenderer.renderToFile(m2, "result_2.png")

    Such aromatic molecules can be dearomatized, all atoms has specific number of implicit hydrogens and we can compute canonical SMILES:

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code
        :includecode: code-unique-dearomatization
        :nocode:
        :noimage:
        :nooutputtitle:

        m1.aromatize()
        m2.aromatize()
        print("(A): " + m1.canonicalSmiles())
        print("(B): " + m2.canonicalSmiles())

    Let's consider that we loaded a molecule (A) or (B) in an aromatic form from molfile. If explicit hydrogens are not saved into molfile then we get the following structure:

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code
        :nocode:

        m3 = indigo.loadMoleculeFromFile('data/ambiguous_arom3.mol')

        indigo.setOption("render-comment", "(C)")
        indigoRenderer.renderToFile(m3, "result_3.png")

    Canonical SMILES computation throws an exception on such molecule because we cannot decided if it is (A) or (B).

    Dearomtization method by default doesn't check uniqueness in terms of number of Hydrogens:

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code

        m3 = indigo.loadMoleculeFromFile('data/ambiguous_arom3.mol')
        m3.dearomatize()

        indigo.setOption("render-comment", "(C)")
        indigoRenderer.renderToFile(m3, "result_3.png")


    But such check it can be set explicitly if needed, and dearomatize method will throw an exception in this case:

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code
        :nooutputtitle:
        :noimage:

        m3 = indigo.loadMoleculeFromFile('data/ambiguous_arom3.mol')

        indigo.setOption("unique-dearomatization", True)

        try:
            m3.dearomatize()
        except IndigoException, ex:
            print(str(ex))

    But we still can dearomatize structures if number if hydrogens is uniquely defined:

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code
        :nooutputtitle:
        :downloads: data/ambiguous_arom4.mol

        m = indigo.loadMoleculeFromFile('data/ambiguous_arom4.mol')
        indigoRenderer.renderToFile(m, "result_1.png")

        indigo.setOption("unique-dearomatization", True)

        m.dearomatize()
        indigoRenderer.renderToFile(m, "result_2.png")
