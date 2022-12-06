from ctypes.wintypes import PINT


def main():
    li1=[1,2,3]
    li2=['a','b','c'
    z = zip(li1,li2)
    print(list(z))
    for zi in z:
        print(zi)
if __name__=="__main__":
    main()