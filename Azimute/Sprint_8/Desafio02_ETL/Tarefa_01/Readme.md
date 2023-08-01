# Tarefa 01: Exercicio TMDB

Nesta atividades iremos criar um processo de extração de dados da API do TMDB utilizando serviços da AWS.

## Instruções da tarefa
240 minutos para concluir


Uma API (Application Programming Interface) é um conjunto de regras, protocolos e ferramentas que permitem que diferentes sistemas de software se comuniquem e troquem informações de forma eficiente e padronizada.



Em outras palavras, uma API é uma interface que permite que desenvolvedores de software acessem dados ou funcionalidades de um sistema ou aplicativo sem precisar conhecer todos os detalhes internos do sistema. Deste modo, a API fornece uma maneira de acessar esses recursos de forma programática, geralmente usando requisições HTTP (Hypertext Transfer Protocol) para recuperar e/ou enviar dados.



A API TMDB é uma API RESTful, o que significa que os dados são acessados através de URLs que correspondem a recursos específicos. Os desenvolvedores podem acessar informações de busca, detalhes de filmes e programas de TV, imagens e informações relacionadas a gêneros e classificações.



Para saber mais sobre a API do The Movie Database, visite o site oficial (https://www.themoviedb.org/documentation/api)  e verifique os termos de uso (https://www.themoviedb.org/documentation/api/terms-of-use) .



Para a realização das atividades é de grande importância que você faça a leitura da documentação disponível em https://developers.themoviedb.org/3/movies/get-movie-details .



Esta atividade corresponde a um laboratório. Não esperamos que você registre resposta neste espaço. Contudo, deves adicionar o código-fonte produzido ao seu repositório no Github. Lembre-se de remover suas credenciais de acesso antes de efetuar commit.

Perguntas dessa tarefa
Etapa 1 -  Criando sua conta no TMDB



Será preciso criar uma conta no porta do TMDB para, após, solicitar as chaves de acesso para uso da API.



Os passos são:



- Acessar o portal pelo link https://www.themoviedb.org/

- Clique no botão Junte-se ao TMDB na barra de navegação no topo da página

- Preencha o formulário de inscrição com as informações solicitadas e clique em Registrar. Utilize seu e-mail pessoal neste passo.

-  Você irá receber um e-mail de confirmação. Siga o processo solicitado

- Faça login em sua nova conta no TMDB e vá para o seu perfil, clicando no ícone de usuário no canto superior direito da página

- Clique na guia  Visão geral, opção Editar Perfil

- Clique no menu API, à esquerda. A seguir, na opção Criar, escolhendo o tipo Developer

- Aceite os termos e preencha o formulário com as informações solicitadas sobre a aplicação.

----- Em Tipo de Uso, informe Pessoal

----- Em URL, você pode informar um endereço fictício.

----- No Resumo, informe que o objetivo é para estudos


### Etapa 2 - Testando rapidamente as credenciais e a biblioteca


Uma vez que você tenha sua chave de API, você pode fazer solicitações à API usando a seguinte estrutura de URL:

https://api.themoviedb.org/3/{endpoint}?api_key={sua_chave_de_api}&{parâmetros_opcionais}



Onde {endpoint} é o recurso que você deseja acessar (por exemplo, movie/{movie_id} para obter detalhes de um filme específico) e {parâmetros_opcionais} são quaisquer parâmetros adicionais que você deseje incluir na solicitação (por exemplo, language=pt-BR para obter informações em português).



Abaixo exemplo de código Python



import requests
import pandas as pd

from IPython.display import display



api_key = "SUA CHAVE"

url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&language=pt-BR"



response = requests.get(url)
data = response.json()



filmes = []



for movie in data['results']:
df = {'Titulo': movie['title'],
'Data de lançamento': movie['release_date'],
'Visão geral': movie['overview'],
'Votos': movie['vote_count'],
'Média de votos:': movie['vote_average']}



filmes.append(df)



df = pd.DataFrame(filmes)
display(df)