# Lab AWS Glue
Introdução


Processos de ETL (Extract, Transform and Load) estão presentes em todos os projetos de dados. O cenário costuma ser o mesmo: fontes de dados diversas com datasets de interesse que precisam ser ingeridos, transformados e armazenados em um ou mais destinos, com formatos diferentes da origem.

Neste laboratório você será guiado na construção de um processo de ETL simplificado utilizando o serviço AWS Glue.



## 1 - Preparando os dados de origem


Faremos uso do arquivo nomes.csv, um dataset que contém os nomes mais comuns de registro de nascimento dos cartórios americanos entre os anos de 1880 e 2014. Trata-se de um arquivos CSV, com a estrutura descrita na amostra a seguir (primeira linha representa o cabeçalho).



nome,sexo,total,ano
Jennifer,F,54336,1983


Para nosso laboratório, o arquivo deverá estar em um bucket do S3. Vamos considerar que o path do arquivo seja s3://{BUCKET}/lab-glue/input/nomes.csv. Lembre-se que o valor {BUCKET} deve ser substituído por um dos buckets disponíveis em sua conta.



## 2 - Configurando sua conta para utilizar o AWS Glue


Acesse a página inicial do serviço AWS Glue. Para que possamos utilizar o serviço com as permissões necessárias, devemos seguir o passo-a-passo disponível a partir da opção Set up roles and users no card Prepare your account for AWS Glue.




No primeiro passo devemos indicar quais roles e usuários terão acesso ao serviço AWS Glue. Procure pelo seu usuário em Choose users e o adicione à lista.






No passo seguinte, informe acesso total ao S3 para leitura e escrita.






Por fim, marque a opção Update the standard AWS Glue service role and set it as the default (recommended) e finalize o processo.






## 3 - Criando a IAM Role para os jobs do Glue


Você deve estar lembrado que Roles são credenciais temporárias assumidas por serviços e aplicações para realizar operações em favor do usuário.



Logo, criaremos uma nova role chamada AWSGlueServiceRole-Lab4, associada a policies geridas pela AWS (  AmazonS3FullAccess, AWSLakeFormationDataAdmin, AWSGlueConsoleFullAccess e CloudWatchFullAccess). Tais policies irão permitir acesso ao serviço do Glue ao S3, bem como outras ações, como executar códigos via Notebooks. Observe que estamos utilizando policies permissivas, o que vai de encontro ao princípio de privilégios mínimos que deve-se seguir em projetos reais. O objetivo aqui é apenas simplificar o processo.

Vamos aos passos:



No console, acesse a página do serviço Identity and Access Management (IAM) e clique no menu Roles à esquerda. Na sequência, clique no botão Create Role.








Na primeira etapa, Select trusted entity, escolha AWS Service e para Use Case, infome Glue. Clique em Next.






Na etapa Add permissions, pesquise por AmazonS3FullAccess e adicione. Repita o processo para as demais policies necessárias: AWSLakeFormationDataAdmin, AWSGlueConsoleFullAccess e CloudWatchFullAccess. Em seguida, clique em Next.






Na última etapa, informe em Role name o valor AWSGlueServiceRole-Lab4 e, para finalizar, clique em Create Role.



## 4 - Configurando as permissões no AWS Lake Formation


AWS Lake Formation é um serviço que facilita a criação e gerenciamento de data lakes. Nos iremos utilizá-lo para criar o banco de dados no qual nosso crawler irá adicionar automaticamente uma tabela a partir dos dados armazenados no S3.

Após acessar o serviço AWS Lake Formation no console, clique na opção Databases, no menu à esquerda. Na sequência, clique no botão Create Database. O nome do novo banco deverá ser glue-lab.

Observe que estamos criando um banco de dados no catálogo do Glue para nosso data lake. Tal banco de dados é um container para tabelas e views, cuja origem de dados pode ser diversa, como S3, RDS ou mesmo fontes de terceiros.






Agora precisamos que você adicione seu usuário IAM como administrador do data lake. Para tal, acesse a opção Administrative roles and tasks no menu à esquerda. Na tela que se apresenta, clique em Choose administrators.






Procure pelo seu usuário em IAM User and roles. Adicione-o à lista e clique em Save.






Retorne ao menu Databases, busque pelo banco glue-lab criado anteriormente. Selecione-o e vá em Actions, escolhendo a opção Grant.






