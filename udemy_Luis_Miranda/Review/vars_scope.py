print(globals()) # variaveis globais

def outside(x):
    a=x
    def inside():
        print(locals()) # variavais locais
        print(inside.__code__.co_freevars) # a is free var (not declared in this inside scope)
        # free var can be accessed but not changed. If want to change:
        nonlocal a
        a=99
        return a  
    return inside

ins1=outside(10)
print(ins1())
