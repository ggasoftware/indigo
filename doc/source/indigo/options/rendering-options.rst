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
    :name: render-output-format
    :type: string
    :default: -
    :short:
        Image file format.

    If this option is not set, then Indigo deduces image format from the file extension.
    Supported formats:
        - png
        - pdf
        - svg
        - emf (windows)
        - cdxml (not all options are supported)

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
        :nocode:

        renderMolfileWithOptions('data/render_example1.mol', 'render-coloring', [ True, False ])

.. indigo_option::
    :name: render-bond-length
    :type: integer
    :default: 100
    :short:
        Desired average bond length in pixels

        The actual average bond length may be less if the ``render-image-size`` option is set. To reset this setting, you can set its value to -1. This option scales label size as well.

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code
        :includecode: render-with-different-options
        :nocode:

        renderMolfileWithOptions('data/render_example1.mol', 'render-bond-length', [ 10, 20, 40 ])

.. indigo_option::
    :name: render-image-size
    :type: size
    :default: -
    :short:
        Width and height of target image.

        If not set, is calculated automatically according to ``render-bond-length``. To reset this setting, you can set the values of width and height to -1.

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code
        :includecode: render-with-different-options
        :nocode:

        indigo.setOption("render-bond-length", -1)
        renderMolfileWithOptions('data/render_example1.mol', 'render-image-size', [ "300, 200", "200, 100" ])


.. indigo_option::
    :name: render-margins
    :type: size
    :default: -
    :short:
        Horizontal and vertical margins around the image, in pixels.

.. indigo_option::
    :name: render-base-color
    :type: coloring
    :default: black (0, 0, 0)
    :short:
        The default color for atoms and bonds.

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code
        :includecode: render-with-different-options
        :nocode:

        renderMolfileWithOptions('data/render_example1.mol', 'render-base-color', [ "0, 0, 1", "0.1, 0.7, 0.4" ])

.. indigo_option::
    :name: render-background-color
    :type: color
    :default: transparent
    :short:
        Background color.

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code
        :includecode: render-with-different-options
        :nocode:

        renderMolfileWithOptions('data/render_example1.mol', 'render-background-color', [ "0.8, 0.8, 0.8", "0.7, 1, 1" ])

    Combination of both ``render-background-color`` and ``render-base-color`` can be used to get negative:

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code

        m = indigo.loadMoleculeFromFile('data/render_example1.mol')

        indigo.setOption("render-background-color", "0, 0, 0")
        indigo.setOption("render-base-color", "1, 1, 1")

        indigoRenderer.renderToFile(m, "result.png")

.. indigo_option::
    :name: render-label-mode
    :type: enum
    :default: terminal-hetero
    :short:
        Atom label rendering mode

    **all**
        show all atoms

    **terminal-hetero**
        show heteroatoms, terminal atoms, atoms with radical, charge, isotope, explicit valence, and atoms having two adjacent bonds in a line

    **hetero**
        the same as terminal-hetero, but without terminal atoms

    **none**
        hide all labels, show only bonds

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code
        :includecode: render-with-different-options
        :nocode:

        renderMolfileWithOptions('data/render_example1.mol', 'render-label-mode', [ "all", "terminal-hetero", "hetero", "none" ])


.. indigo_option::
    :name: render-highlighted-atoms-visible
    :type: boolean
    :default: False
    :short:
        Always show labels of highlighted atoms.


.. indigo_option::
    :name: render-implicit-hydrogens-visible
    :type: boolean
    :default: True
    :short:
        Show implicit hydrogens on visible atoms.

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code
        :includecode: render-with-different-options
        :nocode:

        renderMolfileWithOptions('data/render_example2.mol', 'render-implicit-hydrogens-visible', [ True, False ])

.. indigo_option::
    :name: render-comment-font-size
    :type: integer
    :default: 20
    :short:
        Font size for the comment in absolute units, roughly equal to the height in pixels.

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code
        :includecode: render-with-different-options
        :nocode:

        renderMolfileWithOptions('data/render_example1.mol', 'render-comment-font-size', [ 15, 20, 25 ])

.. indigo_option::
    :name: render-comment-color
    :type: color
    :default: black
    :short:
        Color to use for the comment.

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code
        :includecode: render-with-different-options
        :nocode:

        renderMolfileWithOptions('data/render_example3.mol', 'render-comment-color', [ "0, 0, 0", "0, 0.4, 0.5" ])

.. indigo_option::
    :name: render-bond-line-width
    :type: float
    :default: 1.0
    :short:
        Relative bond line width

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code
        :includecode: render-with-different-options
        :nocode:

        renderMolfileWithOptions('data/render_example1.mol', 'render-bond-line-width', [ 0.5, 1, 2 ])


