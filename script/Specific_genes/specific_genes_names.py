# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 10:37:29 2022

@author: remi.gschwind
"""
#CARD
eff = [] ; ami = [] ; fosfo = [] ; macro = [] ; coum = [] ; nitro = [] ; rif = [] ; qui = [] ; blac = []
daaa = [] ; peptide = [] ; cycline = []
with open("C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_Analysis/analysis0422/output/card_spe_water.csv" , 'r') as f :
    for line in f :
        if ";Multidrug_efflux" in line :
            if line.strip().split(";")[3] not in eff :
                eff.append(line.strip().split(";")[3])
        if ";rifampicin" in line :
            if line.strip().split(";")[3] not in rif :
                rif.append(line.strip().split(";")[3])
        if ";fosfomycin" in line :
            if line.strip().split(";")[3] not in fosfo :
                fosfo.append(line.strip().split(";")[3])
        if ";MLS" in line :
            if line.strip().split(";")[3] not in macro :
                macro.append(line.strip().split(";")[3])
        if ";aminocoumarin" in line :
            if line.strip().split(";")[3] not in coum :
                coum.append(line.strip().split(";")[3])
        if ";nitroimidazole" in line :
            if line.strip().split(";")[3] not in nitro :
                nitro.append(line.strip().split(";")[3])
        if ";quinolone" in line :
            if line.strip().split(";")[3] not in qui :
                qui.append(line.strip().split(";")[3])
        if ";aminoside" in line :
            if line.strip().split(";")[3] not in ami :
                ami.append(line.strip().split(";")[3])
        if ";blactamase" in line :
            if line.strip().split(";")[3] not in blac :
                blac.append(line.strip().split(";")[3])
        if ";Disinfecting_agents_and_antiseptics" in line :
            if line.strip().split(";")[3] not in daaa :
                daaa.append(line.strip().split(";")[3])
        if ";peptide" in line :
            if line.strip().split(";")[3] not in peptide :
                peptide.append(line.strip().split(";")[3])
        if ";cycline" in line :
            if line.strip().split(";")[3] not in cycline :
                cycline.append(line.strip().split(";")[3])                

with open("C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_Analysis/analysis0422/output/card_spe_water_gene.csv" , 'w') as f :
    f.write("multidrug efflux" + ";" + str(eff) + '\n')
    f.write("rifampicin" + ";" + str(rif) + '\n')
    f.write("fosfomycin" + ";" + str(fosfo) + '\n')
    f.write("MLS" + ";" + str(macro) + '\n')
    f.write("aminocoumarin" + ";" + str(coum) + '\n')
    f.write("nitroimidazole" + ";" + str(nitro) + '\n')
    f.write("quinolone" + ";" + str(qui) + '\n')
    f.write("aminoglycoside" + ";" + str(ami) + '\n')
    f.write("blactamase" + ";" + str(blac) + '\n')
    f.write("disinfecting agents/antiseptics" + ";" + str(daaa) + '\n')
    f.write("peptide" + ";" + str(peptide) + '\n')
    f.write("cycline" + ";" + str(cycline) + '\n')
#NCBI
# ami = [] ; bleo = [] ; fosfo = [] ; glyco = [] ; peptide = [] ; phe = [] ; rif = []
# with open("C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_Analysis/analysis0422/output/ncbi_spe_soil.csv" , 'r') as f :
#     for line in f :
#         if ";aminoside" in line :
#             if line.strip().split(";")[3] not in ami :
#                 ami.append(line.strip().split(";")[3])
#         if ";bleomycin" in line :
#             if line.strip().split(";")[3] not in bleo :
#                 bleo.append(line.strip().split(";")[3])
#         if ";fosfomycin" in line :
#             if line.strip().split(";")[3] not in fosfo :
#                 fosfo.append(line.strip().split(";")[3])
#         if ";Glycopeptide/Cycloserine" in line :
#             if line.strip().split(";")[3] not in glyco :
#                 glyco.append(line.strip().split(";")[3])
#         if ";peptide" in line :
#             if line.strip().split(";")[3] not in peptide :
#                 peptide.append(line.strip().split(";")[3])
#         if ";phenicol" in line :
#             if line.strip().split(";")[3] not in phe :
#                 phe.append(line.strip().split(";")[3])
#         if ";rifampicin" in line :
#             if line.strip().split(";")[3] not in rif :
#                 rif.append(line.strip().split(";")[3])

# with open("C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_Analysis/analysis0422/output/ncbi_spe_soil_gene.csv" , 'w') as f :
#     f.write("aminoglycoside" + ";" + str(ami) + '\n')
#     f.write("bleomycin" + ";" + str(bleo) + '\n')
#     f.write("fosfomycin" + ";" + str(fosfo) + '\n')
#     f.write("glycopeptide/cycloserine" + ";" + str(glyco) + '\n')
#     f.write("peptide" + ";" + str(peptide) + '\n')
#     f.write("phenicol" + ";" + str(phe) + '\n')
#     f.write("rifampicin" + ";" + str(rif) + '\n')
    
#RESFINDERFG
# glyco = [] ; sul = [] ; phe = [] ; ami = [] ;  blac = []
# with open("C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_Analysis/analysis0422/output/rfg_spe_soil.csv" , 'r') as f :
#     for line in f :
#         if ";Glycopeptide/Cycloserine" in line :
#             gene = line.strip().split(";")[3]
#             if gene.strip().split("|")[0] not in glyco :
#                 glyco.append(gene.strip().split("|")[0])
#         if ";Sulfonamide/trimethoprim" in line :
#             gene = line.strip().split(";")[3]
#             if gene.strip().split("|")[0] not in sul :
#                 sul.append(gene.strip().split("|")[0])
#         if ";phenicol" in line :
#             gene = line.strip().split(";")[3]
#             if gene.strip().split("|")[0] not in phe :
#                 phe.append(gene.strip().split("|")[0])
#         if ";aminoside" in line :
#             gene = line.strip().split(";")[3]
#             if gene.strip().split("|")[0] not in ami :
#                 ami.append(gene.strip().split("|")[0])
#         if ";blactamase" in line :
#             gene = line.strip().split(";")[3]
#             if gene.strip().split("|")[0] not in blac :
#                 blac.append(gene.strip().split("|")[0])

# with open("C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_Analysis/analysis0422/output/rfg_spe_soil_gene.csv" , 'w') as f :
#     f.write("Glycopeptide/Cycloserine" + ";" + str(glyco) + '\n')
#     f.write("Sulfonamide/trimethoprim" + ";" + str(sul) + '\n')
#     f.write("phenicol" + ";" + str(phe) + '\n')
#     f.write("aminoglycoside" + ";" + str(ami) + '\n')
#     f.write("blactamase" + ";" + str(blac) + '\n')

#ARG-ANNOT

blac = [] ; blane = [] ; ami = [] ; cycline = [] 
with open("C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_Analysis/analysis0422/output/arg_spe_soil.csv" , 'r') as f :
    for line in f :
        if ";blactamase" in line :
            if line.strip().split(";")[3] not in blac :
                blac.append(line.strip().split(";")[3])
        if ";blactam_non_enz" in line :
            if line.strip().split(";")[3] not in blane :
                blane.append(line.strip().split(";")[3])
        if ";aminoside" in line :
            if line.strip().split(";")[3] not in ami :
                ami.append(line.strip().split(";")[3])
        if ";cycline" in line :
            if line.strip().split(";")[3] not in cycline :
                cycline.append(line.strip().split(";")[3])

with open("C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_Analysis/analysis0422/output/arg_spe_soil_gene.csv" , 'w') as f :
    f.write("blactamase" + ";" + str(blac) + '\n')
    f.write("blactam non enz" + ";" + str(blane) + '\n')
    f.write("aminoglycoside" + ";" + str(ami) + '\n')
    f.write("cycline" + ";" + str(cycline) + '\n')