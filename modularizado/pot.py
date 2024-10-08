def pot(n1,n2=0):
    if not isinstance(n1, int):
        raise TypeError("Potência só é definido para números")
    if not isinstance(n2, int):
        raise TypeError("Potência só é definido para números")
    elif n1 == 0:
        raise ValueError("Primeiro número não pode ser zero")
    else:
        return n1 ** n2

