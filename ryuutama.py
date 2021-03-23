import pyinputplus as pyip
import random


class PlayerCharacter:
    def __init__(self):
        self.name = pyip.inputStr("What is your character's name?\n")

    ClassList = sorted(['Minstrel', 'Merchant', 'Farmer', 'Hunter', 'Healer',
                       'Noble', 'Artisan'])

    typeList = sorted(['Attack', 'Technical', 'Magical'])
    genderList = (['girl', 'boy', 'non-gendered', 'other'])

    Class = pyip.inputMenu(ClassList, lettered=True,
                           prompt='Select your class…\n')

    type = pyip.inputMenu(typeList, lettered=True, prompt='Select a type\n')

    level = 1
    XP = 0
    gender = pyip.inputMenu(genderList, lettered=True, prompt='You are a…\n')

    def __repr__(self):
        return f'''{self.name} is a level {self.level} {self.Class}
    of the {self.type} Type.'''


    

    def setStartingAbilityScores(self):
        self.abilityScores = {'STR': 6, 'DEX': 6, 'INT': 6, 'SPI': 6}
        setChoices = ['Average Set, 6 in all ability scores',
                      'Standard Set: 4 6 6 8',
                      'Specialization set: 4 4 8 8'
                      ]
        setWanted = pyip.inputMenu(setChoices, lettered=True, prompt='What set of Ability scores do you want?\n')
        if setWanted == setChoices[1]:
            scoreToDump = pyip.inputMenu(list(self.abilityScores.keys()), lettered=True, prompt='Which score to lower to a 4?\n')
            scoreToBump = pyip.inputMenu([score for score in self.abilityScores.keys() if score != scoreToDump], lettered=True, prompt='Which score to raise to an 8?\n')
            self.abilityScores[scoreToDump] -= 2
            self.abilityScores[scoreToBump] += 2
        elif setWanted == setChoices[2]:
            scoreToDump1 = pyip.inputMenu(list(self.abilityScores.keys()), lettered=True, prompt='Select the first score to lower to a 4\n')
            scoreToDump2 = pyip.inputMenu([score for score in self.abilityScores.keys() if score != scoreToDump1], lettered=True, prompt='Select a second score to lower to a 4\n')
            scoresToBump = [score for score in self.abilityScores.keys() if score not in [scoreToDump1, scoreToDump2]]
            self.abilityScores[scoreToDump1] -= 2
            self.abilityScores[scoreToDump2] -= 2
            for score in scoresToBump:
                self.abilityScores[score] += 2




class Ryuujin:
    pass


phil = PlayerCharacter()

print(phil)
phil.setStartingAbilityScores()

print(f"{phil.name}'s strength is", phil.abilityScores['STR'])
print(f"{phil.name}'s dexterity is", phil.abilityScores['DEX'])
print(f"{phil.name}'s intellect is", phil.abilityScores['INT'])
print(f"{phil.name}'s spirit is", phil.abilityScores['SPI'])