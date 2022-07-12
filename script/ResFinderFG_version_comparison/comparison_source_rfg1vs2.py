# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 15:56:12 2022

@author: remi.gschwind
"""

t=0 ; y=0 ; z=0 ; w=0
tot = [] ; animal = [] ; human = [] ; soil = [] ; poll = [] ; aqua = [] ; plants = []
with open("C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_Analysis/analysis0422/output/rf1.csv" , 'r') as f :
    for line in f :
        t += 1
        tot.append(line.strip().split(';')[1])
        # HUMAN ASSOCIATED
        if ";feces;" in line :
            y += 1
            human.append(line.strip().split(';')[1])
        if ";latrine;" in line :
            y += 1
            human.append(line.strip().split(';')[1])
        # SOIL
        if ";soil;" in line :
            z += 1
            soil.append(line.strip().split(';')[1])
        # POLLUTED ENVIRONMENTS - WASTEWATER
        if ";sewage;" in line :
            w += 1
            poll.append(line.strip().split(';')[1])
num_rf1 = str(len(human)) + ";" + str(len(soil)) + ";" + str(len(poll)) + ";" + str(len(animal)) + ";" + str(len(aqua)) + ";" + str(len(plants))
x = 0 ; y = 0 ; z = 0 ; w = 0  ; v = 0 ; u = 0 ; t = 0
tot = [] ; animal = [] ; human = [] ; soil = [] ; poll = [] ; aqua = [] ; plants = []
with open("C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_Analysis/analysis0422/output/rf2.csv" , 'r') as f :
    for line in f :
        t += 1
        tot.append(line.strip().split(';')[1])
        # ANIMAL ASSOCIATED
        if ";larval_midguts;" in line :
            x += 1
            animal.append(line.strip().split(';')[1])
        if ";Gorilla_feces;" in line :
            x += 1
            animal.append(line.strip().split(';')[1])
        if ";Pan_troglodytes_feces;" in line :
            x += 1
            animal.append(line.strip().split(';')[1])
        if ";Cabrales_cheese;" in line :
            x += 1
            animal.append(line.strip().split(';')[1])
        if ";gull_gut;" in line :
            x += 1
            animal.append(line.strip().split(';')[1])
        if ";honeybee_gut;" in line :
            x += 1
            animal.append(line.strip().split(';')[1])
        if ";cow_manure;" in line :
            x += 1
            animal.append(line.strip().split(';')[1])
        if ";acuatic_sponge;" in line :
            x += 1
            animal.append(line.strip().split(';')[1])
        if ";duck_wastes;" in line :
            x += 1
            animal.append(line.strip().split(';')[1])
        if ";manure;" in line :
            x += 1
            animal.append(line.strip().split(';')[1])
        if ";chicken_microbiota;" in line :
            x += 1
            animal.append(line.strip().split(';')[1])
        # HUMAN ASSOCIATED
        if ";Human_feces;" in line :
            y += 1
            human.append(line.strip().split(';')[1])
        if ";human_fecal_matter;" in line :
            y += 1
            human.append(line.strip().split(';')[1])
        if ";feces;" in line :
            y += 1
            human.append(line.strip().split(';')[1])
        if ";gut;" in line :
            y += 1
            human.append(line.strip().split(';')[1])
        if ";Preterm_infant_stool;" in line :
            y += 1
            human.append(line.strip().split(';')[1])
        if ";newborn_gut;" in line :
            y += 1
            human.append(line.strip().split(';')[1])
        if ";human_gut;" in line :
            y += 1
            human.append(line.strip().split(';')[1])
        if ";pediatric_fecal_sample;" in line :
            y += 1
            human.append(line.strip().split(';')[1])
        if ";human_saliva;" in line :
            y += 1
            human.append(line.strip().split(';')[1])
        if ";retail_host;" in line :
            y += 1
            human.append(line.strip().split(';')[1])
        if ";latrine;" in line :
            y += 1
            human.append(line.strip().split(';')[1])
        # SOIL
        if ";soil;" in line :
            z += 1
            soil.append(line.strip().split(';')[1])
        if ";Soil;" in line :
            z += 1
            soil.append(line.strip().split(';')[1])
        if ";grassland_soil;" in line :
            z += 1
            soil.append(line.strip().split(';')[1])
        if ";Agricultural_soil;" in line :
            z += 1
            soil.append(line.strip().split(';')[1])
        if ";agricultural_soil;" in line :
            z += 1
            soil.append(line.strip().split(';')[1])
        if ";field_soil;" in line :
            z += 1
            soil.append(line.strip().split(';')[1])
        if ";Paenibacillus_from_Lechuguilla_cave;" in line :
            z += 1
            soil.append(line.strip().split(';')[1])
        if ";Active_layer_soil_from_the_Arctic;" in line :
            z += 1
            soil.append(line.strip().split(';')[1])
        if ";loamy_soil_collected_from_the_Zaidin;" in line :
            z += 1
            soil.append(line.strip().split(';')[1])
        if ";Yunnan_forest_soil;" in line :
            z += 1
            soil.append(line.strip().split(';')[1])
        if ";Sichuan_forest_soil;" in line :
            z += 1
            soil.append(line.strip().split(';')[1])
        if ";reed_bed_soil;" in line :
            z += 1
            soil.append(line.strip().split(';')[1])
        # POLLUTED ENVIRONMENTS - WASTEWATER
        if ";pharmaceutical_effluent;" in line :
            w += 1
            poll.append(line.strip().split(';')[1])
        if ";macrolide__polluted_river_sediment;" in line :
            w += 1
            poll.append(line.strip().split(';')[1])
        if ";antibiotics_polluted_stream_sediment;" in line :
            w += 1
            poll.append(line.strip().split(';')[1])
        if ";hospital_effluent;" in line :
            w += 1
            poll.append(line.strip().split(';')[1])
        if ";wastewater+triclosan;" in line :
            w += 1
            poll.append(line.strip().split(';')[1])
        if ";wastewater_treatment_plant;" in line :
            w += 1
            poll.append(line.strip().split(';')[1])
        if ";sewage;" in line :
            w += 1
            poll.append(line.strip().split(';')[1])
        # AQUATIC
        if ";stream_sediment;" in line :
            v += 1
            aqua.append(line.strip().split(';')[1])
        if ";ocean;" in line :
            v += 1
            aqua.append(line.strip().split(';')[1])
        if ";river;" in line :
            v += 1
            aqua.append(line.strip().split(';')[1])
        if ";river_water;" in line :
            v += 1
            aqua.append(line.strip().split(';')[1])
        # PLANTS
        if ";plant-associated_metagenome_(Alpine;" in line :
            u += 1
            plants.append(line.strip().split(';')[1])
        if ";rhizosphere_of_Mammillaria_carnea;" in line :
            u += 1
            plants.append(line.strip().split(';')[1])
num_rf2 = str(len(human)) + ";" + str(len(soil)) + ";" + str(len(poll)) + ";" + str(len(animal)) + ";" + str(len(aqua)) + ";" + str(len(plants))
legend = "Database;Human;Soil;Polluted;Animal;Acquatic;Plants"
with open("C:/Users/remi.gschwind/Desktop/Resfinder FG/ResFinder_FG_Analysis/analysis0422/output/comparison_source.csv" , 'w') as f :
    f.write(legend + "\n" + "ResFinderFG v1.1" + ";" + num_rf1 + "\n" + "ResFinderFG v2.0" + ";" + num_rf2)