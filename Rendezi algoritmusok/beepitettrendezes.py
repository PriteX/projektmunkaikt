with open("ki2.txt", "r", encoding="UTF-8") as f:
        x = f.readline().split(";")
        lista = []
        for i in x:
            if i.isdigit():
                lista.append(int(i))
            else:
                lista.append(str(i))
        lista.remove(i)
        db=0
        for k in range(len(lista)):
            igazvhamis = str(lista[k]).isnumeric()
            if igazvhamis == True:
                db+=1

        if db==len(lista):
            print("Az adatok számok!")
        else:
            print("Az adatok betűk!")


kerdes = str(input("Növekvő(n) vagy csökkenő(cs) sorrend: "))
if kerdes.lower()=="n":
    print("Eredeti lista:", lista)
    lista.sort()
    print("Növekvő lista:", lista) 
else: 
     print("Eredeti lista:", lista)
     lista.sort(reverse=True)
     print("Csökkenő lista:", lista)

valasz = input("Betűt(b) vagy számot(sz) akarsz beírni: ")
if valasz.lower() == 'sz':
    valasz2 = int(input("Milyen szamot akarsz beirni: "))
    lista.append(valasz2)
    print(lista)
    if kerdes.lower() == "n":
        lista.sort()
        print("Növekvő lista:", lista) 
    else:
        lista.sort(reverse=True)
        print("Csökkenő lista:", lista)
else:
    valasz2 = str(input("Milyen karaktert akarsz beirni: "))
    lista.append(str(valasz2))
    if kerdes.lower() == "n":
        lista.sort()
        print("Növekvő lista:", lista) 
    else:
        lista.sort(reverse=True)
        print("Csökkenő lista:", lista)



