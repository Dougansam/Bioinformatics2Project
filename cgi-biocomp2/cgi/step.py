#!/usr/bin/python3
"""
This CGI script obtains the entries that agree with the input from the user
and displays a clickable table populated with those.

Author: Diego Chillon Pino
"""

#------------------------------------------------------------------------------

# Add the bl sub-directory to the module path
# and the directory above to import the config file
import sys
sys.path.insert(0, "../bl/")
sys.path.insert(0, "../")

import cgi
import cgitb
cgitb.enable()
cgitb.enable(display=0, logdir="/path/to/logdir")
form = cgi.FieldStorage()
radio = form.getvalue("radio")
query = form.getvalue("query")

import html_utils
from blapi import *
from config import *

#------------------------------------------------------------------------------

print('Content-Type: text/html\n\n')  # MIME-Type header

html = html_utils.header()

html += '<div class="w3-container">\n'
html += '  <h1>Table of entries</h1>\n'

# Table header
html += '  <table class="w3-table-all w3-hoverable">\n'
html += '    <thead>\n'
html += '      <tr class="w3-green">\n'
html += '        <th>Genbank accession</th>\n'
html += '        <th>Gene ID</th>\n'
html += '        <th>Gene product</th>\n'
html += '        <th>Chromosomal location</th>\n'
html += '      </tr>\n'
html += '    </thead>\n'
html += '    <tbody>\n'

html += html_utils.step_table()

# End table
html += '    </tbody>\n'
html += '  </table>\n'
html += '</div>\n'

html += html_utils.footer()

print(html)
