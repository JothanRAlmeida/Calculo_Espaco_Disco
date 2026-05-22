# Ler dados do usuário e seu espaço utilizado em bytes
def ler_dados(caminho_arquivo: str)->list:
    
    lista_usuarios = []
    lista_bytes = []

    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            lista_usuarios.append(linha[:16].split())
            lista_bytes.append(linha[16:].split())

        return lista_usuarios, lista_bytes