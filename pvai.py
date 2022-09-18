import util
import random
import char

class pvai():
    hmhero = 0
    plist = []
    ailist = []
 
    def nohero(self):
        while True:
            try:
                self.hmhero = int(input("Please enter the number of heroes in battle for each side.\nRemember that default is 3: "))
                if self.hmhero == 0:
                    self.hmhero = 3
                break
            except ValueError:
                print("Only accept numerical value!")
    
    def selectheroP(self):
        character = char.char()
        pdict = {}
        j = 1

        for i in range(0, self.hmhero):
            player_units_name = str(input("Enter player name for unit {}: ". format(j)))
            pdict["ID"] = i+1
            pdict["Name"] = player_units_name

            player_units_hero = input("Enter unit hero type for {} \n(W)arrior \n(T)ank \nType: ".format(pdict["Name"]))
            if player_units_hero == "W" or player_units_hero == "w":
                pdict["Hero"] = "Warrior"
                pdict.update(character.Warrior())
            elif player_units_hero == "T" or player_units_hero == "t":
                pdict["Hero"] = "Tank"
                pdict.update(character.Tank())
            else:
                print("Invalid Hero. Please restart choosing hero.")
                self.selectheroP()

            j += 1
            self.plist.insert(i, pdict)
            pdict = {}

    def selectheroAI(self):

        character = char.char()
        aidict = {}
        ai_units_nno = ""

        for l in range(0, self.hmhero):
            ai_units_nno = random.randint(10, 99)
            ai_units_name = "AI" + str(ai_units_nno)
            aidict["ID"] = l + 1
            aidict["Name"] = ai_units_name

            ai_choose = random.randint(0,1)
            ai_choosable_hero = ["Warrior", "Tank"]
            ai_units_type = ai_choosable_hero[ai_choose]

            if ai_units_type == "Warrior":
                aidict["Hero"] = ai_units_type
                aidict.update(character.Warrior())
            elif ai_units_type == "Tank":
                aidict["Hero"] = ai_units_type
                aidict.update(character.Tank())

            self.ailist.insert(l, aidict)
            aidict = {}
   
    def displaybteams(self):

        print("\nPlayer Hero List")
        for i in range(0, self.hmhero):
            if self.plist[i]["Alive"]:
                print("==================================")
                print("ID: ", self.plist[i]["ID"], "\nName: ", self.plist[i]["Name"], "\nHero: ", self.plist[i]["Hero"], "\nHP: ",self.plist[i]["HP"], "\nLevel: ",self.plist[i]["Level"], "\nAlive: ",self.plist[i]["Alive"], "\nEXP: ", self.plist[i]["EXP"])
                print("==================================")
            else:
                print("Player has lost the game! ")

        print("\nAI Hero List")
        for j in range(0, self.hmhero):
            if self.ailist[i]["Alive"]:
                print("==================================")
                print("ID: ", self.ailist[j]["ID"], "\nName: ", self.ailist[j]["Name"], "\nHero: ", self.ailist[j]["Hero"], "\nHP: ",self.ailist[j]["HP"], "\nLevel: ",self.ailist[j]["Level"], "\nAlive: ",self.plist[j]["Alive"], "\nEXP: ", self.ailist[i]["EXP"])
                print("==================================")
            else:
                print("AI has lost the game! Congratulations!")

    def Pattack(self):

        attacker1 = int(input("Please select one of your hero\'s ID to attack: "))

        if self.plist[attacker1 - 1]["Alive"]:
            defender1 = int(input("Please select one of the AI hero\'s ID to attack: "))
            if self.ailist[defender1 - 1]["Alive"]:
                atk = random.randint(self.plist[attacker1 - 1]["MIN_ATK"], self.plist[attacker1 - 1]["MAX_ATK"])
                dfs = random.randint(self.ailist[defender1 - 1]["MIN_DEF"], self.ailist[defender1 - 1]["MAX_DEF"])
                dmg = atk - dfs
                if dmg < 0:
                    dmg = 0
                atk_exp = dmg + (dmg*0.8)
                def_exp = dmg + (dmg*0.2)

                self.ailist[defender1 - 1]["HP"] -= dmg
                self.plist[attacker1 - 1]["EXP"] += atk_exp
                self.ailist[defender1 - 1]["EXP"] += def_exp

                if self.ailist[defender1 - 1]["EXP"] >= 100:
                    self.ailist[defender1 - 1]["Level"] += 1
                    self.ailist[defender1 - 1]["EXP"] = 0

                if self.plist[attacker1 - 1]["EXP"] >= 100:
                    self.plist[attacker1 - 1]["Level"] += 1
                    self.plist[attacker1 - 1]["EXP"] = 0

            else:
                print("You can\'t attack a dead AI unit.")
                self.Pattack()
        else:
            print("You can\'t choose your dead hero.")
            self.Pattack()

    def AIattack(self):

        attacker2 = random.randint(1, len(self.ailist))
        print("AI Choose Unit: ", attacker2)

        if self.ailist[attacker2 - 1]["Alive"]:
            defender2 = random.randint(1, len(self.ailist))
            print("AI Attack Unit: ", defender2)
            if self.plist[defender2 - 1]["Alive"]:

                atk = random.randint(self.ailist[attacker2 - 1]["MIN_ATK"], self.ailist[attacker2 - 1]["MAX_ATK"])
                dfs = random.randint(self.plist[defender2 - 1]["MIN_DEF"], self.plist[defender2 - 1]["MAX_DEF"])
                dmg = atk - dfs
                if dmg < 0:
                    dmg = 0
                atk_exp2 = dmg + (dmg*0.8)
                def_exp2 = dmg + (dmg*0.3)

                self.plist[defender2 - 1]["HP"] -= dmg
                self.ailist[attacker2 - 1]["EXP"] += atk_exp2
                self.plist[defender2 - 1]["EXP"] += def_exp2

                if self.ailist[attacker2 - 1]["EXP"] >= 100:
                    self.ailist[attacker2 - 1]["Level"] += 1
                    self.ailist[attacker2 - 1]["EXP"] = 0

                if self.plist[defender2 - 1]["EXP"] >= 100:
                    self.plist[defender2 - 1]["Level"] += 1
                    self.plist[defender2 - 1]["EXP"] = 0

            else:
                self.AIattack()
        else:
            self.AIattack()

    def checkp(self):
        status = True
        b = 0
        for h in range(0, len(self.plist)):
            if self.plist[h]["HP"] <= 0:
                self.plist[h]["HP"] = 0
                self.plist[h]["Alive"] = False

        for i in range(0, len(self.plist)):
            if not self.plist[i]["Alive"]:
                b += 1

        if b == len(self.plist):
            status = False
        else:
            status = True

        return status

    def checkai(self):
        status = True
        b = 0
        for h in range(0, len(self.ailist)):
            if self.ailist[h]["HP"] <= 0:
                self.ailist[h]["HP"] = 0
                self.ailist[h]["Alive"] = False
        for l in range(0, len(self.ailist)):
            if not self.ailist[l]["Alive"]:
                b += 1

        if b == len(self.ailist):
            status = False
        else:
            status = True

        return status

    def gamestatus(self):

        status = False
        check1 = self.checkp()
        check2 = self.checkai()

        if (not check1) and (not check2):
            status = True
        elif (not check1) and (check2):
            status = True
        elif (check1) and (not check2):
            status = True
        else:
            status = False

        return status

    def pvai_main(self):
        self.nohero()
        self.selectheroP()
        self.selectheroAI()
        self.displaybteams()
    
        a = self.checkp()
        b = self.checkai()

        gameover = False

        while not gameover:
            if not gameover:
                self.Pattack()
                gameover = self.gamestatus()
                self.displaybteams()
                if not gameover:
                    self.AIattack()
                    gameover = self.gamestatus()
                    self.displaybteams()