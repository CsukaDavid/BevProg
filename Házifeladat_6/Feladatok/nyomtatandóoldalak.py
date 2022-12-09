def tobboldal(szoveg):   
    print("Nyomtatandó oldalak:",end=" ")
    lista=[]
    for i in range(len(szoveg)):
        sor = szoveg[i]
        vhelye = sor.find("-")
        if (vhelye < 0):
            lista.append(int(sor))
        else:
                szam1=int(sor[0:vhelye])
                szam2=int(sor[vhelye+1:])
                while(szam1 !=szam2+1):
                    lista.append(szam1)
                    szam1 +=1
    print(lista)

def main():
    szoveg = str(input())
    li = szoveg.split(",")
    tobboldal(li)
if __name__=="__main__":
    main()