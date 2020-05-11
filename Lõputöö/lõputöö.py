import math
import playerinf
import vastaseinf
import täringuvisked
#import vastused
import Backpack
import random
import pood
import story


# Algse story üles lugemine
text = story.setup()

#tegelase loomine ja vastase paigutus
playerinfo = playerinf.playerSetup()


#Algne poes käimine
print(text[260])
items = ["toiduained", "joogipoolis"]
newItems, newGold = pood.store1(30)
items = Backpack.update(items, newItems)

player = {
    "nimi" : playerinfo[0],
    "relv" : playerinfo[1],
    "turvis" : playerinfo[2],
    "kott" : items,
    "vastupidavus" : playerinfo[3],
    "õnn"  : playerinfo[4],
    "osavus" : playerinfo[5],
    "raha" :  newGold
       }
print("sinu tegelase info on", player)
game = True
while game == True:
    compat = False
    page = story.chapters(text)
    combat, enemyInfo = story.combat(page)    

#ask = int(input("sisesta järgnev tee konna nr")) --- seda pole vaja

    while combat == True:
        enemy = vastaseinf.init(enemyInfo)
        playerHit = täringuvisked.d6korda2() + player["osavus"] 
        enemyHit = täringuvisked.d6korda2() + enemy["osavus"]
        if playerHit == enemyHit:
            print("lõite üksteisest mööda")
        elif playerHit > enemyHit:
            enemy["vastupidavus"] = enemy["vastupidavus"] -2
        else:
            player["vastupidavus"] = player["vastupidavus"] -2

        if player["vastupidavus"] <= 0:
            print("""
            _____
            / ____|
            | |  __  __ _ _ __ ___   ___    _____   _____ _ __
            | | |_ |/ _` | '_ ` _ \ / _ \  / _ \ \ / / _ \ '__|
            | |__| | (_| | | | | | |  __/ | (_) \ V /  __/ |
            \_____|\__,_|_| |_| |_|\___|  \___/ \_/ \___|_|
            """)
            combat = False
        elif enemy["vastupidavus"] <= 0:
            combat = False
            if enemy["drop"] == "mitte midagi":
                print("Vastasel polnud aardeid")
            else:       
                if isinstance(enemy["drop"], int):
                    player["raha"] = player["raha"] + enemy["drop"]
                    print("sul on nüüd", player["raha"], "kulda")
                else:
                    player["kott"].append(enemy["drop"])
                    print("Sinu seljakottis on nüüd", player["kott"])
            print("Võitsid")

#player["kott"] = bacpack.bp(player("kott"), items)