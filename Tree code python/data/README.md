## sequences

I got the sequences from Tyler with the following notes
> I used the base set of CoV RBD sequences used in the phylogeny presented in our DMS manuscript (sequences [here](https://github.com/jbloomlab/SARS-CoV-2-RBD_DMS/blob/master/data/alignments/unaligned-sequences/RBD_nt.fasta)), which consiste of the curated set of SARS-related CoV RBD sequences from [Letko et al. 2020](https://www.nature.com/articles/s41564-020-0688-y), supplemented with newly described SARS-CoV-2-clade sequences from bat and pangolin.
Beyond that, I want to use this analysis to better define the relationship among SARS-CoV-1 epidemic isolates. To do this, I downloaded all sequences given in Supplementary Table 1 from [Song et al. 2005](https://www.pnas.org/content/102/7/2430). I parsed these sequences to their RBD nt sequences, and used the `cd-hit` program to eliminate any identical RBD nt sequences from within this SARS-CoV-1 set. (I have this program downloaded on my local laptop, so this was all done there). This yielded 15 unique SARS-CoV-1 sequecnes between the civet and human isolates.
I then updated the header names to conform with the nomenclature used for the SARS-related isolates (`name_accession`), adding to the name the helpful nomenclature used by Song et al. to distinguish civet (`PC`) and human (`HP`) sequences from the main 2002-2003 (`03`) or sporadic 2003-2004 (`04`) outbreaks, and indicating "Early" (`E`), "Middle" (`M`), or "Late" (`L`) epidemic phase for sequences within the primary 2002-2003 epidemic.
I concatenated this expanded SARS-CoV-1 set with the SARS-related CoV sequences from before. This yields the final set of 51 RBD nt sequences included in the `./unaligned-sequences/RBD_nt.fasta` file. I also translated each nt sequence to its amino acid sequence, which is saved in the file `.unaligned-sequences/RBD_aa.fasta`.
> To do the alignment, I did amino acid alignments in mafft, and then used PAL2NAL to align the underlying nt sequences according to the AA alignment

For a full description of the alignment and how it was made, see https://github.com/jbloomlab/computational_notebooks/tree/master/tstarr/2020/SARSr-CoV_homolog_survey/RBD_ASR

I got the sequences on 8/6/20.

SKH notes: I removed the outgroup `Hp-BCoV_Zhejiang_2013_KF636752` and I changed the codon with the amb. nt in the pangolin sequences into a gapped position.

## preferences

https://media.githubusercontent.com/media/jbloomlab/SARS-CoV-2-RBD_DMS/master/results/single_mut_effects/single_mut_effects.csv
