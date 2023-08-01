# AULA 2

# definindo funções
def nome_funcao():
    #codigo a ser executado, exemplo:
    print("Esse é um teste de definição de função")

#chamar uma função
nome_funcao()
    #ao chamar uma função mesmo que sem argumentos, utilize o parenteses vazio

#atribuindo função a variavel
teste_func = nome_funcao
    #quando atribuirmos deixamos sem os parenteses
 #porem a chamar essa variaveis temo de inserir os parentesse, e os argumentos caso necessario.
teste_func()

# AULA 3
#Funções com retorno

def nome_funcao_1():
    return 'Esse é um teste de definição de função com retorno'
    # o return finaliza a função
        # ou seja oque tiver após o returns não será executado
    # podendo obter return diferentes
        # em casos de de if´s
    # dados variaveis e também multiblos valores
print(nome_funcao_1())

