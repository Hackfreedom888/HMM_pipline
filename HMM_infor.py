#!/bin/python3

import re
import os
import sys
import pandas as pd
from collections import defaultdict

def getHmmIndex(stext, target=' '):
    target_idnex = []
    i = 0
    for s in stext:
        if s == target:
            target_idnex.append(i)
        i+= 1
    return target_idnex

def main(file, out, score):
    infile = open(file)
    headers = {}
    score_left = 0
    score_right = 0
    idx_key = {}
    for line in infile:
        header_line = line.strip()
        if line.startswith('# target name'):
            total = 0
            file_index = 0
            if len(headers) == 0:
                sep_line = next(infile)
                sep_index = getHmmIndex(sep_line)
                start = 0
                for idx in sep_index:
                    key = line[start:idx].strip()
                    for i in range(1,10):
                        if key in headers:
                            key += str(i)
                    idx_key[idx] = key
                    headers[key] = []
                    if key == 'score':
                        score_left = start
                        score_right = idx
                    start = idx + 1 
                headers[line[start:].strip()] = []
                headers['file'] = []
            while True:
                line = next(infile).strip()
                if not line.startswith('#'):
                    if float(line[score_left:score_right].strip()) >= score:
                        #print (line)
                        total += 1
                        start = 0
                        file_index = 1
                        for idx in sep_index:
                            key = idx_key[idx]
                            headers[key].append(line[start:idx])
                            start = idx + 1
                        headers[header_line[start:]].append(line[start:])
                elif line.startswith('# Program') and total == 0:
                    break
                elif line.startswith('# Target file') and file_index == 1:
                    file_name = os.path.basename(line.split(' ')[-1]).strip()
                    for i in range(total):
                        headers['file'].append(file_name)
                    file_index = 0
                    total = 0
                elif line.startswith('# [ok]'):
                    break
    infile.close()
    out_data = pd.DataFrame(headers)
    out_data.to_csv(out, sep='\t', index=False)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print ('Usage: python3 HMM_infor.py hmmsearch_result out_file score')
        sys.exit()
    main(sys.argv[1], sys.argv[2], int(sys.argv[3]))