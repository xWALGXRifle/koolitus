import math
import playerinf
import vastaseinf
import täringuvisked
#import vastused
import Backpack
import random
import pood

playerinfo = playerinf.playerSetup()
enemyinfo = vastaseinf.NÕELUSS()
newItems, newGold = pood.store1(100)
items = ["toiduained", "joogipoolis"]
items = Backpack.update(items, newItems)

player = {
    "nimi" : playerinfo[0],
    "relv" : playerinfo[1],
    "turvis" : playerinfo[2],
    "kott" : ["toiduained", "joogipoolisega"],
    "vastupidavus" : playerinfo[3],
    "õnn"  : playerinfo[4],
    "osavus" : playerinfo[5],
    "raha" :  newGold
       }

enemy = {
    "vastupidavus" : enemyinfo[0],
    "osavus" : enemyinfo[1],
    "drop" : enemyinfo[2]    
    }

#combat kuhu liigud
#ask = int(input("sisesta järgnev tee konna nr")) --- seda pole vaja

combat = True
while combat == True:
    playerHit = täringuvisked.d6korda2() + player["osavus"] 
    enemyHit = täringuvisked.d6korda2() + enemy["osavus"]
    if playerHit == enemyHit:
        print("lõite üksteisest mööda")
    elif playerHit > enemyHit:
        enemy["vastupidavus"] = enemy["vastupidavus"] -2
    else:
        player["vastupidavus"] = player["vastupidavus"] -2

    if player["vastupidavus"] == 0:
        print("""
   _____
  / ____|
 | |  __  __ _ _ __ ___   ___    _____   _____ _ __
 | | |_ |/ _` | '_ ` _ \ / _ \  / _ \ \ / / _ \ '__|
 | |__| | (_| | | | | | |  __/ | (_) \ V /  __/ |
  \_____|\__,_|_| |_| |_|\___|  \___/ \_/ \___|_|
        """)
        combat = False
    elif enemy["vastupidavus"] == 0:
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

#player["kott"] = bacpack.bp(player("kott"), items)