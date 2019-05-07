#!/usr/bin/python3
"""
This CGI script retrieves all the entries from the BL layer and formats them 
for HTML display as a table.

Author: Diego Chillon Pino
"""

#------------------------------------------------------------------------------

# Add the bl sub-directory to the module path
# and the directory above to import the config file
import sys
sys.path.insert(0, "../bl/")
sys.path.insert(0, "../")

import html_utils
from blapi import *
from config import *
from config import *

#------------------------------------------------------------------------------

print('Content-Type: text/html\n\n')  # MIME-Type header

html = html_utils.header()

html += '<div class="w3-container">\n'
html += '  <h1>Table of entries</h1>\n'

# Table header
html += '<table class="w3-table-all w3-hoverable">\n'
html += '  <thead>\n'
html += '    <tr class="w3-green">\n'
html += '      <th>Genbank accession</th>\n'
html += '      <th>Gene ID</th>\n'
html += '      <th>Gene product</th>\n'
html += '      <th>Chromosomal location</th>\n'
html += '    </tr>\n'
html += '  </thead>\n'
html += '  <tbody>\n'

html += html_utils.list_all_table()

html += '  </tbody>\n'
html += '</table>\n'
html += '</div>\n'

html += html_utils.footer()

print(html)
