def dekodolas(codetext):
    originaltext =""
    codetext=codetext.lower()
    for i in range(len((codetext))):
        print(codetext[i])
        textord = ord(codetext[i])
        if textord>96 and textord<121:
            originaltext +=chr(textord+2)
        elif textord==121:
            originaltext+="a"
        elif textord==122:
            originaltext+="b"
        else:
            originaltext +=chr(textord)
    print(originaltext)

def main():
    dekodolas("""Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb
""")
if __name__=="__main__":
    main() 