import random
def main():
    n = 2^1024
    n = str(n)
    osszeg = 0
    li=[]
    for i in range(len(str(n))):
        li.append(str(n[i]))
    for i in range(len(li)-1):
        if int(li[i]) > int(li[i+1]):
            osszeg += int(li[i])-int(li[i+1])
        else:
            osszeg += int(li[i+1])-int(li[i])
    print(osszeg)

if __name__=="__main__":
    main()