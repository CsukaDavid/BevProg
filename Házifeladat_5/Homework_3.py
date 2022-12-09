# reading the file

def main():
    filename='F:\BevProg\Házifeladat_5\string1.py'
    f= open(filename,"r")
    contents=f.readlines()
    eredmeny=""
    for i in range(len(contents)):
        if contents[i].find("#")>0:
            pass
        else:
            eredmeny+=contents[i]
    print(eredmeny)
    f.close()
    file='F:\BevProg\Házifeladat_5\string1_clear.py'
    f =open(file,"w")
    print(eredmeny,file=f)
    f.close

if __name__=="__main__":
    main()