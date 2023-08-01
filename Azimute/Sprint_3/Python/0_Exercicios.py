# 1.
# Escreva um código Python que lê do teclado o nome e a idade de um usuário e que imprima apenas
# o ano em que ele completará 100 anos.
# Dica: você pode ler strings digitadas no teclado utilizando a função builtin input('mensagem').
# Lembre-se de converter números para seu respectivo tipo (int ou float) antes fazer operações aritméticas.
from datetime import datetime
def ano_faz_cem ():
    nome = input('Digite seu nome:')
    idade = int(input('Digite sua idade:'))
    return (datetime.today().year + (100-idade))

print(ano_faz_cem())


# 2.
#Escreva um código Python que verifique se três números digitados pelo usuário são pares ou ímpares.
# Para cada número, imprima o Par: ou Ímpar: e o número correspondente.

for i in range(1,4):
    numero = int(input('Escreva um numero: '))
    if (numero % 2) == 0:
        print(f' Par: {numero}')
    else:
        print(f' Ímpar: {numero}')

# 3.
#Escreva um código Python que imprime os números pares de 0 até 20 (incluso).
# Dica: Utilize a função range().

for i in range(0,21):
    if (i % 2) == 1:
        continue
    print(i)

# 4.
# Escreva um código Python que imprime todos os números primos de 1 até 100.
# Abaixo uma imagem de exemplo dos números primos entre 1 e 1000

cont = 2
for i in range(2,101):
    for j in range(2,i):
        if ((i % j) == 0):
            break
    else:
       print(i)


# 5.
# Escreva um código Python que tem 3 variáveis dia (22), mês(10) e ano(2022) e 
# imprime a data completa no formato a seguir:
# Exemplo: 22/10/2022
# Importante: É necessário formatar as variáveis como strings antes de concatená-las e imprimi-las na tela.

dia, mes, ano = 22, 10, 2022
print(f'{dia}/{mes}/{ano}')


#
#6.
#Dada duas listas como as no exemplo abaixo:

a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
"""
Escreva um programa que retorne o que ambas as listas têm em comum (sem repetições).
O seu programa deve funcionar para listas de qualquer tamanho.
"""

def inner_join(list_a, list_b):
    lista_a = set(list_a)
    lista_b = set(list_b)
    nova_lista = []
    for i in lista_a:
        if (i in lista_b):
            nova_lista.append(i)
    
    return nova_lista

print(inner_join(a,b))

#
#7.
# Dada a seguinte lista:
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#Faça um programa que gere uma nova lista contendo apenas números ímpares.
def somente_pares(array):
    nova_lista=[]
    for i in range(len(array)):
        if (array[i] % 2) != 0:
            nova_lista.append(array[i])
    return nova_lista

print(somente_pares(a))


#8.
#Verifique se cada uma das palavras da lista ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']
# é ou não um palíndromo.
# Obs: Palíndromo é uma palavra que permanece igual se lida de traz pra frente.

def palindromo(string, ini=0, fim=None):
    if fim is None:
        fim = len(string)-1
    if ini == fim:
        print("A palavra: " + string + " é um palíndromo")        
    elif string[ini] == string[fim]:
        return palindromo(string, ini +1, fim-1)
    else:
        print("A palavra: " + string + " não é um palíndromo")
        
list = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

for i in range(len(list)):
  palindromo(list[i])

"""
vou resumir, pois como o curso começa com funções, acabei fazendo o codigo como uma função 
na verdade eu particulamente retornaria um boleano ao invés de um print na função acima para poder
ter a possibilidade de reutilização em outros treços de codigos tornando-o mais versátil
"""

list = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']
for string in list:
    if string == i[::-1]:
        print("A palavra: " + string + " é um palíndromo")
    else:
        print("A palavra: " + string + " não é um palíndromo")


 #
 # 9
 # Dada as listas a seguir:

primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]
"""""
#Faça um programa que imprima o dados na seguinte estrutura: 
# "índice - primeiroNome sobreNome está com idade anos".

#Exemplo:
#0 - João Soares está com 19 anos 

# Você deve Utilizar a função enumerate().
"""
for i, primeirosNomes in enumerate(primeirosNomes):
    pessoa = f"{i} - {primeirosNomes} {sobreNomes[i]} está com {idades[i]} anos"
    print(pessoa)

#
#10
#Escreva uma função que recebe uma lista e retorna uma nova lista sem elementos duplicados. 
# Utilize a lista a seguir para testar sua função.
exercicio_10 = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']


def distinct(lista):
    lista = set(lista)
    return list(lista)
    
print(distinct(exercicio_10))

#
#11
#Escreva um programa que lê o conteúdo do arquivo texto arquivo_texto.txt e imprime o seu conteúdo.
# Dica: leia a documentação da função

with open('arquivo_texto.txt') as arquivo:
    leitor = arquivo.read()
    print(leitor, end='')

#
#12
#Leia o arquivo person.json, faça o parsing e imprima seu conteúdo.
# Dica: leia a documentação do pacote

import json
with open('person.json', 'r') as arquivo:
    leitor = arquivo.read()
    ret = json.loads(leitor)
    print(ret)

