import random
def main():
    randomnumber=random.randint(1,100)
    print(randomnumber)
    number=0
    i = 0
    while number !=randomnumber:
        number=int(input("your guess> "))
        if number > randomnumber:
            print("my number is smaller")
        if number < randomnumber:
            print("my number is larger")
        i+=1
    print("Good job! That's it!")
    print("Number of guesses: {0}".format(i))
if __name__=="__main__":
    main()