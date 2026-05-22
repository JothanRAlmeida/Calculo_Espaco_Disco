# Transformando o espaço de armazenamento de bytes para megabytes
def bytes_megabytes(lista_bytes: list, valor_transformacao: int = 1048576)->list:

    lista_megabytes = []

    return [float(valor[0])/valor_transformacao for valor in lista_bytes]


# Calcula o percentual de ocupação de cada usuário
def percentual(lista_bytes: list)->list:

    espaco_total = sum(lista_bytes)

    return [(valor/espaco_total)*100 for valor in lista_bytes]