class fejlesztok():
    def __init__(self,name,rang,year,payment):
        self.name=name
        match rang:
            case "Intern":
                self.rang=rang
            case "Medior":
                self.rang=rang
            case "Senior":
                self.rang=rang
            case _:
                self.rang="Junior"
        match year:
            case 0|"":
                self.year=0
            case _:
                self.year=year
        self.payment=payment
    
    def fizetes(self,pay):
        if (pay !=""):
            self.payment +=pay
        else:
            self.payment +=10000

    def pluszyear(self):
        self.year +=1

    def kiir(self):
        print("""
Name:       {0} 
Rang:       {1} 
Operate:    {2} year
Wage:       {3} HUF\n""".format(self.name,self.rang,self.year,self.payment))

    def rangja(self):
        if self.year >= 5:
            self.rang="Senior"
        elif self.year > 1 & self.year<5:
            self.rang ="Medior"
        elif self.year==1:
            self.rang="Junior"
        elif self.year==0:
            self.rang="Intern"


def main():   
    FirstWorker = fejlesztok("Csuka Dávid","","",30000)
    FirstWorker.fizetes(10000)
    FirstWorker.rangja()
    FirstWorker.kiir()
if __name__=='__main__':
    main()