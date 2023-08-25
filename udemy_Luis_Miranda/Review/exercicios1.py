# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
from copy import deepcopy
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
n_produtos=deepcopy(produtos)
for prod in n_produtos:
    prod["preco"]*=1.1
print(n_produtos)

# Usando list comprehention
novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in deepcopy(produtos)
]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
n2_produtos=deepcopy(produtos)
n2_produtos.sort(key=lambda produto: produto['nome'], reverse=True)
print(n2_produtos)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
n3_produtos=deepcopy(produtos)
n3_produtos.sort(key=lambda produto: produto['preco'])
print(n3_produtos)