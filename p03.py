l=[]
s="01"
def listaOttetti():        
    L=[a+b+c+d+e+f+g+h for a in s for b in s for c in s for d in s for e in s for f in s for g in s for h in s]
    return L
h=listaOttetti()
for z in h:
    print(z)
listaOttetti()
