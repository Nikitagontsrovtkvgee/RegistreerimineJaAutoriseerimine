import MyModule

import MyModule

kasutajad = []
paroolid = []

while True:
    print("\nMenüü:")
    print("1. Registreerimine")
    print("2. Autoriseerimine")
    print("3. Parooli muutmine")
    print("4. Parooli taastamine")
    print("5. Välju")

    valik = input("Valige tegevus (1-5): ")

    if valik == "1":
        MyModule.registreeri(kasutajad, paroolid)
    elif valik == "2":
        MyModule.autoriseeri(kasutajad, paroolid)
    elif valik == "3":
        MyModule.muuda_parool(kasutajad, paroolid)
    elif valik == "4":
        MyModule.taasta_parool(kasutajad, paroolid)
    elif valik == "5":
        print("Programm lõpetatud.")
        break
    else:
        print("Vigane sisestus! Proovige uuesti.")

