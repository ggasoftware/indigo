############
Bingo plug-in
############

.. toctree::
    example/example.rst
        
********
Overview
********

Bingo plug-in implements a key-value storage for the chemical data types with chemical search functionality.

Bingo instance corresponds to a single chemical database stored in files. Call Bingo.createDatabaseFile to create a new database, or Bingo.loadDatabaseFile to load an existing one:

.. codeexample::
    :language: csharp
    :light: True

    Bingo database = Bingo.createDatabaseFile(indigo, "db1", "molecule");

    int id = database.insert(indigo.loadMolecule("OC1C(C(=O)O)=CC=CC1O"));
    Console.WriteLine("Id = {0}", id);
    
    database.close();
    
After the database is created you can load it:    

.. codeexample::
    :language: csharp
    :light: True

    Bingo database = Bingo.loadDatabaseFile(indigo, "db1", "molecule", "storage:ram");
    
You can insert records with specifing record ID, or without it. In the second case Bingo will assign record id automatically:    
    
.. codeexample::
    :language: csharp
    :light: True
    
    int id = database.insert(indigo.loadMolecule("OC1C(C(=O)O)=CC=CC1O"));
    Console.WriteLine("Id = {0}", id);
    
    database.insert(indigo.loadMolecule("CCCCC1CCCC1"), 1);
    
Substructure search:

.. codeexample::
    :language: csharp
    :light: True
    
    IndigoObject query = indigo.loadQueryMolecule("C1=CC=CC=C1");
    BingoObject search = database.searchSub(query);
    while (search.next())
        Console.WriteLine("  Found id = {0}", search.getCurrentId());    
    
Similarity search:

.. codeexample::
    :language: csharp
    :light: True
    
    IndigoObject query = indigo.loadMolecule("NC1C=CC=C(C1O)C(O)=O");
    BingoObject search = database.searchSim(query, 0.7f, 1.0f);
    while (search.next())
        Console.WriteLine("  Found id = {0}", search.getCurrentId());


Look at the :ref:`bingo-plugin-usage-example` for the complete example.
    
.. _bingo-options-label:
    
********
Options
********

Bingo can work in two modes that can be specified in the options parameter in `createDatabaseFile` and `loadDatabaseFile`:

 * **storage:ram** mode
    This is a default mode and Bingo duplicates all the file data into the memory. This mode consumes 
    more memory, but search operations are faster.
 
 * **storage:file** mode
    In this mode Bingo loads only a small amount of essential data into the memory, while with each search operation is reads data from files.
 
********
Bingo methods
********

.. function:: static Bingo createDatabaseFile(Indigo indigo, string location, string type, string options = null)

   Static method to close a database
   
   :param indigo: Indigo instance
   :param location: Directory with the files location
   :param type: "molecule" or "reaction"
   :param options: Additional options separated with a semicolon. See :ref:`bingo-options-label`.
   :return: Bingo database instance

----------
   
.. function:: static Bingo loadDatabaseFile(Indigo indigo, string location, string type, string options = null)

   Static method to load a chemical storage of a specifed type from a specified location
   
   :param indigo: Indigo instance
   :param location: Directory with the files location
   :param type: "molecule" or "reaction"
   :param options: Additional options separated with a semicolon. See :ref:`bingo-options-label`.
   :return: Bingo database instance
     
----------

.. function:: int insert(IndigoObject record)
        
   Insert a structure into the database and return id of this structure     
        
   :param record: Indigo object with a chemical structure (molecule or reaction)
   :return: record id
   
----------

.. function:: void insert(IndigoObject record, int id)
        
   Insert a structure into the database and return id of this structure     
        
   :param record: Indigo object with a chemical structure (molecule or reaction)
   :param id: record id
   
----------
   
.. function:: void delete(int id)

   Method to delete a record by id
   
   :param id: Record id
   
----------
        
.. function:: BingoObject searchSim (IndigoObject query, float min, float max, string metric = null)

    Execute similarity search operation

   :param query: Indigo object (molecule or reaction)
   :param min: Minimum similarity value
   :param max: Maximum similairy value
   :param metric: Similarity search metric. Default value is "tanimoto"
   :return: Bingo search object instance
        
----------

.. function:: BingoObject searchSub (IndigoObject query, string options = null)

    Execute substructure search operation

   :param query: Indigo query object (query molecule or query reaction)
   :param min: Minimum similarity value
   :param max: Maximum similairy value
   :param options: Options
   :return: Bingo search object instance
   
----------

.. function:: void close()
    
    Method to close database and dispose allocated memory. This method is automatically called in the object destructor. Same as Dispose().
    
----------

.. function:: void Dispose()

    Method to close database and dispose allocated memory. This method is automatically called in the object destructor. Same as close().


********
BingoObject methods
********

.. function:: bool next()
    
    Method to move to the next record

   :return: True if there are any more records
   
---------        
        
.. function:: int getCurrentId()
    
    Method to return current record id. Should be called after next() method.

   :return: Record id
   
---------        
        
.. function:: IndigoObject getIndigoObject()
    
    *Not implemented yet*

   :return: Shared Indigo object for the current search operation

----------

.. function:: void close()
    
    Method to terminate search and dispose allocated memory. This method is automatically called in the object destructor. Same as Dispose().
    
----------

.. function:: void Dispose()

    Method to terminate search and dispose allocated memory. This method is automatically called in the object destructor. Same as close().
        