import pvsp
import pvai
import sys

def NewGame(self):
    upvsp = pvsp.pvsp()
    upvai = pvai.pvai()

    while True:
        game_mode = input("(1) Player Vs AI \n(2) Player Vs Player \nOption: ")

        if game_mode == "1":
            upvai.pvai_main()
            break
        elif game_mode == "2":
            upvsp.pvsp_main()
            break
        else:
            print("No option. Restart the game.")