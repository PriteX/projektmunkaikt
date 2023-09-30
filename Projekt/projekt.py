import random
import string

x = int(input("Adja meg melyik program fusson le: (1, 2, 3, 4) "))
if x == 1:
    alhat=int(input("Adja meg az alsó határt:"))
    felhat=int(input("Adja meg az felső határt:"))
    dbszam=int(input("Adja meg a kívánt darabszámot:"))
    randszamok=[]
    for i in range(dbszam):
        genszam=random.randint(alhat, felhat)
        randszamok.append(genszam)
        print(genszam)
    with open("ki.txt", "w") as l:
        for p in randszamok:
            l.write(str(p))
            l.write(";")

if x == 2:
    betuk=string.ascii_letters
    dbszam=int(input("Adja meg a kívánt darabszámot: "))
    with open("ki.txt", "w") as l:
        for i in range(dbszam):
            for j in range(random.randint(1, 20)):
                ltr=random.choices(string.ascii_letters)
                l.write(str(ltr).replace("[","").replace("]","").replace("'",""))
            l.write(";")

if x == 3:
    alhat=int(input("Adja meg az alsó határt:"))
    felhat=int(input("Adja meg az felső határt:"))
    dbszam=int(input("Adja meg a kívánt darabszámot:"))
    db=0
    with open("ki.txt", "r") as l:
        for i in l.read().replace(";",""):
            if i.isnumeric()==False:
                print(f"Hiba: {i} nem szám")
            elif int(i) < alhat:
                print(f"Hiba: {i} túl kicsi")
            elif int(i) > felhat:
                print(f"Hiba: {i} túl nagy")
            db+=1
    if db != dbszam:
        print("Hiba, nem egyezik meg a darabszám")
    
            
if x == 4:
    betuk=string.ascii_letters
    dbszam=int(input("Adja meg a kívánt darabszámot: "))
    db=0
    with open("ki.txt") as l:
        for i in l.read():
            if i == ";":
                db+=1
        for i in l.read().replace(";",""):
            if i.isalpha()==False:
                print(f"Hiba: {i} nem betű")
        if db!=dbszam:
            print("Hiba, nem egyezik meg a darabszám")


    