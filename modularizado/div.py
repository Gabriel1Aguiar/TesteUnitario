def div(n1,n2=0):
    if n2 == 0:
        raise ValueError("Não é possível dividir por 0")
    elif not isinstance(n1, int):
        raise TypeError("Divisão só é definido para números")
    elif not isinstance(n2, int):
        raise TypeError("Divisão só é definido para números")
    else:
        return n1 / n2
