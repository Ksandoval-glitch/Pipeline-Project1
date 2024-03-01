query_seqfile = "/home/ksandoval/ncbi_dataset/data/Human_betaherpesvirus_5_seqeunce.fasta"
output_file = 'pipeline_part5_results.csv'
blast_command = 'tblastn -query ' +query_seqfile+' -db pipeline_part5db -out ' +output_file+' -outfmt "10 sacc pident length qstart qend sstart send bitscore evalue stitle"' 



import os 
os.system(blast_command)