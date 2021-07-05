#Todo for character creator

# 1. Finish Setting up classes.
# 2. Add ability to add +1's for ability scores for races that have it.
# 3. Create final description of character after all settings inputed.
# 4. Create weapon selection when picking class.



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
Player_sheet = open('Playersheet.txt', "w+")
name = input("Adventuer what is your name?: ").capitalize()

#Race Select(Will loop back if Option "No is selected at race confirmation")
while True:
    race = input("What is your race ?:" + ("\n" * 2) + "Elf""\nDwarf""\nGnome""\nHalf-Elf""\nHalfling""\nOrc""\nHuman"+ ("\n" * 2) + "Choose one: ").capitalize()

    if race == "Elf":
        print("Elf Description here")
        race2 = input("Would you like to be an Elf: (Yes/No) ").capitalize()
    
        if race2 == "Yes":
            Base_Stats["Dexterity"] += 2
            Rtrait2 = ["Darkvision", "Keen_Senses", "Fey_Ancestory", "Trance"]
            Racial_Traits.append(Rtrait2)
            break
        
        elif race2 == "No":
            continue

      
    if race == "Dwarf":
        print("Dwarf Description here")
        race3 = input("Would you like to be an Dwarf: (Yes/No) ").capitalize()
    
        if race3 == "Yes":
            Base_Stats["Constitution"] += 2
            Rtrait3 = ["Darkvision", "Dwarven Resilience", "Dwarven Combat Training", "Stone Cunning"]
            Racial_Traits.append(Rtrait3)
            break
    
        elif race3 == "No":
            continue 

   
    
    if race == "Half-Elf":
        print("Half-Elf Desciption here")
        race4 = input("Would you like to be a Half-Elf: (Yes/No) ").capitalize()

        if race4 == "Yes":
            Base_Stats["Charisma"] += 2
            Rtrait4 = ["Darkvision", "Fey Ancestry", "Skill Versatility"]
            Racial_Traits.append(Rtrait4)
            #Add option to choose two more abilitys to +1
            break
        
        elif race4 == "No":
            continue 

    
    if race == "Gnome":
        print("Gnome Description here")
        race5 = input("Would you like to be an Gnome: (Yes/No) ").capitalize()

        if race5 == "Yes":
            Base_Stats["Intelliigence"] += 2
            Rtrait5 = ['Darkvision', "Gnome Cunning"]
            Racial_Traits.append(Rtrait5)
            break
        
        elif race4 == "No":
            continue 


    
    if race == "Halfling":
        print("Halfling Description here")
        race6 = input("Would you like to be an Halfling: (Yes/No) ").capitalize()

        if race6 == "Yes":
            Base_Stats["Charisma"] += 2
            Rtrait6 = ["Lucky", "Brave", "Halfling Nimbleness"]
            break

        elif race5 == "No":
            continue



    if race == "Orc":
        print("Orc Description here")
        race7 = input("Would you like to be an Orc: (Yes/No) ").capitalize()

        if race7 == "Yes":
            Base_Stats["Strength"] += 2
            Rtrait7 = ["Darkvision", "Menacing","Relentless Endurance ", "Savage Attacks"]
            Racial_Traits.append(Rtrait7)
            break
        
        elif race6 == "No":
            continue


    if race == "Human":
        print("Human Description here")
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
        Bconfirm = input("So you prefer brute force over skill (Yes/No): ")

        if Bconfirm == "Yes":
            break

        else:
            continue
    
    if player_role == "Wizard":
        Wconfirm = input("So you dable in the mystical arts (Yes/No): ").capitalize()

        if Wconfirm == "Yes":
            print("What school of magic do you excel in?","\nAbjuration,","Transmutation,","Conjuration,","Divination,","Enchantment,","Illusion,","Necromancy,")
            Magic_Proficency = input("What have you chosen?: ").capitalize()
            break

        else:
            continue
      


#if Magic_Proficency == "Abjuration":
        #Magic_Stats["Abjuration"] += 2

#elif Magic_Proficency == "Transmutation":
        #Magic_Stats["Transmutation"] += 2
    
#elif Magic_Proficency == "Conjuration":
        #Magic_Stats["Conjuration"] += 2
    
#elif Magic_Proficency == "Divination":
        #Magic_Stats["Divination"] += 2
    
#elif Magic_Proficency == "Enchantment":
        #Magic_Stats["Enchantment"] += 2
    
#elif Magic_Proficency == "Illusion":
        #Magic_Stats["Illusion"] += 2
    
#elif Magic_Proficency == "Necromancy":
       # Magic_Stats["Necromancy"] += 2

    

        

        

        
 #Sheet editor       
Sheet_contents = ["Name: "+ name +"\n", 
"Race: " + race +"\n", 
"Racial Traits:" + str(Racial_Traits) + 
"\n","Magic Proficency: " + Magic_Proficency + ("\n" * 5 ),
"-------------------Level Stats-------------------""\n",
"Character Level: " + str(Level) + "\n",
"Experience: " + str(xp) + "\n", 
"Experince till next level: " + str(nxt_lvl) + ("\n" * 5),
"-------------------Stats-------------------""\n",
"Strength: " + str(Base_Stats.get("Strength")) + "\n", 
"Dexterity: " + str(Base_Stats.get("Dexterity"))+ "\n",
"Constitution: " + str(Base_Stats.get("Constitution")) + "\n", 
"Intelligence: " + str(Base_Stats.get("Intelliigence")) + "\n", 
"Charisma: " + str(Base_Stats.get("Charisma")) + "\n", 
"Wisdom: " + str(Base_Stats.get("Wisdom"))  +  ("\n" * 5),
"-------------------Magic Stats-------------------""\n",
"Abjuration: " + str(Magic_Stats.get("Abjuration")) + "\n", 
"Transmutation: " + str(Magic_Stats.get("Transmutation")) + "\n", 
"Conjuration: " + str(Magic_Stats.get("Conjuration")) + "\n", 
"Divination: " + str(Magic_Stats.get("Divination")) + "\n", 
"Enchantment: " + str(Magic_Stats.get("Enchantment")) + "\n", 
"Illusion: " + str(Magic_Stats.get("Illusion")) + "\n", 
"Necromancy: " + str(Magic_Stats.get("Necromancy")) + "\n", 


]


Player_sheet.writelines(Sheet_contents)




