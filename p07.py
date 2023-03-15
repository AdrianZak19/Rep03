from  random import random
def generaTarga():
    x1=generaCarattere(65,26)
    y1=generaCarattere(65,26)
    x2=generaCarattere(65,26)
    y2=generaCarattere(65,26)
    z=generaCarattere(48,10)
    w=generaCarattere(48,10)
    k=generaCarattere(48,10)
    return x1+y1+" "+z+w+k+" "+x2+y2
def generaCarattere(a,b):
   return chr(int((random()*b+a))) 


l=[generaTarga() for x in range(10)]
for x in l:
    print("> ",x)
