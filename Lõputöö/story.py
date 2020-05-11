import vastaseinf

def setup():
    f = open("koolitus/Lõputöö/Vastused.txt", "r", encoding="UTF-8")

    story =[]
    for x in f:
        story.append(str(x))
    return story

def chapters(story):
    chapter = input("Sisesta lehekülje numnber") + "."
    for y in story:
        if chapter in y:
            print(y)
            break
    return chapter

def combat(page):
    if page == "7.":
        combat = True
        enemy = vastaseinf.MÕRTSUKMESILASED()
        return combat, enemy
    else:
        return None, None

def combat(page):
    if page == "9.":
        combat = True
        enemy = vastaseinf.GOBLIN()
        return combat, enemy
    else:
        return None, None

def combat(page):
    if page == "15.":
        combat = True
        enemy = vastaseinf.NÕELUSS()
        return combat, enemy
    else:
        return None, None
                
def combat(page):
    if page == "29.":
        combat = True
        enemy = vastaseinf.ORK()
        return combat, enemy
    else:
        return None, None

        
def combat(page):
    if page == "43.":
        combat = True
        enemy = vastaseinf.METSIK MÄGILANE()
        return combat, enemy
    else:
        return None, None

        
def combat(page):
    if page == "49.":
        combat = True
        enemy = vastaseinf.GREMLIN()
        return combat, enemy
    else:
        return None, None

        
def combat(page):
    if page == "71.":
        combat = True
        enemy = vastaseinf.GREMLIN()
        return combat, enemy
    else:
        return None, None

        
def combat(page):
    if page == "79.":
        combat = True
        enemy = vastaseinf.VAMPIIRNAHKHIIR()
        return combat, enemy
    else:
        return None, None

        
def combat(page):
    if page == "84.":
        combat = True
        enemy = vastaseinf.RÜNKAELUKAS()
        return combat, enemy
    else:
        return None, None

        
def combat(page):
    if page == "96.":
        combat = True
        enemy = vastaseinf.JAHIKOER()
        return combat, enemy
    else:
        return None, None

        
def combat(page):
    if page == "104.":
        combat = True
        enemy = vastaseinf.RÖÖVELNAINE()
        return combat, enemy
    else:
        return None, None

        
def combat(page):
    if page == "107.":
        combat = True
        enemy = vastaseinf.TULEDEEMON()
        return combat, enemy
    else:
        return None, None

        
def combat(page):
    if page == "117.":
        combat = True
        enemy = vastaseinf.GOBLIN()
        return combat, enemy
    else:
        return None, None

        
def combat(page):
    if page == "118.":
        combat = True
        enemy = vastaseinf.METSSIGA()
        return combat, enemy
    else:
        return None, None

        
def combat(page):
    if page == "123.":
        combat = True
        enemy = vastaseinf.PUUMEES()
        return combat, enemy
    else:
        return None, None

        
def combat(page):
    if page == "128.":
        combat = True
        enemy = vastaseinf.BARBAR()
        return combat, enemy
    else:
        return None, None

        
def combat(page):
    if page == "153.":
        combat = True
        enemy = vastaseinf.KASSNAINE()
        return combat, enemy
    else:
        return None, None

        
def combat(page):
    if page == "165.":
        combat = True
        enemy = vastaseinf.GREMLIN()
        return combat, enemy
    else:
        return None, None

        
def combat(page):
    if page == "167.":
        combat = True
        enemy = vastaseinf.TIIVULINE LOHE()
        return combat, enemy
    else:
        return None, None

        
def combat(page):
    if page == "181.":
        combat = True
        enemy = vastaseinf.KALAMEES()
        return combat, enemy
    else:
        return None, None

        
def combat(page):
    if page == "186.":
        combat = True
        enemy = vastaseinf.VEREANGERJAS()
        return combat, enemy
    else:
        return None, None

        
def combat(page):
    if page == "193.":
        combat = True
        enemy = vastaseinf.GREMLIN()
        return combat, enemy
    else:
        return None, None

        
def combat(page):
    if page == "203.":
        combat = True
        enemy = vastaseinf.KUJUMUUTJA()
        return combat, enemy
    else:
        return None, None

        
def combat(page):
    if page == "212.":
        combat = True
        enemy = vastaseinf.KLOONSÕDALANE()
        return combat, enemy
    else:
        return None, None

        
def combat(page):
    if page == "227.":
        combat = True
        enemy = vastaseinf.GUUL()
        return combat, enemy
    else:
        return None, None

        
def combat(page):
    if page == "231.":
        combat = True
        enemy = vastaseinf.SURMAHAUGAS()
        return combat, enemy
    else:
        return None, None

        
def combat(page):
    if page == "241.":
        combat = True
        enemy = vastaseinf.KARU()
        return combat, enemy
    else:
        return None, None

        
def combat(page):
    if page == "265.":
        combat = True
        enemy = vastaseinf.METSAHIIGLANE()
        return combat, enemy
    else:
        return None, None

        
def combat(page):
    if page == "276.":
        combat = True
        enemy = vastaseinf.JUHTKOER()
        return combat, enemy
    else:
        return None, None

        
def combat(page):
    if page == "285.":
        combat = True
        enemy = vastaseinf.LIBAHUNT()
        return combat, enemy
    else:
        return None, None

        
def combat(page):
    if page == "286.":
        combat = True
        enemy = vastaseinf.KUJUMUUTJA()
        return combat, enemy
    else:
        return None, None

        
def combat(page):
    if page == "290.":
        combat = True
        enemy = vastaseinf.HIIDKOLL()
        return combat, enemy
    else:
        return None, None

        
def combat(page):
    if page == "298.":
        combat = True
        enemy = vastaseinf.HIIDÄMBLIK()
        return combat, enemy
    else:
        return None, None

        
def combat(page):
    if page == "303.":
        combat = True
        enemy = vastaseinf.PTERODAKTÜL()
        return combat, enemy
    else:
        return None, None

        
def combat(page):
    if page == "310.":
        combat = True
        enemy = vastaseinf.KOOPATROLL()
        return combat, enemy
    else:
        return None, None

        
def combat(page):
    if page == "317.":
        combat = True
        enemy = vastaseinf.PAHARET()
        return combat, enemy
    else:
        return None, None

        
def combat(page):
    if page == "330.":
        combat = True
        enemy = vastaseinf.HUNT()
        return combat, enemy
    else:
        return None, None

        
def combat(page):
    if page == "347.":
        combat = True
        enemy = vastaseinf.KÄÄBUS()
        return combat, enemy
    else:
        return None, None

        
def combat(page):
    if page == "352.":
        combat = True
        enemy = vastaseinf.AHVMEES()
        return combat, enemy
    else:
        return None, None

        
def combat(page):
    if page == "377.":
        combat = True
        enemy = vastaseinf.PÜGMEE()
        return combat, enemy
    else:
        return None, None

