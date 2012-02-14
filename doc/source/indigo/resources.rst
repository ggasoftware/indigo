.. _resources:

=========
Resources
=========

.. _resources_algorithms:

==========
Algorithms
==========

Fingerprinting is a common technique for molecular screening. Daylight, Inc. introduced this technique, and it is described in the following article. Bingo fingerprints, as compared to Daylight fingerprints, are built not from bond paths, but from trees and rings. A Russian article describes the enumeration of subtrees, which in turn is based on reverse search by David Avis and Komei Fukuda.

For tautomer substructure search, Bingo incorporates a unique type of fingerprinting.

For subgraph matching, we developed an original algorithm. It is somewhat similar to an algorithm by Luigi Cordella et al.

For the molecule layout in Indigo and Bingo, we developed a unique algorithm, based on biconnected components extraction. It incorporates some ideas of Craig Shelley.

For the aromaticity matching and resonance search, we developed unique algorithms as well.

For the canonical SMILES, Brendan McKay's nauty canonical labeling algorithm was re-implemented. Many of the original nauty's features and optimizations were not included. There is also a description of the algorithm in Russian.

For the affine transformation matching, Wolfgang Kabsch's algorithm was implemented.

In internal molecule and reaction formats, the LZW algorithm with some modifications was used for compression.

For the exact maximum common substructure search, we developed a unique algorithm partially based on Thierry Hanser's algorithm (which in turn has its roots in an algorithm by Coen Bron and Joep Kerbosh). For the approximate maximum common substructure search, the 2DOM algorithm with some modifications was implemented. A Russian paper describes both algorithms.

