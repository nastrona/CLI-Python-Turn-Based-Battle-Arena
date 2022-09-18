import util
import random
import char

class pvsp():
    hmhero = 0
    p1list = []
    p2list = []
 
    def nohero(self):
        while True:
            try:
                self.hmhero = int(input("Please enter the number of heroes in battle for each side.\nRemember that default is 3 and if lower than 3 is auto assigned to 3: "))
                if self.hmhero < 3:
                    self.hmhero = 3
                    print("Automatically assigned to 3 units.")
                    
                    break
                elif self.hmhero >= 3:
                    break
                else:
                    print("No input. Please re-enter!")
            except ValueError:
                print("Only accept numerical value!")

    def selectheroP1(self):
        character = char.char()
        p1dict = {}
        j = 1

        for i in range(0, self.hmhero):
            player_units_name = str(input("For Player1: Enter name for unit {}: ". format(j)))
            p1dict["ID"] = i+1
            p1dict["Name"] = player_units_name

            player_units_hero = input("Enter unit hero type for {} \n(W)arrior \n(T)ank \nType: ".format(p1dict["Name"]))
            if player_units_hero == "W" or player_units_hero == "w":
                p1dict["Hero"] = "Warrior"
                p1dict.update(character.Warrior())
            elif player_units_hero == "T" or player_units_hero == "t":
                p1dict["Hero"] = "Tank"
                p1dict.update(character.Tank())
            else:
                print("Invalid Hero. Please restart choosing hero.")
                self.selectheroP1()

            j += 1
            self.p1list.insert(i, p1dict)
            p1dict = {}

    def selectheroP2(self):

        character = char.char()
        p2dict = {}
        j = 1

        for i in range(0, self.hmhero):
            player_units_name = str(input("For Player2 : Enter name for unit {}: ". format(j)))
            p2dict["ID"] = i+1
            p2dict["Name"] = player_units_name

            player_units_hero = input("Enter unit hero type for {} \n(W)arrior \n(T)ank \nType: ".format(p2dict["Name"]))
            if player_units_hero == "W" or player_units_hero == "w":
                p2dict["Hero"] = "Warrior"
                p2dict.update(character.Warrior())
            elif player_units_hero == "T" or player_units_hero == "t":
                p2dict["Hero"] = "Tank"
                p2dict.update(character.Tank())
            else:
                print("Invalid Hero. Please restart choosing hero.")
                self.selectheroP2()

            j += 1
            self.p2list.insert(i, p2dict)
            p2dict = {}

    def displaybteams(self):

        print("\nPlayer1 Hero List")
        for i in range(0,self.hmhero):
            if self.p1list[i]["Alive"]:
                print("==================================")
                print("ID: ", self.p1list[i]["ID"], "\nName: ", self.p1list[i]["Name"], "\nHero: ", self.p1list[i]["Hero"], "\nHP: ",self.p1list[i]["HP"], "\nLevel: ",self.p1list[i]["Level"], "\nAlive: ",self.p1list[i]["Alive"], "\nEXP: ", self.p1list[i]["EXP"])
            else:
                print("Player1 has lost the game!")
            print("==================================")

        print("\nPlayer2 Hero List")

        for i in range(0,self.hmhero):
            if self.p2list[i]["Alive"]:
                print("==================================")
                print("ID: ", self.p2list[i]["ID"], "\nName: ", self.p2list[i]["Name"], "\nHero: ", self.p2list[i]["Hero"], "\nHP: ",self.p2list[i]["HP"], "\nLevel: ",self.p2list[i]["Level"], "\nAlive: ",self.p2list[i]["Alive"], "\nEXP: ", self.p2list[i]["EXP"])
            else:
                print("Player2 has lost the game!")
            print("==================================")

    def P1attack(self):

        attacker1 = int(input("For Player1: Please select one of your hero\'s ID to attack: "))

        if self.p1list[attacker1 - 1]["Alive"]:
            defender1 = int(input("Please select one of the Player2 hero\'s ID to attack: "))
            if self.p2list[defender1 - 1]["Alive"]:
                atk = random.randint(self.p1list[attacker1 - 1]["MIN_ATK"], self.p1list[attacker1 - 1]["MAX_ATK"])
                dfs = random.randint(self.p2list[defender1 - 1]["MIN_DEF"], self.p2list[defender1 - 1]["MAX_DEF"])
                dmg = atk - dfs
                if dmg < 0:
                    dmg = 0
                atk_exp = dmg + (dmg*0.8)
                def_exp = dmg + (dmg*0.3)

                self.p2list[defender1 - 1]["HP"] -= dmg
                self.p1list[attacker1 - 1]["EXP"] += atk_exp
                self.p2list[defender1 - 1]["EXP"] += def_exp

                if self.p2list[defender1 - 1]["EXP"] >= 100:
                    self.p2list[defender1 - 1]["Level"] += 1
                    self.p2list[defender1 - 1]["EXP"] = 0

                if self.p1list[attacker1 - 1]["EXP"] >= 100:
                    self.p1list[attacker1 - 1]["Level"] += 1
                    self.p1list[attacker1 - 1]["EXP"] = 0

                if self.p2list[defender1 - 1]["HP"] <= 0:
                    self.p2list[defender1 - 1]["Alive"] = False

            else:
                print("You can\'t attack a dead AI unit.")
                self.P1attack()
        else:
            print("You can\'t choose your dead hero.")
            self.P1attack()

    def P2attack(self):

        attacker2 = int(input("For Player2: Please select one of your hero\'s ID to attack: "))

        if self.p2list[attacker2 - 1]["Alive"]:
            defender2 = int(input("Please select one of the Player1 hero\'s ID to attack: "))
            if self.p1list[defender2 - 1]["Alive"]:
                atk = random.randint(self.p2list[attacker2 - 1]["MIN_ATK"], self.p2list[attacker2 - 1]["MAX_ATK"])
                dfs = random.randint(self.p1list[defender2 - 1]["MIN_DEF"], self.p1list[defender2 - 1]["MAX_DEF"])
                dmg = atk - dfs
                if dmg < 0:
                    dmg = 0
                atk_exp = dmg + (dmg*0.8)
                def_exp = dmg + (dmg*0.3)

                self.p1list[defender2 - 1]["HP"] -= dmg
                self.p2list[attacker2 - 1]["EXP"] += atk_exp
                self.p1list[defender2 - 1]["EXP"] += def_exp

                if self.p1list[defender2 - 1]["EXP"] >= 100:
                    self.p1list[defender2 - 1]["Level"] += 1
                    self.p1list[defender2 - 1]["EXP"] = 0

                if self.p2list[attacker2 - 1]["EXP"] >= 100:
                    self.p2list[attacker2 - 1]["Level"] += 1
                    self.p2list[attacker2 - 1]["EXP"] = 0

                if self.p1list[defender2 - 1]["HP"] <= 0:
                    self.p1list[defender2 - 1]["Alive"] = False

            else:
                print("You can\'t attack a dead AI unit.")
                self.P2attack()
        else:
            print("You can\'t choose your dead hero.")
            self.P2attack()

    def checkp1(self):
        status = True
        b = 0
        for h in range(0, len(self.p1list)):
            if self.p1list[h]["HP"] <= 0:
                self.p1list[h]["HP"] = 0
                self.p1list[h]["Alive"] = False
        for l in range(0, len(self.p1list)):
            if not self.p1list[l]["Alive"]:
                b += 1

        if b == len(self.p1list):
            status = False
        else:
            status = True

    def checkp2(self):
        status = True
        b = 0
        for h in range(0, len(self.p2list)):
            if self.p2list[h]["HP"] <= 0:
                self.p2list[h]["HP"] = 0
                self.p2list[h]["Alive"] = False
        for l in range(0, len(self.p2list)):
            if not self.p2list[l]["Alive"]:
                b += 1

        if b == len(self.p2list):
            status = False
        else:
            status = True

    def gamestatus(self):

        status = False
        check1 = self.checkp1()
        check2 = self.checkp2()

        if (not check1) and (not check2):
            status = True
        elif (not check1) and (check2):
            status = True
        elif (check1) and (not check2):
            status = True
        else:
            status = False

        return status

    def pvsp_main(self):
        self.nohero()
        self.selectheroP1()
        self.selectheroP2()
        self.displaybteams()

        a = self.checkp1()
        b = self.checkp2()

        gameover = False

        while not gameover:
            if not gameover:
                self.P1attack()
                gameover = self.gamestatus()
                self.displaybteams()
                if not gameover:
                    self.P2attack()
                    gameover = self.gamestatus()
                    self.displaybteams()