user = input("Sisesta nimi")
print ("Tere tulemast surnuaeda", user)

game = True
elud = 10
sõnaSpikker = []
sõna = []
test = ""

for x in "raamatukoguhoidija":
    sõna.append(x)

for x in range(14):
    sõnaSpikker.append("_")

while elud > 0:
    print (sõnaSpikker)
    asukoht = 0
    pakkumine = input("Paku mingi täht")
    for x in sõna:
        täht = x
        if pakkumine == täht:
            sõnaSpikker[asukoht] = pakkumine
        else:
            elud = elud - 1
            print ("seda tähte ei ole")
        asukoht = asukoht + 1
        break
print ("The END")