import math
from turtle import end_fill

def faktoriális():
    print("Faktoriális")
    print("n = ",end=" ")
    n = int(input())
    Pn=n
    i=1
    while i < n:
        Pn=(n-i)*Pn
        i=i+1
    print("Pň= {0}\n".format(Pn))

def pitagorasz():
    print("Pitagorasz tétel\n")
    print("Adj meg 2 befogót: ")
    print("a = ",end=" ")
    a = int(input())
    print("b = ",end=" ")
    b = int(input())
    print("Átfogó hossza: {0} \n".format(math.sqrt(a**2+b**2)))

def masodfoku():
    print("Másodfokú egyenlet")
    print("Írd be x^2 előtagját: ",end=" ")
    a = int(input())
    print("Írd be x előtagját: ",end=" ")
    b = int(input())
    print("Írd be a konstanst: ",end=" ")
    c = int(input())

    x1 = (-b+math.sqrt(b**2+4*a*c))/2*a
    x2 = (-b-math.sqrt(b**2+4*a*c))/2*a
    print("x1 = {0}\n".format(x1))
    print("x2 = {0}\n".format(x2))


def main():
    pitagorasz()
    masodfoku()
    faktoriális()
    
if __name__=='__main__':
    main()