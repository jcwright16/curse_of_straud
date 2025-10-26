#!/bin/bash
echo -n "Enter your character's race: " 
read character_race
echo -n "Enter your character's class: "
read character_class
echo -n "Enter target filename: "
read filename

python roll_character.py $character_race $character_class $filename