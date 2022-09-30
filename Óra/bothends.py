def both_ends(s):
    print(s[0]+s[1]+s[len(s)-2]+s[len(s)-1])

def main():
    print("\nSzöveg: ",end=" ")
    s = str(input())
    print("Két elsö és utolsó betü együtt: ",end=" ")
    both_ends(s)

if __name__=="__main__":
    main()