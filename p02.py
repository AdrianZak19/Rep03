def creaListaIterativa(s):
    l = []
    for x in s:
        if x != "P":
            l.append(x)
    return l

def creaListaComprehension(s):
    l = [x for x in s if x != "P"]
    return l

def main():
    s="PIPPO"
    print(creaListaIterativa(s))
    print(creaListaComprehension(s))

main()
