import MyMOdule

kasutajad, paroolid = MyMOdule.loe_andmed()

while True:
    print("\nMenüü:")
    print("1. Registreerimine")
    print("2. Autoriseerimine")
    print("3. Parooli muutmine")
    print("4. Parooli taastamine")
    print("5. Välju")

    valik = input("Valige tegevus (1-5): ")

    if valik == "1":
        MyMOdule.registreeri(kasutajad, paroolid)
    elif valik == "2":
        MyMOdule.autoriseeri(kasutajad, paroolid)
    elif valik == "3":
        MyMOdule.muuda_parool(kasutajad, paroolid)
    elif valik == "4":
        MyMOdule.taasta_parool(kasutajad, paroolid)
        nimi = kasutajad[-1]  # последний пользователь
        uus_parool = paroolid[-1]
        MyMOdule.saada_paaniline_sonum(nimi, uus_parool)
    elif valik == "5":
        MyMOdule.salvesta_andmed(kasutajad, paroolid)
        print("Andmed salvestatud. Programm lõpetatud.")
        break
    else:
        print("Vigane sisestus! Proovige uuesti.")
