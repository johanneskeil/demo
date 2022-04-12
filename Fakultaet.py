while True:
    zahl = int(input("Gegen Sie eine Zahl ein: "))
    ergebnis = 1
    if zahl < 0:
        print("Bitte eine positive Zahl eingeben!")
        continue
    while zahl > 0:
        ergebnis = ergebnis * zahl
        zahl = zahl - 1
    print("Ergebnis: ", ergebnis)