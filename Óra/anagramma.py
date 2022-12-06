def fuggveny(text1,text2):
    li1=[]
    li2=[]
    for i in range(len(text1)):
        if (text1[i]!=" "):
            li1.append(text1[i].lower())
    for j in range(len(text2)):
        if (text2[j]!=" "):
            li2.append(text2[j].lower())
    print(li1)
    print(li2)
    good=False
    if len(li1)!= len(li2):
        good=False
    else:
        print(len(li1))
        print(len(li2))
        for i in range(len(li1)):
            for j in range(len(li2)):
                if li1[i]==li2[j]:
                    good=True
                    break
                else:
                    good=False
    if good==False:
        print("a második szó nem az első szó anagrammája")
    else:
        print("a második szó az első szó anagrammája")

def main():
    fuggveny("Clint Eastwood","Old west action")
if __name__=="__main__":
    main()