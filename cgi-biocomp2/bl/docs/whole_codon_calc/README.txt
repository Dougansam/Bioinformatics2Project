all files in this folder relate to the production of the whole genome cds frequency.

run whole_chrom_codon_freq_counter.py with the chrom_CDS_18 in the same folder. This generates
a text file containing the DNA and outputs a dictionary that contains the entire chromosomes codon
frequencys.


{'total': 139467, 'tct': 3094, 'aga': 3059, 'gat': 2000, 'tta': 3194, 'ttc': 2797,
 'aca': 2419, 'aat': 3406, 'tat': 2957, 'cca': 2435, 'gtt': 2241, 'cat': 2540, 'tca': 2646,
 'ctg': 2701, 'tag': 1917, 'act': 2250, 'cag': 2687, 'gaa': 2673, 'agc': 1885, 'att': 3689,
 'ttt': 6009, 'tcc': 2110, 'tga': 2883, 'ata': 2720, 'aag': 2656, 'ttg': 2832, 'cta': 1689,
 'ctt': 2914, 'cac': 1918, 'taa': 2963, 'caa': 2362, 'tgc': 1936, 'tgt': 3062, 'atg': 2439,
 'gtg': 2075, 'agt': 2457, 'tgg': 2600, 'ggc': 1573, 'gga': 2165, 'gag': 2246, 'agg': 2359,
 'gac': 1241, 'gtc': 1250, 'ctc': 2204, 'gca': 1858, 'gta': 1786, 'aaa': 4990, 'acc': 1569,
 'atc': 1846, 'ccc': 1760, 'cct': 2533, 'gct': 1954, 'ccg': 519, 'gcc': 1655, 'acg': 349,
 'tac': 1589, 'aac': 1949, 'tcg': 363, 'ggg': 1686, 'ggt': 1640, 'cgt': 407, 'cgc': 444,
 'cga': 372, 'cgg': 482, 'gcg': 463}

'total' is the total codons counted by the program and each codon has been given a number of times it appears
in the whole genome.

written by Sam Dougan
