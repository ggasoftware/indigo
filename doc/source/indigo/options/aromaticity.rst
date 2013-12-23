###################
Aromaticity options
###################

.. indigo_option::
    :name: aromaticity-model
    :type: enum
    :default: basic
    :short: Aromaticity model

    Supported values:

    * **basic**
    * **generic**


.. indigo_option::
    :name: dearomatize-verification
    :type: boolean
    :default: true
    :short: Verify dearomatization method

.. indigo_option::
    :name: unique-dearomatization
    :type: boolean
    :default: false
    :short: Find dearomatization if all possible configurations uniquely define hydrogens.
