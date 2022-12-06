import random
def main():
    n = 2^1024
    n = str(n)
    li = []
    osszeg = 0
    for i in range(len(n)):
        li.append(n[i])
    for i in range(len(li)):
        if int(li[i]) > int(li[i+1]):
            osszeg += int(li[i])-int(li[i+1])
        else:
            osszeg += int(li[i+1])-int(li[i])
    print(osszeg)

if __name__=="__main__":
    main()