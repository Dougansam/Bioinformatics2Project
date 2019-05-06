#!/usr/bin/python3

index_path = "http://student.cryst.bbk.ac.uk/~cd002/index.html"
details_accession_path = "http://student.cryst.bbk.ac.uk/cgi-bin/cgiwrap/cd002/details.py?option=accession&query="
favicon_path = "http://student.cryst.bbk.ac.uk/~cd002/favicon.ico"
logo_path = "http://student.cryst.bbk.ac.uk/~cd002/logo.svg"
microarray_fig_path = "http://student.cryst.bbk.ac.uk/~cd002/microarray.jpg"
mysql_db_login = 'mysql -u tg001 -p"f29z70k#r" tg001'

# Acces cgi-biocomp2, where config.py file is
import sys
sys.path.insert(0, "../cgi-biocomp2/")

# Import the config.py itself
import config

# This is how you use the variable
config.mysql_db_login
