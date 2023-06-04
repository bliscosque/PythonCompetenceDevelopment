import os
import random

# Lista de nomes populares no Brasil
common_names = [
    "Miguel", "Arthur", "Davi", "Gabriel", "Bernardo", "Sophia", "Alice", "Laura", "Valentina",
    "Heitor", "Helena", "Theo", "Pedro", "Lorenzo", "Isabella", "Manuela", "Júlia", "Heloísa",
    "Enzo", "Luiza", "Matheus", "Maria Eduarda", "Lucca", "Giovanna", "Rafael", "Lara", "Guilherme",
    "Beatriz", "Nicolas", "Isadora", "Samuel", "Maria Clara", "João Miguel", "Ana Clara", "Enzo Gabriel",
    "Lívia", "Henrique", "Mariana", "Pietro", "Rafaela", "Pedro Henrique", "Giovana", "Cauã", "Vitória",
    "Vinícius", "Emanuelly", "Bento", "Larissa", "Fernando", "Letícia", "Gustavo", "Maria Luiza",
    "Felipe", "Sarah", "Benjamin", "Isabelly", "João Pedro", "Melissa", "Samuel", "Yasmin",
    "Daniel", "Ana Júlia", "Vitor", "Maria Alice", "Leonardo", "Marina", "Murilo", "Clara",
    "Eduardo", "Ana Laura", "João", "Carolina", "Antônio", "Cecília", "Pablo", "Esther",
    "Davi Lucca", "Laís", "Anthony", "Maitê", "Francisco", "Isis", "Bryan", "Luna",
    "Thomas", "Rebeca", "Davi Lucas", "Agatha", "João Vitor", "Ana Beatriz", "Yuri", "Ana Sophia",
    "Ruan", "Bianca", "Kauê", "Lavínia", "Otávio", "Fernanda", "Augusto", "Amanda"
]

# Diretório onde os arquivos serão criados
directory = './arquivos_texto'

# Verifica se o diretório existe, caso contrário, cria-o
if not os.path.exists(directory):
    os.makedirs(directory)

# Criação dos arquivos de texto
for i in range(1, 101):
    file_name = f'{i}.txt'
    file_path = os.path.join(directory, file_name)
    
    # Escolhe um nome aleatório da lista de nomes comuns
    random_name = random.choice(common_names)
    
    # Escreve o nome no arquivo
    with open(file_path, 'w') as file:
        file.write(random_name)
    
    print(f'Criado o arquivo: {file_path}')
