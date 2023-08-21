pessoa={
    'nome': 'Th',
    'sobrenome': 'Gon'
}

a,b=pessoa # nome sobrenome
print(a,b)
a,b=pessoa.values() # Th Gon
print(a,b)
a,b=pessoa.items() # ('nome', 'Th') ('sobrenome', 'Gon')
print(a,b)

# Copia os itens e ja adiciona mais um parametro
novo_dic={**pessoa,'novo_param':'novo_val'} # {'nome': 'Th', 'sobrenome': 'Gon', 'novo_param': 'novo_val'}
print(novo_dic)