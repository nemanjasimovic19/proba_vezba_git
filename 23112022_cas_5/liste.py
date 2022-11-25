# # osoba = ("sofija", 25, "plava", False)

# # # for x in range(len(osoba)):
# # #     print(osoba[x])

# # # for osobina in osoba:
# # #     print(osobina)

# # voce_i_povrce = ["jabuka", "beli luk", "crni luk", "banana", "mandarina", "krastavac"]

# # for stavka in voce_i_povrce:
# #     print(stavka)

# # for i in range(len(voce_i_povrce)):
# #     print(voce_i_povrce[i])

# # for indeks, vrednost in enumerate(voce_i_povrce):
# #     print("indeks: ", indeks, "stavka: ", vrednost)


# automobili = ["citroen", "BMW", "opel", "kia", "yugo"]
# #pozicija: auto

# for pozicija, auto in enumerate(automobili):
#     print("Pozicija: ", pozicija, "Automobil", auto)

# automobili.append("mercedes")

# print(automobili)

# automobili[3] = "opel corsa"
# print(automobili)

# del automobili[3]
# print(automobili)
# automobili.remove("BMW")
# print(automobili)

# automobili.clear()
# print(automobili)

# automobili = ["citroen", "BMW", "opel", "kia", "yugo", "peugeot", "audi"]

# automobili_akcija = []

# for i in range(len(automobili)):
#     if i == 1 or i == 2 or i == 3:
#         automobili_akcija.append(automobili[i])
# print(automobili_akcija)

# automobili_akcija = automobili[1:4]

lista = [1, 2, 4, 5, 11, 13, 9, 7, 21]
parni = []
neparni = []

for broj in lista:
    if broj % 2 == 0:
        print(broj)
        parni.append(broj)
    else:
        neparni.append(broj)
print("lista parnih: ", parni)
print("lista neparnih: ", neparni)