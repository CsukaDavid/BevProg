def foo(text,find,place):
    print(place+" "+find)
    number =text.rfind(find)
    text = text[0:number]+place+" "+find+text[number+len(find):len(text)]
    print(text)

def main():
    print("Írj be egy mondatot:")
    text =str(input())
    print("Szeretnél valamelyik szó elé valamit rakni?(Y/N)")
    character=str(input())
    if (character=="N"):
        print(text)
    else:
        print("Keresendö szó: ")
        find = str(input())
        print("A szó elé mit szeretnél rakni :")
        place= str(input())
        foo(text,find,place)
    print("""\nHa jönn Szondi.akkor kéne nézni telefonhoz gyors töltött
,kábelel,adapterrel. a Redmi Note 9 Prohoz hajtogatos tok és kettö db PEREMMENTES(Keretmentes) üvegfólia(Note 9 prohoz,
Huawei Mate 20 Litehoz) Emag-rol , Code Vein Deluxe edition game 4660huf OKTOBER 10 85% DARK SOULS GAME WIFU SOULS. MINÉL HAMARABB\n""")

if __name__=="__main__":
    main()