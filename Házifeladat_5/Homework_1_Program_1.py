def main():
    filename='F:\Bevezetés a programozásba\BevProg-1\Házifeladat_5\goal.txt'
    nev=str(input("Add meg a neved: "))
    eletkor=str(input("Add meg a eletkorod: "))
    
    f = open(filename,'a')
    print(nev,file=f,end=",")
    print(eletkor,file=f,end=",")
    f.close()

if __name__=="__main__":
    main()