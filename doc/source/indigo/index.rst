.. indigo documentation master file, created by

######
Indigo
######

Contents:

.. toctree::
   :maxdepth: 2

   concepts/index.rst
   options/index.rst
   examples/index.rst
   release-notes/index.rst

********
Overview
********

Indigo is a universal organic chemistry toolkit. It contains first-class tools for end users, as well as a documented API for developers.
 Indigo it is completely free and open-source, while also available on a commercial basis.

Indigo is based on a cheminformatics library that incorporates a number of unique algorithms developed by GGA, as well as 
some standard algorithms well-known in the cheminformatics world. Since the core part of Indigo is written in modern 
C++ with no third-party code or dependencies except the ubiquitous `zlib <http://zlib.net>`_ and `Cairo <http://cairographics.org>`_, 
the toolkit provides outstanding performance and excellent portability.

Indigo is used by many corporations and institutions. This includes some Indigo-based commercial tools developed exclusively for our clients. Also, our open-source chemical search engine Bingo is developed on top of the Indigo library.

Indigo SDK does not make any restrictions for developers. Whatever your favorite platform is—Java, C#, or Python, not to mention plain C—you can easily integrate Indigo into your application. All problems you may be afraid of, such as loading binary modules appropriate for the system, or threading issues, or stack overflows, are already solved for you. Also, it is easy to start, as the interface is very neat. No data types besides the absolute minimum required for it to work. No internal data formats. No painful initialization procedures.

Indigo SDK is highly configurable and extensible. You can write C/C++/C#/Java/Python plugins for it and distribute them independently.

Indigo has got support from the cheminformatics community. Any question or comment you have, you can always post it publicly and get a timely reply from the developers' team.

""""""""
Features
""""""""

* Input formats support: Molfiles/Rxnfiles v2000 and v3000, SDF, RDF, CML, SMILES, SMARTS.
* Portability: Pre-built binary packages are provided for Linux and Windows (both 32-bit and 64-bit), and also for Mac OS X systems (both 10.5 and 10.6).
* Molecule and reaction rendering. Best picture quality among all available products. Easy SVG support.
* Automatic layout for SMILES-represented molecules and reactions.
* Canonical (isomeric) SMILES computation.
* Exact matching, substructure matching, SMARTS matching.
* Matching of tautomers and resonance structures.
* Molecule fingerprinting, molecule similarity computation.
* Fast enumeration of SSSR rings, subtrees, and edge sugraphs.
* Molecular weight, molecular formula computation.
* R-Group deconvolution and scaffold detection. Pioneer work in computing the exact maximum common substructure for an arbitrary amount of input structures.
* Combinatorial chemistry
* Plugins support in the API. As a reference, please see the Renderer plugin distributed together with the Indigo API.

"""""""""""
Portability
"""""""""""

Indigo is written from scratch in portable C++ and supports Linux, Windows, and Mac OS X operating systems. The rendering 
is done via `Cairo <http://cairographics.org>`_ vector graphics library. `zlib <http://zlib.net>`_ and `libpng <http://www.libpng.org>`_ 
are needed for Cairo. `TinyXML <http://www.grinninglizard.com/tinyxml/>`_ is used to parse CML files. `InChI <http://www.inchi-trust.org>`_ library is used to generate and parse InChI strings.
No other third-party components are used.

Indigo exposes the C interface to applications. Java, Python, and .NET wrappers are available for all of the supported platforms.

All of the the code of Indigo is thread-safe, and so its use does not present a problem in multi-threaded applications.
