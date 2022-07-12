# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 10:12:39 2022

@author: remi.gschwind
"""
source = []
with open("C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_Analysis/analysis0422/output/all_soil.csv" , 'r') as f :
    for line in f :
        if "ResFinderFG" in line :
           source.append(line.strip().split("|")[2])
           
with open("C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_Analysis/analysis0422/output/source_rfg_soil.csv" , 'w') as f :
    f.write("source" + "\n")
    for element in source :
        f.write(element + "\n")          