Vamos conceder privilégios para a role do IAM criada anteriormente (AWSGlueServiceRole-Lab4). Para tal, escolha a opção IAM users and roles na seção Principals. Selecione a role a partir da lista apresentada.




Na seção LF-Tags or catalog resources, escolha Named data catalog resources, procurando pela base glue-lab em Databases.






E, finalmente, na seção Database permissions, em Database permissions, escolha as opções Create table, Alter, Drop e Describe. Para finalizar, clique em Grant.






## 5 - Criando novo job no AWS Glue


Para realizar o processamento do arquivo nomes.csv iremos criar um job através do serviço AWS Glue.

Após acessar a página inicial do Glue na console AWS, busque pela opção Job, no menu à esquerda.






Você perceberá que existem diferentes opções para criarmos um job. Em nosso laboratório, faremos uso  da opção Jupyter Notebook, escolhendo a alternativa Upload and edit an existing notebook. Em File Upload, procure pelo arquivo job_aws_glue_lab_4.ipynb (anexo como recurso a esta aula)






A próxima etapa será informar os dados para criar nosso notebook. Em Job Name, informe job_aws_glue_lab_4. Para Kernel, escolha Spark. Já para IAM Role, pesquise por AWSGlueServiceRole-Lab4.

Você perceberá que o notebook contém algumas células em branco. Em cada uma delas, desenvolva o código que está sendo solicitado pelo enunciado da célula imediatamente acima.

Somente avance para a próxima seção após concluir o desenvolvimento das atividades propostas no notebook.



Observe que você deverá desenvolver código Spark nas células para responder às questões propostas no laboratório. Após concluir a atividade, faça download do notebook e adicione ao seu repositório Git.



Lembre-se sempre de terminar as sessões de notebook para não incorrer em custos desnecessários. Também verifique a presença de sessões em execução, conforme explicamos na sequência.



## 5.1 - Eliminando sessões interativas


Após executar seu job, devemos nos certificar que não hajam sessões em execução ou em situação Stopping.  A forma mais rápida para isso é excluir todas as instâncias listadas.






## 6 - Criando novo crawler


Crawlers são mecanismos que podemos utilizar para monitorar nosso armazenamento de dados de modo a criar/atualizar metadados no catálogo do Glue de forma automática (diretamente em um database).

Na sequência iremos desenvolver um crawler para, automaticamente, criar uma tabela chamada frequencia_registro_nomes_eua a partir dos dados escritos no S3 (verifique a última atividade do notebook).

Vamos aos passos para criação de nosso crawler:



No console, acesse o serviço AWS Glue. Na página do serviço, escolha a opção Crawlers no menu à esquerda. Na sequência, clique no botão Create.

No primeiro passo de criação do Crawler, informe FrequenciaRegistroNomesCrawler no campo Name. Clique em Next.




Em Choose data sources and classifiers, devemos informar o caminho do S3 a ser monitorado. Para Is your data already mapped to Glue tables?, informe Not yet. E, na sequência, clique em Add a data source.






Na tela aberta, em Data source, certifique que esteja S3. Em Location of S3 data, informe In this account. Finalmente, no campo S3 path, informe o caminho s3://{BUCKET}/lab-glue/frequencia_registro_nomes_eua/, lembrando de substituir {BUCKET} pelo utilizado anteriormente.




Na etapa Configure security settings informe a role AWSGlueServiceRole-Lab4 no campo Existing IAM role. Avance clicando em Next.




Em Set output and scheduling, no campo Target database, informe glue-lab. Em Crawler schedule, no campo Frequency, defina On Demand. Avance e finalize o processo de criação.






Crawler criado, agora vamos executá-lo. Na tela inicial (Crawlers), selecione FrequenciaRegistroNomesCrawler e clique em Run. A execução pode leva alguns segundos. O status da execução estará disponível na própria tela.

Se a execução for bem sucedida, nós esperamos que uma nova tabela, de nome frequencia_registro_nomes_eua, tenha sido criada na base glue-lab. Você poderá vê-la por meio do Glue Catalog e/ou também no Athena.

Para consultar os dados via Athena, você deverá conceder privilégios de DESCRIBE e SELECT no Lake Formation. Vamos deixar essa parte como desafio para você 😁.

Recursos para esta aula