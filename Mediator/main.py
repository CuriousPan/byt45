from BoardMediator import *
from msvcrt import getch

def main():

    board = BoardMediator()

    cannonBtn = Button("Fire cannon", 1, board)
    rocketBtn = Button("Launch rocket", 2, board)
    machineGunBtn = Button("Fire machine gun", 3, board) 

    while (True):
        print("Use 1, 2 or 3 buttons to click the buttons")
        print("Use q or Q to exit")
        print("|(1)" + cannonBtn.text + "| |(2)" + rocketBtn.text + "| |(3)" + machineGunBtn.text + "|") 

        key = ord(getch())
        if (key == 49):
            cannonBtn.click()
        elif (key == 50):
            rocketBtn.click()
        elif (key == 51):
            machineGunBtn.click()
        elif (key == 113 or key == 81):
            break
        print()
        

if __name__ == "__main__":
    main()
