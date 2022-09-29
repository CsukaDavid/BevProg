def main():
    print("Add meg az életkorod: ",end =" ")
    eletkor=int(input())
    print("1. Fogyaszthat-e legálisan alkoholt Amerikában? (21 év) ",end=" ")
    if (eletkor>20):
        print("Igen")
    else:
        print(" Nem")
    print("2. Vásárolhat-e dohányterméket Magyarországon? (18 év)",end=" ")
    if (eletkor>17):
        print("  Igen")
    else:
        print("   Nem")
    print("3. Szerezhet-e jogosítványt? (16 év)",end=" ")
    if (eletkor>15):
        print("                    Igen")
    else:
        print("                     Nem")
    print("4. Megnézheti-e egyedül a Shrek 2-t?",end=" ")
    if (eletkor>11):
        print("                    Igen")
    else:
        print("                     Nem")
if __name__=='__main__':
    main()