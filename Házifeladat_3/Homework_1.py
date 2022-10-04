def dekodolas(codetext):
    originaltext =""
    for i in range(len((codetext))):
       textord = ord(codetext[i])
       originaltext +=chr(textord-3)
    print("The original text: {0}".format(originaltext))

def main():
    print("Text encrypted with Caesar encoding: kwwsv=22|rxwx1eh2gTz7z<Zj[fT")
    dekodolas("kwwsv=22|rxwx1eh2gTz7z<Zj[fT")

if __name__=="__main__":
    main()