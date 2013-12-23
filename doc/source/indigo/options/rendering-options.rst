#################
Rendering options
#################

.. code::
    :name: render-with-different-options
    :hidden:

    def renderWithOptions (mol, name, optvalues, draw_default=False, separator='='):
        if draw_default:
            indigo.setOption("render-comment", "default")
            indigoRenderer.renderToFile(mol, 'result.png')

        for idx, value in enumerate(optvalues):
            indigo.setOption("render-comment", "%s%s%s" % (name, separator, value))
            indigo.setOption(name, value)
            indigoRenderer.renderToFile(mol, 'result_%d.png' % (idx))

    def renderMolfileWithOptions (molfile, name, optvalues, draw_default=False, separator='='):
        mol = indigo.loadMoleculeFromFile(molfile)
        renderWithOptions(mol, name, optvalues, draw_default=draw_default, separator=separator)

    def renderRxnfileWithOptions (rxnfile, name, optvalues):
        rxn = indigo.loadReactionFromFile(rxnfile)
        renderWithOptions(rxn, name, optvalues)

.. indigo_option::
    :name: render-output-format
    :type: string
    :default: automatic
    :short:
        Image file format.

    If this option is not set, then Indigo deduces image format from the file extension.
    Supported formats:
    
    * png
    * pdf
    * svg
    * emf (windows)
    * cdxml (not all options are supported)

.. indigo_option::
    :name: render-image-size
    :type: size
    :default: auto
    :short:
        Width and height of target image.

        If not set, is calculated automatically according to ``render-bond-length``. To reset this setting, you can set the values of width and height to -1. This options defines both width and height that can be set independently via ``render-image-width`` and ``render-image-height`` options.

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code
        :includecode: render-with-different-options
        :nocode:

        indigo.setOption("render-bond-length", -1)
        renderMolfileWithOptions('data/render_example1.mol', 'render-image-size', [ "300, 200", "200, 100" ])

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
    :name: render-image-width
    :type: int
    :default: auto
    :short: Image width

.. indigo_option::
    :name: render-image-height
    :type: int
    :default: auto
    :short: Image height

.. indigo_option::
    :name: render-image-max-width
    :type: int
    :default: auto
    :short: Maximum image width

.. indigo_option::
    :name: render-image-max-height
    :type: int
    :default: auto
    :short: Maximum image height

.. indigo_option::
    :name: render-margins
    :type: size
    :default: auto
    :short:
        Horizontal and vertical margins around the image, in pixels.

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
    :name: render-comment
    :type: string
    :default: 
    :short:
        Put a comment at the top or bottom of the image

     If the image size is set explicitly, it must not be smaller than the size of the comment bounding box.

     All the examples on this page contain comment with option value.

     Comment can have multiple line:

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code
        :includecode: render-with-different-options
        :nocode:

        renderMolfileWithOptions('data/render_example1.mol', 'render-comment', [ "multiline\ncomment" ])

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
    :name: render-comment-alignment
    :type: enum
    :default: center
    :short: Comment alignment

    Supported values: left, right, center, center-left

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code
        :includecode: render-with-different-options
        :nocode:

        renderMolfileWithOptions('data/render_example4.mol', 'render-comment-alignment', [ 'left', 'right', 'center', 'center-left' ], separator='=\n')


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
    :type: boolean
    :default: true
    :short: Detect and draw bold bond for Haworth projection

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code
        :includecode: render-with-different-options
        :nocode:
        :downloads: data/bold-bond.mol

        renderMolfileWithOptions('data/bold-bond.mol', 'render-bold-bond-detection', [ True, False ])

.. indigo_option::
    :name: render-catalysts-placement
    :type: enum
    :default: above-and-below
    :short: Reaction catalysts place relative to the reaction arrow

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code
        :includecode: render-with-different-options
        :nocode:
        :downloads: data/catalysts3000.rxn

        renderRxnfileWithOptions('data/catalysts3000.rxn', 'render-catalysts-placement', [ "above", "above-and-below" ])


