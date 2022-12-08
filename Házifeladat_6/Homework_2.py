import modul as m
def primszam(n):
    i=0
    print("{0} alatti primszamok: ".format(n),end="")
    while i in range(n):
        if (m.is_prime(i)==True):
            print(i,end=" ")
        i +=1
    print("\n")

def primossz(n):
    i=0
    osszeg=0
    print("{0} alatti primszamok összege: ".format(n),end="")
    while i in range(n):
        if (m.is_prime(i)==True):
            osszeg+=i
        i +=1
    print(osszeg,end="\n\n")

def main():
    primszam(100)
    primossz(200)
if __name__=="__main__":
    main()