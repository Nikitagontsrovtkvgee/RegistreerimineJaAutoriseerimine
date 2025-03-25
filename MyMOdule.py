import random
import string


def genereeri_parool():
    märgid = string.ascii_letters + string.digits + ".,:;!_*-+()/#¤%&"
    return ''.join(random.choice(märgid) for _ in range(8))

"""Генерирует случайный пароль длиной 8 символов.
Включает буквы (заглавные и строчные), цифры и специальные символы.
Использует random.choice() для случайного выбора символов.
"""

def kontrolli_parool(parool):
    return (any(c.isdigit() for c in parool) and 
            any(c.islower() for c in parool) and 
            any(c.isupper() for c in parool) and
            any(c in ".,:;!_*-+()/#¤%&" for c in parool))
"""Проверяет, содержит ли пароль:
* хотя бы одну цифру,
* хотя бы одну строчную букву,
* хотя бы одну заглавную букву,
* хотя бы один специальный символ.
Возвращает True, если пароль соответствует требованиям, иначе False.
"""

def registreeri(kasutajad, paroolid):
    nimi = input("Sisestage kasutajanimi: ")
    if nimi in kasutajad:
        print("Kasutaja on juba olemas!")
    else:
        parool = input("Sisestage parool: ")
        if not kontrolli_parool(parool):
            print("Parool peab sisaldama numbreid, suur- ja väike tähti ning sümboleid!")
        else:
            kasutajad.append(nimi)
            paroolid.append(parool)
            print("Kasutaja on edukalt registreeritud!")
"""Запрашивает у пользователя имя и пароль.
Проверяет, существует ли уже такой пользователь.
Если имя уникально, проверяет сложность пароля с помощью kontrolli_parool().
Если пароль подходит, добавляет пользователя в систему.
"""

def autoriseeri(kasutajad, paroolid):
    nimi = input("Sisestage kasutajanimi: ")
    if nimi in kasutajad:
        parool = input("Sisestage parool: ")
        if paroolid[kasutajad.index(nimi)] == parool:
            print("Sisselogimine õnnestus!")
        else:
            print("Vale parool!")
    else:
        print("Sellist kasutajat ei eksisteeri!")
"""Запрашивает имя пользователя и пароль.
Проверяет, существует ли пользователь в списке.
Если имя есть в базе и пароль совпадает, вход выполнен.
Если пароль неверный, сообщает об ошибке.
"""

def muuda_parool(kasutajad, paroolid):
    nimi = input("Sisestage kasutajanimi: ")
    if nimi in kasutajad:
        vana_parool = input("Sisestage vana parool: ")
        if paroolid[kasutajad.index(nimi)] == vana_parool:
            uus_parool = input("Sisestage uus parool: ")
            if not kontrolli_parool(uus_parool):
                print("Parool peab sisaldama numbreid, suur- ja väike tähti ning sümboleid!")
            else:
                paroolid[kasutajad.index(nimi)] = uus_parool
                print("Parool edukalt muudetud!")
        else:
            print("Vale vana parool!")
    else:
        print("Sellist kasutajat ei eksisteeri!")
"""Запрашивает имя пользователя.

Если пользователь существует, запрашивает старый пароль.

Если старый пароль совпадает, предлагает ввести новый.

Новый пароль проверяется на сложность.

Если он подходит, заменяет старый пароль на новый.
"""

def taasta_parool(kasutajad, paroolid):
    nimi = input("Sisestage kasutajanimi: ")
    if nimi in kasutajad:
        uus_parool = genereeri_parool()
        paroolid[kasutajad.index(nimi)] = uus_parool
        print(f"Teie uus parool: {uus_parool}")
    else:
        print("Sellist kasutajat ei eksisteeri!")
"""Запрашивает имя пользователя.

Если пользователь существует, генерирует новый случайный пароль.

Обновляет пароль в системе.

Выводит новый пароль на экран.
"""