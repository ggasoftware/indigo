.. _api:

==========
Indigo API
==========

Overview

This page describes the API of Indigo library and its rendering plugin. The API allows developers to integrate Indigo into their C/Java/C#/Python projects. Please note that Indigo is under active development, and you can always post your comments and suggestions to our team.

Image example:

.. indigorenderer::
    :indigoobjecttype: reaction
    :indigoloadertype: text

    C1=CN=CC=C1.C2CFCC2>>C2CNCC2.C1=CF=CC=C1

.. codeexample::

    import com.ggasoftware.indigo.Indigo;
    Indigo indigo = new Indigo();
    print indigo.version();

