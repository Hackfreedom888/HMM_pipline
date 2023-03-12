Extraction pipline of biosynthetic gene clusters (BGCs)

Extraction of HMMER:
#The porA1-A3 genes were trained through HMMER and all the protein sequences were placed in the protein folder.
#Search genes through the HMMER v3.3.2, take the porA as an example:
for i in `less protein.txt`;
do
        hmmsearch  --domtblout  result/${i}_porA1.tab  -E 0.00001  --domT 0.5 --noali --acc --notextw --cpu 4  SEED/porA/porA1.hmm   protein/${i}.faa
        hmmsearch  --domtblout  result/${i}_porA2.tab  -E 0.00001  --domT 0.5 --noali --acc --notextw --cpu 4  SEED/porA/porA2.hmm  protein/${i}.faa
        hmmsearch  --domtblout  result/${i}_porA3.tab  -E 0.00001  --domT 0.5 --noali --acc --notextw --cpu 4  SEED/porA/porA3.hmm  protein/${i}.faa;
done

step1, HMMER information extraction(the score is set to 200):
python3 HMM_info.py porA ./label ./data porA_results 200

step2, filter results according to gene synteny:
python HMM_synteny.py extracted_hmmer_results/6406_porA.txt porA_synteny.txt

step3, gene sequences extraction(nucleotides and proteins):
python3  HMM_seq.py  -i cds -f all_porA_out.txt -s species -o result_cds_porA
python3  HMM_seq.py  -i protein -f all_porA_out.txt -s species -o result_protein_porA


Extraction of gutSMASH:
#First of all, download and install the gutSMASH python source from the GitHub repo: 
https://github.com/victoriapascal/antismash/tree/gutsmash

#step1, annotation through gutSMASH:
python3  run_gutsmash.py --cb-knownclusters --enable-genefunctions  genomes/GCF_000954195.1_ASM95419v1_genomic.fna  --output-dir  gutSMASH_annotation/results_GCF_000954195.1_ASM95419v1_genomic  --genefinding-tool  prodigal  -c  16

#step2, gene sequences extraction(nucleotides and proteins)：
python3 Gut_extractor.py -n porA -i gutSMASH_annotation -o porA_extraction
