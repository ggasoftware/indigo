######################
Grid rendering options
######################

.. indigo_option::
    :name: render-grid-margins
    :type: size
    :default: 0, 0
    :short: Horizontal and vertical margins around the grid cell, in pixels.

.. indigo_option::
    :name: render-grid-title-property
    :type: string
    :default: none
    :short: The name of the molecule's property that defines the title that is put under each molecule.

    If not defined, no titles are shown. The special value "^NAME" means to use the molecule's name as its title.

.. indigo_option::
    :name: render-grid-title-alignment
    :type: enum
    :default: center
    :short: Cell title alignment

    Supported values: left, right, center

.. indigo_option::
    :name: render-grid-title-font-size
    :type: int
    :default: 20
    :short: Font size for the title in absolute units, roughly equal to the height in pixels.

.. indigo_option::
    :name: render-grid-title-offset
    :type: int
    :default: 0
    :short: Vertical space (in pixels) between the title and the rendered structure.
