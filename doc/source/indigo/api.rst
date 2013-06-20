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

Image with code execution example:

.. indigorenderer::
    :indigoobjecttype: code
    :indigoloadertype: code

    indigo = Indigo()
    indigoRenderer = IndigoRenderer(indigo)
    result = indigo.loadReaction('C1=CN=CC=C1.C2CFCC2>>C2CNCC2.C1=CF=CC=C1')
    result.addProduct(indigo.loadMolecule('C'))
    result.addReactant(indigo.loadMolecule('C'))
    indigo.setOption('render-relative-thickness', '0.3')
    indigoRenderer.renderToFile(result, 'result.png')

Another image with code execution example:

.. code::
    :name: test

    def testFunc():
        indigo.setOption('render-relative-thickness', '2')

.. indigorenderer::
    :indigoobjecttype: code
    :indigoloadertype: code
    :includecode: test

    testFunc()
    result = indigo.loadReaction('C1=CN=CC=C1.C2CFCC2>>C2CNCC2.C1=CF=CC=C1')
    result.addProduct(indigo.loadMolecule('C'))
    result.addReactant(indigo.loadMolecule('C'))
    indigoRenderer.renderToFile(result, 'result.png')
   
To use Indigo in your source files:

.. codeexample::
    :language: csharp

    using com.ggasoftware.indigo;

.. codeexample::
    :language: csharp

    Indigo indigo = new Indigo();
    Console.WriteLine(indigo.version());