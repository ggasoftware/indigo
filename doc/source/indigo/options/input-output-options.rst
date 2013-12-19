***************
Generic options
***************

.. indigo_option::
    :name: ignore-stereochemistry-errors
    :type: boolean
    :default: false
    :short: When reading a Molfile/Rxnfile with incorrectly marked stereobonds, ignore them rather than raise an error.

    Sometimes molecules contain stereobond marks that do not define stereocenters properly. It can be either mistake made by a user, or stereoconfiguration notation is not known to Indigo. Let's condside the following molecule:

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code
        :downloads: molecules/stereoerrors.mol
        :nocode:

        indigo.setOption("ignore-stereochemistry-errors", True)
        m = indigo.loadMoleculeFromFile('molecules/stereoerrors.mol')
        indigoRenderer.renderToFile(m, 'result.png')

    Stereobond near Oxygen atom is probably set in a wrong direction bny mistake, and when loaded with Indigo one gets an exception about invalid stereobonds configuration:

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code
        :downloads: molecules/stereoerrors.mol
        :noimage:

        # Load structure and get exception about stereocenters
        try:
            m = indigo.loadMoleculeFromFile('molecules/stereoerrors.mol')
        except IndigoException, ex:
            print("Exception: " + str(ex))

    To load this structure we can ignore such errors:

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code
        :codename: opt-ignore-stereo-load
        :noimage:

        indigo.setOption("ignore-stereochemistry-errors", True)
        m = indigo.loadMoleculeFromFile('molecules/stereoerrors.mol')

    All other valid stereocenters are loaded. All stereobond marks are also loaded even if they correspond to an invalid stereocenter. In the example below we see that ``layout`` methods marked only valid stereocenter.

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code
        :includecode: opt-ignore-stereo-load

        print("Smiles:\n" + m.smiles())

        indigo.setOption("render-comment", "Original")
        indigoRenderer.renderToFile(m, 'result_1.png')

        indigo.setOption("render-comment", "With bond indices")
        indigo.setOption("render-bond-ids-visible", True)
        indigoRenderer.renderToFile(m, 'result_2.png')
        indigo.setOption("render-bond-ids-visible", False)

        m.layout()
        indigo.setOption("render-comment", "After cleanup")
        indigoRenderer.renderToFile(m, 'result_3.png')

.. indigo_option::
    :name: ignore-noncritical-query-features
    :type: boolean
    :default: false
    :short: 
        When true, the "bond topology", "stereo care", "ring bond count", and "unsaturation" specifications are
        ignored when a non-query molecule is being loaded.

    Indigo has two kind of molecule object: molecule and query molecule. Query molecules represent patterns for ordinary molecules and they are used in substructure search. Many properties are not defined for query molecules, for example, implicit hydrogens count, because query molecule is a pattern. 

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code
        :downloads: molecules/noncritial_query.mol

        # Load structure and get exception about stereocenters
        query = indigo.loadQueryMoleculeFromFile('molecules/noncritial_query.mol')
        indigoRenderer.renderToFile(query, 'result.png')

    When such query molecule is loaded as ordinary molecule Indigo throws an exception about query features:

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code

        # Load structure and get exception about query features
        try:
            m = indigo.loadMoleculeFromFile('molecules/noncritial_query.mol')
        except IndigoException, ex:
            print("Exception: " + str(ex))

    To load such structure we have to set ``ignore-noncritical-query-features`` option.

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code

        indigo.setOption("ignore-noncritical-query-features", True)
        m = indigo.loadMoleculeFromFile('molecules/noncritial_query.mol')
        indigoRenderer.renderToFile(m, 'result.png')
