from cgitb import text
from tracemalloc import start


pi = 3.14
def hibakezeles(a,b):
    if a < b:
        print("Error")
        main()
def kor(r):
    korterulet = r**2*pi
    return korterulet
def teglalap(a,b):
    teglaterulet = a*b
    return teglaterulet
def gula(teglaterulet,m):
    gulaterfogat = teglaterulet*m/3
    return gulaterfogat
def kup(r,m):
    kupterfogat = r**2*pi*m/3
    return kupterfogat
def main():
    print("Kör sugara:",end=" ")
    r = int(input())
    print("Téglalap hosszabik oldala:",end=" ")
    a = int(input())
    print("Téglalap rövidebbik oldala:",end=" ")
    b = int(input())
    hibakezeles(a,b)
    print('\n')
    print("Kör területe: {0}".format(kor(r)),end='\n\n')
    print("Téglalap területe: {0}".format(teglalap(a,b)),end='\n\n')
    print("A gúla magassága: ",end=" ")
    gulam = int(input())
    print("A gúla térfogata: {0}".format(gula(teglalap(a,b),gulam)),end='\n\n')
    print("A kúp magassága: ",end=" ")
    kupm = int(input())
    print("A kúp térfogata: {0}".format(kup(r,kupm)),end='\n\n')
if __name__ == '__main__':
    main()