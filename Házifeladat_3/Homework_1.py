def dekodolas(codetext):
    originaltext =""
    for i in range(len((codetext))):
       textord = ord(codetext[i])
       originaltext +=chr(textord-3)
    print("Az eredeti szöveg: {0}".format(originaltext))

def main():
    print("Caesar kódolással titkosított szöveg: kwwsv=22|rxwx1eh2gTz7z<Zj[fT")
    codetext = "kwwsv=22|rxwx1eh2gTz7z<Zj[fT"
    dekodolas(codetext)

if __name__=="__main__":
    main()