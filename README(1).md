## Pipline of metabolic gene clusters (MGCs) extraction

## Extraction of HMMER3:
#### The porA genes were trained through HMMER3 and all the protein sequences were placed in the protein folder.
#### Search genes through the HMMER v3.3.2, take the porA as an example:
```
hmmsearch  --domtblout  result/genome_porA1.tab  -E 0.00001  --domT 0.5 --noali --acc --notextw --cpu 6  seed/porA/porA1.hmm   protein/genome.faa
```
```
hmmsearch  --domtblout  result/genome_porA2.tab  -E 0.00001  --domT 0.5 --noali --acc --notextw --cpu 6  seed/porA/porA2.hmm  protein/genome.faa
```
```
hmmsearch  --domtblout  result/genome_porA3.tab  -E 0.00001  --domT 0.5 --noali --acc --notextw --cpu 6  seed/porA/porA3.hmm  protein/genome.faa
```
#### Step 1, HMMER information extraction(the filter score is set to 200):
```
python3 HMM_info.py porA ./label ./data porA_results 200
```
#### Step 2, filter results according to gene synteny:
```
python HMM_synteny.py extracted_hmmer_results/6406_porA.txt porA_synteny.txt
```
#### Step 3, gene sequences extraction(nucleotides and proteins):
```
python3  HMM_seq.py  -i cds -f all_porA_out.txt -s species -o result_cds_porA
```
```
python3  HMM_seq.py  -i protein -f all_porA_out.txt -s species -o result_protein_porA
```

### Annotation and extraction through gutSMASH:
#### Download and install the gutSMASH python source from the GitHub repo: 
```
https://github.com/victoriapascal/antismash/tree/gutsmash
```
#### Step 1, annotation through gutSMASH:
```
python3  run_gutsmash.py --cb-knownclusters --enable-genefunctions  genomes/GCF_000954195.1_ASM95419v1_genomic.fna  --output-dir  gutSMASH_annotation/results_GCF_000954195.1_ASM95419v1_genomic  --genefinding-tool  prodigal  -c  16
```
#### Step 2, gene sequence extraction(nucleotides and proteins)：
```
python3 Gut_extractor.py -n porA -i gutSMASH_annotation -o porA_extraction
```


## Copyright
Jia Shulei, jiasl@im.ac.cn  
CAS Key laboratory of Pathogenic Microbiology and Immunology  
Institute of Microbiology, Chinese Academy of Sciences, Beijing 100101, China
School of Basic Medical Sciences, Tianjin Medical University, Tianjin, 300070, China
