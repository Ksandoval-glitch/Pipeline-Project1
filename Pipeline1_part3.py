### Goal ####
#1.) already created the new Direcotries with Kallisto with their own directories 
#2.) Quanitfy the TPM for each CDS from the results in each adbundance.tsv file in each directory
#.3) Perform biostats to get the minimum, median, mean, maximum TPM 

import os
import numpy as np
import argparse


#This function will take the abundance file and extract the TPM values from the 4th column of each line. 
#It will then calculate the statistics of the TPM then return the stats as a dictionary
def calculate_tpm_statistics(abundance_file):
    tpm_values = [] # Intializes an empty list to store TPM values that are extracted from the abundance file. 
    with open(abundance_file, 'r') as f: # opening the abundance file 
        next(f)  # This will skip oover the first line to skip the header
        for line in f: # This will iterate over the next lines in the file 
            fields = line.strip().split('\t') # This will strip the leading and trailing whitespace and split the lines using \t as the delimiter
            tpm_values.append(float(fields[4]))  # This converts the fifth field from the fields list to a float and appends it to the tpm values list
    return {
        'Minimum TPM': np.min(tpm_values),
        'Median TPM': np.median(tpm_values),
        'Mean TPM': np.mean(tpm_values),
        'Maximum TPM': np.max(tpm_values)  # This will return a dictionary containing all of the statistics calculated from the tpm values list. 
    }
    
# This function will take a list of directories as an input to construct a path to the abundance file. 
# If the file is there, it will call the definition function above. It will also make a log with the sample name and TPM stats and saves it. 
# if the abundance file isnt found, it will produce an error message. 
def main(sample_dirs):
    header = ['Sample', 'Minimum TPM', 'Median TPM', 'Mean TPM', 'Maximum TPM'] # this line will define a list containing the column headers for the log file. 
    with open('Pipeline_log3.txt', 'w') as log_file: # this will open / write the Pipeline log3 file
        log_file.write('\t'.join(header) + '\n') #  this line will write the header to the log file with the header list
        for sample_dir in sample_dirs: #  To iterate over each direcotry path in the list 
            sample_name = os.path.basename(sample_dir) #This ill extract the base name of each directory and assigns it as the sample name
            abundance_file = os.path.join(sample_dir, 'abundance.tsv') # this will construct the path to the abundance file in the directory provided 
            if os.path.exists(abundance_file): # this will double check to make sure an abdundance file is there 
                tpm_stats = calculate_tpm_statistics(abundance_file) # This line will call the tpm stat function above 
                log_line = [sample_name] + [str(tpm_stats[key]) for key in header[1:]] # This will create a list of the sample name followed by the TPM stats which are converted to a string. 
                log_file.write('\t'.join(log_line) + '\n')  # this will write the log line to the log file 
            else:
                print(f"Abundance file not found for sample {sample_name}.") # this will produce a manual error message 

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate TPM statistics for each sample.")
    parser.add_argument("sample_dirs", nargs='+', help="List of directories containing kallisto output for each sample")
    args = parser.parse_args()
    
    main(args.sample_dirs)
