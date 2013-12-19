#################
Rendering options
#################

.. code::
    :name: render-with-different-options
    :hidden:

    def renderWithOptions (mol, name, optvalues, draw_default=False):
        if draw_default:
            indigo.setOption("render-comment", "default")
            indigoRenderer.renderToFile(mol, 'result.png')

        for idx, value in enumerate(optvalues):
            indigo.setOption(name, value)
            indigo.setOption("render-comment", "%s=%s" % (name, value))
            indigoRenderer.renderToFile(mol, 'result_%d.png' % (idx))

    def renderMolfileWithOptions (molfile, name, optvalues):
        mol = indigo.loadMoleculeFromFile(molfile)
        renderWithOptions(mol, name, optvalues)

.. indigo_option::
    :name: render-coloring
    :type: boolean
    :default: false
    :short: 
        Turn on atom coloring, e.g. nitrogen is blue, oxygen is red, etc.

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code
        :includecode: render-with-different-options
        :downloads: molecules/noncritial_query.mol
        :nocode:

        # Load structure and get exception about stereocenters
        renderMolfileWithOptions('molecules/render_example1.mol', 'render-coloring', [ True, False ])
