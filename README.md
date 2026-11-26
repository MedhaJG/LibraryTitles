 Library's Half-Remembered Titles
Problem Statement
Visitors to a digital library often remember only the beginning and ending of a title but not the complete name. Searching through every record for every query becomes inefficient as the catalog grows.

This project implements a Partial-Title Retrieval System that efficiently finds catalog entries matching both a given prefix and suffix using Trie-based indexing.

Features
✅ Fast prefix search using a Prefix Trie

✅ Fast suffix search using a Reversed Suffix Trie

✅ Returns the most recently added matching record

✅ Supports duplicate titles with unique insertion IDs

✅ Provides clear no-match responses

✅ User-friendly GUI built with Tkinter

✅ Reusable search index (catalog indexed only once)

✅ No full catalog scan during queries

Data Structures Used
1. Prefix Trie
Stores catalog names for efficient prefix matching.

2. Reversed Suffix Trie
Stores reversed catalog names for efficient suffix matching.

3. Hash Map
Stores records and allows O(1) retrieval by ID.

Project Structure
LibraryHalfRememberedTitles/
│
├── main.py
├── search_index.py
├── trie.py
├── record.py
├── gui.py
├── tests.py
└── README.md
How It Works
Index Building
Each catalog title is assigned a unique insertion ID.

Example:

ID	Title
0	catalog
1	catch
2	catdog
3	batdog
4	catalog
5	catlog
6	catdog
The title is inserted into:

Prefix Trie
Reversed Suffix Trie
This indexing happens only once.

Query Processing
Given:

Prefix = cat
Suffix = og
The system:

Finds all records beginning with "cat"
Finds all records ending with "og"
Computes the intersection
Returns the record with the highest ID
Example
Catalog
catalog
catch
catdog
batdog
catalog
catlog
catdog
Query
Prefix: cat
Suffix: og
Matching Records
ID 0 → catalog
ID 2 → catdog
ID 4 → catalog
ID 6 → catdog
Output
Matched Record: catdog
Record ID: 6
The latest matching record is selected, satisfying the project requirements.

Functional Requirements Covered
Requirement	Status
Load catalog in insertion order	✅
Prefix search	✅
Suffix search	✅
Return latest matching record	✅
Handle duplicate titles	✅
No-match reporting	✅
Reusable index	✅
GUI interface	✅
Testing support	✅
Complexity Analysis
Index Construction
O(N × L)
Where:

N = Number of titles
L = Maximum title length
Query
O(P + S + K)
Where:


Run GUI Application
python main.py
Run Test Cases
python tests.py
Test Cases
Test 1
Prefix = cat
Suffix = og
Output:

ID=4, Title=catdog
Test 2
Prefix = ca
Suffix = ch
Output:

ID=1, Title=catch
Test 3
Prefix = abc
Suffix = xyz
Output:

No Match
Demonstration Requirements Satisfied
Multiple catalog entries match the same clues
Latest insertion wins
Duplicate titles supported
No full catalog scan during search
Fast Trie-based retrieval


Technologies Used
Python 3
Tkinter (GUI)
Trie Data Structure
Object-Oriented Programming
Author
Developed as a solution to Problem Statement 08 – The Library's Half-Remembered Titles.