.. indigo_option::
    :name: render-relative-thickness
    :type: float
    :default: 1.0
    :short:
        Set the thickness of bonds and atom labels to X/30 of the average bond length.

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code
        :includecode: render-with-different-options
        :nocode:

        renderMolfileWithOptions('data/render_example1.mol', 'render-relative-thickness', [ 0.5, 1, 2 ])

.. indigo_option::
    :name: render-comment
    :type: string
    :default: 
    :short:
        Put a comment at the top or bottom of the image

     If the image size is set explicitly, it must not be smaller than the size of the comment bounding box.

     All the examples on this page contain comment with option value.

.. indigo_option::
    :name: render-comment-position
    :type: enum
    :default: bottom
    :short:
        top or bottom.

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code
        :includecode: render-with-different-options
        :nocode:

        renderMolfileWithOptions('data/render_example1.mol', 'render-comment-position', [ "top", "bottom" ])

.. indigo_option::
    :name: render-comment-offset
    :type: integer
    :default: 0
    :short:
        Vertical space (in pixels) between the comment and the rendered structure or reaction.

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code
        :includecode: render-with-different-options
        :nocode:

        renderMolfileWithOptions('data/render_example1.mol', 'render-comment-offset', [ 0, 10, 20 ])

.. indigo_option::
    :name: render-atom-ids-visible
    :type: boolean
    :default: False
    :short:
        Show atom numbers (for debugging purposes only).

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code
        :includecode: render-with-different-options
        :nocode:

        renderMolfileWithOptions('data/render_example3.mol', 'render-atom-ids-visible', [ True, False ])

.. indigo_option::
    :name: render-bond-ids-visible
    :type: boolean
    :default: False
    :short:
        Show bond numbers (for debugging purposes only).

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code
        :includecode: render-with-different-options
        :nocode:

        renderMolfileWithOptions('data/render_example3.mol', 'render-bond-ids-visible', [ True, False ])

.. indigo_option::
    :name: render-atom-bond-ids-from-one
    :type: boolean
    :default: False
    :short:
        Show atom and bond numbers starting from one, not from zero.


.. indigo_option::
    :name: render-aam-color
    :type: color
    :default: black
    :short: Atom-by-atom mapping indices color in reactions.

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code
        :includecode: render-with-different-options
        :nocode:

        rxn = indigo.loadReactionFromFile("data/amiderxn2.rxn")
        rxn.automap()
        renderWithOptions(rxn, "render-aam-color", ["0.1, 0.5, 0.7"] )

.. indigo_option::
    :name: render-atom-color-property
    :type: string
    :default: none
    :short: S-group name for atom colors

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

    See :ref:`indigo-example-atom-coloring` for a larger example.

.. indigo_option::
    :name: render-bold-bond-detection
    :type: -
    :default: -
    :short: -

.. indigo_option::
    :name: render-catalysts-placement
    :type: -
    :default: -
    :short: -

.. indigo_option::
    :name: render-center-double-bond-when-stereo-adjacent
    :type: -
    :default: -
    :short: -

.. indigo_option::
    :name: render-comment-alignment
    :type: -
    :default: -
    :short: -

.. indigo_option::
    :name: render-data-sgroup-color
    :type: -
    :default: -
    :short: -

.. indigo_option::
    :name: render-hdc-offset
    :type: -
    :default: -
    :short: -

.. indigo_option::
    :name: render-highlight-color
    :type: -
    :default: -
    :short: -

.. indigo_option::
    :name: render-highlight-color-enabled
    :type: -
    :default: -
    :short: -

.. indigo_option::
    :name: render-highlight-thickness-enabled
    :type: -
    :default: -
    :short: -

.. indigo_option::
    :name: render-highlighted-labels-visible
    :type: -
    :default: -
    :short: -

.. indigo_option::
    :name: render-image-height
    :type: -
    :default: -
    :short: -

.. indigo_option::
    :name: render-image-max-height
    :type: -
    :default: -
    :short: -

.. indigo_option::
    :name: render-image-max-width
    :type: -
    :default: -
    :short: -

.. indigo_option::
    :name: render-image-width
    :type: -
    :default: -
    :short: -

.. indigo_option::
    :name: render-stereo-style
    :type: -
    :default: -
    :short: -

.. indigo_option::
    :name: render-superatom-mode
    :type: -
    :default: -
    :short: -

.. indigo_option::
    :name: render-valences-visible
    :type: -
    :default: -
    :short: -

