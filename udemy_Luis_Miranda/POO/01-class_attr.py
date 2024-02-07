class Pessoa:
    classAttr='Thiago'
    def __init__(self):
        print(self.classAttr) # also accessing class attr

print(Pessoa.classAttr) # not need to instanciate