import random
kasutaja = input("mis on teie nimi")

kontroll = True
while kontroll == True:
    klass = input("warrior\ndefender\nberseker\nassasin")
    relv = input("axe\nswordshield\ntwohandssword\ntwoswords")
    turvis = input("leather\nlight\nmedium\nheavy")
    if (klass == "warrior" or klass == "defender" or klass == "berseker" or klass == "assasin") and (relv == "axe" or relv == "swordshield" or relv == "twohandssword" or relv == "twoswords") and (turvis == "leather" or turvis == "light" or turvis == "medium" or turvis == "heavy"):
        kontroll = False
    else:
        print("palun sisesta uuesti")

player = {
    "nimi" : kasutaja,
    "elud" : 50,
    "relv" : relv,
    "turvis" : turvis,
    "elu pott" : 2
    }

Diablo = {
    "nimi" : "Diablo",
    "elud" : 1500,
    "relv" : "põrgu küüned",
    "turvis" : "lohe nahk",
    "maagia" : "tõukab vastast"
    }

if turvis == "leather":
    armor = 2
elif turvis == "light":
    armor = 4
elif turvis == "medium":
    armor = 8
elif turvis == "heavy":
    armor = 25

if klass == "warrior":
     elu = 100    
elif klass == "defender":
      elu = 150
elif klass == "berseker":
      elu = 125
elif klass == "assasin":
      elu = 75

if relv == "axe":
    tugevus = 25
elif relv == "swordshield":
    tugevus = 14
elif relv == "twohandssword":
    tugevus = 30
elif relv == "twoswords":
    tugevus = 28
    
combat = True
while combat == True:
    """print ("kasutaja lööb")
    Diablo ["elud"] = Diablo["elud"] - random.randint(0, 10)
    print ("Diblo lööb, pane valm valmis")
    player["elud"] = player["elud"] - random.randint(15, 25)""" #lihtsam versioon
    
    if player ["klass"] == "warrior":# siin laheb errorrisse
        dmg = random.randint(12, 25)
    elif player ["klass"] == "defender":
        dmg = random.randint(4, 21) 
    elif player ["klass"] == "berseker":
        dmg = random.randint(9, 20)
    elif player ["klass"] == "assasin":
        dmg = random.randint(7, 24)
    
    if dmg >= 25:
        Diablo["elud"] = Diablo["elud"] - dmg
        print(Diablo["elud"])
    else:
        print("Diablo ei saanud haiget")
        
    if random.randint(0, 20) >=armor:           #Diablo ründab
        player["elud"] = player["elud"] - dmg
        print(player["elud"])
    else:
        print("Diablo ei saanud haiget")
    
    if player ["elud"] < 50:
        lisa = "elu pott"
        print("elu pott")
    if player["elud"] < 0:
        combat = False
        print("You DIED!")
print("""
   _____
  / ____|
 | |  __  __ _ _ __ ___   ___    _____   _____ _ __
 | | |_ |/ _` | '_ ` _ \ / _ \  / _ \ \ / / _ \ '__|
 | |__| | (_| | | | | | |  __/ | (_) \ V /  __/ |
  \_____|\__,_|_| |_| |_|\___|  \___/ \_/ \___|_|
""")