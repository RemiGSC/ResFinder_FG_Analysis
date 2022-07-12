# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 10:43:42 2022

@author: remi.gschwind
"""
rfg = [] ; rf = [] ; ncbi = [] ; card = [] ; arg = []
with open("C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_Analysis/analysis0422/output/water_spe.csv" , 'r') as f :
    for line in f :
        if "ARG-ANNOT" not in line :
            rfg.append(line.strip().split(";")[4])
            rf.append(line.strip().split(";")[3])
            ncbi.append(line.strip().split(";")[2])
            card.append(line.strip().split(";")[1])
            arg.append(line.strip().split(";")[0])

rfg_spe = [] ; rf_spe = [] ; ncbi_spe = [] ; card_spe = [] ; arg_spe = []
with open("C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_Analysis/analysis0422/output/all_soil.csv" , 'r') as f :
    for line in f :
        if line.strip().split(";")[0] in rf :
            if ";ResFinder;" in line :
                rf_spe.append(line.strip())
        else :
            if line.strip().split(";")[0] in ncbi :
                if ";NCBI;" in line :
                    ncbi_spe.append(line.strip())
            else :
                if line.strip().split(";")[0] in arg :
                    if ";ARG-ANNOT;" in line :
                        arg_spe.append(line.strip())
                else :
                    if line.strip().split(";")[0] in rfg :
                        if ";ResFinderFG;" in line :
                            rfg_spe.append(line.strip())                    
                    else :
                        if line.strip().split(";")[0] in card :
                            if ";CARD;" in line :
                                card_spe.append(line.strip())
                            
with open("C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_Analysis/analysis0422/output/rfg_spe_soil.csv" , 'w') as f :
    for spe in rfg_spe :
        f.write(spe + '\n')
with open("C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_Analysis/analysis0422/output/card_spe_soil.csv" , 'w') as f :
    for spe in card_spe :
        f.write(spe + '\n')
with open("C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_Analysis/analysis0422/output/rf_spe_soil.csv" , 'w') as f :
    for spe in rf_spe :
        f.write(spe + '\n')
with open("C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_Analysis/analysis0422/output/arg_spe_soil.csv" , 'w') as f :
    for spe in arg_spe :
        f.write(spe + '\n')
with open("C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_Analysis/analysis0422/output/ncbi_spe_soil.csv" , 'w') as f :
    for spe in ncbi_spe :
        f.write(spe + '\n')            