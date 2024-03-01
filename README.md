# Pipeline-Project1
 
Documentation. Include what tools need to be installed (dependencies) to run your code and how to run the code in your GitHub repo’s README. 

Part 1: 
In this step, you will need to download the fastq files from the SRA tab of NCBI. This can be down by using < wget sra_location_address >. Next, the files must be unzipped. Using < fastq-dump -I -split-files -SR00XXX > in the terminal will prodsuce 2 paired end fastq files. 

Part 2:
This section will require kallisto to be installed before running the script. Biopython, Argparse, Seq.IO and subprocess will also needed to be imported to run the script. 
This section will also need to have the Genbank file downloaded. 
The syntax needed to run this code will look like this: python /home/ksandoval/Pipeline1/Pipeline1_part2.py /home/ksandoval/Pipeline1/NC_006273.2.gb : where the terminal will need the python script and the Genbank file to run. 

Part 3: 
This part will require the index created in the previous step to be quantified using > time kallisto quant -i kallisto_index -o DRR00XX -b 30  -2  path/to/Fastq1/and /Fastq2/files> in the terminal. This will create new directories for each sample. 
The script will take the abundance file created in the directory for each sample and extract the TPM values to calculate the statistics. The tool needed for this step is kallisto. Import os, numpy and argprase. The syntac to run this code will look like: 
 python part3_script path/to/directory. 

Part 4:
The first step in part 4 is to make a space delimited text file formatted like this: 

sample condition path
SRR5660030 HCMV /home/ksandoval/DRR5660030
SRR5660033 HCMV /home/ksandoval/DRR5660033
SRR5660044 HCMV /home/ksandoval/Pipeline1/DRR5660044
SRR5660045 HCMV /home/ksandoval/DRR5660045 



This step will require sleuth and kallisto to be installed. pipeline_part4.R script should be run to produce the most significant results. 

Part 5:
Using the top hit (YP_081530.1), place that in the NCBI database and select the top hit which should be YP_081530.1. Then download the blast file from the "sent to" option in the top right corner of the webpage in a FASTA file format. 
And use "datasets download virus genome taxon 10359"  to download the genome directly from NCBI from the terminal. 10359 is the taxon id for the Betaherpesvirinae-5 family. 
then perform " unzip ncbi_dataset.zip" to unzip the file downloaded from NCBI. 
Next, make a local database from the unzipped ncbi file with "makeblastdb -in genomic.fna -out pipeline_part5db -title pipeline_part5db -dbtype nucl " 




