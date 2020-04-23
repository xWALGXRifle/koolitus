import random
import playerinf
import dmginf
import vastaseinf

player = playerinf.playerSetup()
print (player)


character = {
    "nimi" : player[0],
    "klass" : player[1],
    "elud" : 50 + playerinf.health(player[1]),
    "relv" : playerinf.weapon(player[2]),
    "turvis" : playerinf.armor(player[3]),
    "elu pott" : 2
    }

Diablo = {
    "nimi" : "Diablo",
    "elud" : 1500,
    "relv" : vastaseinf.weapon(Diablo[2]), #100 dmg
    "turvis" : vastaseinf.armor(Diablo[1]), # lisab 45 armorit
    #"maagia" : "vastaseinf.magics(Diablo[3]) #kui eulud on all 100
    }
   
combat = True
while combat == True:    

    dmg = dmginf.dmg(character["klass"])
  
    if dmg >= 19:                                              #player ründab
        Diablo["elud"] = Diablo["elud"] - dmg
        print("Diablo elud", Diablo["elud"])
    else:
        print("Diablo ei saanud haiget")
        
    if random.randint(0, 20) >=character["turvis"]:           #Diablo ründab
        character["elud"] = character["elud"] - dmg
        print("Sinu elud", character["elud"])
    else:
        print("Sa ei saanud haiget") #klass ei saanud haiget
    
    if character ["elud"] < 50:
        lisa = "elu pott"
        print("elu pott")
        
    if character["elud"] < 0:
        combat = False
        print("You DIED!")
    if Diablo["elud"] < 0:
        combat = False
        print("Mission completed!")
print("""
   _____
  / ____|
 | |  __  __ _ _ __ ___   ___    _____   _____ _ __
 | | |_ |/ _` | '_ ` _ \ / _ \  / _ \ \ / / _ \ '__|
 | |__| | (_| | | | | | |  __/ | (_) \ V /  __/ |
  \_____|\__,_|_| |_| |_|\___|  \___/ \_/ \___|_|
""")