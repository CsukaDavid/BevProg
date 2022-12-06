def alkoholUSA(eletkor):
    print("1. Fogyaszthat-e legálisan alkoholt Amerikában? (21 év)")
    if (eletkor>=21):
        print("     Fogyaszthat alkoholt Amerikában\n")
    else:
        print("     Nem fogyaszthat alkoholt Amerikában\n")

def dohanyHUN(eletkor):
    print("2. Vásárolhat-e dohányterméket Magyarországon? (18 év)")
    if (eletkor>=18):
        print("     Vásárolhat dohányterméket Magyarországon\n")
    else:
        print("     Nem vásárolhat dohányterméket Magyarországon\n")

def jogositvány(eletkor):
    print("3. Szerezhet-e jogosítványt? (16 év)")
    if (eletkor>=16):
        print("      Szerezhet jogosítványt\n")
    else:
        print("      Nem szerezhet jogosítványt?\n")
    

def Shrek(eletkor):
    print("4. Megnézheti-e egyedül a Shrek 2-t (12 év)?")
    if (eletkor>=12):
        print("      Megnézheti egyedül a Shrek 2-t\n")
    else:
        print("      Nem nézheti egyedül a Shrek 2-t\n")    

def main():
    print("Adja meg az életkorát: ",end="")
    eletkor=int(input())
    alkoholUSA(eletkor)
    dohanyHUN(eletkor)
    jogositvány(eletkor)
    Shrek(eletkor)

if __name__=='__main__':
    main()