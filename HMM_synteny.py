# 运行代码：python HMM_synteny.py extracted_hmmer_results/6406_porA.txt porA_synteny.txt
# !/bin/python3

import sys
from collections import defaultdict
import json

infile = sys.argv[1]
outfile = sys.argv[2]
# dict_ko = {"porA1": 1, "porA2": 1, "porA3": 1}
# count = {}
dict_data = {}
data = defaultdict(list)
# target = []
in_file = open(infile)
for line in in_file:
    line_info = line.strip().split('\t')
    if line_info[0] in dict_data:
        dict_data[line_info[0]]["data"].append(line)
    else:
        dict_data[line_info[0]] = {"data": [line], "dict_ko": {"porA1": 1, "porA2": 1, "porA3": 1}}
    if line_info[2] in dict_data[line_info[0]]["dict_ko"]:
        dict_data[line_info[0]]["dict_ko"][line_info[2]] = 0

in_file.close()

out_file = open(outfile, 'w')

for key in dict_data:
    if len(dict_data[key]["data"]) >= 3:
        cout_flag = True
        for ko_key in dict_data[key]["dict_ko"]:
            if dict_data[key]["dict_ko"][ko_key] == 1:
                cout_flag = False
        if cout_flag == True:
            for line in dict_data[key]["data"]:
                out_file.write(line)
out_file.close()
