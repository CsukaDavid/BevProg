def main():
    f =open("./Github/BevProg/Óra/barmi.txt",'r')
    li = f.readlines()
    print(li)
    f.close()

    f=open("./Github/BevProg/Óra/barmi.txt",'a')
    for i in range(i,file=f):
        print(i,file=f)
        f.close()
    
    f=open("barmi.txt",'w')
        
if __name__=="__main__":
    main()