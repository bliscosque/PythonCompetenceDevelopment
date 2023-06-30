"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -          # + aparecer o + se o número for positivo
Ex.: 0>-100,.1f
Conversion flags - !r !s !a  # chama os métodos __repr__, __str__, __ascii__
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}') # preenche até 10 char (com espaço, mas pode ser outro char)
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.4873648123746:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')