.. indigo_option::
    :name: render-center-double-bond-when-stereo-adjacent
    :type: boolean
    :default: false
    :short: Center double done if there is an attached stereobond

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code
        :includecode: render-with-different-options
        :nocode:

        indigo.setOption("ignore-stereochemistry-errors", True)
        renderMolfileWithOptions('data/render-center-double-bond-when-stereo-adjacent.mol', 'render-center-double-bond-when-stereo-adjacent', [ True, False ])

.. indigo_option::
    :name: render-data-sgroup-color
    :type: color
    :default: black
    :short: Color for data-sgroups

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code
        :includecode: render-with-different-options
        :nocode:
        :downloads: data/render_example-sgroup.mol

        renderMolfileWithOptions('data/render_example-sgroup.mol', 'render-data-sgroup-color', [ '0.5, 0.3, 0.5', '0.1, 0.1, 0.9' ])

.. indigo_option::
    :name: render-hdc-offset
    :type: offset
    :default: 0, 0
    :short: Offset for the rendering area

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code
        :includecode: render-with-different-options
        :nocode:

        renderMolfileWithOptions('data/render_example1.mol', 'render-hdc-offset', [ '0, 0', '30, 5' ])

.. indigo_option::
    :name: render-stereo-style
    :type: enum (old, ext, none)
    :default: old
    :short: Stereocenters rendering mode

    **old**:
        Only display the "Chiral" sign when appropriate.
    **ext**:
        Display "abs", "and", "or" labels near each stereocenter.
    **none**:
        Hide all the information about the stereogroups.

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code
        :includecode: render-with-different-options
        :nocode:
        :downloads: data/stereo-chiral.mol

        renderMolfileWithOptions('data/stereo-chiral.mol', 'render-stereo-style', [ 'old', 'ext', 'none' ])

    `Old` style of rendering is used only with ordinary stereocenters, and enhanced stereocenters with `and` and `or` groups are rendered the same in the `old` and `ext` mode:

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code
        :includecode: render-with-different-options
        :nocode:
        :downloads: data/stereo-chiral2.mol

        renderMolfileWithOptions('data/stereo-chiral2.mol', 'render-stereo-style', [ 'old', 'ext', 'none' ])


.. indigo_option::
    :name: render-superatom-mode
    :type: enum (expand, collapse)
    :default: expand
    :short: Supertatoms rendering mode

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code
        :includecode: render-with-different-options
        :nocode:
        :downloads: data/abbr.mol

        renderMolfileWithOptions('data/abbr.mol', 'render-superatom-mode', [ 'expand', 'collapse' ])

.. indigo_option::
    :name: render-valences-visible
    :type: boolean
    :default: true
    :short: Render explicit valences

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code
        :includecode: render-with-different-options
        :nocode:

        renderMolfileWithOptions('data/render_example-valence.mol', 'render-valences-visible', [ True, False ])

.. indigo_option::
    :name: render-highlight-color
    :type: color
    :default: red
    :short: The color to be used for highlighting.

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code
        :includecode: render-with-different-options
        :nocode:
        :downloads: data/highlighting.mol

        renderMolfileWithOptions('data/highlighting.mol', 'render-highlight-color', [ '1, 0, 0', '0, 0, 1' ])

.. indigo_option::
    :name: render-highlight-color-enabled
    :type: boolean
    :default: true
    :short: Enable highlighting with color.

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code
        :includecode: render-with-different-options
        :nocode:
        :downloads: data/highlighting.mol

        renderMolfileWithOptions('data/highlighting.mol', 'render-highlight-color-enabled', [ True, False ])

.. indigo_option::
    :name: render-highlight-thickness-enabled
    :type: boolean
    :default: false
    :short: Enable highlighting with thick bonds and bold atom labels.

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code
        :includecode: render-with-different-options
        :nocode:
        :downloads: data/highlighting.mol

        renderMolfileWithOptions('data/highlighting.mol', 'render-highlight-thickness-enabled', [ True, False ])

.. indigo_option::
    :name: render-highlighted-labels-visible
    :type: boolean
    :default: False
    :short:
        Always show labels of highlighted atoms.

    .. indigorenderer::
        :indigoobjecttype: code
        :indigoloadertype: code
        :includecode: render-with-different-options
        :nocode:
        :downloads: data/highlighting.mol

        renderMolfileWithOptions('data/highlighting.mol', 'render-highlighted-labels-visible', [ True, False ])
