# osoba = ["Sofija", 20, "plava", True]
# print(osoba)

# print(osoba[0])
# print("godine", osoba[1])

# automobili = ["opel", "mercedes", "kia"]
# print(automobili[1])


# for x in range(5, 10, 2):
#     print(x)

kurs = "python"
# print(kurs[0])
# print(kurs[1])
# print(kurs[2])
# print(kurs[3])
# print(kurs[4])
# print(kurs[5])


# for x in range(len(kurs)):
#     print(kurs[x])

# ustanova = "IT Academy"

# for indeks in range (len(ustanova)):
#     print(indeks[ustanova])


primer = "zadatak1"

for clan in range(len(primer)):
    print(primer[clan])

broj_karaktera  = len(primer)
indeks = 0

while indeks < broj_karaktera:
    print(primer[indeks])
    indeks += 1

korisnicko_ime = "admin"
uneto_korisnicko_ime = input("unesi korisnicko ime: ")

if korisnicko_ime == uneto_korisnicko_ime.lower():
    print("dobrodosli")
else:
    print("pogresni podaci")

# racunar = "laptop"
# racunar[1] = "C"