# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 14:47:21 2022

@author: remi.gschwind
"""

rf1 = []
with open("C:/Users/remi.gschwind/Desktop/Resfinder FG/ARDs_functional_metagenomics_nr_2016_12_21.faa" , 'r') as f :
    for line in f :
        if ">" in line :
            rf1.append(line.strip().split(">")[1])
            
with open("C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_Analysis/analysis0422/output/rf1.csv" , 'w') as f :
    f.write("gene" + "|" + "AN" + "|" + "origin" + "|" + "antibiotic" + "\n")
    for element in rf1 :
        f.write(element + "\n")            
            
rf2 = []
with open("C:/Users/remi.gschwind/Desktop/Resfinder FG/210811/ResFinder_FG_db/compilation/ResFinder_FG_60.faa" , 'r') as f :
    for line in f :
        if ">" in line :
            rf2.append(line.strip().split(">")[1])
            
with open("C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_Analysis/analysis0422/output/rf2.csv" , 'w') as f :
    f.write("gene" + "|" + "AN" + "|" + "origin" + "|" + "antibiotic" + "\n")
    for element in rf2 :
        f.write(element + "\n")

print(len(rf1))
print(len(rf2))
print(len(rf2)-len(rf1))

blac = [] ; phen = [] ; quin = [] ; amin = [] ; cyc = [] ; cycli = [] ; tmp = [] ; mls = []
with open("C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_Analysis/analysis0422/output/rf1.csv" , 'r') as f :
    for line in f :
        if "AN" not in line :
            if ";AMC" in line :
                blac.append(line)
            if ";AMP" in line :
                blac.append(line)
            if ";AMX" in line :
                blac.append(line)
            if ";ATM" in line :  
                blac.append(line)
            if ";CAR" in line :
                blac.append(line)
            if ";CAZ" in line :
                blac.append(line)
            if ";CDR" in line :
                blac.append(line)
            if ";CTX" in line :
                blac.append(line)
            if ";FEP" in line :  
                blac.append(line)
            if ";FOX" in line :
                blac.append(line)
            if ";PEN" in line :
                blac.append(line)
            if ";PIP" in line :
                blac.append(line)
            if ";TZP" in line :  
                blac.append(line)
                
            if ";CHL" in line :
                phen.append(line)
                
            if ";CIP" in line :                
                quin.append(line)
                
            if ";CYC" in line :
                cyc.append(line)
                
            if ";GEN" in line :
                amin.append(line)
            if ";SIS" in line :                
                amin.append(line)
                
            if ";MIN" in line :
                cycli.append(line)
            if ";OXY" in line :
                cycli.append(line)
            if ";TET" in line :
                cycli.append(line)
            if ";TGC" in line :
                cycli.append(line)

            if ";SXT" in line :
                tmp.append(line)
            if ";TMP" in line :
                tmp.append(line)
                
legend = "Database;Blactam;Phenicol;Quinolone;Glycopeptide/cycloserine;Aminoglycoside;Cycline;Sulfonamide/trimethoprim;Macrolide"
num_rf1 = str(len(blac)) + ";" + str(len(phen)) + ";" + str(len(quin)) + ";" + str(len(cyc)) + ";" + str(len(amin)) + ";" + str(len(cycli)) + ";" + str(len(tmp)) + ";" + str(len(mls))
print(legend + "\n" + num_rf1)


blac = [] ; phen = [] ; quin = [] ; amin = [] ; cyc = [] ; cycli = [] ; tmp = [] ; mls = []
with open("C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_Analysis/analysis0422/output/rf2.csv" , 'r') as f :
    for line in f :
        if "AN" not in line :
            if ";AMC" in line :
                blac.append(line)
            if ";AMP" in line :
                blac.append(line)
            if ";AMX" in line :
                blac.append(line)
            if ";ATM" in line :  
                blac.append(line)
            if ";CAR" in line :
                blac.append(line)
            if ";CAZ" in line :
                blac.append(line)
            if ";CEF" in line :
                blac.append(line)
            if ";CDR" in line :
                blac.append(line)
            if ";CTX" in line :
                blac.append(line)
            if ";FEP" in line :  
                blac.append(line)
            if ";FOX" in line :
                blac.append(line)
            if ";MEM" in line :
                blac.append(line)
            if ";PEN" in line :
                blac.append(line)
            if ";PIP" in line :
                blac.append(line)
            if ";TZP" in line :  
                blac.append(line)
            if ";TZB" in line :  
                blac.append(line)
                
            if ";CHL" in line :
                phen.append(line)
                
            if ";CIP" in line :                
                quin.append(line)
                
            if ";CYC" in line :
                cyc.append(line)
                
            if ";GEN" in line :
                amin.append(line)
            if ";SIS" in line :                
                amin.append(line)
            if ";AMK" in line :                
                amin.append(line)                
            if ";KAN" in line :                
                amin.append(line)
            if ";SPT" in line :
                amin.append(line)                
            if ";STR" in line :
                amin.append(line)
                
            if ";MIN" in line :
                cycli.append(line)
            if ";OXY" in line :
                cycli.append(line)
            if ";TET" in line :
                cycli.append(line)
            if ";TGC" in line :
                cycli.append(line)

            if ";SXT" in line :
                tmp.append(line)
            if ";TMP" in line :
                tmp.append(line)
            if ";SDX" in line :
                tmp.append(line)
            if ";STX" in line :
                tmp.append(line)
            if ";SMZ" in line :
                tmp.append(line)
                
            if ";AZM" in line :
                mls.append(line)                
            if ";ERY" in line :
                mls.append(line)
                
legend = "Database;Blactam;Phenicol;Quinolone;Glycopeptide/cycloserine;Aminoglycoside;Cycline;Sulfonamide/trimethoprim;Macrolide"
num_rf2 = str(len(blac)) + ";" + str(len(phen)) + ";" + str(len(quin)) + ";" + str(len(cyc)) + ";" + str(len(amin)) + ";" + str(len(cycli)) + ";" + str(len(tmp)) + ";" + str(len(mls))
print(legend + "\n" + num_rf2)

with open("C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_Analysis/analysis0422/output/comparison.csv" , 'w') as f :
    f.write(legend + "\n" + "ResFinderFG v1.1" + ";" + num_rf1 + "\n" + "ResFinderFG v2.0" + ";" + num_rf2)               