import random

def d6Add6():    # kuuetahuline täringu juurde lisamine
    value = random.randint(1, 6) + 6
    return value

def d6Add12():
    value = random.randint(1, 6) + 12
    return value  
def d6korda2():
    kokku = 0
    for x in range(2):
        täringud = random.randint(1, 6)
        kokku = kokku + täringud
    return kokku