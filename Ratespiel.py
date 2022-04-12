loesung = 120
ratewert = 0
i = 0

while ratewert != loesung:
    ratewert = int(input("Raten Sie mal: "))

    if ratewert == 1:
        print("Ende")
        break

    if ratewert > loesung:
        print("Zu groß!")

    if ratewert < loesung:
        print("Zu klein!")
    
    i = i + 1

    print("Sie haben", i, "Versuche benötigt.")