#############################
Substructure matching options
#############################

.. indigo_option::
    :name: embedding-uniqueness
    :type: enum
    :default: atoms
    :short: Defines how the uniqueness of a substructure match is determined when counting or iterating unique matches.

    **atoms:**
        by atoms; "CCC" matches "C1CC1" once

    **bonds:**
        by bonds, "CCC" matches "C1CC1" three times

    **none:**
        no test for uniqueness; "CCC" matches "C1CC1" six times

.. indigo_option::
    :name: max-embeddings
    :type: int
    :default: 0
    :short: The maximum number of embeddings allowed to enumerate when counting all embeddings. 

    If the limit is reached, an exception is thrown. Zero value means no limit.

