library(sleuth)
library(dplyr)

#Reading in the required table for Sleuth describing the sample, the conditon, and the location to the kallisto directory results. 
s2c <- read.table("pipeline_part4.txt",header=TRUE,stringsAsFactors=FALSE)
# Initialize sleuth object using sleuth_prep function from sleuth library
so <- sleuth_prep(s2c, extra_bootstrap_summary = TRUE)
# Fit a model comparing the two conditions of 2DPI and 6DPI
so <- sleuth_fit(so, ~condition, 'full')
#fit the reduced model to compare in the likelihood ratio test
so <- sleuth_fit(so, ~1, 'reduced')
#perform the likelihood ratio test for differential expression between conditions 
so <- sleuth_lrt(so, 'reduced', 'full')
# Extract the test results from the sleuth object 
sleuth_table <- sleuth_results(so, 'reduced:full', 'lrt', show_all = FALSE)
# Filter most significant results where the q val is less than or equal to 0.5 then selects the columns named traget_id, test-stat, pval, and qval. 
sleuth_significant <- dplyr::filter(sleuth_table, qval <= 0.05) %>% dplyr::select(target_id, test_stat, pval, qval)
#this will print the top 10 hits of the most significant results 
sleuth_significant <- head(sleuth_significant, n = 10)
# this will create a log_file to save the most significant 
write.table(sleuth_significant,"log_file4.txt.txt",quote=F,row.names=F,sep="\t")
