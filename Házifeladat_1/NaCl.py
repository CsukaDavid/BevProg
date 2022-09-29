from turtle import color, down

def main():
    print("Mennyi hidrogént akarsz összekeverni oxigénnel ?")
    print("Natrium: ",end=" ")
    Natrium = int(input())
    print("Klorid: ",end=" ")
    Klorid = int(input())
    NaCl=0
    MaradekNatrium=0
    MaradekKlorid=0
    if(Natrium<0 or Klorid<0):
        print("/////////ERROR////////////\n")
        main()
    elif(Natrium==0 or Klorid==0):
        MaradekNatrium=Klorid
        MaradekKlorid=Natrium
    elif(Natrium==Klorid):
        NaCl=Natrium
    elif(Natrium>Klorid):
        NaCl=Klorid
        MaradekNatrium=Natrium-Klorid
    elif(Natrium<Klorid):
         NaCl=Natrium
         MaradekKlorid=Klorid-Natrium
    print("NaCl = {0}\nMaradék nátrium= {1}\nMaradék klórid= {2}".format(NaCl,MaradekNatrium,MaradekKlorid))
        

if __name__=="__main__":
    main()
