import random

class ValueOutOfRange(Exception):
    pass

def runMenu(menuList):
    loop = True
    while loop == True:
        try:
            print(menuList[0])
  
            for x in range(1, len(menuList)):
                print(str(x) + ': ' + menuList[x])
  
            menuChoice = int(input('\nPlease make a selection from the list provided: \n'))
            if menuChoice > len(menuList) -1 or menuChoice < 1:
                raise ValueOutOfRange
        except ValueOutOfRange:
            print('\n\nEnter a number from the list provided...\n')
            print('[Press Enter To Continue]')
      
        except ValueError:
            print('\n\nEnter a whole number from the list provided...\n')
            print('[Press Enter To Continue]')

        except:
            print('\n\nan unknown error has occured... please try again...\n')
            print('[Press Enter To Continue]')

        else:
            loop = False
            return menuChoice

#------------------------------------------Main Code---------------------------------------------

mainLoop = True
while mainLoop == True:
    menuList = ['\n\n---------------Main Menu---------------\n\n', 'Roll a D4', 'roll a D6', 'Roll a D8', 'Roll a D10', 'Roll a D12', 'Roll a D20', 'Quit']

    menuChoice = runMenu(menuList)

    if menuChoice == 1:
        print('EEE')
        #rollD4()
    elif menuChoice == 2:
        rollD6()
    elif menuChoice == 3:
        rollD8()
    elif menuChoice == 4:
        rollD10()
    elif menuChoice == 5:
        rollD12()
    elif menuChoice == 6:
        print('wewe')
        #rollD20()
    elif menuChoice == 7:
        Exit()



