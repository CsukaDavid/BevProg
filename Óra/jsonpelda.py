import json

def main():
    f = open("pelda.json",'r')
    d = json.load(f)

    print(d['people'])
    print(type(d['people']))
    print("-"*10)
    print(d['people'][0])
    print(type(d['people'][0]))
    print('-'*10)
    print(d['people'][0]['name'])
    print(type(d['people'][0]['name']))
    f.close()

if __name__=="__main__":
    main()