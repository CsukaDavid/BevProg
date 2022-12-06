def main():

f2=open('txki.json','w')
jsontxt=json.dumps(d)
print(jsontxt,file=f2)
f2.close

if __name__=="__main__":
    main()