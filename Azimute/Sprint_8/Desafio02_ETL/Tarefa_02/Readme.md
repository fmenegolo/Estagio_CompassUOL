# Tarefa 2: Desafio Parte 2 - Ingestão de dados do Twitter e/ou _TMBD_

Compreende a captura dos tweets em tempo real com Python e/ou a captura de dados existentes na API TMBD. Os dados coletados devem ser persistidos em Amazon S3 RAW Zone, mantendo o formato da origem (JSON), agrupando-os em arquivos com, no máximo, 100 tweets cada.

## Etapa 2 - Ingestão streaming/micro batch

Neste etapa do desafio, nos iremos capturar tweets em tempo real com Python por meio da lib tweepy e/ou dados existentes na API do TMDB via AWS Lambda. Os dados coletados devem ser persistidos em Amazon S3, camada de RAW Zone, mantendo o formato da origem (JSON) e agrupando-os em arquivos com, no máximo, 100 tweets cada.




Esta atividade corresponde a parte do desafio final. Não esperamos que você registre resposta neste espaço. Contudo, deves adicionar o código-fonte produzido ao seu repositório no Github. Lembre-se de remover suas credenciais de acesso antes de efetuar commit.

Perguntas dessa tarefa
Em sua conta AWS, no serviço AWS Lambda, realize as seguintes atividades:



1.  Criar nova camada (layer) no AWS Lambda para as libs necessárias à ingestão de dados (por exemplo,  tweepy, se você utilizar o Tweeter)



2. Implementar o código Python em AWS Lambda para consumo de dados do Twitter/TMDB:

   - Se está utilizando Twitter, buscar os tweets de interesse para a análise (neste ponto você já deve ter definido qual análise planeja realizar com os dados) e agrupar os tweets em arquivo JSON com, no máximo, 100 registros cada

   - Se está utilizando TMDB,  buscar pela API os dados que complementem a análise

   - Utilizar a lib boto3 para gravar os dados no AWS S3

    -----| no momento da gravação dos dados deve-se considerar o padrão de path: <nome do bucket>\<camada de armazenamento>\<origem do dado>\<formato do dado>\<especificação do dado>\<data de processamento separada por ano\mes\dia>\<arquivo>

              São exemplos de caminhos de arquivos válidos:

               - S3:\\data-lake-do-fulano\Raw\Twitter\JSON\2022\05\02\prt-uty-nfd.json

               - S3:\\data-lake-do-fulano\Raw\Twitter\JSON\2022\05\02\idf-uet-wqt.json



3. Caso esteja utilizando o Twitter, execute a função Lambda periodicamente para alimentar seu conjunto de dados no S3.



### Informação adicional:


Podemos utilizar os serviços  CloudWatch Event ou Amazon EventBridge para agendar extrações periódicas de dados no Twitter de forma automática.