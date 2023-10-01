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

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def reverse_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

kerdes = str(input("Növekvő(n) vagy csökkenő(cs) sorrend: "))
if kerdes.lower()=="n":
    print("Eredeti lista:", lista)
    bubble_sort(lista)
    print("Növekvő lista:", lista) 
else: 
     print("Eredeti lista:", lista)
     reverse_bubble_sort(lista)
     print("Csökkenő lista:", lista)

valasz = input("Betűt(b) vagy számot(sz) akarsz beírni: ")
if valasz.lower() == 'sz':
    valasz2 = int(input("Milyen számot akarsz beirni: "))
    lista.append(valasz2)
    print("Eredeti lista:", lista)
    if kerdes.lower() == "n":
        bubble_sort(lista)
        print("Növekvő lista:", lista) 
    else:
        reverse_bubble_sort(lista)
        print("Csökkenő lista:", lista)
else:
    valasz2 = str(input("Milyen betűt akarsz beirni: "))
    lista.append(str(valasz2))
    if kerdes.lower() == "n":
        bubble_sort(lista)
        print("Növekvő lista: ", lista) 
    else:
        reverse_bubble_sort(lista)
        print("Csökkenő lista: ", lista)



