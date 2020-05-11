def store1(gold):
    boughtList = []
    storeDict = {
        "Tervendav Võlujook" : 3,
        "Taimetõrje Võlujook" : 2,
        "Vaigistav Võlujook" : 3,
        "Putukatõrje Võlujook" : 2,
        "Vastumürgi Võlujook" : 2,
        "Pühitsetud Vesi" : 3,
        "Valguse Sõrmus" : 3,
        "Hüppamise Saapad" : 2,
        "Ronimise Köis" : 2,
        "Mässimisvõrk" : 3,
        "Tugevuse Käeside" : 3,
        "Viskerelva Täpsuskinnas" : 2,
        "Veeleidmise Ora" : 2,
        "Küüslaugud" : 2,
        "Keskendumise Peapael" : 3,
        "Tulekapslid" : 3,
        "Ninafiltrid" : 3,
        "n" : 1
    }
    store = True
    while store == True:
        print ("Meistervõlur Yaztromo \n")
        print ("Ulatab tahvli", storeDict)
        soov = input("sisesta mida osta tahad")
        for x in storeDict:
            if soov == x:
                if gold < storeDict.get(x):
                  print ("pole piisavalt kulda")
                else :
                    boughtList.append(x)
                    gold = gold - storeDict.get(x)
                    del storeDict[x]
                    break
                soov = input("soovid veel y/n")
                if soov == "n":
                    store = False
                break
        soov = input(" Kas sa soovid veel midagi y/n")
        if soov == "n":
            store = False 
            
    return boughtList, gold