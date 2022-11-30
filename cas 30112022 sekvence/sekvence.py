# brojevi = [9, 1, 3, 2, 5, 8, 7]
# brojevi.sort()
# brojevi.reverse()
# print(brojevi)

# brojevi = [9, 1, 3, 2, 5, 8, 7]
# while True:
#     izvrsena_zamena = False
#     for i in range (1, len(brojevi)):
#         if brojevi[i] < brojevi [i-1]:
#             privremena = brojevi[i]
#             brojevi[i] = brojevi[i-1]
#             brojevi[i-1] = privremena
#             izvrsena_zamena = True
#     if izvrsena_zamena == False:
#         break


# print(brojevi)
# ["Telefon", "TV", "Lap-Top"]
# proizvodi = ["Telefon", "TV", "Lap-Top"]
# cene = [100, 200, 300]

# for x in range(3):
#     print(proizvodi[x], cene[x])

# automobili = ["Audi", "BMW", "Yugo", "Citroen", "Kia", "Peougeot"]

# for x in range(len(automobili)):
#     print(automobili[x])
#     if x == 3:
#         print("Aleksandra vozi:", automobili[x])

# proizvodi = [["Iphone 11", "Samsung s22", "Xiaomi x3"], ["Acer", "McBook", "Dell"], ["ipad", "samsung galaxy tab", "xiaomi tablet"]]

# telefoni = ["Iphone 11", "Samsung s22", "Xiaomi x3"]
# laptopovi = ["Acer", "McBook", "Dell"]
# tableti = ["ipad", "samsung galaxy tab", "xiaomi tablet"]

# print(proizvodi[0][0])
# print(proizvodi[1][1])

# # proizvodi = [telefoni, laptopovi, tableti]
# # print

# # for kategorija  in proizvodi:
# #     for stavka in kategorija:
#         print(stavka)

# for i in range(len(proizvodi)):
#     print(proizvodi[i])
#     for j in range(len(proizvodi[i])):
#         print(proizvodi[i][j])

# hrana = [["cokolada", "bombone", "palacinke"], ["sarma", "musaka", "kiseli kupus"], ["pecena paprika", "ajvar", "sopska"]]
# slatkisi = ["cokolada", "bombone", "palacinke"]
# slano = ["sarma", "musaka", "kiseli kupus"]
# salata = ["pecena paprika", "ajvar", "sopska"]

# for kategorija in hrana:
#     for jelo in kategorija:
#         print("jelo dana je:", jelo)
1

biblioteka = []
while True:
    print("Odaberi komandu: 1-unos, 2-prikaz, 3-brisanje, > 3 izlaz")
    komanda = int(input("Unesite komandu: "))

    if komanda == 1:
        # unos knjige, preuzmi podatke
        naslov = input("Unesite naslov: ")
        autor = input("Unesite autora: ")
        isbn = int(input("Unesite isbn: "))
        biblioteka.append([naslov, autor, isbn])
        print("Dodata knjiga")
    if komanda == 2:
        for knjiga in biblioteka:
            for detalj in knjiga:
                print(detalj)
    if komanda == 3:
        #ovde vrsim brisanje
        kljucna_rec = input("Unesite naziv knjige koju zelite da obrisem. ")
        for knjiga in biblioteka:
            #proveravam detalje KNJIGE
            for detalj in knjiga:
                if detalj == kljucna_rec:
                    biblioteka.remove(knjiga)
                    print("Knjiga je obrisana")