### Goal Part 1 ###
#1.) Get the Genbank file from NCBI
#2.) parse the genbank file for all of the Cds
#3.) make a fasta file with biopython 
#4.) Use Kallisto to build the transcripte index from the fasta file. 
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
import subprocess
import argparse

def main(genbank_file):
    try: # I used this try function to try to find some errors I was encountering. Its a way to help witht e debugging process 
        print("Parsing GenBank file...") # This would print a message saying the GenBank file is being parsed. 
        cds_records = [] # This will initialize the cDs records to store SeqRecords later on. 
        for record in SeqIO.parse(genbank_file, "genbank"): #this will go over each record in the GenBank File using SeqIO.Parse 
            for feature in record.features: #  This will go over every feature in the SeqIO Parse
                if feature.type == "CDS": #this will check if the feature is in the CDS. 
                    if "protein_id" in feature.qualifiers: #This will check to see if the feature has a protein_id Qualifer 
                        protein_id = feature.qualifiers["protein_id"][0] # This will get the protein ID from the CDS
                        cds_seq = feature.location.extract(record).seq # This line will take out the coding sequence of the CDS. 
                        cds_records.append(SeqRecord(cds_seq, id=protein_id, description="")) # This line will make a SeqRecord for the CDS seqeunce 
                                                                                                #with the protien ID as the identifer and appends that to the cds_records list I initalized in the beginning. 
        
        print(f"The HCMV genome (NC_006273.2) has {len(cds_records)} CDS") # this will print the number of CDS records found

        fasta_file = "hcmv_cds.fasta" #This is to set the filename for the FASTA file which will be made this part can be updated to match the genome name of the organism 
        print(f"Writing to FASTA file: {fasta_file}") #Prints a message saying that the fasta a file will be saved 
        SeqIO.write(cds_records, fasta_file, "fasta") # this line will write the CDS records to the FASTA File in the fasta format
        
        index_name = "hcmv_kallisto_index" # This will make the index name for Kallisto
        print(f"Building kallisto index: {index_name}") # This will print a message saying that the kallisto index is being built and the name of it. 
        subprocess.run(["kallisto", "index", "-i", index_name, fasta_file]) # This will a run the kallisto command to buiild the index using the fasta file I created 
        
        with open("Pipeline_log2.txt", "w") as log_file: # this will write aq file named Part2 that specifically defines the nymber of Coding Sequernces based on the len of the CDS records list. 
            log_file.write(f"The HCMV genome (NC_006273.2) has {len(cds_records)} CDS")
        
        print("Process completed successfully.") # this lets me know that my code ran without a problem. If a message didnt print before this, I can try to debug where it went wrong. 
    except Exception as e:
        print(f"An error occurred: {e}") # I get the error message printed, I was havign issues with no error message being printed but no outcome either. 

if __name__ == "__main__": #This will set the following script as the main program so I can run the script from the command line/ 
    parser = argparse.ArgumentParser(description="Build HCMV transcriptome index using kallisto.") #
    parser.add_argument("genbank_file", help="Path to the GenBank file for HCMV") # this will make a path for the GenBank file
    args = parser.parse_args() #parses the command line arguments 
    
    main(args.genbank_file) # calls the main function with the genbank file path to begin the process. 
