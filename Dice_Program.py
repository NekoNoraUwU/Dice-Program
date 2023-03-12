import diceFunctions as DF, Menu

#------------------------------------------Main Code---------------------------------------------

mainLoop = True
while mainLoop == True:
    menuList = ['\n\n---------------Main Menu---------------\n\n', 'Roll a D4', 'roll a D6', 'Roll a D8', 'Roll a D10', 'Roll a D12', 'Roll a D20', 'Quit']

    menuChoice = Menu.runMenu(menuList)

    if menuChoice == 1:
        DF.rollD4()
    elif menuChoice == 2:
        DF.rollD6()
    elif menuChoice == 3:
        DF.rollD8()
    elif menuChoice == 4:
        DF.rollD10()
    elif menuChoice == 5:
        DF.rollD12()
    elif menuChoice == 6:
        DF.rollD20()
    elif menuChoice == 7:
        quit()



