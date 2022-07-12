# -*- coding: utf-8 -*-
"""
Created on Wed May 11 10:48:12 2022

@author: remi.gschwind
"""
GMGC_id = []
line_hit = []
fam_id = []
db = []
with open("C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_Analysis/analysis0422/output/all_soil.csv" , 'r') as f :
    for line in f :
        cut = line.strip().split(";")
        if not line.strip() in line_hit :
            line_hit.append(line.strip())
            GMGC_id.append(cut[0])
            fam_id.append(cut[-1])
            db.append(cut[1])
print(len(line_hit))

dup = []
for element in line_hit :
    index = line_hit.index(element)
    if index < len(line_hit)-1 :
        if GMGC_id[index] == GMGC_id[index+1] :
            if db[index] == db[index+1] :
                print(element)
                
                if fam_id[index] != fam_id[index+1] :
                    if fam_id[index] == "glycopeptide" :
                        if fam_id[index+1] == "peptide" :
                            line_hit.pop(index+1)

                    print(line_hit[index].strip().split(";")[-1])
                    
                    if db[index] == db[index+1] :
                        dup.append(element)
print(len(dup))

for duplicate in dup :
    if duplicate in line_hit :
        print(duplicate , "dup")
        line_hit.remove(duplicate)
        print(len(line_hit))

with open("C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_Analysis/analysis0422/output/all_gut_seq_id_nodup.csv" , 'w') as f :
    for element in line_hit :
        f.write(element + '\n')


    