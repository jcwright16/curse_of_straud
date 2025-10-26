import sys
import os
import random

character_race = sys.argv[0]
character_class = sys.argv[1]

if character_race not in ['Human', 'Dwarf', 'Elf', 'Gnome', 'Half-elf', 'Half-orc', 'Halfling']:
    print("Your character's race was not found in the PHB.")
    sys.exit()

if character_class not in ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Wizard']:
    print("Your character's class was not found in the PHB.")
    sys.exit()

filepath = f'/home/jason/Documents/repos/curse_of_straud/characters/{sys.argv[2]}'

if not os.path.exists(filepath):
    os.mknod(filepath)

racial_bonus_dict = {
    'Human': 'None',
    'Dwarf': '+2 CON, -2 CHA',
    'Elf': '+2 DEX, -2 CON',
    'Gnome': '+2 CON, -2 STR',
    'Half-elf': 'None',
    'Half-orc': '+2 STR, -2 INT, -2 CHA',
    'Halfling': '+2 DEX, -2 STR'
}

# Roll Base Stats
base_stats = []

while len(base_stats) < 7:
    rolls = random.choices(range(1, 7), k=4)
    rolls.remove(min(rolls))
    total = sum(rolls)
    base_stats.append(total)

base_stats.remove(min(base_stats)) 

# Roll Age
if character_race == 'Human':
    if character_class in ['Barbarian', 'Rogue', 'Sorcerer']:
        character_age = 15 + random.randint(1,4)
    elif character_class in ['Bard', 'Fighter', 'Paladin', 'Ranger']:
        character_age = 15 + random.randint(1,6)
    elif character_class in ['Cleric', 'Druid', 'Monk', 'Wizard']:
        character_age = 15 + random.randint(1,6) + random.randint(1,6)
    else: 
        character_age = 0
else:
    character_age = 0

# Roll Height

# Roll Weight

# Roll Wealth