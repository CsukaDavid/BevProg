from random import Random, random


j = 0
while j < 20:
    j=j+1
    print(j*7)

euro = 1
while euro < 16385:
  print('{0} euro:{1:.2f} dollar'.format(euro,round(euro*1.65,2)))
  euro=euro*2

a,b,c = 1,1,1
while c<13:
  print(b)
  a,b,c = b,c*3