def soma(n1,n2=0):
    if not isinstance(n1, int):
        raise TypeError("Soma só é definido para números")
    elif not isinstance(n2, int):
        raise TypeError("Soma só é definido para números")
    else:
        return n1+n2
