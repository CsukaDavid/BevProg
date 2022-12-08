def main():
    
    filename='F:\Bevezetés a programozásba\BevProg-1\Házifeladat_5\goal.txt'
    f = open(filename,'r')
    li = f.readlines()
    lista=[]
    lista=li[0].split(",")
    lista.remove('')
    for k in range(len(lista)):
        print(lista[k],end="      ")
        if k%2==1:
            print("\n")
    f.close()

if __name__=="__main__":
    main()