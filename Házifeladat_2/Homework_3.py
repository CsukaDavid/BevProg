def main():
    print("írj egy számot: ",end=" ")
    szam = int(input())
    szam = str(szam)
    hossz = len(szam)
    i = 0
    tukor = True
    if (hossz%2==0):
        while hossz/2 > i:
            if szam[i]==szam[hossz-1-i]:
                tukor=True
                i=i+1
            else:
                tukor=False
                break
    if (hossz%2==1):
        while (hossz-1)/2 > i:
            if szam[i]==szam[hossz-1-i]:
                tukor=True
                i=i+1
            else:
                tukor=False
                break
    if (tukor==False):
        print("A {0} szám nem tükörszám".format(szam))
    else:
        print("A {0} szám tükörszám".format(szam))
if __name__=='__main__':
    main()