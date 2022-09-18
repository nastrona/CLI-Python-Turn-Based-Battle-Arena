import random
import sys
import util
import pvai
import pvsp

class BattleArena:
    util = util
    cpvai = pvai.pvai()
    cpvsp = pvsp.pvsp()

    def __init__(self):
        print("Welcome to PSB Turn-Based Battle Arena!")

        while True:
            choice = input("Choose an option: (N)ew Game \n\t\t  (L)oad Game \n\t\t  (Q)uit \nOption: ")
            if choice == "N" or choice =="n":
                util.NewGame(self)
                break
            elif choice == "L" or choice == "l":
                print("To load an existing saved game, \nplease make changes in the source python code in this following format. \n\nimport <Module_Name> \nModule_Name.Function_Name()")
                print()
                break
                choice = ""
            elif choice == "q" or choice == "Q":
                print("Quitting Game...")
                sys.exit()
                print()
                break

            else:
                print("Please reenter the option!")

BattleArena()

