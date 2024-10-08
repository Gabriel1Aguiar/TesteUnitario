def subt(n1,n2=0):
    if not isinstance(n1, int):
        raise TypeError("Subtração só é definido para números")
    elif not isinstance(n2, int):
        raise TypeError("Subtração só é definido para números")
    elif n1 == 0:
        return -n2
    else:
        return n1 - n2
