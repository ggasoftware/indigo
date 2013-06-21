.. _indigo-example-atom-coloring:

=====================
Atom Coloring Example
=====================

.. indigoimage::
    :imagename: atom-coloring-main

Here is an example how to highlight molecule atoms according to the fragments activity:

We can assign activity value for each functional group:

.. code::
    :name: ac-patterns

    # Active fragment patterns
    patterns = [
        ("C-O", +1.0),
        ("C=O", +2.0),
        ("C-N", -1.0),
        ("C-C-n", -1.0),
        ("C-C=C", +0.5),
        ("C-F", -2.0),
        ("*:*", +1.0), # aromatic bond
        ("C-[Cl]", -1.0),
        ("C-S-C", 1.0),
    ]

For a specified molecule one can fine all the embeddings of fragment patterns, and accumulate activity for each atom that was matched:

.. code::
    :name: ac-assignColorGroups

    import collections
    
    def assignColorGroups (m):
        matcher = indigo.substructureMatcher(m)

        atom_values = collections.defaultdict(float)
        for pattern, value in patterns:
            query = indigo.loadQueryMolecule(pattern)
            for match in matcher.iterateMatches(query):
                for qatom in query.iterateAtoms():
                    atom = match.mapAtom(qatom)
                    atom_values[atom.index()] += value
        
        min_value = min(atom_values.itervalues())
        max_value = max(atom_values.itervalues())

        # Interpolate atom_values
        for atom_index, atom_value in atom_values.iteritems():
            if atom_value < 0:
                color = "0, 0, %f" % (atom_value / min_value)
            else:
                color = "%f, 0, 0" % (atom_value / max_value)
                
            m.addDataSGroup([atom_index], [], "color", color)
        
        m.setProperty("comment", "Min=%0.1f,  Max=%0.1f" % (min_value, max_value))

Rendering options:
        
.. code::
    :name: ac-rendering
    
    indigo.setOption("render-atom-color-property", "color")
    indigo.setOption('render-coloring', False)
    indigo.setOption('render-comment-font-size', 14.0)
        
        
.. indigorenderer::
    :indigoobjecttype: code
    :indigoloadertype: code
    :includecode: ac-patterns,ac-assignColorGroups,ac-rendering
    :imagename: atom-coloring-main
    
    # Load structure
    m = indigo.loadMolecule('CCN1C(SC(C)C(=O)NCC2=CC=C(F)C=C2)=NN=C1C1=CC=CC=C1OC')
    
    assignColorGroups(m)
    
    indigo.setOption('render-comment', "CID=46758793,  " + m.getProperty("comment"))
    indigoRenderer.renderToFile(m, 'result.png')

.. indigorenderer::
    :indigoobjecttype: code
    :indigoloadertype: code
    :includecode: ac-patterns,ac-assignColorGroups,ac-rendering
    
    # Load structure
    m = indigo.loadMolecule('[O-][N+](=O)C1=CN2CC3(CCN(CC3)C(=O)OCC3=CC=C(C=C3)C(F)(F)F)OC2=N1')
    
    assignColorGroups(m)
    
    indigo.setOption('render-comment', "CID=23081329,  " + m.getProperty("comment"))
    indigoRenderer.renderToFile(m, 'result.png')

