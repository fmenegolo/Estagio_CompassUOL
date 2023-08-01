"""
Nesta tarefa iremos utilizar as bibliotecas Pandas e NumPy para responder a quatro exercícios.
Lembre-se de adicionar o código desenvolvido ao seu repositório no GitHub para que o monitor(a) da Sprint possa avaliá-lo posteriormente.
-----------------------------------------------------
Leia o arquivo actors.csv e codifique os cálculos solicitados sobre o conjunto de dados utilizando a biblioteca Pandas. Adicione apenas a resposta da questões nos espaços indicados. Seu código-fonte deverá estar no Github.

Perguntas dessa tarefa

"""
path = f'/mnt/wsl/PHYSICALDRIVE2/Projects/Compasso/Azimute/Sprint_7/Tarefa_1/'
import pandas as pd
actors = pd.read_csv(path + 'actors.csv')

# 1. Identifique o ator/atriz com maior número de filmes e o respectivo número de filmes.
print("RESPOSTA 1")
id_maior_num_filmes = actors['Number of Movies'].idxmax()

maior_num_filmes = actors.loc[id_maior_num_filmes]

nome_ator1 = maior_num_filmes['Actor']

num_filmes = maior_num_filmes['Number of Movies']

print("Ator/atriz com maior número de filmes é:",[nome_ator1,num_filmes])

# 2. Apresente a média da coluna contendo o número de filmes.
print("RESPOSTA 2")
actors = pd.read_csv(path + 'actors.csv')

media_filme = actors['Number of Movies'].mean()

print("A média da coluna contendo o número de filmes é:", media_filme)

# 3. Apresente o nome do ator/atriz com a maior média por filme.
print("RESPOSTA 3")
id_maior_media = actors['Average per Movie'].idxmax()

maior_media = actors.loc[id_maior_media]

nome_ator3 = maior_media['Actor']

media_filmes_ator = maior_media['Average per Movie']
print("Ator/atriz com a maior média por filme é:",[nome_ator3,media_filmes_ator])

# 4. Apresente o nome do(s) filme(s) mais frequente(s) e sua respectiva frequência.
print("RESPOSTA 4")
frequencia_filmes = actors['#1 Movie'].value_counts()
top1 = frequencia_filmes.index[0]
frenq_top1 = frequencia_filmes[0]
print("O filme de maior frequência é:", [top1, frenq_top1])



