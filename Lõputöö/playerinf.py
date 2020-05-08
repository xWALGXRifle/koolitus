import täringuvisked

def playerSetup():
    info = []
    kasutaja = input("mis on teie nimi")
    info.append(kasutaja)
    info.append("mõõk")
    info.append("nahkrüü")
    info.append(täringuvisked.d6Add12()) # vasdupidavus
    info.append(täringuvisked.d6Add6())  # õnn
    info.append(täringuvisked.d6Add6())  # osavus
    return info