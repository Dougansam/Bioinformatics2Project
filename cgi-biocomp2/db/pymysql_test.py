#!/usr/bin/env python3
"""
Program:    
File:       
Version:    V1.0
Date:       07.05.19
Author:     Dr Georgina R Toye 
Address:    Department of Biological Sciences
            School of Science
            Birkbeck College
            University of London
-------------------------------------------------------------------------------

---------------
 PyMySQL 
---------------
            
Description:
------------

This program serves to test that the project database is contactable, and that
data can be appropriately extracted from it using PyMySQL (PEP249 compliant).

================================================================================
"""

import pymysql.cursors

# Set parameters
dbname   = "tg001"
dbhost   = "hope"
dbuser   = "tg001"
dbpass   = "f29z70k#r"   
port     = 3306

# Create MySQL statement
sql  = "SELECT chrom_loc, acc_num FROM gb_main WHERE acc_num = 'Z27420'"

# Connect to Genbank Project database
db = pymysql.connect(host=dbhost, port=port, user=dbuser, passwd=dbpass, db=dbname)

# Create a cursor and execute the SQL on it
cursor = db.cursor()
nrows  = cursor.execute(sql)

# In this case only one row needs to be returned and printed
data = cursor.fetchone()

chrom_loc = data[0]
acc_num = data[1]

print("[['",chrom_loc,"'],['",acc_num,"']]")

"""
================================================================================

Output for this test function was the appropriate set of values from the database:

[[' NF '],[' Z27420 ']]

================================================================================
"""
