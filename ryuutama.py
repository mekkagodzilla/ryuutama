import pyinputplus as pyip
import random


class PlayerCharacter:



    def __repr__(self):
        return f'{self.name} is a level {self.level} {self.Class} of the {self.type} Type.'
   

    def setStartingAbilityScores(self):
        print("\nLet's set ability scores for", self.name,'\n')
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
        
        self.maxHP = self.abilityScores['STR'] * 2
        self.maxSP = self.abilityScores['SPI'] * 2
        
        print("Your ability scores are:", self.abilityScores)


    def __init__(self):
        print("Let's create a character for you…\n")
        ClassList = sorted(['Minstrel', 'Merchant', 'Farmer', 'Hunter', 'Healer',
                       'Noble', 'Artisan'])

        typeList = sorted(['Attack', 'Technical', 'Magical'])
    
        genderList = (['girl', 'boy', 'non-gendered', 'other'])

        self.name = pyip.inputStr("What is your character's name?\n")
        self.Class = pyip.inputMenu(ClassList, lettered=True,
                           prompt='Select your class…\n')

        self.type = pyip.inputMenu(typeList, lettered=True, prompt='Select a type\n')

        self.level = 1
        self.XP = 0
        self.gender = pyip.inputMenu(genderList, lettered=True, prompt='You are a…\n')

        self.fumbles = 0
        self.condition = None
    

    def rollTest(self, ability1, ability2, modifier=0):
        roll = [random.randint(1, self.abilityScores[ability1]), random.randint(1, self.abilityScores[ability2]), modifier]
        if sum(roll[:-1]) == 2:
            print('Oh no, a fumble!')
            self.fumbles += 1
        elif roll[:-1] == [self.abilityScores[ability1], self.abilityScores[ability2]] or roll[:-1] == [6, 6]:
            print('CRITICAL SUCCESS!')
        else:
            print(f"You rolled a {sum(roll)}.")
    
    def rollCondition(self, modifier=0):
        return self.rollTest('STR', 'SPI', modifier)
            

class Ryuujin:
    pass




