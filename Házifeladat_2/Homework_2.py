def main():
    print("írj egy számot: ",end=" ")
    n = int(input())
    F0 = 0
    F1 = 1
    i = 0
    while i < n:
        F1 = F1+F0
        F0 = F1-F0
        i = i+1
    print("A végeredmény : {0}".format(F0))
if __name__=='__main__':
    main()