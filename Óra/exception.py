def main():
    try:
        d1=int(input("Szam: "))
        d2=int(input("Szam: "))
        print(d1/d2)
    except ZeroDivisionError as e:
        print(e)
    except ValueError:
        print("Szamot adj meg")
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
    except:
        print("Ha nem megy hát nem megy")
    print("Vége")
if __name__=="__main__":
    main()