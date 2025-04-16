# SeqSender-BPHL
The modified SeqSender specifically for Florida BPHL to upload data to NCBI.       
The modified version can log in directly to FL-BPHL's ftp directory.             
  
## Installation
Clone repository
```
Create your conda environment
Navigate to seqsender-BPHL/
Execute the command below, and a conda environment named seqsender will be created.    
```
conda env create -f env.yaml
```
conda activate seqsender

### Prepare Data and Files for NCBI Submission
Note: All file templates can be found in /prepare.
Create a folder with a unique name, such as date_location_2batch. Copy all files and folders from /prepare to the new folder.

Place the FASTQ files in the /raw_reads/ directory.

Fill out the following templates with the necessary information:

config_template_bs.yaml
config_template_sra.yaml
metadata_template_bs.csv
metadata_template_sra.csv

The SPUID_NAMESPACE is used to identify the submitter. The username and password are provided by NCBI for the center account FTP server submission.

If submitting SRA samples with known BioSample accessions, add a column named biosample_accession to the SRA metadata file.


#### Run commands for NCBI submission
1. biosample upload
python /path/to/SeqSender-BPHL/seqsender-BPHL/seqsender.py submit --organism '{FLU,COV,POX,ARBO,RSV,OTHER}' --biosample --submission_name 'folder name' --submission_dir /path/to/SeqSender-BPHL/ --config_file config_template_bs.yaml --metadata_file metadata_template_bs_.csv

2. sra upload
python /path/to/SeqSender-BPHL/seqsender-BPHL/seqsender.py submit --organism '{FLU,COV,POX,ARBO,RSV,OTHER}' --sra --submission_name 'folder name' --submission_dir /path/to/SeqSender-BPHL/ --config_file config_template_sra.yaml --metadata_file metadata_template_sra.csv

3. check status
python /path/to/SeqSender-BPHL/seqsender-BPHL/seqsender.py submission_status --submission_dir /path/to/SeqSender-BPHL/ --submission_name 'folder name'


For more information:
python /path/to/SeqSender-BPHL/seqsender-BPHL/seqsender.py -h

              
               
##### Note 
1: The original SeqSender can be found in https://github.com/CDCgov/seqsender/tree/master

2: More detailed introduction about how to prepare for config.yaml and metada.csv files can be found in https://cdcgov.github.io/seqsender/
