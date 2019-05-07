#!/usr/bin/python3
'''
Support code for generating HTML files.

Author: Diego Chillon Pino
'''

#------------------------------------------------------------------------------
# Add the bl sub-directory to the module path
# and the directory above to import the config file
import sys
sys.path.insert(0, "../bl/")
sys.path.insert(0, "../")

from config import *
from blapi import *
from format_functions import *

#------------------------------------------------------------------------------

def header():
    '''
    Returns the header of the website, including logo.
    '''
    html = '<!doctype html>'
    html += '<html lang="en">\n'
    html += '  <head>\n'
    html += '    <title>Chrom18</title>\n'
    html += '    <meta charset="utf-8">\n'
    html += '    <link rel="icon" href="' + favicon_path + '">\n'
    html += '    <link rel="stylesheet" href="' + css_path + '">\n'
    html += '    <link href="https://fonts.googleapis.com/css?family=Fjalla+One" rel="stylesheet">\n'
    html += '  </head>\n'
    html += '  \n'
    html += '  <body>\n'
    html += '    <div class="w3-display-container w3-animate-opacity">\n'
    html += '      <img class="w3-opacity-max" src="' + microarray_fig_path + '" alt="Microarray">\n'
    html += '      <h1 class="w3-padding w3-display-topleft w3-fjalla w3-text-deep-orange">Chrom18</h1>\n'
    html += '      <h2 class="w3-padding w3-display-bottomleft w3-hide-small w3-text-white">Gene browser of \
                   the 18<sup>th</sup> chromosome in the 21<sup>st</sup> century</h2>\n'
    html += '      <img class="logo w3-image w3-display-right w3-hide-medium w3-hide-small" src="' + logo_path + '" alt="Logo">\n'
    html += '    </div>\n'
    return(html)

#******************************************************************************

def footer():
    '''
    Returns the footer of the website, essentially closing the <body> and <html> tags.
    '''
    html = ''
    html += '  </body>\n'
    html += '</html>\n'
    return(html)

#******************************************************************************

# The HTML tags added affect the way the CDSs are displayed
# They make the highlightText plugin functional

def dna_seq_format(dna_seq):
    '''
    Highlights in red CDSs in a DNA sequence. The start and end of a CDS must 
    be marked with '<' and '>' respectively. Also, add certain attributes to
    the strings so a jQuery plugin can be functional.
    '''
    import re
    rep = {"<": "</span><b class=\"w3-text-red\">", ">": "</b><span class=\"text\">"}
    rep = dict((re.escape(k), v) for k, v in rep.items())
    pattern = re.compile("|".join(rep.keys()))
    formatted_dna = pattern.sub(lambda m: rep[re.escape(m.group(0))], dna_seq)
    return(formatted_dna)

#******************************************************************************
 
def step_table():
    '''
    Populates an HTML table with entries from the database that agree with 
    the user's input.
    '''
    # This uses dummy data for now
    basic = retrieve_basic("accession", "1A")

    table = ''
    for i in range(len(basic[0])):
        table += '<tr onclick="document.location=\'' + details_accession_path + basic[0][i] + '\'" style="cursor:pointer">\n'
        table += '  <td>' + basic[0][i] + '</td>\n'
        table += '  <td>' + basic[2][i] + '</td>\n'
        table += '  <td>' + basic[3][i] + '</td>\n'
        table += '  <td>' + basic[1][i] + '</td>\n'
        table += '</tr>\n'
    return(table)

#******************************************************************************

def list_all_table():
    '''
    Populates an HTML table with all the entries from the database.
    '''
    # This uses dummy data for now
    all_entries = retrieve_all()

    table = ''
    for i in range(len(all_entries[0][0])):
        table += '<tr onclick="document.location=\'' + details_accession_path + all_entries[0][0][i] + '\'" style="cursor:pointer">\n'
        table += '  <td>' + all_entries[0][0][i] + '</td>\n'
        table += '  <td>' + all_entries[0][2][i] + '</td>\n'
        table += '  <td>' + all_entries[0][3][i] + '</td>\n'
        table += '  <td>' + all_entries[0][1][i] + '</td>\n'
        table += '</tr>\n'
    return(table)

#******************************************************************************

def codon_table():
    '''
    Populates an HTML table with the codon usage in a particular gene.
    '''
    table = ''
    codon_freq_dict = codon_freq_gene(radio, typed)  # Dummy data from config file
    for k, v in codon_freq_dict.items():
        if k != 'total':
            calc = v / codon_freq_dict['total'] * 100
            table += '    <tr>\n'
            table += '      <td>' + k + '</td>\n'
            table += '      <td>' + str(v) + '</td>\n'
            table += '      <td>' + str(round(calc, 2)) + '</td>\n'
            table += '    </tr>\n'
    return(table)

#******************************************************************************

def genome_codon_table():
    '''
    Populates an HTML table with the codon usage in chromosome 18.
    '''
    table = ''
    genome_freq_dict = whole_chrom_codons()
    for k, v in genome_freq_dict.items():
        if k != 'total':
            calc = v / genome_freq_dict['total'] * 100
            table += '    <tr>\n'
            table += '      <td>' + k + '</td>\n'
            table += '      <td>' + str(v) + '</td>\n'
            table += '      <td>' + str(round(calc, 2)) + '</td>\n'
            table += '    </tr>\n'
    return(table)

#******************************************************************************

# This function may not be used

def dna_seq_spacer(dna_seq_highlighted):
    '''
    Adds spaces every 10 characters in a string.
    '''
    new_string = ''
    counter = 0
    for i in range(0, len(dna_seq_highlighted), 10):
        new_string += dna_seq_highlighted[i+counter:i+counter+10] + ' '
        counter = 1
    return(new_string)
