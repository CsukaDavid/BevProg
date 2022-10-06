def foo(second,first):
    print("Az egy {0}".format(second))
    print("Az egy {0} {1}".format(first,second))

def main():
    foo("bögre","piros")

if __name__=="__main__":
    main()