from modularizado.soma import soma
from modularizado.subt import subt
from modularizado.multi import multi
from modularizado.div import div
from modularizado.fatorial import fatorial
from modularizado.subt import subt

def calc(n1,op,n2=0):
    if op == "+":
        return soma(n1,n2)
    elif op == "-":
        return subt(n1,n2)
    elif op == "*":
        return n1*n2
    elif op == "/":
        return n1/n2
    elif op == "!":
        return fatorial(n1)

print(calc(3,"!")) 
