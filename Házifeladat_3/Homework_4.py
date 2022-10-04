import math
def binaris(number):
    remainder = ""
    while number !=0:
        if number%2==1:
            remainder += "1"
        elif number%2==0:
            remainder += "0"
        number = math.floor(number/2)
    binary =""
    for i in range(len(remainder)):
        binary  +=remainder[len(remainder)-1-i]+" "
    print("The number in binary number system: {0}".format(binary))


def main():
    print("Write a number that you want to convert into a binary number: ",end=" ")
    number = int(input())
    binaris(number)

if __name__=="__main__":
    main()