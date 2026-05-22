# Programa que calcula e gera relatório com a taxa de ocupação de disco de usuários de uma empresa

## Descrição

A ACME Inc., uma empresa com aproximadamente 500 funcionários, está enfrentando problemas de espaço em disco em seu servidor de arquivos. Para auxiliar na identificação dos usuários que mais consomem armazenamento, foi desenvolvido um programa capaz de gerar um relatório detalhado de utilização de disco.

O sistema utiliza como entrada um arquivo chamado `usuarios.txt`, contendo o nome dos usuários e a quantidade de espaço ocupado em bytes no servidor.

A partir desses dados, o programa gera um relatório chamado `relatorio.txt`, contendo:

- Espaço utilizado por cada usuário em MB
- Percentual de uso individual
- Total de espaço utilizado
- Média de utilização dos usuários

---

## 📂 Estrutura do Arquivo de Entrada

O arquivo `usuarios.txt` possui os dados no seguinte formato:

```txt
alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
```

Saída:

```txt
ACME Inc.           Uso de espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuários       Espaço utilizado    % do uso

1    alexandre       434.99 MB          16.11%
2    anderson       1187.99 MB          44.01%
3    antonio         117.74 MB           4.36%
4    carlos           87.03 MB           3.22%
5    cesar             0.94 MB           0.03%
6    rosemary        752.88 MB          27.89%
7    jothan          117.74 MB           4.36%


Espaço total ocupado: 2699.31 MB
Espaço médio ocupado: 385.62 MB
```
