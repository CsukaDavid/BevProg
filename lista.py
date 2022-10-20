def main():
    text = "1234567"
    li = [s for s in text]
    print(li)

    li.clear()
    text ="The quick brown fox jumps over the lazy dog"
    li = [len(n) for n in text.split()]
    print(li)
if __name__=="__main__":
    main()