import math
import vastaseinf
import vastused
#import backpack
#import random

player = {
"relv" : mõõk,
"turvis" : nahknerüü,
"kott" : ["toiduained", "joogipoolisega"],
"elud" : vastupidavus,
"õnn"  : õnn,
"osavus" : osavus
"raha" : Kuldmünt
       }

vastane1 = {
    "elu" :vastaseinf.vastupidavus,
    "relv" :vastaseinf.osavus,
         
    }
vastane2 = {
    "elu" :vastaseinf.vastupidavus,
    "relv" :vastaseinf.osavus,
         
    }

vastane3 = {
    "elu" :vastaseinf.vastupidavus,
    "relv" :vastaseinf.osavus,
         
    }

    #combat kuhu liigud
#ask = int(input("sisesta järgnev tee konna nr")) --- seda pole vaja
rännak = (
misioon1 = 261, 
misioon2 = 177,
misioon3 = 160,
misioon4 = 8,
misioon5 = 392,
misioon6 = 15, 
misioon7 = 217,
misioon8 = 262,
misioon9 = 377, 
misioon10 = 205,
misioon11 = 92,
misioon12 = 299,
misioon13 = 65,
misioon14 = 330, 
misioon15 = 116,
misioon16 = 314,
misioon17 = 294,
misioon18 = 106,
misioon19 = 288,
misioon20 = 84,
misioon21 = 146, 
misioon22 = 245,
misioon23 = 393,
misioon24 = 369,
misioon25 = 390,
misioon26 = 190,
misioon27 = 318,
misioon28 = 231,
misioon29 = 224,
misioon30 = 332,
misioon31 = 103,
misioon32 = 57)

# kui on vaja täringut veeretada
kokku = 0
for x in range(2):
    täringud = random.randint(1, 6)
    kokku = kokku + täringud
    print(täringud)
print(kokku)





#backpack
     def bp(list, items):
            list.append(item)
    return list

    player["kott"] = bacpack.bp(player("kott"), items)