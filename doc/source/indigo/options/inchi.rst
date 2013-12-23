#############
InChI options
#############

.. indigo_option::
    :name: inchi-options
    :type: string
    :default: none
    :short: Options supported by the official InChI plugin.

    The following options are supported by the official InChI plugin:

    * /NEWPSOFF
    * /DoNotAddH
    * /SNon
    * /SRel
    * /SRac
    * /SUCF
    * /ChiralFlagON
    * /ChiralFlagOFF
    * /SUU
    * /SLUUD
    * /FixedH
    * /RecMet
    * /KET
    * /15T


.. indigorenderer::
    :indigoobjecttype: code
    :indigoloadertype: code

    m = indigo.loadMolecule("CC1CC(C)OC(C)N1")
    print(indigoInchi.getInchi(m))

    indigo.setOption("inchi-options", "/SUU")
    print(indigoInchi.getInchi(m))

    indigo.setOption("inchi-options", "/DoNotAddH /SUU")
    print(indigoInchi.getInchi(m))
