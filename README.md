# Pipeline-Project1
 
Documentation. Include what tools need to be installed (dependencies) to run your code and how to run the code in your GitHub repo’s README. 

Part 1: 


Part 2:
This section will require kallisto to be installed before running the script. Biopython, Argparse, Seq.IO and subprocess will also needed to be imported to run the script. 
This section will also need to have the Genbank file downloaded from the 
The syntax needed to run this code will look like this: python /home/ksandoval/Pipeline1/Pipeline1_part2.py /home/ksandoval/Pipeline1/NC_006273.2.gb : where the terminal will need the python script and the Genbank file to run. 

Part 3: 
This part will require the index created in the previous step to be quantified using > time kallisto quant -i kallisto_index -o DRR00XX -b 30  -4  path/to/Fastq1/and /Fastq2/files> in the terminal. This will create new directories for each sample. 
The script will take the abundance file created in the directory for each sample and extract the TPM values to calculate the statistics. The tool needed for this step is kallisto. Import os, numpy and argprase. The syntac to run this code will look like: 
 python part3_script path/to/directory. 

Part 4:


Part 5:



