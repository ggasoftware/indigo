#######
Options
#######

Indigo instance represents an environment for IndigoObjects. Many methods in Indigo has additional options that can be set via Indigo.setOption method:

.. indigorenderer::
    :indigoobjecttype: code
    :indigoloadertype: code

    indigo.setOption("render-comment", "text comment")
    indigo.setOption("render-comment-color", "0, 0.4, 0.5")
    indigo.setOption("ignore-stereochemistry-errors", True)

Contents:

.. toctree::
    :maxdepth: 2

    input-output-options.rst
    layout-options.rst
    rendering-options.rst
    grid-rendering-options.rst
    substructure-matching-options.rst
    fingerprints.rst
    deconvolution.rst
    aromaticity.rst
    timeout.rst
    reaction-product-enumeration.rst
    inchi.rst

.. indigo_options_table::

