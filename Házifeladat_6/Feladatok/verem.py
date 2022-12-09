class Verem():
    def __init__(self) -> None:
        self.verem= []

    
    def betesz(self,szamok):
        self.verem.append(szamok)
    
    def ures(self):
        if (len(self.verem) == 0):
            return True
        else:
            return False

    def meret(self):
        return len(self.verem)

    def kivesz(self):
        ertek = str(self.verem)[len(str(self.verem))-2]
        self.verem = self.verem[0:-1]
        if (len(self.verem)==0):
            return "None"
        return ertek

    def __str__(self) -> str:
        return "["+str(self.verem)[1:-1].replace(","," ")

def main():
    v = Verem()      # üres verem létrehozása
    print(v)         # [
    print(v.ures())  # True
    v.betesz(1)
    v.betesz(4)
    v.betesz(5)
    print(v)         # [1 4 5
    print(v.meret()) # 3
    print(v.ures())  # False
    x = v.kivesz()
    print(x)         # 5
    print(v)         # [1 4
    v.kivesz()
    v.kivesz()       # most már üres
    x = v.kivesz()
    print(x)         # None (jelezzük pl. így, hogy egy üres veremből akarunk kivenni) 
if __name__=="__main__":    
    main()