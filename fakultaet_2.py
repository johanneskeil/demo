while True:
    zahl = int(input("Schreiben Sie eine Zahl: "))
    if zahl < 0:
        print("Negativ geht nicht")
        continue
    ergebnis = 1
    for i in range(2, zahl+1):
        ergebnis = ergebnis * i
    print("Ergebnis: ", ergebnis)