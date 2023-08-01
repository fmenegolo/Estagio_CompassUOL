path = f'/mnt/wsl/PHYSICALDRIVE2/Projects/Compasso/Azimute/Sprint_4/'
#
# 1.
# Você está recebendo um arquivo contendo 10.000 números inteiros, um em cada linha. 
# Utilizando lambdas e high order functions, apresente os 5 maiores valores pares e a soma destes.
"""
Você deverá aplicar as seguintes funções no exercício:

map
filter
sorted
sum

Seu código deverá exibir na saída (simplesmente utilizando 2 comandos `print()`):

a lista dos 5 maiores números pares em ordem decrescente;

a soma destes valores.

"""

print(list(filter(lambda x: x % 2 == 0, sorted(map(int, open(path + "number.txt").read().splitlines()), reverse=True)))[:5])

print(sum(list(filter(lambda x: x % 2 == 0, sorted(map(int, open(path + "number.txt").read().splitlines()), reverse=True)))[:5]))


#
# 2.
# Utilizando high order functions, implemente o corpo da função conta_vogais.
# O parâmetro de entrada será uma string e o resultado deverá ser a contagem de vogais presentes em seu conteúdo.
"""
É obrigatório aplicar as seguintes funções:

len
filter
lambda

Desconsidere os caracteres acentuados. Eles não serão utilizados nos testes do seu código.
"""
def conta_vogais(texto:str)-> int:
  vogais = ['a', 'e', 'i', 'o', 'u']
  filtro = list(filter(lambda x: x in vogais, texto.lower()))
  frequencia_vogais = {}
  for i in range(len(filtro)):
    vogal = filtro[i]
    if vogal in frequencia_vogais:
      frequencia_vogais[vogal] += 1
    else:
      frequencia_vogais[vogal] = 1
  soma = sum(frequencia_vogais.values())
  return soma

print(str(conta_vogais("Ola mundo, este e um importante teste")))

  #
  # 3.
  # A função calcula_saldo recebe uma lista de tuplas,
  # correspondendo a um conjunto de lançamentos bancários.
  # Cada lançamento é composto pelo seu valor (sempre positivo) e pelo seu tipo (C - crédito ou D - débito). 
"""
Abaixo apresentando uma possível entrada para a função.
"""
lancamentos = [
    (200,'D'),
    (300,'C'),
    (100,'C')
]
# A partir dos lançamentos, a função deve calcular o valor final, 
# somando créditos e subtraindo débitos. Na lista anterior, por exemplo,
# teríamos como resultado final 200.
"""
Além de utilizar lambdas, você deverá aplicar, obrigatoriamente, as seguintes funções na resolução:

reduce (módulo functools)
map
"""
from functools import reduce

def calcula_saldo(lancamentos) -> float:
    #continue este código
    extrato = map(lambda x: x[0] if x[1] == "C" else -x[0], lancamentos)
    saldo = reduce(lambda x, y: x + y, extrato)
    return saldo

print(calcula_saldo(lancamentos))

#
# 4.
# A função calcular_valor_maximo deve receber dois parâmetros,chamados de operadores e operandos.
# Em operadores, espera-se uma lista de caracteres que representam as operações matemáticas suportadas (+, -, /, *, %),
# as quais devem ser aplicadas à lista de operadores nas respectivas posições.
# Após aplicar cada operação ao respectivo par de operandos, a função deverá retornar o maior valor dentre eles.


""" Veja o exemplo: """

#Entrada
operadores = ['+','-','*','/','+']
operandos  = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]

"""
Aplicar as operações aos pares de operandos
[ 3+6 , -7-4.9, 8*-8 , 10/2 , 8+4 ] 


Obter o maior dos valores
12

Na resolução da atividade você deverá aplicar as seguintes funções:

max
zip
map

"""

def calcular_valor_maximo(operadores,operandos) -> float:
  t = list(zip(operandos, operadores))
  n1 = list(map(lambda x: x[0][0] + x[0][1] if x[1] == "+" else x[0][0] - x[0][1] if x[1] == "-" else x[0][0] * x[0][1] if x[1] == "*" else x[0][0] / x[0][1] if x[1] == "/" else 0, t))
  return max(n1)

print(calcular_valor_maximo(operadores,operandos))

#
# 5.
# Um determinado sistema escolar exporta a grade de notas dos estudantes em formato CSV.
# Cada linha do arquivo corresponde ao nome do estudante, acompanhado de 5 notas de avaliação,
# no intervalo [0-10]. É o arquivo estudantes.csv de seu exercício.

# Precisamos processar seu conteúdo, de modo a gerar como saída um relatório em formato textual
# contendo as seguintes informações:
"""
Nome do estudante

Três maiores notas, em ordem decrescente

Média das três maiores notas, com duas casas decimais de precisão

O resultado do processamento deve ser escrito na saída padrão (print), 
ordenado pelo nome do estudante e obedecendo ao formato descrito a seguir:
"""
# Nome: <nome estudante> Notas: [n1, n2, n3] Média: <média>
"""
Exemplo:
Nome: Maria Luiza Correia Notas: [7, 5, 5] Média: 5.67
Nome: Maria Mendes Notas: [7, 3, 3] Média: 4.33
"""
# Em seu desenvolvimento você deverá utilizar lambdas e as seguintes funções:
"""
round
map
sorted
"""

#print(list(filter(lambda x: x % 2 == 0, sorted(map(int, open(path + "estudantes.csv").read().splitlines()), reverse=True)))[:5])
def rel_aluno(csv):
  from csv import reader

  nome_notas = list(reader(open(csv)))
  top_5 = list(map(lambda x: (sorted(x[1:], key=int, reverse=True)),nome_notas))
  media = []
  for notas in top_5:
    media.append(round(sum(map(float, notas[:3]))/3,2))
  msg = list(sorted(zip(map(lambda x: x[0],nome_notas),map(lambda x: x[:3], top_5), media)))
    
  for i in msg:
    print(f"Nome: {str(i[0])} Notas: {list(map(int, i[1]))} Média: {i[2]}")

rel_aluno((path + "estudantes.csv"))

