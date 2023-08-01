"""
Armazene o arquivo actors.csv dentro de uma nova pasta, após isso crie 5 arquivos do tipo “txt” vazios 
(1 para cada exercício do desafio).

Em seguida para cada uma das tarefas da sequencia, leia o arquivo actors.csv utilizando Python
como linguagem de programação e depois de obter as repostas necessárias armazene cada um dos resultados
em um dos arquivos “txt” criados.

Pontos de Atenção:

Para desenvolvimento deste exercício, não deve ser utilizado as bibliotecas Pandas e NumPy e/ou 
outras bibliotecas e engines que utilizam de dataframes.

Todas as transformações que julgarem necessárias, devem ser feitas utilizando os scripts
Python e nenhuma modificação deve ser feita no arquivo actors.csv

Para leitura do arquivo actors.csv, não deve ser utilizado o módulo csv nativo do Python.

Perguntas dessa tarefa
1. O ator/atriz com maior número de filmes e o respectivo número de filmes.

2. A média do número de filmes por autor.

3. O ator/atriz com a maior média por filme.

4. O nome do(s) filme(s) mais frequente(s) e sua respectiva frequência.

5. A lista dos Autores ordenada por pagamento. Do mais bem pago para o menos bem pago
"""
# Pergunta_1

from csv import DictReader
path = f'/mnt/wsl/PHYSICALDRIVE2/Projects/Compasso/Azimute/Sprint_3/Python/Desafio/'
with open(path + 'actors.csv') as arquivo:
    leitor_csv = DictReader(arquivo)
    next(leitor_csv)
    resultado = []
    for i in leitor_csv:
        ator = i["Actor"]
        num_filmes = i["Number of Movies"]
        resultado.append([ator, num_filmes])

resultado.sort(key=lambda x: x[1], reverse=True)

with open( path +'Pergunta_1.txt', 'w') as resposta1:
    resultado1=resultado[0]
    resposta1.write(str(resultado1))

#  Pergunta_2

from csv import DictReader
#path = f'C:/Users/fmene/OneDrive/Documentos/GitHub/Compasso/Udemy/Sprint_3/Python/Desafio/'
with open(path + 'actors.csv') as arquivo:
    leitor_csv = DictReader(arquivo)
    next(leitor_csv)
    resultado = []
    num_filmes_total = 0

    for i in leitor_csv:
        ator = i["Actor"]
        num_filmes = int(i["Number of Movies"])
        resultado.append([ator, num_filmes])
        num_filmes_total += num_filmes

resultado2 = num_filmes_total/len(ator)

with open( path +'Pergunta_2.txt', 'w') as resposta2:
    resultado2=resultado
    resposta2.write(str(resultado2))

# Pergunta_3

from csv import DictReader
#path = f'C:/Users/fmene/OneDrive/Documentos/GitHub/Compasso/Udemy/Sprint_3/Python/Desafio/'
with open(path + 'actors.csv') as arquivo:
    leitor_csv = DictReader(arquivo)
    next(leitor_csv)
    resultado = []
    for i in leitor_csv:
        ator = i["Actor"]
        num_filmes = i["Average per Movie"]
        resultado.append([ator, num_filmes])

resultado.sort(key=lambda x: x[1], reverse=True)

with open( path +'Pergunta_3.txt', 'w') as resposta3:
    resultado3=resultado[0]
    resposta3.write(str(resultado3))

# Pergunta_4

from csv import DictReader
#path = f'C:/Users/fmene/OneDrive/Documentos/GitHub/Compasso/Udemy/Sprint_3/Python/Desafio/'
with open(path + 'actors.csv') as arquivo:
    leitor_csv = DictReader(arquivo)
    next(leitor_csv)
    resultado = []
    frequencia_filmes = {}

    for i in leitor_csv:
        filme = i["#1 Movie"]
        if filme in frequencia_filmes:
            frequencia_filmes[filme] += 1
        else:
            frequencia_filmes[filme] = 1
maior_frequencia_filmes = max(frequencia_filmes.values())
filme_mais_frequente = [filme for filme, frequencia in frequencia_filmes.items() if frequencia == maior_frequencia_filmes]

resultado = f'{filme_mais_frequente[0]}, {maior_frequencia_filmes}'

with open( path +'Pergunta_4.txt', 'w') as resposta4:
    resultado4=resultado
    resposta4.write(str(resultado4))

# Pergunta_5

from csv import DictReader
#path = f'C:/Users/fmene/OneDrive/Documentos/GitHub/Compasso/Udemy/Sprint_3/Python/Desafio/'
with open(path + 'actors.csv') as arquivo:
    leitor_csv = DictReader(arquivo)
    next(leitor_csv)
    resultado = []
    for i in leitor_csv:
        ator = i["Actor"]
        num_filmes = i["Total Gross"]
        resultado.append([ator, num_filmes])

resultado.sort(key=lambda x: x[1], reverse=True)

with open( path +'Pergunta_5.txt', 'w') as resposta5:
    resultado5=resultado
    resposta5.write(str(resultado5))
