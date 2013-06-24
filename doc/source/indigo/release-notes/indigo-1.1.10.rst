#############
Indigo 1.1.10
#############

*********
Rendering
*********

=============
Atom coloring
=============

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

For a larger example see :ref:`indigo-example-atom-coloring`.

===============
Bond line width
===============

.. indigorenderer::
    :indigoobjecttype: code
    :indigoloadertype: code

    m = indigo.loadMolecule('CC1=C(Cl)C=CC2=C1NS(=O)S2')
    
    # Default visualization
    indigo.setOption('render-comment', 'default')
    indigoRenderer.renderToFile(m, 'result.png')

    # Bonds are twice thicker
    indigo.setOption('render-bond-line-width', 2.0)
    indigo.setOption('render-comment', 'render-bond-line-width=2.0')
    indigoRenderer.renderToFile(m, 'result.png')
    
    # Bonds are twice thinner
    indigo.setOption('render-bond-line-width', 0.5)
    indigo.setOption('render-comment', 'render-bond-line-width=0.5')
    indigoRenderer.renderToFile(m, 'result.png')
    
    
..
    .. image:: ../../_images/test.svg
       :width: 20%
    .. image:: ../../_images/test.svg
       :width: 20%
    .. image:: ../../_images/test.svg
       :width: 20%    
    