################################################
Reaction Products Enumeration and Transformation
################################################

.. indigo_option::
    :name: rpe-multistep-reactions
    :type: boolean
    :default: false
    :short: Enable multistep reactions

.. indigo_option::
    :name: rpe-mode
    :type: enum (grid, one-tube)
    :default: grid
    :short: Monomers mixing mode

    **grid:**
        different sets of monomers react in different tubes

    **one-tube:**
        reactions take place in one tube

.. indigo_option::
    :name: rpe-self-reaction
    :type: boolean
    :default: false
    :short: Enable intramolecular reactions, where one molecule of monomers can play role of two (or more) reactants

.. indigo_option::
    :name: rpe-max-depth
    :type: int
    :default: 2
    :short: Maximum level of representing product like a monomer (works only with ``rpe-multistep-reactions enabled``).


.. indigo_option::
    :name: rpe-max-products-count
    :type: int
    :default: 1000
    :short: Maximum amount of generated products.

