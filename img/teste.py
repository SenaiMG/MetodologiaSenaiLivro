import os

def rename_files_in_directory(prefix_to_remove):
    # Obter o diretório atual de trabalho
    directory = os.getcwd()
    
    # Listar todos os arquivos no diretório especificado
    for filename in os.listdir(directory):
        # Verificar se o arquivo começa com o prefixo que queremos remover
        if filename.startswith(prefix_to_remove):
            # Criar o novo nome removendo o prefixo
            new_filename = filename[len(prefix_to_remove):]
            # Obter o caminho completo para os arquivos
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_filename)
            # Renomear o arquivo
            os.rename(old_file, new_file)
            print(f"Renomeado: {filename} -> {new_filename}")

# Defina o prefixo a ser removido
prefix_to_remove = 'Livro MSEP 2019_'  # Substitua pelo prefixo real que você quer remover

# Chamar a função para renomear os arquivos
rename_files_in_directory(prefix_to_remove)