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
    6 = exon positions in the sequence, and start codon position*

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

Alternatively, db_input can be used to indicate particular categories
of data selected for browsing, where db_input can take values of 1-8.

2. Database query
-----------------
The db_query is a string argument which may be used for the following
purposes:

    (i) The db_query string can be used to search the data category
        specified by db_input for all records containing the string
        term entered;

   (ii) The db_query string can alternatively signal for browsing of
        the data category indicated by the db_input. In this case the
        BL submits 'B' as the string argument, which enables browsing.

3. Database output
------------------
The db_output is a flexible argument which selects one or more data
types to be returned to the BL for one or more records.

In particular, it allows expanded functionality for string searches,
beyond the single data type stipulated by the search_by argument.
The BL submits a second integer argument which may be selected from
the full range of values shown above i.e. 1-8. This allows multiple
data types to be selected for return during a string-based search. It
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
Results are returned as nested strings, as illustrated by the
examples below. Where a field is not found for a particular data type,
'NF' will be reported:

Example 1: Unique string search; single data type:

db_request(1,'AY177663',4)
db_result = [['desmoglein 4 preproprotein'], ['AY177663']]

Example 2: Non-unique string search; single data type:

db_request(3,'SSCA',3)
db_result = [['SSCA2', 'SSCA', 'pseudoSSCA'], ['AF485254', 'U49845',
'AF165912']]

Example 3: Browse; single data type:

db_request(2,'B',2)
db_result = [[['18q24.3', '18q24', 'NF', '18q11.2', 'q12.1', '18q11'],
['AF485254', 'U49845', 'AF165912', 'U55184', 'U19576', 'U55184']]]

Example 4: Unique string search; multiple data types:

db_request(4,'desmoglein 4 preproprotein',7)
db_result = [['AY177663'], ['18q24'], ['DSG4'], ['desmoglein 4
preproprotein']]

Example 5: Non-unique string; multiple data types:

db_request(2,'18q24.1',8)

[['D00596', 'U11424'], ['18q24.1', '18q24.1'], ['TPMT', 'pseudoTPMT'],
['thiopurine methyltransferase processed', 'pseudo-thiopurine methyltrans
ferase'], ['cacccacat...ataacccaatca', 'tcttagaatat...atatatgacaac'],
['99..987, 6619..7050', '20..125, 300..490'], ['start=1', 'start=3']]

Example 6: Browse request; multiple data types:

db_request(5,"B",6)
db_result = [[['cacccacat...tctcacacc', 'tcttagaag...ttgactaaac',
'aggactcat...cacatataac', 'tatatccagg...tgaaccttt'],['AF485254', 'U49845',
'AF165912', 'AJ001716']], [['1799..5187,6619..7050','20..125, 300..490',
'NF', '111..183,8360..8395,9912..10043'], ['start=2', 'start=1',
'start=3', 'start=1'], ['AF485254', 'U49845', 'AF165912', 'AJ001716']]]

Notes on usage and further examples
-----------------------------------
When submitting a multiple data category query i.e. category 7 or 8,
the use of a non-unique db_query might deliver unexpectedly large
quantities of data.

Therefore, unless a unique search term is already known - such as a
Genbank accession code - it is recommended that a two step search
procedure is used. This would consist of two separate calls to the
db_query function as follows:

Example 7: Prelininary, non-unique string search; single data type:

    (i) A preliminary search where the db_return argument is confined
        to options 1-4, 6 or 7:

        db_request(3,'DSG',4)
        db_result = [['desmoglein type 1', 'desmoglein 4 preproprotein'],
        ['AF485254', 'U49845']]
        
Example 8: Follow-up, unique string search; multiple data types:

   (ii) A follow-up search where a unique db_query (obtained during the
        initial search) can be submitted, together with a multiple data
        type request;

        db_request(1,'AF485254',8)   
        db_result = [['AF485254'], ['18q11.2'], ['DSG1'], ['desmoglein type 1'],
        ['cacccacatatgtcgtgtcgatcacccctactacataggatggatacgataacgatccaccac'],
        ['99..987,6619..7050', '20..125, 300..490'], ['start=3']]


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

if db_query != 'B' or 'b':
    if db_input < 1 or db_input > 4:
        print("String search: data category error")
else:
    if db_input < 1 or db_input > 8:
        print("Browse: data category error")
        
db_output = int(input("Enter output data category (1-8): "))

if db_output < 1 or db_output > 8:
        print("Output data category error")

db_result = db_request(db_input, db_query, db_output)

print("Database request results:",db_result) 



Known issues:
    
None at present
