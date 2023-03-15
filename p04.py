nomi1=["LUCA", "MARIO", "MARCO", "ANDREA", "FRANCO"]
nomi2=["UGO", "LEO", "MAO", "MARIO", "JO", "LUCA", "DEN"]
l=[]
for x in nomi1:
    if x not in nomi2:
        l.append(x)
for x in nomi2:
    if x not in nomi1:
        l.append(x)
print(l)
print("................")

l1=[x for x in nomi1 if x not in nomi2]
l2=[x for x in nomi2 if x not in nomi1]
l=l1+l2
print(l)





