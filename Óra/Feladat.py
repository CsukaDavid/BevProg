def main():
    while True:
        try:
            szam1=float(input("1. szám: "))
            szam2=float(input("2. szám: "))
            result=szam1/szam2
            print("Az osztás eredmenye: {0:.2f}".format(result))
            print("-"*10)
        except ZeroDivisionError:
            szam2=1
            print("Nullával osztottál ezért a második számod értékét 1-re állitotam így a result: {0:.2f}".format(szam1/szam2))
            print("-"*10)
        except ValueError:
            print("Szamot adj meg")
        except KeyboardInterrupt:
            break
if __name__=="__main__":
    main()