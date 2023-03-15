def creaListaIterativa(s):
    l = []
    for x in s:
        l.append(x)
    return l

def creaListaComprehension(s):
    l = [x for x in s]
    return l

def main():
    s="PIPPO"
    print(creaListaIterativa(s))
    print(creaListaComprehension(s))

main()
