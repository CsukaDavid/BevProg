from turtle import back


def valid(text,chars):
    characters=""
    for i in range(len(text)):
        for j in range(len(chars)):
            if text[i]==chars[j]:
                characters +=text[i]
    print("{0}      ----->   {1} ".format(text,characters))

def main():
    valid("Barking!","B")
    valid("KL754", "0123456789")
    valid("BEAN", "abcdefghijklmnopqrstuvwxyz")
    
if __name__=="__main__":
    main()