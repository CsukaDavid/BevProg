import sys
def main():
    print(sys.argv[0][0:len(sys.argv[0])-3])
if __name__=="__main__":
    main()