from reader import ler_dados
from transformation import bytes_megabytes, percentual
from writer import gerar_relatorio

CAMINHO_ENTRADA = 'data/input/usuarios.txt'
CAMINHO_SAIDA = 'data/output/relatorio.txt'

def main()->None:

    lista_usuarios, lista_bytes = ler_dados(CAMINHO_ENTRADA)
    lista_megabytes = bytes_megabytes(lista_bytes)
    lista_percentual = percentual(lista_megabytes)

    gerar_relatorio(CAMINHO_SAIDA, lista_usuarios, lista_megabytes, lista_percentual)

    print("O relatório foi gerado com sucesso!")

if __name__ == '__main__':
    main()