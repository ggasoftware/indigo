.. _indigo-example-atom-coloring:

=====================
Atom Coloring Example
=====================

Here is an example how to highlight molecule atoms according to the fragments activity:

.. indigorenderer::
    :indigoobjecttype: code
    :indigoloadertype: code

    import collections
    
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
    
    # Load structure
    m = indigo.loadMolecule('CCN1C(SC(C)C(=O)NCC2=CC=C(F)C=C2)=NN=C1C1=CC=CC=C1OC')
    
    assignColorGroups(m)
    
    indigo.setOption("render-atom-color-property", "color")
    indigo.setOption('render-coloring', False)
    #indigo.setOption('render-comment', m.getProperty("comment"))
    #print m.getProperty("comment")
    indigo.setOption('render-comment', "CID=46758793,  " + m.getProperty("comment"))
    indigo.setOption('render-comment-font-size', 14.0)
    
    indigoRenderer.renderToFile(m, 'result.png')

