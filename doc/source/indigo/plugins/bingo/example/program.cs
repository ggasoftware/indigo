using System;

using com.ggasoftware.indigo;

namespace BingoUsageExamples
{
    class Program
    {
        static void Main(string[] args)
        {
            Indigo indigo = new Indigo();

            // By default Bingo loads a database and stores all the data in RAM for faster operations
            // But if the application is limited in the memory usage Bingo can work 
            // in a file mode with loading only minor parts of data into the memory
            Bingo database = Bingo.createDatabaseFile(indigo, "db1", "molecule", "storage:file");

            // Insert structures from the file 
            using (IndigoObject input = indigo.iterateSmilesFile("input.smi"))
                foreach (IndigoObject obj in input)
                {
                    Console.WriteLine("  Object: {0}", obj.name());

                    // When loading from SMILES the only information that we have is an object name
                    // that is stored on the same line with the SMILES in the file
                    int id = int.Parse(obj.name());

                    // Insert loaded object into the database
                    database.insert(obj, id);

                    // Dispose native Indigo object as .NET object is much smaller than native object
                    // and GC can postpone disposing of this object resulting in a large memory 
                    // consumption
                    obj.Dispose();
                }

            // Bingo can also assign structure ID automatically
            int autoId1 = database.insert(indigo.loadMolecule("OC1C(C(=O)O)=CC=CC1O"));
            Console.WriteLine("Automatic id = {0}", autoId1);

            int autoId2 = database.insert(indigo.loadMolecule("OC1C(C(=O)O)=CC=CC1O"));
            Console.WriteLine("Automatic id = {0}", autoId2);

            // Search over the database
            Console.WriteLine("Search Benzene:");
            IndigoObject query = indigo.loadQueryMolecule("C1=CC=CC=C1");
            BingoObject search = database.searchSub(query);
            while (search.next())
                Console.WriteLine("  Found id = {0}", search.getCurrentId());

            // You can close and reopen database at any moment
            database.close();
            // Load Bingo in a RAM mode with caching all data into the memory
            // Search operations works faster in this mode
            database = Bingo.loadDatabaseFile(indigo, "db1", "molecule", "storage:ram");

            // Search the same query but in the aromatic form
            // Results are the same
            Console.WriteLine("Search Benzene in the aromatic form:");
            query = indigo.loadQueryMolecule("c1ccccc1");
            search = database.searchSub(query);
            while (search.next())
                Console.WriteLine("  Found id = {0}", search.getCurrentId());

            Console.WriteLine("Search C=O");
            query = indigo.loadQueryMolecule("C=O");
            // Using block will automatically call search.Dispose() that calls search.close()
            // to terminate further search
            using (search = database.searchSub(query))
            {
                int count = 0;
                while (search.next())
                {
                    Console.WriteLine("  Found id = {0}", search.getCurrentId());
                    count++;
                    if (count == 4)
                        break;
                }
            }

            // Database will be closed automatically in the object destructor
            // but we can close it manually to dispose memory
            database.close();
        }
    }
}
