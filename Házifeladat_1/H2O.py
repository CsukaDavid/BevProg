from turtle import color, down

def main():
    print("Mennyi hidrogént akarsz összekeverni oxigénnel ?")
    print("Hidrogen: ",end=" ")
    Hidrogen = int(input())
    print("Oxigen: ",end=" ")
    Oxigen = int(input())
    H2O=0
    MaradekOxigen=0
    MaradekHidrogen=0
    if(Hidrogen<0 or Oxigen<0):
        print("/////////ERROR////////////\n")
        main()
    elif(Hidrogen==1 or Hidrogen==0 or Oxigen==0):
        MaradekHidrogen=Hidrogen
        MaradekOxigen=Oxigen
    elif (Hidrogen == Oxigen*2):
        H2O = Oxigen
    elif(Hidrogen>Oxigen*2):
        H2O=Oxigen
        MaradekHidrogen=Hidrogen-(Oxigen*2)
    elif(Hidrogen<Oxigen*2):
        H2O=round(Hidrogen//2)
        MaradekOxigen=Oxigen-H2O
        if(H2O*2+1==Hidrogen):
            MaradekHidrogen=1
        else:
            MaradekHidrogen=0
    print("H2O = {0}\nMaradék Hidrogén= {1}\nMaradék oxigén= {2}".format(H2O,MaradekHidrogen,MaradekOxigen))
        

if __name__=="__main__":
    main()
