pozicija_automobila = 0
pozicija_cilja = 10

print(pozicija_automobila == pozicija_cilja)

pozicija_automobila += 2
print(pozicija_automobila == pozicija_cilja)

pozicija_automobila += 2
print(pozicija_automobila == pozicija_cilja)

pozicija_automobila += 2
print(pozicija_automobila == pozicija_cilja)

pozicija_automobila += 2
print(pozicija_automobila == pozicija_cilja)

pozicija_automobila += 2
print(pozicija_automobila == pozicija_cilja)

for sledeci in ["marko", "milos", "marija", "ana", "sofija"]:
    print("hello", sledeci)

print("prva sledeca linija")

for broj in [1, 2, 3, 4, 5]:
    print("ovo je broj", broj)

    
    for broj in range(5, 10, 2):
        print("STAMPANJE BROJA", broj)

for broj in range(100, 0, -1):
    print("prikaz", broj)



pozicija_automobila = 0
pozicija_cilja = 10

for kretanje in range(5):
    pozicija_automobila += 2
    print(pozicija_automobila == pozicija_cilja)




print("***********************************************")
for godine in range(2010, 2022, 1):
    print("godina:", godine)
print("***********************************************")


# print("1\t2\t3\t")
# print("********************")

# for brojac in range(1, 6):
#     print(brojac * 1, end="\t")
#     print(brojac * 2, end="\t")
#     print(brojac * 3, end="\n")

# for x in range(5):
#     for y in range(3):
#         print("ovo je X", x, "ovo je y", y)

x = range(0, 5)
y = range(0, 5)

for x in range(6):
    for y in range(6):
        if x == y:
            print("x", end=" ")
        else:
            print("#", end=" ")
    print()

for x in range(10):
    for y in range(10):
        if x == 0 or x == 9 or y == 0 or y == 9:
            print("#", end=" ")
        else:
            print(" ", end="")
        print()


# sekunde = 10

# while sekunde > 0:
#     print(sekunde)
#     sekunde -= 1

baterija = 90

while baterija > 0:
    print("mozes koristiti telefon", baterija, "%")
    baterija -= 10

print("baterija je prazna")


for broj in range(11):
    if broj == 2:
        continue
    print(broj)    
        


