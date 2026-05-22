# Escreve o relatório estruturado em novo arquivo .txt
def gerar_relatorio(caminho_saida: str, lista_usuarios: list, lista_megabytes: list, lista_percentual: list)->None:

    with open(caminho_saida, 'w', encoding= 'utf-8') as arquivo:

        # Cabeçalho do relatório
        arquivo.write(f"{'ACME Inc.':<20}Uso de espaço em disco pelos usuários\n")
        arquivo.write("-" * 72 + "\n")
        arquivo.write(f"{'Nr.':5}{'Usuários':<15}{'Espaço utilizado':<20}{'% do uso':<10}\n\n")

        numero = 1

        # Escreve todos os usuários, a quantidade megabytes utilizados e a taxa de ocupação
        for usuario, megabytes, percentual in zip(lista_usuarios, lista_megabytes, lista_percentual):
            
            arquivo.write(
                f"{numero:<5}"
                f"{usuario[0].capitalize():<15}"
                f"{megabytes:>7.2f} MB"
                f"{percentual:>15.2f}%\n"
            )

            numero += 1
        
        # Final do relatório
        total_megabytes = sum(lista_megabytes)
        ocupacao_media = total_megabytes/len(lista_usuarios)

        arquivo.write(f"\n\nEspaço total ocupado: {total_megabytes:.2f} MB")
        arquivo.write(f"\nEspaço médio ocupado: {ocupacao_media:.2f} MB")







