# SeqSender-BPHL
The modified SeqSender specifically for Florida BPHL to upload data to NCBI
## How to run
### Prepare data and files for NCBI submission
Note: all file templates can be found in /prepare.      
1) Put fastq files in /prepare/raw_reads/        
2) Fill out config_template_bs.yaml, config_template_sra.yaml, metadata_template_bs.csv, metadata_template_sra.csv
### Run commands for NCBI submission
1) In a terminal, jump to the directory of /seqsender-BPHL/seqsender-BPHL/
2) Run any command listed in /prepare/commands in the current directory.

              
               
#### Note 1: the original SeqSender can be found in https://github.com/CDCgov/seqsender/tree/master
#### Note 2: More detailed introduction about how to prepare for config.yaml and metada.csv files can be found in https://cdcgov.github.io/seqsender/
