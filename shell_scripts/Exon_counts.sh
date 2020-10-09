#!/bin/bash
#$ -V ## pass all environment variables to the job, VERY IMPORTANT
#$ -N unicycler ## job name
#$ -S /bin/bash ## shell where it will run this job
#$ -j y ## join error output to normal output
#$ -cwd ## Execute the job from the current working directory
#$ -pe multi 4

# https://github.com/rrwick/Unicycler#quick-usage
cd $HOME

# to activate the software, paste the following in your terminal (with the dot):
. /shelf/apps/pjt6/conda/etc/profile.d/conda.sh 

# copy (cp) all (-rv) the training files to your home directory (~/)
#cp -rv /shelf/Computational_Genomics/genome_assembly_workshop/ ~/
wait

conda activate unicyclerENV

cd $HOME/genome_assembly_workshop/

unicycler -1 $HOME/genome_assembly_workshop/reads/ERR861370_1.fastq.gz \
    -2 $HOME/genome_assembly_workshop/reads/ERR861370_2.fastq.gz \
    -o unicycler -t 4 

