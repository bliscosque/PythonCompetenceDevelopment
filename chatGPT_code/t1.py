import os
import random
import string

# Função para gerar um nome aleatório
def generate_random_name():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(10))

# Diretório onde os arquivos serão criados
directory = './arquivos_texto'

# Verifica se o diretório existe, caso contrário, cria-o
if not os.path.exists(directory):
    os.makedirs(directory)

# Criação dos arquivos de texto
for i in range(1, 101):
    file_name = f'{i}.txt'
    file_path = os.path.join(directory, file_name)
    
    # Gera o nome aleatório para o conteúdo do arquivo
    random_name = generate_random_name()
    
    # Escreve o nome aleatório no arquivo
    with open(file_path, 'w') as file:
        file.write(random_name)
    
    print(f'Criado o arquivo: {file_path}')
