import random, time, rFunctions as rF, Menu

randomisedDice = list()

def rollD4():
    bRollD4 = True
    while bRollD4 == True:
        numRolls = int(input('Enter number of rolls:  '))
        for x in range(numRolls):
            randDice = (random.randint(1,4))
            time.sleep(0.75)
            print(randDice)
            randomisedDice.append(randDice)
        Sum = sum(randomisedDice)
        print('The total of all rolls is ' + str(Sum))
        randomisedDice.clear()

        rF.Enter()

        Rerole = True
        while Rerole == True:
            menuList = ['Do you want to keep rolling?', 'Yes', 'No']
            menuChoice = Menu.runMenu(menuList)

            if menuChoice == 1:
                Rerole = False
            elif menuChoice == 2:
                Rerole = False
                bRollD4 = False



