#Level Stats
Level = 1
xp = 1
nxt_lvl = 25

#Leveling system
while xp >= nxt_lvl:
    Level += 1
    xp * xp - nxt_lvl
    nxt_lvl = round(nxt_lvl *1.5)

#Base Stats stored here
Base_Stats = {
            "Strength" :       1,
            "Dexterity" :      1,
            "Constitution" :   1,
            "Intelliigence" :  1,
            "Wisdom" :         1,
            "Charisma" :       1
}


BarbClassTraits = {
            "Animal Handling" : 1,
            "Athletics"       : 1,
            "Intimidation"    : 1,
            "Nature"          : 1,
            "Perception"      : 1,
            "Survival"        : 1







}


#Race Traits stored here
Racial_Traits = []

#Schools of magic/Magic stats

Magic_Stats = {

            "Abjuration" : 1,
            "Conjuration" :  1,
            "Divination" : 1,
            "Enchantment" : 1,
            "Evocation" : 1,
            "Illusion" : 1,
            "Necromancy" : 1,
            "Transmutation" : 1 

}



#Character Creation
Player_sheet = open('Playersheet.txt', "a+")
name = input("Adventuer what is your name?: ").capitalize()



#Race Select(Will loop back if Option "No is selected at race confirmation")
while True:
    race = input("What is your race ?:" + ("\n" * 2) + "Elf""\nDwarf""\nGnome""\nHalfElf""\nHalfling""\nOrc""\nHuman"+ ("\n" * 2) + "Choose one: ").capitalize()

    if race == "Elf":
        print("Elves are a magical people of otherworldly grace, living in the world but not entirely part of it. They live in places of ethereal beauty, in the midst of ancient forests or in silvery spires glittering with faerie light, where soft music drifts through the air and gentle fragrances waft on the breeze. Elves love nature and magic, art and artistry, music and poetry, and the good things of the world.")
        race2 = input("Would you like to be an Elf: (Yes/No) ").capitalize()
    
        if race2 == "Yes":
            Base_Stats["Dexterity"] += 2
            Rtrait2 = ["Darkvision", "Keen_Senses", "Fey_Ancestory", "Trance"]
            Racial_Traits.append(Rtrait2)
            break
        
        elif race2 == "No":
            continue

      
    if race == "Dwarf":
        print("Kingdoms rich in ancient grandeur, halls carved into the roots of mountains, the echoing of picks and hammers in deep mines and blazing forges, a commitment to clan and tradition, and a burning hatred of goblins and orcs—these common threads unite all dwarves.")
        race3 = input("Would you like to be an Dwarf: (Yes/No) ").capitalize()
    
        if race3 == "Yes":
            Base_Stats["Constitution"] += 2
            Rtrait3 = ["Darkvision", "Dwarven Resilience", "Dwarven Combat Training", "Stone Cunning"]
            Racial_Traits.append(Rtrait3)
            break
    
        elif race3 == "No":
            continue 

   
    
    if race == "Halfelf":
        print("Walking in two worlds but truly belonging to neither, half-elves combine what some say are the best qualities of their elf and human parents: human curiosity, inventiveness, and ambition tempered by the refined senses, love of nature, and artistic tastes of the elves. Some half-elves live among humans, set apart by their emotional and physical differences, watching friends and loved ones age while time barely touches them. Others live with the elves, growing restless as they reach adulthood in the timeless elven realms, while their peers continue to live as children. Many half-elves, unable to fit into either society, choose lives of solitary wandering or join with other misfits and outcasts in the adventuring life.")
        race4 = input("Would you like to be a Half-Elf: (Yes/No) ").capitalize()

        if race4 == "Yes":
            
            Base_Stats["Charisma"] += 2
            Rtrait4 = ["Darkvision", "Fey Ancestry", "Skill Versatility"]
            Racial_Traits.append(Rtrait4)

            print("Please choose two more Stats to +2:""\n" 
            "Strength""\n"       
            "Dexterity""\n"       
            "Constitution""\n"   
            "Intelliigence""\n"    
            "Wisdom""\n"         
            "Charisma") 

            HfStat1 = input("Stat one : ").capitalize()
            
            if HfStat1 == "Strength":
                Base_Stats["Strength"] +=2
            
            if HfStat1 == "Dexterity":
                Base_Stats["Dexterity"] +=2

            if HfStat1 == "Constitution":
                Base_Stats["Constitution"] +=2

            if HfStat1 == "Intelliigence":
                Base_Stats["Intelliigence"] +=2

            if HfStat1 == "Wisdom":
                Base_Stats["Wisdom"] +=2

            if HfStat1 == "Charisma":
                Base_Stats["Charisma"] +=2
                
                

            HfStat2 = input("Stat two : ").capitalize() 
            
            if HfStat2 == "Strength":
                Base_Stats["Strength"] +=2
            
            if HfStat2 == "Dexterity":
                Base_Stats["Dexterity"] +=2

            if HfStat2 == "Constitution":
                Base_Stats["Constitution"] +=2

            if HfStat2 == "Intelliigence":
                Base_Stats["Intelliigence"] +=2

            if HfStat2 == "Wisdom":
                Base_Stats["Wisdom"] +=2

            if HfStat2 == "Charisma":
                Base_Stats["Charisma"] +=2


            break 

        elif race4 == "No":
            continue 

        
             
    
    if race == "Gnome":
        print("A constant hum of busy activity pervades the warrens and neighborhoods where gnomes form their close-knit communities. Louder sounds punctuate the hum: a crunch of grinding gears here, a minor explosion there, a yelp of surprise or triumph, and especially bursts of laughter. Gnomes take delight in life, enjoying every moment of invention, exploration, investigation, creation, and play.")
        race5 = input("Would you like to be an Gnome: (Yes/No) ").capitalize()

        if race5 == "Yes":
            Base_Stats["Intelliigence"] += 2
            Rtrait5 = ['Darkvision', "Gnome Cunning"]
            Racial_Traits.append(Rtrait5)
            break
        
        elif race4 == "No":
            continue 


    
    if race == "Halfling":
        print("The comforts of home are the goals of most halflings’ lives: a place to settle in peace and quiet, far from marauding monsters and clashing armies; a blazing fire and a generous meal; fine drink and fine conversation. Though some halflings live out their days in remote agricultural communities, others form nomadic bands that travel constantly, lured by the open road and the wide horizon to discover the wonders of new lands and peoples. But even these wanderers love peace, food, hearth, and home, though home might be a wagon jostling along a dirt road or a raft floating downriver")
        race6 = input("Would you like to be an Halfling: (Yes/No) ").capitalize()

        if race6 == "Yes":
            Base_Stats["Charisma"] += 2
            Rtrait6 = ["Lucky", "Brave", "Halfling Nimbleness"]
            break

        elif race5 == "No":
            continue



    if race == "Orc":
        print("Orcs are savage humanoids with stooped postures, piggish faces, and prominent teeth that resemble tusks. They gather in tribes that satisfy their bloodlust by slaying any humanoids that stand against them.")
        race7 = input("Would you like to be an Orc: (Yes/No) ").capitalize()

        if race7 == "Yes":
            Base_Stats["Strength"] += 2
            Rtrait7 = ["Darkvision", "Menacing","Relentless Endurance ", "Savage Attacks"]
            Racial_Traits.append(Rtrait7)
            break
        
        elif race6 == "No":
            continue


    if race == "Human":
        print("In the reckonings of most worlds, humans are the youngest of the common races, late to arrive on the world scene and short-lived in comparison to dwarves, elves, and dragons. Perhaps it is because of their shorter lives that they strive to achieve as much as they can in the years they are given. Or maybe they feel they have something to prove to the elder races, and that’s why they build their mighty empires on the foundation of conquest and trade. Whatever drives them, humans are the innovators, the achievers, and the pioneers of the worlds. A Broad Spectrum")
        race8 = input("Would you like to be an Human: (Yes/No) ").capitalize()
        if race8 == "Yes":
           Base_Stats["Strength"] += 1 
           Base_Stats["Dexterity"] += 1
           Base_Stats["Constitution"] += 1
           Base_Stats["Intelliigence"]  += 1
           Base_Stats["Wisdom"]  += 1
           Base_Stats["Charisma"]  += 1  
           Rtrait8 = ["Extra Language"]
           Racial_Traits.append(Rtrait8)
           break
        
        elif race7 == "No":
            continue 
    
