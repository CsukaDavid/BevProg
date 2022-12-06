from enum import Enum


class Type(Enum):
    HOUSE = 'house'
    BOF = 'Block of Flats'
    TREE ='tree'
    FREE = 'free'

class Place:
    def __init__(self,begin,end): #type = Type.FREE
        self.begin=min(begin,end)
        self.end=max(begin,end)
        self.type=Type.FREE #self.type=type
    
    def distance(self):
        return self.end-self.begin
    
    def __str__(self):
        return('{0}; {1}',format(self.begin,self.end))

    def __add__(self,b):
        newElement=Place(min(self.begin,b.begin),max(self.end,b.end))   
        return newElement

    def __sub__(self,b):
        newElement=Place(max(self.begin,b.begin),min(self.end,b.end))   
        return newElement
    
    def __ge__(self,b):
        if self.distance() >= b.distance():
            return True
        else:
            return False
    
    def __iadd__(self,b):
        newElement=Place(min(self.begin,b.begin),max(self.end,self.end))
        return newElement

def main():
    a = Place(3,4)
    b = Place(4,2)

if __name__=="__main__":
    main()