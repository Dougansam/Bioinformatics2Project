'''
------------
------------
DATABASE API
------------
------------

The Database API function, db_request, takes all database search
requests from the BL, and is the only function which is directly
available to it.

The function allows searching of particular data categories using a
string query. Browsing of certain categories is also possible. A
variety of data output options is available, depending on search type
and string entered.

Three arguments, db_input, db_query and db_output, should be entered
by the BL, such that:

db_result = db_request(db_input, db_query, db_output)

For the purposes of db_input and db_output, which are both integer
arguments, the following protocol is used:

    1 = Genbank accession code*
    2 = chromosomal location*
    3 = gene identifier code*
    4 = protein product name*
    
    5 = complete DNA sequence*
    6 = exon positions in complete DNA sequence*

    7 = 'Summary list' consisting of data types 1-4    
    8 = 'Full detail list' consisting of data types 1-6

    *The Genbank accession code is included as a tag when data types
    are returned individually, to identify all results unambiguously.
    
Note that, in data selected from raw Genbank records, only category 1
(Genbank accession code) is guaranteed to be unique to a single record.

1. Database input
-----------------
The db_input argument indicates which data category should be searched
by a given search term, "db_query". When used with the search term
query, db_input can only take values 1-4.

In addition, db_input can be used to indicate particular categories
of data selected for browsing, where db_input can take values of 1-8.

2. Database query
-----------------
The db_query is a string argument which may be used for the following
purposes:

    (i) The db_query string can be used to search the data category
        specified by db_input for all records containing the string
        term entered;

   (ii) The db_query string can alternatively signal for browsing of
        the data categories indicated by the db_input. In this case the
        BL submits 'B' as the string argument, which enables browsing.

3. Database output
------------------
The db_output is a flexible argument which selects one or more data
categories to be returned to the BL for one or more records.

In particular, it allows expanded functionality for string searches,
beyond the single data category stipulated by the search_by argument.
The BL submits a second integer argument which may be selected from
the full range of values shown above i.e. 1-8. This allows multiple
categories to be selected for return during a string-based search. It
also allows the data category which is returned to be different from
the data category used to carry out the search itself.

The browsing feature described earlier may also be expanded upon by
appropriate use of the db_output argument. The browsing feature
automatically returns the data categories entered for db_input, but,
by entering a different data category into db_output, the selection of
any two of data categories 1-6 is enabled, which may be useful for
delivering results to the user directly, or for processing sets of data
in the BL before passing to the user.

Data return and examples
------------------------
Example 1.
Where a unique string is entered to search a type of data, and a
single data type is requested for output, a single list containing
a single string will be returned*:

db_request(1,"AY177663",4)
db_result = [["desmoglein 4 preproprotein"],["AY177663"]]

Example 2.
Where a non-unique string is entered,and a single data type is
requested, a single list of one or several strings will be returned*:

db_request(3,"SSCA",3)
db_result = [["SSCA1","SCCA2"],["U19568","U19576"]]

Example 3.
Where a browse request is made, and a single data type is requested, a
single list of several or many strings will be returned*:

db_request(2,"B",2)
db_result = [["18q12","18p11.32","18q21.1","18q21.3","18q21.3"],
["AY177663","D00596","U11424","U19568","U19576"]]

Example 4.
Where a unique string is entered, and multiple data types are
requested, a nested list will be returned, with each inner list
containing a single string:

db_request(4,"desmoglein 4 preproprotein",7)
db_result = [["AY177663"],["18q12"],["DSG4"],["desmoglein 4
preproprotein"]]

Example 5.
Where a non-unique string is entered, and multiple data types are
requested, a nested list will be returned, with each inner list
containing one or several strings:

db_request(2,"18q21",8)
db_result = [["U11424","U19568","U19576"],["18q21.1","18q21.3",
"18q21.3"],["pseudoTPMT","SSCA1","SCCA2"],["thiopurine
methyltransferase processed pseudogene","squamous cell carcinoma
antigen","squamous cell carcinoma antigen"],["99..987,6619..7050",
"20..125, 300..490","99..587,619..950"],["cacccacatataacccaatgtatttatat
attctaataataataaagaacctttgtcgtgtcgatcacttacctacccaggactcacaccaggactcata
cactta","catacacatacacct......actgattcttttatataacatgtattt","tatatccagga
tcatattttgcctgaacctttgtcgatcacttacctacacattacatatacataaactgattgcctat"]]

Example 6.
Where a browse request is made, and multiple data types are requested,
a nested list will be returned, with each inner list containing several
or many strings*:

db_request(5,"B",6)
db_result = [[["cacccacatataacccaatgtatttatatatccaggactcatattttgcctatta
attctaataataataaagaacctttgtcgtgtcgatcacttacctacccaggactcacaccaggactcata
cactta","catacacatacacct......actgattcttttatataacatgtattt","tatatccagga
tcatattttgcctgaacctttgtcgatcacttacctacacattacatatacataaactgattgcctat"],
["99..987,6619..7050", "20..125, 300..490","99..587,619..950","11..183,
8360..8395,9912..10043,11591..11746", "159..987,1200..5079","360..8395,
9912..10043"]],["AY177663","D00596","U11424","U19568","U19576"]]

Notes on usage and further examples
-----------------------------------
When submitting a multiple data category query i.e. category 7 or 8,
the use of a non-unique db_query might deliver unexpectedly large
quantities of data.

Therefore, unless a unique search term is already known - such as a
Genbank accession code - it is recommended that a two step search
procedure is used. This would consist of two separate calls to the
db_query function as follows:

    Example 7.
    (i) A preliminary search where the db_return argument is confined
        to options 1-4*, 6* or 7*:

        db_request(3,"SCCA",4)
        db_result = [["squamous cell carcinoma antigen","squamous cell
        carcinoma antigen"],["U19568","U19576"]]
        
    Example 8.   
    (ii)A follow-up search where a unique db_query (obtained during the
        initial search) can be submitted, together with a multiple data
        type request;

        db_request(1,"U19568",8)   
        db_result = [["U19576"],["18q21.3"],["SCCA1"],["squamous cell
        carcinoma antigen"],["65..98,103..540"],["acacattacatatacataaa
        tcttttatacacatacacatataacccaatgtatttatatatccaggactcatattttgcct
        attagaataataatatctaataaagtgaaccttctgtatttcacatttgttgccaaaataag
        gattctccacatagtcaattcattgttaaggttcttccagaaaaattctccttgaggaaaaa
        tgtccaaaataagatgaatcacttaatacggaatcattagagtatgggtgaatgaagagaaa
        aataataatatctaataagc"]]
       
*together with a separate list containing appropriate accession no/s.)

'''
    
db_input = []
db_query = []
db_output = []

db_result = []

from db_access import db_request

db_input = int(input("Enter data input category for search (1-4) or \
browse (1-8): "))

db_query = str(input("Enter a search term string for the \
selected category, or enter 'B' to browse a category: "))

if db_query != 'B':
    if db_input < 1 or db_input > 4:
        print("String search data category error")
else:
    if db_input < 1 or db_input > 8:
        print("Browse data category error")
        
db_output = int(input("Enter output data category (1-8): "))

db_result = db_request(db_input, db_query, db_output)

print("Database request results:",db_result) 










    