#
#13
#Implemente a função my_map(list, f) que recebe uma lista como primeiro argumento e 
# uma função como segundo argumento. Esta função aplica a função recebida para 
# cada elemento da lista recebida e retorna o resultado em uma nova lista.
"""
Teste sua função com a lista de entrada [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
e com uma função que potência de 2 para cada elemento.
"""
lista_input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def my_map(array, f):
    nova_lista=[]
    for i in range(len(array)):
        nova_lista.append(array[i] ** f)
    return nova_lista

print(my_map(lista_input,2))

#
#14
# Escreva uma função que recebe um número variável de parâmetros não nomeados e um 
# número variado de parâmetros nomeados e imprime o valor de cada parâmetro recebido.

#Teste sua função com os seguintes parâmetros:
#(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)
"""
Para organizar o seu código e torná-lo mais legível para a correção, é necessário que 
você utilize a declaração 'def func()' para definir sua função
"""

def func(*args,**kwargs):
    for var in args:
        print(var)
    for nome, valor in kwargs.items():
        print(valor)

func(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)

#
#15
#Implemente a classe Lampada. A classe Lâmpada recebe um booleano no seu construtor,
# Truese a lâmpada estiver ligada, False caso esteja desligada. A classe Lampada possuí os seguintes métodos:
"""
liga(): muda o estado da lâmpada para ligada

desliga(): muda o estado da lâmpada para desligada

esta_ligada(): retorna verdadeiro se a lâmpada estiver ligada, falso caso contrário

Para testar sua classe:

Ligue a Lampada

Imprima: A lâmpada está ligada? True

Desligue a Lampada

Imprima: A lâmpada ainda está ligada? False
"""
class Lampada:
    def __init__(self, ligada=False):
        self.ligada = False  

    def desliga(self):
        self.ligada = False
        self.esta_ligada()

    def liga(self):
        self.ligada = True
        self.esta_ligada()
    
    def esta_ligada(self):
        if self.ligada is True:
           return True
        else:
            return False
            

lamp1 = Lampada()

lamp1.liga()

print(f"A lâmpada está ligada? {lamp1.esta_ligada}")

lamp1.desliga()

print(f"A lâmpada ainda está ligada? {lamp1.esta_ligada}")    

#
#16
#Escreva uma função que recebe uma string de números separados por vírgula e retorne a soma de todos eles.
# Depois imprima a soma dos valores.

#A string deve ter valor  "1,3,4,6,10,76"

def soma_string(string):
    lista = string.split(",")
    lista_soma = []
    for i in lista:
        lista_soma.append(int(i))
    return sum(lista_soma)
        
print(soma_string("1,3,4,6,10,76"))

#
#17
#Escreva uma função que recebe como parâmetro uma lista e retorna 3 listas: 
# a lista recebida dividida em 3 partes iguais. Teste sua implementação com a lista abaixo
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def uma_para_tres(lista0):
    lista1 = []
    lista2 = []
    lista3 = []
    for i, j in enumerate(lista0):
        if i < len(lista0)//3:
            lista1.append(j)
        elif i < 2 * (len(lista0)//3):
            lista2.append(j)
        else:
            lista3.append(j)
    return f'{lista1} {lista2} {lista3}'

print(uma_para_tres(lista))


#
#18
#Dado o dicionário a seguir:

speed = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}

#Crie uma lista com todos os valores (não as chaves!) e 
# coloque numa lista de forma que não haja valores duplicados.

def valor_dic(dic):
    dic_valor = []
    for nome, valor in dic.items():
        dic_valor.append(valor)
    lista_valor = set(dic_valor)
    return list(lista_valor)

print(valor_dic(speed))

#
#19
#Calcule o valor mínimo, valor máximo, valor médio e a mediana da lista gerada na célula abaixo:
"""
Obs.: Lembrem-se, para calcular a mediana a lista deve estar ordenada!

import random 
# amostra aleatoriamente 50 números do intervalo 0...500
random_list = random.sample(range(500),50)

Use as variáveis abaixo para representar cada operação matemática

mediana
media
valor_minimo 
valor_maximo 
"""
import random

random_list = random.sample(range(500), 50)

