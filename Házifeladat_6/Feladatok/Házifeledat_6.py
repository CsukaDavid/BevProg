import random
def main():
    n = str(3212333)
    osszeg = 0
    li=[]
    for i in range(len(n)) :
        li.append(n[i])
    print(li)
    for i in range(len(li)-1):
        if int(li[i])>int(li[i+1]):
            osszeg+=int(li[i-1])-int(li[i])
        else:
            osszeg+=int(li[i])-int(li[i-1])
    print(osszeg)

if __name__=="__main__":
    main()