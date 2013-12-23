####################
Fingerprints options
####################

.. indigo_option::
    :name: fp-ord-qwords
    :type: integer
    :default: 25
    :short: Size of "ordinary" part of a fingerprint, in 8-byte blocks.
 
.. indigo_option::
    :name: fp-sim-qwords
    :type: integer
    :default: 8
    :short: Size of "similarity" part of a fingerprint, in 8-byte blocks.

.. indigo_option::
    :name: fp-any-qwords
    :type: integer
    :default: 15
    :short: Size of "any" part of a fingerprint, in 8-byte blocks.

.. indigo_option::
    :name: fp-tau-qwords
    :type: integer
    :default: 25
    :short: Size of "tautomer" part of a fingerprint, in 8-byte blocks.

.. indigo_option::
    :name: fp-ext-enabled
    :type: boolean
    :default: true
    :short: Sets whether to include or not 3-byte "EXT" part of the fingerprint.
