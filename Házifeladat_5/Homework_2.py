def main():
    filename='F:\Bevezetés a programozásba\BevProg-1\Házifeladat_5\pivers.txt'
    f = open(filename,'r')
    li =f.readlines()
    szoveg=""
    for k in range(len(li)):
        lista=li[k].split(" ")
        donelist=[]
        for i in range(len(lista)):
            donelist.append(lista[i].replace("\n",""))
        for i in range(len(donelist)):
            szoveg+=str(len(donelist[i]))
            if len(szoveg)==1:
                szoveg+="."
    filename='F:\Bevezetés a programozásba\BevProg-1\Házifeladat_5\piertek.txt'
    f = open(filename,"w")
    print(szoveg,file=f,end="")

if __name__=="__main__":
    main()