while True:    
    print("Oh is that so . . . . " + ("\n" *2) + "Tell me, what is your class?","\nWizard", "\nBarbarian", "\nBard","\nCleric", "\nDruid", "\nFighter", "\nMonk", "\nPaladin","\nRanger", "\nRogue", "\nSorcerer", "\nWarlock" )

    player_role = input("What have you chosen: ").capitalize()

    if player_role == "Barbarian":
        Bconfirm = input("So you prefer brute force over skill (Yes/No): ").capitalize()


        

        if Bconfirm == "Yes":
            print("What do your barbarian instincts allows you to excel at? Choose two:,  ""\nAnimal Handling", "\nAthletics", "\nIntimidation", "\nNature", "\nPerception", "\nSurvival")
            while True:
                BarbChoice1 = input(" What is your first choice? : ").capitalize()

              
                if BarbChoice1 == "":
                    continue

                else:

                    if BarbChoice1 == "Animal Handling":
                        BarbClassTraits["Animal Handling"] +=1
                        

                    if BarbChoice1 == "Athletics":
                        BarbClassTraits["Athletics"] +=1
                        

                    if BarbChoice1 == "Intimidation":
                        BarbClassTraits["Intimidation"] +=1  
            
                    if BarbChoice1 == "Nature":
                        BarbClassTraits["Nature"] +=1
            
                    if BarbChoice1 == "Perception":
                        BarbClassTraits["Perception"] +=1

                    if BarbChoice1 == "Survival":
                        BarbClassTraits["Survival"] +=1
                
                    break

            while True:
                BarbChoice2 = input(" What is your second choice? : ").capitalize()

              
                if BarbChoice2 == "":
                    continue

                else:

                    if BarbChoice2 == "Animal Handling":
                        BarbClassTraits["Animal Handling"] +=1
                        

                    if BarbChoice2 == "Athletics":
                        BarbClassTraits["Athletics"] +=1
                        

                    if BarbChoice2 == "Intimidation":
                        BarbClassTraits["Intimidation"] +=1  
            
                    if BarbChoice2 == "Nature":
                        BarbClassTraits["Nature"] +=1
            
                    if BarbChoice2 == "Perception":
                        BarbClassTraits["Perception"] +=1

                    if BarbChoice2 == "Survival":
                        BarbClassTraits["Survival"] +=1
                
                    break

           

           

               
            
       

    if player_role == "Wizard":
        Wconfirm = input("So you dable in the mystical arts (Yes/No): ").capitalize()

        if Wconfirm == "Yes":
            print("What school of magic do you excel in?","\nAbjuratio","\nTransmutation","\nConjuration","\nDivination","\nEnchantment","\nIllusion","\nnIllusion")
            Magic_Proficency = input("What have you chosen?: ").capitalize()

            if Magic_Proficency == "Abjuration":
                Magic_Stats["Abjuration"] += 2

            elif Magic_Proficency == "Transmutation":
                Magic_Stats["Transmutation"] += 2
    
            elif Magic_Proficency == "Conjuration":
                Magic_Stats["Conjuration"] += 2
    
            elif Magic_Proficency == "Divination":
                Magic_Stats["Divination"] += 2
    
            elif Magic_Proficency == "Enchantment":
                Magic_Stats["Enchantment"] += 2
    
            elif Magic_Proficency == "Illusion":
                Magic_Stats["Illusion"] += 2
    
            elif Magic_Proficency == "Necromancy":
                Magic_Stats["Necromancy"] += 2

        
            break

        else:
            continue




    
    exit()
    
