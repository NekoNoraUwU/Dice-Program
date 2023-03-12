import random, time, randomFunctions as rF, Menu

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

def rollD6():
    bRollD6 = True
    while bRollD6 == True:
        numRolls = int(input('Enter number of rolls:  '))
        for x in range(numRolls):
            randDice = (random.randint(1,6))
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
                bRollD6 = False

               


def rollD8():
    bRollD8 = True
    while bRollD8 == True:
        numRolls = int(input('Enter number of rolls:  '))
        for x in range(numRolls):
            randDice = (random.randint(1,8))
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
                bRollD8 = False


def rollD10():
    bRollD10 = True
    while bRollD10 == True:
        numRolls = int(input('Enter number of rolls:  '))
        for x in range(numRolls):
            randDice = (random.randint(1,10))
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
                bRollD10 = False


def rollD12():
    bRollD12 = True
    while bRollD12 == True:
        numRolls = int(input('Enter number of rolls:  '))
        for x in range(numRolls):
            randDice = (random.randint(1,12))
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
                bRollD12 = False


def rollD20():
    bRollD20 = True
    while bRollD20 == True:
        numRolls = int(input('Enter number of rolls:  '))
        for x in range(numRolls):
            randDice = (random.randint(1,20))
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
                bRollD20 = False



