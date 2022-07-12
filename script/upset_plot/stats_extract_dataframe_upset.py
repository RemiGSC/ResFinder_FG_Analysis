# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 15:35:42 2022

@author: remi.gschwind
"""
aminocoumarin = 0 ; aminoside = 0 ; bicyclomicin = 0 ; blactam_non_enz = 0 ; blactamase = 0 ; bleomycin = 0
cycline = 0 ; Disinfecting_agents_and_antiseptics = 0 ; fosfomycin = 0  ; fus_acid = 0
Glycopeptide_Cycloserine = 0 ; MLS = 0 ; Multidrug = 0 ; Multidrug_efflux= 0 ; mupirocin = 0
nitroimidazole = 0 ; nucleoside = 0 ; peptide = 0 ; phenicol = 0 ; quinolone = 0 ; rifampicin = 0
streptothricin = 0 ; Sulfonamide_trimethoprim = 0

arg = "line.strip().split(";")[2]" ; card = "line.strip().split(";")[3]" ; ncbi = "line.strip().split(";")[4]"
resfinder = "line.strip().split(";")[5]" ; rfg = "line.strip().split(";")[6]"

with open("C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_Analysis/analysis0422/output/dataframe_water.csv" , 'r') as f :
    for line in f :
        print(line.strip().split(";")[1])
        if line.strip().split(";")[3] == str(1) :
            if (int(line.strip().split(";")[2])+int(line.strip().split(";")[3])+int(line.strip().split(";")[4])
                +int(line.strip().split(";")[5])+int(line.strip().split(";")[6])) == int(1) :
                if ";aminocoumarin;" in line :
                    aminocoumarin +=1
                if ";aminoside;" in line :
                    aminoside += 1
                if ";bicyclomicin;" in line :
                    bicyclomicin += 1
                if ";blactam_non_enz;" in line :
                    blactam_non_enz += 1
                if ";blactamase;" in line :
                    blactamase += 1
                if ";bleomycin;" in line :
                    bleomycin += 1
                if ";cycline;" in line :
                    cycline += 1
                if ";Disinfecting_agents_and_antiseptics;" in line :
                    Disinfecting_agents_and_antiseptics += 1
                if ";fosfomycin;" in line :
                    fosfomycin += 1
                if ";fus_acid;" in line :
                    fus_acid += 1
                if ";Glycopeptide/Cycloserine;" in line :
                    Glycopeptide_Cycloserine += 1
                if ";MLS;" in line :
                    MLS += 1
                if ";Multidrug;" in line :
                    Multidrug += 1                
                if ";Multidrug_efflux;" in line :
                    Multidrug_efflux += 1
                if ";mupirocin;" in line :
                    mupirocin += 1
                if ";nitroimidazole;" in line :
                    nitroimidazole += 1
                if ";nucleoside;" in line :
                    nucleoside += 1
                if ";peptide;" in line :
                    peptide += 1
                if ";phenicol;" in line :
                    phenicol += 1
                if ";quinolone;" in line :
                    quinolone += 1
                if ";rifampicin;" in line :
                    rifampicin += 1
                if ";streptothricin;" in line :
                    streptothricin += 1
                if ";Sulfonamide/trimethoprim;" in line :
                    Sulfonamide_trimethoprim += 1                
print(str(aminocoumarin) + " aminocoumarin")
print(str(aminoside) + " aminoside" + "           /           " + str(bicyclomicin )+ " bicyclomycin")
print(str(blactam_non_enz) + " blactam_non_enz" + "           /           " + str(blactamase) + " blactamase")
print(str(bleomycin) + " bleomycin" + "           /           " + str(cycline) + " cycline")
print(str(Disinfecting_agents_and_antiseptics) + " Disinfecting_agents_and_antiseptics" + "           /           " + str(fosfomycin) + "fosfomycin")
print(str(fus_acid) + " fus_acid" + "           /           " + str(Glycopeptide_Cycloserine) + " Glycopeptide_Cycloserine")
print(str(MLS) + " MLS" + "           /           " + str(Multidrug) + " Multidrug")
print(str(Multidrug_efflux) + " Multidrug_efflux" + "           /           " + str(mupirocin) + " mupirocin")
print(str(nitroimidazole) + " nitroimidazole" + "           /           " + str(nucleoside) + " nucleoside")
print(str(peptide) + " peptide" + "           /           " + str(phenicol) + " phenicol")
print(str(quinolone) + " quinolone" + "           /           " + str(rifampicin) + " rifampicin")
print(str(streptothricin) + " streptothricin" + "           /           " + str(Sulfonamide_trimethoprim) + " sulfonamide")            

