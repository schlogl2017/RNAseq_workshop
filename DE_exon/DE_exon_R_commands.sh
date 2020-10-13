R
# further reading
# https://bioconductor.org/packages/release/bioc/vignettes/DEXSeq/inst/doc/DEXSeq.html
#to install the DEXSEQ package:

if (!requireNamespace("BiocManager", quietly = TRUE))
    install.packages("BiocManager")

BiocManager::install("DEXSeq")

# set the working directory to where you want:
# in Rstudio you can do this easily with File, new project
setwd("/Users/pjt6/Documents/RNAseq_workshop/DE_exon")

# Make sure all the files are decompressed. (gunzip file.gz)

# check it
getwd()

# load the R package that does the DE exon analysis
library("DEXSeq")

inDir = '/Users/pjt6/Documents/RNAseq_workshop/DE_exon'

countFiles = list.files(inDir, pattern=".exon.counts$", full.names=TRUE)

# show is the files that it found
basename(countFiles)

# this is the gff file, (genome feature files) which contains the exon - to gene info
flattenedFile = list.files(inDir, pattern="gff$", full.names=TRUE)

basename(flattenedFile)


	# create a sample table of our conditons and the replicas
# pairend is the library prep type.			
				#cherry gallium			
sampleTable = data.frame(row.names = c("Mc_PR_Cherry_1", "Mc_PR_Cherry_2", "Mc_PR_Cherry_3", "Mc_PR_Galium_1", "Mc_PR_Galium_2", "Mc_PR_Galium_3", "Mc_PR_cress_1", "Mc_PR_cress_2", "Mc_PR_cress_3"), condition = c("Mc_PR_Cherry", "Mc_PR_Cherry", "Mc_PR_Cherry", "Mc_PR_Galium", "Mc_PR_Galium", "Mc_PR_Galium", "Mc_PR_cress", "Mc_PR_cress", "Mc_PR_cress"),libType = c("paired-end", "paired-end", "paired-end", "paired-end", "paired-end", "paired-end", "paired-end", "paired-end", "paired-end"))
			
# see the sample table
sampleTable

######################################################################################################

# this is a more complex experimental design where the exon and sample (plant host type) is compared
# (condition:exon is an interation term under stood in R statistics). 
dxd = DEXSeqDataSetFromHTSeq(countFiles,sampleData=sampleTable,design= ~ sample + exon + condition:exon,flattenedfile=flattenedFile)

# create a file with gene name, grep genome.gff | cut -f gene_name > geneIDsinsubset.txt
# if you want to run this on a smaller number of genes then you can control the list here
genesForSubset = read.table(file.path(inDir, "geneIDsinsubset.txt"),stringsAsFactors=FALSE)[[1]]


dxd = dxd[geneIDs( dxd ) %in% genesForSubset,]

colData(dxd)


# lots at the first 5 entries
head( counts(dxd), 5)

head( featureCounts(dxd), 5) 

head ( rowRanges(dxd), 3 )

sampleAnnotation( dxd )

####################################################################################################################################################################################
4) normalisation

# can use multiple core if using  package BiocParallel,  and  implemented  the BPPARAM


BPPARAM = MultiCoreParam(workers=3)

# uses DEseq2 method (control for the different lib sizes - sequencing depths)
dxd = estimateSizeFactors( dxd )


# dispersion estimation -  estimate the technical variation - THIS IS SUPER SLOW
dxd = estimateDispersions( dxd)

# multi core -  you can run this in multi threaded mode. - Never worked for me!!
#dxd = estimateDispersions( dxd, BPPARAM=BPPARAM)

# this graph represents per-exon dispertion estimates vs the mean normalised count.
# Then the fitted line is added which has been used to normalise the data set for 
# technical variation. 
plotDispEsts( dxd )

# Now we have worked out the dipersion of the data (estimates of ...), technical variation,
# we have worked ou tthe size factors which is a result of different sequecing depths of 
# the raw data. A generalised linear model is used to fit the data. 
# test for DE (exon) expression for each exon in each gene
dxd = testForDEU( dxd )

		# multi core
		dxd = testForDEU( dxd, BPPARAM=BPPARAM)



# estimate fold change per exon based on the condition. This is based on the formula and the GLM. 
dxd = estimateExonFoldChanges( dxd, fitExpToVar="condition")

# get the results and store in a variable called dxr1
dxr1 = DEXSeqResults( dxd )

# see the datadxr1

dxr1

# get a description of each coloumn:
mcols(dxr1)$description

# write ou the full results table
write.table(dxr1, file = "Dexseq_results.out", append = FALSE, quote = TRUE, sep = "\t",
            eol = "\n", na = "NA", dec = ".", row.names = TRUE,
            col.names = TRUE, qmethod = c("escape", "double"),
            fileEncoding = "")

dxr1

#From this object, we can ask how many genes are significant with a false discovery rate of 5%:
table ( dxr1$padj < 0.05 )

#From this object, we can ask how many genes are significant with a false discovery rate of 1%:
table ( dxr1$padj < 0.01 )

# ask how many genes are affected (FDR 0.001)
table ( tapply( dxr1$padj < 0.001, dxr1$groupID, any ) )

# MA lot: plot the log of fold change vs the average normalised count per exon. Red are exons
# considered significant. 
plotMA(dxr1, cex=0.8)



####################################################################################################################################################################################
4) visualization
# put in the appropriate gene name of interest!!!!!!!

#plotDEXSeq( dxr1, "FBgn0010909", legend=TRUE, cex.axis=1.2, cex=1.3, lwd=2 )

plotDEXSeq( dxr1, "1005", displayTranscripts=TRUE, legend=TRUE, cex.axis=1.2, cex=1.3, lwd=2 )


# WRITE TO BROWSEABLE HTML USING DEXSeqHTML
#
DEXSeqHTML( dxr1, FDR=0.001)

