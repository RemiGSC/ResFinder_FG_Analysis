# ResFinder_FG_Analysis
Scripts for the analysis included in the manuscript

## Version comparison
Number of ARGs found in ResFinderFG v2.0 and v1.0 was compared using the following scripts :  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- **comparison_atb_rfg1vs2.py**  (to compare gene numbers regarding antibiotic families)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- **comparison_source_rf1vs2.py** (to compare gene numbers regarding original sample source)  
Then, **comparison_plot.Rmd** was used with R to generate the figure.

## Abricate analysis
Abricate was use with default parameters and 5 different antibiotic resistance genes databases (ResFinderFG v2.0, ResFinder 4.0, CARD, ARG-ANNOT and NCBI) to detect antibiotic resistance genes in 3 global microbial gene catalog (GMGC, https://gmgc.embl.de/download.cgi):  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;> Human gut  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;> Soil  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;> Water (freshwater + marine)  

## Antibiotic families classification
Antibiotic families were chosen using a deduplicated list of gene names obtained with each database and specific gene classification tables were made for each database. 

## Abricate results comparison regarding database used
Unigene hits were then categorized by gene catalog and information such as gene families (with the need of database specific gene classification table) were added using the folowing scripts :  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- **script_hits_retriever_gut.py**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- **script_hits_retriever_soil.py**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- **script_hits_retriever_water.py**  
And all the unigene hits obtained within one environment were concatenated into one table :  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;> hits_gut_all.csv  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;> all_soil.csv  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;> all_water.csv  
To generate the upset plots, first, duplicate unigene_hits were remove using the script duplicate.py
Then, the following R scripts were used :  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- **upset_gut.rmd**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- **upset_soil.rmd**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- **upset_water.rmd**  
Upset plot generated were :  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;> upset_gut.jpeg  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;> upset_soil.jpeg  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;> upset_water.jpeg  

To retrieve statistics such as number of unigene hits, specific unigene hits regarding database used and antibiotic families, we used **stats_extract_dataframe_upset.py**
Retrieved statistics were then written in the stats.csv tables.  

## Specific unigene hits gene names
First, specific unigene hits were retrieved using : **exclusive_genes.py**  
Second, gene names were retrieved using **specific_gene_names.py**  
