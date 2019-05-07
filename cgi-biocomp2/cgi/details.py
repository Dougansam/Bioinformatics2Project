#!/usr/bin/python3
"""
This CGI script displays the details of a particular entry in the Genbank file
using the business layer API.

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
# radio = form.getvalue("radio")
# query = form.getvalue("query")

import html_utils
from blapi import *
from config import *

#------------------------------------------------------------------------------

print("Content-Type: text/html\n")

html = html_utils.header()

html += '<div class="w3-container">\n'
html += '  <h1>Details</h1>\n'
html += '</div>\n'

# Tab links********************************************************************

html += '<div class="w3-bar w3-black">\n'
html += '  <button class="w3-bar-item w3-button" onclick="openTab(\'dna\')">Genomic DNA</button>\n'
html += '  <button class="w3-bar-item w3-button" onclick="openTab(\'protein/cds\')">Protein/CDS</button>\n'
html += '  <button class="w3-bar-item w3-button" onclick="openTab(\'codons\')">Codon usage</button>\n'
html += '  <button class="w3-bar-item w3-button" onclick="openTab(\'restriction\')">Restriction enzymes</button>\n'
html += '</div>\n'

# DNA seq with higlighted CDSs*************************************************

html += '<div id="dna" class="w3-container w3-border tab">\n'
html += '  <h3>Genomic DNA sequence with CDSs highlighted</h3>\n'

html += '  <div>\n'
html += '    <pre class="long-seq"><span>' + html_utils.dna_seq_format(coding_regions(radio, typed)) + '</span></pre>\n'
html += '  </div>\n'
html += '</div>\n'

# CDS/aa***********************************************************************

# Add aa per codon?
html += '<div id="protein/cds" class="w3-container w3-border tab" style="display:none">\n'
html += '  <h3>Protein/CDS</h3>\n'
html += '  <pre class="long-seq">' + coding_seq(radio, typed) + '</pre>\n'
html += '  <pre>\n'

html += protein_seq(radio, typed)

html += '  </pre>\n'
html += '</div>\n'

# Codon usage******************************************************************

# Codon frequency in a particular gene
html += '<div id="codons" class="w3-container w3-border tab" style="display:none">\n'
html += '  <h3>Codon usage</h3>\n'

html += '<span class="w3-left" style="margin-left:200px">Codon usage in gene</span>\n'
html += '<span class="w3-right" style="margin-right:200px">Codon usage in chromosome 18</span>\n'

html += '<br>'

html += '<table class="w3-table-all w3-hoverable w3-centered w3-left" style="width:300px; margin-left:200px">\n'
html += '  <thead>\n'
html += '    <tr class="w3-green">\n'
html += '      <th>Codon</th>\n'
html += '      <th>Count</th>\n'
html += '      <th>Frequency (%)</th>\n'
html += '    </tr>\n'
html += '  </thead>\n'
html += '  <tbody>\n'

html += html_utils.codon_table()

html += '  </tbody>\n'
html += '</table>\n'

# Codon frequency in chromosome 18
html += '<table class="w3-table-all w3-hoverable w3-centered w3-right" style="width:300px; margin-right:200px">\n'
html += '  <thead>\n'
html += '    <tr class="w3-green">\n'
html += '      <th>Codon</th>\n'
html += '      <th>Count</th>\n'
html += '      <th>Frequency (%)</th>\n'
html += '    </tr>\n'
html += '  </thead>\n'
html += '  <tbody>\n'

html += html_utils.genome_codon_table()

html += '  </tbody>\n'
html += '</table>\n'

html += '</div>\n'

# Restriction sites************************************************************

html += '<div id="restriction" class="w3-container w3-border tab" style="display:none">\n'
html += '  <h3>Find targets</h3>\n'

# Add targets of as many restriction enzymes as desired

# Table of enzymes
html += '<div>\n'
html += '<table class="w3-table-all w3-hoverable">\n'
html += '  <thead>\n'
html += '    <tr class="w3-green">\n'
html += '      <th>Enzyme</th>\n'
html += '      <th>Source</th>\n'
html += '      <th>Recognition Sequence</th>\n'
html += '    </tr>\n'
html += '  </thead>\n'
html += '  <tbody>\n'

html += '    <tr onclick="javascript:void($(\'#highlight-plugin\').removeHighlight().highlight(\'GAATTC\'));" style="cursor:pointer">\n'
html += '      <td><i>EcoRI</i></td>\n'
html += '      <td><i>Escherichia coli</i></td>\n'
html += '      <td>5\'G/AATTC</td>\n'
html += '    </tr>\n'

html += '    <tr onclick="javascript:void($(\'#highlight-plugin\').removeHighlight().highlight(\'GGATCC\'));" style="cursor:pointer">\n'
html += '      <td><i>BamHI</i></td>\n'
html += '      <td><i>Bacillus amyloliquefaciens</i></td>\n'
html += '      <td>5\'G/GATCC</td>\n'
html += '    </tr>\n'

html += '    <tr onclick="javascript:void($(\'#highlight-plugin\').removeHighlight().highlight(\'CTCGAG\'));" style="cursor:pointer">\n'
html += '      <td><i>BsuMI</i></td>\n'
html += '      <td><i>Bacillus subtilis</i></td>\n'
html += '      <td>5\'CTCGAG*</td>\n'
html += '    </tr>\n'

html += '  </tbody>\n'
html += '</table>\n'
html += '*The site of cleavage is unknown.\n'
html += '<a href="javascript:void($(\'#highlight-plugin\').removeHighlight());"><button class="w3-button w3-green w3-round w3-right">Remove highlight</button></a>\n'
html += '</div>\n'

html += '<br>\n'

html += 'Search for a particular sequence outside a CDS: <input type="text" id="search" class="search form-control">'

# Add/remove 'text' class to activate the highlightText plugin
# Add opening and closing <span> tags to complete the dna_seq_format() function
# id and class mark the text subject to highlighting plugins
html += '<p><pre class="long-seq" id="highlight-plugin"><span class="text">' + html_utils.dna_seq_format(dna_seq) + '</span></pre></p>\n'

html += '</div>\n'

# JavaScript ******************************************************************

html += '<script src="' + simple_tab_path + '"></script>\n'
html += '<script src="' + jquery_path + '"></script>\n'
html += '<script src="' + re_highlight_plugin_path + '"></script>\n'
html += '<script src="' + text_highlight_plugin_path + '"></script>\n'
html += '<script src="' + app_path + '"></script>\n'

html += html_utils.footer()

print(html)