def mediana(random_list):
    ordenada = sorted(random_list)
    
    if (len(ordenada) % 2) == 1:
        return ordenada[len(ordenada) // 2]
    else:
        return ((ordenada[len(ordenada)//2] - 1) + ordenada[len(ordenada) // 2]) / 2

mediana = mediana(random_list)
media = sum(random_list)/len(random_list)
valor_minimo = min(random_list)
valor_maximo = max(random_list)

print(f'Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}')


#
#20
#Imprima a lista abaixo de trás para frente.

a = [1, 0, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
for i in a[::-1]:
    b.append(i)
print(b)

#
#21
#Implemente duas classes Pato e Pardal que herdem de uma classe Passaro a 
#habilidade de voar e emitir som, porém, tanto Pato quanto Pardal devem emitir 
#sons diferentes (de maneira escrita) no console.
"""
Imprima no console exatamente assim:
Pato
Voando...
Pato emitindo som...
Quack Quack
Pardal
Voando...
Pardal emitindo som...
Piu Piu
"""
class Passaro:
    def __init__(self):
        print(type(self).__name__)
    
    def voar(self):
        print('Voando...')
    
    def emitir_som(self, som):
        print(f'{type(self).__name__} emitindo som...')
        print(som)
        

class Pato(Passaro):
    def __init__(self):
      super().__init__()
      super().voar()
      super().emitir_som('Quack Quack')

class Pardal(Passaro):
    def __init__(self):
      super().__init__()
      super().voar()
      super().emitir_som('Piu Piu')

patolino = Pato()

pard1 = Pardal()

#
#22
# Crie uma classe chamada "Pessoa" com um atributo privado "nome" (representado como "__nome")
# e um atributo público "id". Adicione duas funções à classe, uma para definir o valor de "nome" 
# e outra para obter o valor de "nome". Observe que o atributo "nome" deve ser privado 
# e acessado somente através dessas funções.
"""
Para testar seu código use:
pessoa = Pessoa(0) 
pessoa.nome = 'Fulano De Tal'
print(pessoa.nome)
"""
class Pessoa():
  def __init__(self, id):
    self.__nome = None
    self.id = id
  
  def nome(self, nome):
    self.__nome = nome
    
    
pessoa = Pessoa(0) 
pessoa.nome = 'Fulano De Tal'
print(pessoa.nome)

#
#23
#Crie uma classe  Calculo  que contenha um método que aceita dois parâmetros, X e Y,
# e retorne a soma dos dois. Nessa mesma classe, implemente um método de subtração, 
# que aceita dois parâmetros, X e Y, e retorne a subtração dos dois (resultados negativos são permitidos).
"""
Utilize os valores abaixo para testar seu exercício:
x = 4 
y = 5

imprima:
Somando: 4+5 = 9
Subtraindo: 4-5 = -1
"""

class Calculo:
    def __init__(self,x,y):
        self.x = x
        self.y = y
            
    def soma(self):
      soma = self.x + self.y
      print(f'Somando: {self.x}+{self.y} = {soma}')
    
    def subtracao(self):
      subtracao = self.x - self.y
      print(f'Subtraindo: {self.x}-{self.y} = {subtracao}')
      
x = 4 
y = 5

calc = Calculo(x,y)
calc.soma()
calc.subtracao()

#
#24
# Crie uma classe Ordenadora que contenha um atributo listaBaguncada e que contenha
# os métodos ordenacaoCrescente e ordenacaoDecrescente.

# Instancie um objeto chamado crescente dessa classe Ordenadora que tenha como 
# listaBaguncada a lista [3,4,2,1,5] e 

# instancie um outro objeto, decrescente dessa mesma classe com uma outra 
# listaBaguncada sendo [9,7,6,8].

# Para o primeiro objeto citado, use o método ordenacaoCrescente e 
# para o segundo objeto, use o método ordenacaoDecrescente.
"""
Imprima o resultado da ordenação crescente e da ordenação decresce
[1, 2, 3, 4, 5] 
[9, 8, 7, 6]
"""
class Ordenadora:
    def __init__(self, listaBaguncada):
        self.listaBaguncada = listaBaguncada
    
    def ordenacaoCrescente(self):
        self.listaCrescente = sorted(self.listaBaguncada)
        return self.listaCrescente
    
    def ordenacaoDecrescente(self):
        self.listaDecrescente = reversed(sorted(self.listaBaguncada))
        return list(self.listaDecrescente)
    
lista1 = [3,4,2,1,5]   
crescente = Ordenadora(lista1)
print(crescente.ordenacaoCrescente())

lista2 = [9,7,6,8]
decrescente = Ordenadora(lista2)
print(decrescente.ordenacaoDecrescente())

#
#25
#Crie uma classe Avião que possua os atributos modelo, velocidade_maxima, cor e capacidade.

#Defina o atributo cor de sua classe , de maneira que todas as instâncias de sua classe avião sejam da cor “azul”.

# Após isso, a partir de entradas abaixo, instancie e armazene em uma lista 3 objetos da classe Avião.

# Ao final, itere pela lista imprimindo cada um dos objetos no seguinte formato:
"""
“O avião de modelo “x” possui uma velocidade máxima de “y”, capacidade para “z” passageiros e é da cor “w”.
"""
# Sendo x, y, z e w cada um dos atributos da classe “Avião”.

class Aviao:
    def __init__(self, modelo, velocidade_maxima, capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.capacidade = capacidade
        self.cor = "azul"
        
        

Boieng = Aviao("BOIENG456", "1500 km/h", 400)
Praetor = Aviao("Embraer Praetor 600", "863km/h", 14)
Antonov = Aviao("Antonov An-2", "258 Km/h", 12)

lista = [Boieng, Praetor, Antonov]

for i in lista:
  print(f'O avião de modelo {i.modelo} possui uma velocidade máxima de {i.velocidade_maxima}, capacidade para {i.capacidade} passageiros e é da cor {i.cor}')
