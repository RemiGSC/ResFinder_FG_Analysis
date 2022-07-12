# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 15:58:10 2022

@author: remi.gschwind
"""
#### SCRIPT DATABASE COMPARISON OF ARGs DETECTION IN GMGC water CATALOG ####

# First, a list of the GMGC water catalog genes is made
i_water1 = "C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_Analysis/analysis0422/data/subcatalogs_GMGC10.freshwater.95nr.fna"
i_water2 = "C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_Analysis/analysis0422/data/subcatalogs_GMGC10.marine.95nr.fna"
water_gene = []
with open(i_water1 , 'r') as f :
    for line in f :
        if ">" in line :
            water_gene.append(line.strip().split(">")[1])
with open(i_water2 , 'r') as f :
    for line in f :
        if ">" in line :
            water_gene.append(line.strip().split(">")[1])

#-----------ResFinderFG-----------#
i_rfg = "C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_Analysis/analysis0422/data/all_hamronized_abricate_resfinderfg.txt"
o_rfg_water = "C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_Analysis/analysis0422/output/rfg_water.csv"
i_gene_rfg = "C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_Analysis/analysis0422/data/ResFinderFG_gene_classified.csv"

# ARGs found in ResFinderFG are put in list.
aminoside = [] ; bacitracin = [] ; blactamase = [] ; cancer = [] ; colistin = [] ; aminocoumarin = []
cycline = [] ; cycloserine = [] ; edein = [] ; efflux = [] ; fosfomycin = [] ; fus_acid = [] ; bicyclomycin = []
glycopeptide = [] ; MLS = [] ; mupirocin = [] ; nitro = [] ; nucleoside = [] ; blactam_non_enz = []
peptide = [] ; phenicol = [] ; quinolone = [] ; rifampicin = [] ; bleomycin = [] ; Multidrug = [] ; Multidrug_efflux = []
streptothricin = [] ; sulfonamide = [] ; Tetracenomycin = [] ; Disinfecting_agents_and_antiseptics = []
factumycin = [] ; Fatty_acid = []
with open(i_gene_rfg , 'r') as f :
    for line in f :
        if "aminocoumarin;" in line :
            aminocoumarin.append(line.strip().split(";")[1])
        if "aminoside;" in line :
            aminoside.append(line.strip().split(";")[1])
        if "bicyclomycin;" in line :
            bicyclomycin.append(line.strip().split(";")[1])        
        if "blactam_non_enz;" in line :
            blactam_non_enz.append(line.strip().split(";")[1])
        if "blactamase;" in line :
            blactamase.append(line.strip().split(";")[1])        
        if "bleomycin;" in line :
            bleomycin.append(line.strip().split(";")[1])           
        if "cycline;" in line :
            cycline.append(line.strip().split(";")[1])
        if "Disinfecting_agents_and_antiseptics;" in line :
            Disinfecting_agents_and_antiseptics.append(line.strip().split(";")[1])
        if "edein;" in line :
            edein.append(line.strip().split(";")[1])
        if "factumycin;" in line :
            factumycin.append(line.strip().split(";")[1])
        if "Fatty_acid;" in line :
            Fatty_acid.append(line.strip().split(";")[1])
        if "fosfomycin;" in line :
            fosfomycin.append(line.strip().split(";")[1])
        if "fusidic acid;" in line :
            fus_acid.append(line.strip().split(";")[1])
        if "Glycopeptide/cycloserine;" in line :
            glycopeptide.append(line.strip().split(";")[1])
        if "MLS;" in line :
            MLS.append(line.strip().split(";")[1])
        if "Multidrug;" in line :
            Multidrug.append(line.strip().split(";")[1])
        if "Multidrug_efflux;" in line :
            Multidrug_efflux.append(line.strip().split(";")[1])
        if "mupirocin;" in line :
            mupirocin.append(line.strip().split(";")[1])
        if "nitroimidazole;" in line :
            nitro.append(line.strip().split(";")[1])            
        if "nucleoside;" in line :
            nucleoside.append(line.strip().split(";")[1])            
        if "peptide;" in line :
            peptide.append(line.strip().split(";")[1])            
        if "phenicol;" in line :
            phenicol.append(line.strip().split(";")[1])
        if "quinolone;" in line :
            quinolone.append(line.strip().split(";")[1])
        if "rifampicin;" in line :
            rifampicin.append(line.strip().split(";")[1])
        if "streptothricin;" in line :
            streptothricin.append(line.strip().split(";")[1])
        if "Sulfonamide/trimethoprim;" in line :
            sulfonamide.append(line.strip().split(";")[1])
        if "Tetracenomycin;" in line :
            Tetracenomycin.append(line.strip().split(";")[1])            


# ARGs found in water_gene list and in abricate results file are pooled in a list with :
    # GMGC_id ; db ; seqid ; ARG ; ATB_fam 
rfg_water = []
info = []
x = 0
y = 4537
with open(i_rfg , 'r') as f :
 	for line in f :
         if "resfinderfg" in line :
             x+=1
             cutline = line.strip().split("	")[3]
             gene = cutline.strip().split("\"")[1]
             rfg_water.append(line.strip())
             if line.strip().split("	")[10] in water_gene :
                 print(gene , (x/y)*100)
                 if gene in aminocoumarin :
                    info.append(line.strip().split("	")[10] + ";" + line.strip().split("	")[4] 
                                + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                + ";" + "aminocoumarin")
                 if gene in aminoside :
                    info.append(line.strip().split("	")[10] + ";" + line.strip().split("	")[4] 
                                + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                + ";" + "aminoside")
                 if gene in bicyclomycin :
                    info.append(line.strip().split("	")[10] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "bicyclomicin")
                 if gene in blactam_non_enz :
                    info.append(line.strip().split("	")[10] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "blactam_non_enz")
                 if gene in blactamase :
                    info.append(line.strip().split("	")[10] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "blactamase")
                 if gene in bleomycin :
                    info.append(line.strip().split("	")[10] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "bleomycin")                      
                 if gene in cycline :
                    info.append(line.strip().split("	")[10] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "cycline")
                 if gene in Disinfecting_agents_and_antiseptics :
                    info.append(line.strip().split("	")[10] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "Disinfecting_agents_and_antiseptics")                      
                 if gene in edein :
                    info.append(line.strip().split("	")[10] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "edein")
                 if gene in Fatty_acid :
                    info.append(line.strip().split("	")[10] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "Fatty_acid")
                 if gene in factumycin :
                    info.append(line.strip().split("	")[10] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "factumycin")
                 if gene in fosfomycin :
                    info.append(line.strip().split("	")[10] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "fosfomycin") 
                 if gene in fus_acid :
                    info.append(line.strip().split("	")[10] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "fus_acid")
                 if gene in glycopeptide :
                    info.append(line.strip().split("	")[10] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "Glycopeptide/Cycloserine")                    
                 if gene in MLS :
                    info.append(line.strip().split("	")[10] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "MLS")
                 if gene in Multidrug :
                    info.append(line.strip().split("	")[10] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "Multidrug")
                 if gene in Multidrug_efflux :
                    info.append(line.strip().split("	")[10] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "Multidrug_efflux")
                 if gene in mupirocin :
                    info.append(line.strip().split("	")[10] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "mupirocin")                     
                 if gene in nitro :
                    info.append(line.strip().split("	")[10] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "nitroimidazole")
                 if gene in nucleoside :
                    info.append(line.strip().split("	")[10] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "nucleoside") 
                 if gene in peptide :
                    info.append(line.strip().split("	")[10] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "peptide")                   
                 if gene in phenicol :
                    info.append(line.strip().split("	")[10] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "phenicol") 
                 if gene in quinolone :
                    info.append(line.strip().split("	")[10] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "quinolone")                  
                 if gene in rifampicin :
                    info.append(line.strip().split("	")[10] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "rifampicin") 
                 if gene in streptothricin :
                    info.append(line.strip().split("	")[10] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "streptothricin")
                 if gene in sulfonamide :
                    info.append(line.strip().split("	")[10] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "Sulfonamide/trimethoprim")
                 if gene in Tetracenomycin :
                    info.append(line.strip().split("	")[10] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "tetracenomycin") 


# Writting down in files the resulting hits.
with open(o_rfg_water , 'w') as f :
    for line in rfg_water :
        f.write(line + '\n')

with open("C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_Analysis/analysis0422/output/rfg_water_seq_id.csv" , 'w') as f :
    for information in info :
        f.write(information + "\n")

#-----------ResFinder-----------#
i_rf = "C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_Analysis/analysis0422/data/abricate.resfinder.tsv"
o_rf_water = "C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_Analysis/analysis0422/output/rf_water.csv"
i_gene_rf = "C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_Analysis/analysis0422/data/ResFinder_gene_classified.csv"        

aminoside = [] ; bacitracin = [] ; blactamase = [] ; cancer = [] ; colistin = [] ; aminocoumarin = []
cycline = [] ; cycloserine = [] ; edein = [] ; efflux = [] ; fosfomycin = [] ; fus_acid = [] ; bicyclomycin = []
glycopeptide = [] ; MLS = [] ; mupirocin = [] ; nitro = [] ; nucleoside = [] ; blactam_non_enz = []
peptide = [] ; phenicol = [] ; quinolone = [] ; rifampicin = [] ; bleomycin = [] ; Multidrug = [] ; Multidrug_efflux = []
streptothricin = [] ; sulfonamide = [] ; Tetracenomycin = [] ; Disinfecting_agents_and_antiseptics = []
factumycin = [] ; Fatty_acid = []
with open(i_gene_rf , 'r') as f :
    for line in f :
        if "aminocoumarin;" in line :
            aminocoumarin.append(line.strip().split(";")[1])
        if "aminoside;" in line :
            aminoside.append(line.strip().split(";")[1])
        if "bicyclomycin;" in line :
            bicyclomycin.append(line.strip().split(";")[1])        
        if "blactam_non_enz;" in line :
            blactam_non_enz.append(line.strip().split(";")[1])
        if "blactamase;" in line :
            blactamase.append(line.strip().split(";")[1])        
        if "bleomycin;" in line :
            bleomycin.append(line.strip().split(";")[1])           
        if "cycline;" in line :
            cycline.append(line.strip().split(";")[1])
        if "Disinfecting_agents_and_antiseptics;" in line :
            Disinfecting_agents_and_antiseptics.append(line.strip().split(";")[1])
        if "edein;" in line :
            edein.append(line.strip().split(";")[1])
        if "factumycin;" in line :
            factumycin.append(line.strip().split(";")[1])
        if "Fatty_acid;" in line :
            Fatty_acid.append(line.strip().split(";")[1])
        if "fosfomycin;" in line :
            fosfomycin.append(line.strip().split(";")[1])
        if "fusidic acid;" in line :
            fus_acid.append(line.strip().split(";")[1])
        if "Glycopeptide/cycloserine;" in line :
            glycopeptide.append(line.strip().split(";")[1])
        if "MLS;" in line :
            MLS.append(line.strip().split(";")[1])
        if "Multidrug;" in line :
            Multidrug.append(line.strip().split(";")[1])
        if "Multidrug_efflux;" in line :
            Multidrug_efflux.append(line.strip().split(";")[1])
        if "mupirocin;" in line :
            mupirocin.append(line.strip().split(";")[1])
        if "nitroimidazole;" in line :
            nitro.append(line.strip().split(";")[1])            
        if "nucleoside;" in line :
            nucleoside.append(line.strip().split(";")[1])            
        if "peptide;" in line :
            peptide.append(line.strip().split(";")[1])            
        if "phenicol;" in line :
            phenicol.append(line.strip().split(";")[1])
        if "quinolone;" in line :
            quinolone.append(line.strip().split(";")[1])
        if "rifampicin;" in line :
            rifampicin.append(line.strip().split(";")[1])
        if "streptothricin;" in line :
            streptothricin.append(line.strip().split(";")[1])
        if "Sulfonamide/trimethoprim;" in line :
            sulfonamide.append(line.strip().split(";")[1])
        if "Tetracenomycin;" in line :
            Tetracenomycin.append(line.strip().split(";")[1]) 

rf_water = []
info = []
x = 0
with open(i_rf , 'r') as f :
 	for line in f :
         if "resfinder" in line :
             x+=1
             gene = line.strip().split("	")[3]
             if line.strip().split("	")[0] in water_gene :
                  rf_water.append(line.strip())
                  print(gene , (x/2780)*100)
                  if gene in aminocoumarin :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                + ";" + "aminocoumarin")
                  if gene in aminoside :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                + ";" + "aminoside")
                  if gene in bicyclomycin :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "bicyclomicin")
                  if gene in blactam_non_enz :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "blactam_non_enz")
                  if gene in blactamase :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "blactamase")
                  if gene in bleomycin :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "bleomycin")                      
                  if gene in cycline :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "cycline")
                  if gene in Disinfecting_agents_and_antiseptics :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "Disinfecting_agents_and_antiseptics")                      
                  if gene in edein :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "edein")
                  if gene in Fatty_acid :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "Fatty_acid")
                  if gene in factumycin :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "factumycin")
                  if gene in fosfomycin :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "fosfomycin") 
                  if gene in fus_acid :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "fus_acid")
                  if gene in glycopeptide :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "Glycopeptide/Cycloserine")                    
                  if gene in MLS :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "MLS")
                  if gene in Multidrug :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "Multidrug")
                  if gene in Multidrug_efflux :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "Multidrug_efflux")
                  if gene in mupirocin :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "mupirocin")                     
                  if gene in nitro :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "nitroimidazole")
                  if gene in nucleoside :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "nucleoside") 
                  if gene in peptide :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "peptide")                   
                  if gene in phenicol :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "phenicol") 
                  if gene in quinolone :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "quinolone")                  
                  if gene in rifampicin :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "rifampicin") 
                  if gene in streptothricin :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "streptothricin")
                  if gene in sulfonamide :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "Sulfonamide/trimethoprim")
                  if gene in Tetracenomycin :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "tetracenomycin")
                
with open(o_rf_water , 'w') as f :
    for line in rf_water :
        f.write(line + '\n')

with open("C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_Analysis/analysis0422/output/rf_water_seq_id_bis.csv" , 'w') as f :
    for information in info :
        f.write(information + "\n")

#-----------ARG-ANNOT-----------#
i_arg = "C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_Analysis/analysis0422/data/abricate.argannot.tsv"
o_arg_water = "C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_Analysis/analysis0422/output/arg_water.csv"
i_gene_arg = "C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_Analysis/analysis0422/data/argannot_gene_classidied.csv"

aminoside = [] ; bacitracin = [] ; blactamase = [] ; cancer = [] ; colistin = [] ; aminocoumarin = []
cycline = [] ; cycloserine = [] ; edein = [] ; efflux = [] ; fosfomycin = [] ; fus_acid = [] ; bicyclomycin = []
glycopeptide = [] ; MLS = [] ; mupirocin = [] ; nitro = [] ; nucleoside = [] ; blactam_non_enz = []
peptide = [] ; phenicol = [] ; quinolone = [] ; rifampicin = [] ; bleomycin = [] ; Multidrug = [] ; Multidrug_efflux = []
streptothricin = [] ; sulfonamide = [] ; Tetracenomycin = [] ; Disinfecting_agents_and_antiseptics = []
factumycin = [] ; Fatty_acid = []
with open(i_gene_arg , 'r') as f :
    for line in f :
        if "aminocoumarin;" in line :
            aminocoumarin.append(line.strip().split(";")[1])
        if "aminoside;" in line :
            aminoside.append(line.strip().split(";")[1])
        if "bicyclomycin;" in line :
            bicyclomycin.append(line.strip().split(";")[1])        
        if "blactam_non_enz;" in line :
            blactam_non_enz.append(line.strip().split(";")[1])
        if "blactamase;" in line :
            blactamase.append(line.strip().split(";")[1])        
        if "bleomycin;" in line :
            bleomycin.append(line.strip().split(";")[1])           
        if "cycline;" in line :
            cycline.append(line.strip().split(";")[1])
        if "Disinfecting_agents_and_antiseptics;" in line :
            Disinfecting_agents_and_antiseptics.append(line.strip().split(";")[1])
        if "edein;" in line :
            edein.append(line.strip().split(";")[1])
        if "factumycin;" in line :
            factumycin.append(line.strip().split(";")[1])
        if "Fatty_acid;" in line :
            Fatty_acid.append(line.strip().split(";")[1])
        if "fosfomycin;" in line :
            fosfomycin.append(line.strip().split(";")[1])
        if "fusidic acid;" in line :
            fus_acid.append(line.strip().split(";")[1])
        if "Glycopeptide/cycloserine;" in line :
            glycopeptide.append(line.strip().split(";")[1])
        if "MLS;" in line :
            MLS.append(line.strip().split(";")[1])
        if "Multidrug;" in line :
            Multidrug.append(line.strip().split(";")[1])
        if "Multidrug_efflux;" in line :
            Multidrug_efflux.append(line.strip().split(";")[1])
        if "mupirocin;" in line :
            mupirocin.append(line.strip().split(";")[1])
        if "nitroimidazole;" in line :
            nitro.append(line.strip().split(";")[1])            
        if "nucleoside;" in line :
            nucleoside.append(line.strip().split(";")[1])            
        if "peptide;" in line :
            peptide.append(line.strip().split(";")[1])            
        if "phenicol;" in line :
            phenicol.append(line.strip().split(";")[1])
        if "quinolone;" in line :
            quinolone.append(line.strip().split(";")[1])
        if "rifampicin;" in line :
            rifampicin.append(line.strip().split(";")[1])
        if "streptothricin;" in line :
            streptothricin.append(line.strip().split(";")[1])
        if "Sulfonamide/trimethoprim;" in line :
            sulfonamide.append(line.strip().split(";")[1])
        if "Tetracenomycin;" in line :
            Tetracenomycin.append(line.strip().split(";")[1])

arg_water = []
info = []
x = 0
with open(i_arg , 'r') as f :
 	for line in f :
         if "argannot" in line :
             gene = line.strip().split("	")[3]
             if line.strip().split("	")[0] in water_gene :
                 x+=1
                 arg_water.append(line.strip())
                 print(gene , x)
                 if gene in aminocoumarin :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                + ";" + "aminocoumarin")
                 if gene in aminoside :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                + ";" + "aminoside")
                 if gene in bicyclomycin :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "bicyclomicin")
                 if gene in blactam_non_enz :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "blactam_non_enz")
                 if gene in blactamase :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "blactamase")
                 if gene in bleomycin :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "bleomycin")                      
                 if gene in cycline :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "cycline")
                 if gene in Disinfecting_agents_and_antiseptics :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "Disinfecting_agents_and_antiseptics")                      
                 if gene in edein :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "edein")
                 if gene in Fatty_acid :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "Fatty_acid")
                 if gene in factumycin :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "factumycin")
                 if gene in fosfomycin :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "fosfomycin") 
                 if gene in fus_acid :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "fus_acid")
                 if gene in glycopeptide :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "Glycopeptide/Cycloserine")                    
                 if gene in MLS :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "MLS")
                 if gene in Multidrug :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "Multidrug")
                 if gene in Multidrug_efflux :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "Multidrug_efflux")
                 if gene in mupirocin :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "mupirocin")                     
                 if gene in nitro :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "nitroimidazole")
                 if gene in nucleoside :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "nucleoside") 
                 if gene in peptide :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "peptide")                   
                 if gene in phenicol :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "phenicol") 
                 if gene in quinolone :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "quinolone")                  
                 if gene in rifampicin :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "rifampicin") 
                 if gene in streptothricin :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "streptothricin")
                 if gene in sulfonamide :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "Sulfonamide/trimethoprim")
                 if gene in Tetracenomycin :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "tetracenomycin")

print("ARG :" , x)
with open(o_arg_water , 'w') as f :
    for line in arg_water :
        f.write(line + '\n')

with open("C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_Analysis/analysis0422/output/arg_water_seq_id_bis.csv" , 'w') as f :
    for information in info :
        f.write(information + "\n")
        
#-----------CARD-----------#
i_card = "C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_Analysis/analysis0422/data/abricate.card.tsv"
o_card_water = "C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_Analysis/analysis0422/output/card_water.csv"
i_gene_card = "C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_Analysis/analysis0422/data/card_gene_classified.csv"

aminoside = [] ; bacitracin = [] ; blactamase = [] ; cancer = [] ; colistin = [] ; aminocoumarin = []
cycline = [] ; cycloserine = [] ; edein = [] ; efflux = [] ; fosfomycin = [] ; fus_acid = [] ; bicyclomycin = []
glycopeptide = [] ; MLS = [] ; mupirocin = [] ; nitro = [] ; nucleoside = [] ; blactam_non_enz = []
peptide = [] ; phenicol = [] ; quinolone = [] ; rifampicin = [] ; bleomycin = [] ; Multidrug = [] ; Multidrug_efflux = []
streptothricin = [] ; sulfonamide = [] ; Tetracenomycin = [] ; Disinfecting_agents_and_antiseptics = []
with open(i_gene_card , 'r') as f :
    for line in f :
        if "aminocoumarin;" in line :
            aminocoumarin.append(line.strip().split(";")[1])
        if "aminoside;" in line :
            aminoside.append(line.strip().split(";")[1])
        if "bicyclomycin;" in line :
            bicyclomycin.append(line.strip().split(";")[1])        
        if "blactam_non_enz;" in line :
            blactam_non_enz.append(line.strip().split(";")[1])
        if "blactamase;" in line :
            blactamase.append(line.strip().split(";")[1])        
        if "bleomycin;" in line :
            bleomycin.append(line.strip().split(";")[1])           
        if "cycline;" in line :
            cycline.append(line.strip().split(";")[1])
        if "Disinfecting_agents_and_antiseptics;" in line :
            Disinfecting_agents_and_antiseptics.append(line.strip().split(";")[1])
        if "edein;" in line :
            edein.append(line.strip().split(";")[1])
        if "factumycin;" in line :
            factumycin.append(line.strip().split(";")[1])
        if "Fatty_acid;" in line :
            Fatty_acid.append(line.strip().split(";")[1])
        if "fosfomycin;" in line :
            fosfomycin.append(line.strip().split(";")[1])
        if "fusidic acid;" in line :
            fus_acid.append(line.strip().split(";")[1])
        if "Glycopeptide/cycloserine;" in line :
            glycopeptide.append(line.strip().split(";")[1])
        if "MLS;" in line :
            MLS.append(line.strip().split(";")[1])
        if "Multidrug;" in line :
            Multidrug.append(line.strip().split(";")[1])
        if "Multidrug_efflux;" in line :
            Multidrug_efflux.append(line.strip().split(";")[1])
        if "mupirocin;" in line :
            mupirocin.append(line.strip().split(";")[1])
        if "nitroimidazole;" in line :
            nitro.append(line.strip().split(";")[1])            
        if "nucleoside;" in line :
            nucleoside.append(line.strip().split(";")[1])            
        if "peptide;" in line :
            peptide.append(line.strip().split(";")[1])            
        if "phenicol;" in line :
            phenicol.append(line.strip().split(";")[1])
        if "quinolone;" in line :
            quinolone.append(line.strip().split(";")[1])
        if "rifampicin;" in line :
            rifampicin.append(line.strip().split(";")[1])
        if "streptothricin;" in line :
            streptothricin.append(line.strip().split(";")[1])
        if "Sulfonamide/trimethoprim;" in line :
            sulfonamide.append(line.strip().split(";")[1])
        if "Tetracenomycin;" in line :
            Tetracenomycin.append(line.strip().split(";")[1])

card_water = []
info = []
x = 0
with open(i_card , 'r') as f :
 	for line in f :
         if "card" in line :
             gene = line.strip().split("	")[2]
             if line.strip().split("	")[0] in water_gene :
                 x+=1
                 card_water.append(line.strip())
                 print(gene , x)
                 if gene in aminocoumarin :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                + ";" + "aminocoumarin")
                 else :
                     if gene in bicyclomycin :
                        info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                   + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                   + ";" + "bicyclomicin")
                     else :
                         if gene in bleomycin :
                            info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                       + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                       + ";" + "bleomycin") 
                         else :
                             if gene in Disinfecting_agents_and_antiseptics :
                                info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                           + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                           + ";" + "Disinfecting_agents_and_antiseptics")
                             else :
                                 if gene in edein :
                                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                               + ";" + "edein")
                                 else :
                                     if gene in Fatty_acid :
                                        info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                                   + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                                   + ";" + "Fatty_acid")
                                     else :
                                        if gene in factumycin :
                                            info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                                   + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                                   + ";" + "factumycin")
                                        else :
                                            if gene in mupirocin :
                                               info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                                          + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                                          + ";" + "mupirocin")
                                            else :
                                                if gene in nitro :
                                                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                                          + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                                          + ";" + "nitroimidazole")
                                                else :
                                                    if gene in Tetracenomycin :
                                                       info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                                                  + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                                                  + ";" + "tetracenomycin")
                                                    else :
                                                        if gene in streptothricin :
                                                           info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                                                      + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                                                      + ";" + "streptothricin")
                                                        else :
                                                            if gene in nucleoside :
                                                               info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                                                          + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                                                          + ";" + "nucleoside")
                                                            else :
                                                                if gene in fosfomycin :
                                                                   info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                                                              + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                                                              + ";" + "fosfomycin") 
                                                                else :
                                                                    if gene in fus_acid :
                                                                       info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                                                                  + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                                                                  + ";" + "fus_acid")
                                                                    else :
                                                                        if gene in rifampicin :
                                                                           info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                                                                      + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                                                                      + ";" + "rifampicin")
                                                                        else :
                                                                            if gene in Multidrug :
                                                                               info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                                                                          + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                                                                          + ";" + "Multidrug")
                                                                            else :
                                                                                if gene in blactam_non_enz :
                                                                                   info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                                                                              + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                                                                              + ";" + "blactam_non_enz")
                                                                                else :
                                                                                    if gene in peptide :
                                                                                       info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                                                                                  + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                                                                                  + ";" + "peptide")
                                                                                    else :
                                                                                        if gene in Multidrug_efflux :
                                                                                           info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                                                                                      + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                                                                                      + ";" + "Multidrug_efflux")
                                                                                        else :
                                                                                            if gene in phenicol :
                                                                                               info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                                                                                          + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                                                                                          + ";" + "phenicol")
                                                                                            else :
                                                                                                if gene in quinolone :
                                                                                                   info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                                                                                              + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                                                                                              + ";" + "quinolone")
                                                                                                else :
                                                                                                    if gene in MLS :
                                                                                                       info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                                                                                                  + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                                                                                                  + ";" + "MLS")
                                                                                                    else :
                                                                                                        if gene in cycline :
                                                                                                           info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                                                                                                      + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                                                                                                      + ";" + "cycline")
                                                                                                        else :
                                                                                                            if gene in aminoside :
                                                                                                               info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                                                                                                           + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                                                                                                           + ";" + "aminoside")
                                                                                                            else :
                                                                                                                if gene in glycopeptide :
                                                                                                                   info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                                                                                                              + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                                                                                                              + ";" + "Glycopeptide/Cycloserine") 
                                                                                                                else :
                                                                                                                    if gene in sulfonamide :
                                                                                                                       info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                                                                                                                  + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                                                                                                                  + ";" + "Sulfonamide/trimethoprim")
                                                                                                                    else :
                                                                                                                        if gene in blactamase :
                                                                                                                           info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                                                                                                                      + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                                                                                                                      + ";" + "blactamase")
                                                                                                                           
with open(o_card_water , 'w') as f :
    for line in card_water :
        f.write(line + '\n')

with open("C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_Analysis/analysis0422/output/card_water_seq_id_bis.csv" , 'w') as f :
    for information in info :
        f.write(information + "\n")


#-----------NCBI-----------#
i_ncbi = "C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_Analysis/analysis0422/data/abricate.ncbi.tsv"
o_ncbi_water = "C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_Analysis/analysis0422/output/ncbi_water.csv"
i_gene_ncbi = "C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_Analysis/analysis0422/data/ncbi_gene_classified.csv"

aminoside = [] ; bacitracin = [] ; blactamase = [] ; cancer = [] ; colistin = [] ; aminocoumarin = []
cycline = [] ; cycloserine = [] ; edein = [] ; efflux = [] ; fosfomycin = [] ; fus_acid = [] ; bicyclomycin = []
glycopeptide = [] ; MLS = [] ; mupirocin = [] ; nitro = [] ; nucleoside = [] ; blactam_non_enz = []
peptide = [] ; phenicol = [] ; quinolone = [] ; rifampicin = [] ; bleomycin = [] ; Multidrug = [] ; Multidrug_efflux = []
streptothricin = [] ; sulfonamide = [] ; Tetracenomycin = [] ; Disinfecting_agents_and_antiseptics = []

with open(i_gene_ncbi , 'r') as f :
    for line in f :
        if "aminocoumarin;" in line :
            aminocoumarin.append(line.strip().split(";")[1])
        if "aminoside;" in line :
            aminoside.append(line.strip().split(";")[1])
        if "bicyclomycin;" in line :
            bicyclomycin.append(line.strip().split(";")[1])        
        if "blactam_non_enz;" in line :
            blactam_non_enz.append(line.strip().split(";")[1])
        if "blactamase;" in line :
            blactamase.append(line.strip().split(";")[1])        
        if "bleomycin;" in line :
            bleomycin.append(line.strip().split(";")[1])           
        if "cycline;" in line :
            cycline.append(line.strip().split(";")[1])
        if "Disinfecting_agents_and_antiseptics;" in line :
            Disinfecting_agents_and_antiseptics.append(line.strip().split(";")[1])
        if "edein;" in line :
            edein.append(line.strip().split(";")[1])
        if "factumycin;" in line :
            factumycin.append(line.strip().split(";")[1])
        if "Fatty_acid;" in line :
            Fatty_acid.append(line.strip().split(";")[1])
        if "fosfomycin;" in line :
            fosfomycin.append(line.strip().split(";")[1])
        if "fusidic acid;" in line :
            fus_acid.append(line.strip().split(";")[1])
        if "Glycopeptide/cycloserine;" in line :
            glycopeptide.append(line.strip().split(";")[1])
        if "MLS;" in line :
            MLS.append(line.strip().split(";")[1])
        if "Multidrug;" in line :
            Multidrug.append(line.strip().split(";")[1])
        if "Multidrug_efflux;" in line :
            Multidrug_efflux.append(line.strip().split(";")[1])
        if "mupirocin;" in line :
            mupirocin.append(line.strip().split(";")[1])
        if "nitroimidazole;" in line :
            nitro.append(line.strip().split(";")[1])            
        if "nucleoside;" in line :
            nucleoside.append(line.strip().split(";")[1])            
        if "peptide;" in line :
            peptide.append(line.strip().split(";")[1])            
        if "phenicol;" in line :
            phenicol.append(line.strip().split(";")[1])
        if "quinolone;" in line :
            quinolone.append(line.strip().split(";")[1])
        if "rifampicin;" in line :
            rifampicin.append(line.strip().split(";")[1])
        if "streptothricin;" in line :
            streptothricin.append(line.strip().split(";")[1])
        if "Sulfonamide/trimethoprim;" in line :
            sulfonamide.append(line.strip().split(";")[1])
        if "Tetracenomycin;" in line :
            Tetracenomycin.append(line.strip().split(";")[1])

ncbi_water = []
info = []
x = 0
with open(i_ncbi , 'r') as f :
 	for line in f :
         if "ncbi" in line :
             gene = line.strip().split("	")[3]
             if line.strip().split("	")[0] in water_gene :
                 x += 1
                 ncbi_water.append(line.strip())
                 print(gene , x)
                 if gene in blactamase :
                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                               + ";" + "blactamase")
                 else :
                     if gene in aminoside :
                        info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                    + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                    + ";" + "aminoside")
                     else :
                         if gene in glycopeptide :
                            info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                       + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                       + ";" + "Glycopeptide/Cycloserine")
                         else :
                             if gene in MLS :
                                info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                           + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                           + ";" + "MLS")
                             else :
                                 if gene in sulfonamide :
                                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                               + ";" + "Sulfonamide/trimethoprim")
                                 else :
                                    if gene in cycline :
                                       info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                                  + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                                  + ";" + "cycline")
                                    else :
                                        if gene in quinolone :
                                           info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                                      + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                                      + ";" + "quinolone")
                                        else :
                                            if gene in phenicol :
                                               info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                                          + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                                          + ";" + "phenicol") 
                                            if gene in blactam_non_enz :
                                                info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                                           + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                                           + ";" + "blactam_non_enz")
                                            else :
                                                if gene in Multidrug_efflux :
                                                   info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                                              + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                                              + ";" + "Multidrug_efflux")
                                                if gene in peptide :
                                                   info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                                              + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                                              + ";" + "peptide")                      
                                                if gene in Multidrug :
                                                   info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                                              + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                                              + ";" + "Multidrug")
                                                if gene in fosfomycin :
                                                   info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                                              + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                                              + ";" + "fosfomycin")
                                                if gene in nitro :
                                                   info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                                              + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                                              + ";" + "nitroimidazole")
                                                if gene in edein :
                                                   info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                                              + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                                              + ";" + "edein") 
                                                if gene in factumycin :
                                                   info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                                              + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                                              + ";" + "factumycin")
                                                if gene in Fatty_acid :
                                                   info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                                              + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                                              + ";" + "Fatty_acid")
                                                if gene in aminocoumarin :
                                                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                                                + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                                                + ";" + "aminocoumarin")
                                                if gene in bicyclomycin :
                                                   info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                                              + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                                              + ";" + "bicyclomicin")
                                                if gene in nucleoside :
                                                   info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                                              + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                                              + ";" + "nucleoside")
                                                if gene in mupirocin :
                                                   info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                                              + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                                              + ";" + "mupirocin")
                                                if gene in fus_acid :
                                                   info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                                              + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                                              + ";" + "fus_acid")  
                                                if gene in bleomycin :
                                                   info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                                              + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                                              + ";" + "bleomycin")
                                                if gene in Disinfecting_agents_and_antiseptics :
                                                   info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                                              + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                                              + ";" + "Disinfecting_agents_and_antiseptics")            
                                                if gene in rifampicin :
                                                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                                               + ";" + "rifampicin") 
                                                if gene in streptothricin :
                                                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                                               + ";" + "streptothricin")
                                
                                                if gene in Tetracenomycin :
                                                    info.append(line.strip().split("	")[0] + ";" + line.strip().split("	")[4] 
                                                               + ";" + line.strip().split("	")[9] + ";" + line.strip().split("	")[3] 
                                                               + ";" + "tetracenomycin")               

print("NCBI :" , x)
with open(o_ncbi_water , 'w') as f :
    for line in ncbi_water :
        f.write(line + '\n')

with open("C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_Analysis/analysis0422/output/ncbi_water_seq_id_bis.csv" , 'w') as f :
    for information in info :
        f.write(information + "\n")
        