#### TAREFA 4



Modelagem de dados - Camada Refined





A camada Refined corresponde à camada de um data lake em que os dados estão prontos para análise e extração de insights. Sua origem corresponde aos dados da camada anterior, a Trusted.



Devemos pensar em estruturar os dados seguindo os princípios de modelagem multidimensional, a fim de permitir consultas sobre diferentes perspectivas.



Nesta etapa do desafio, devem ser criadas no AWS Glue Data Catalog  as tabelas e, se necessário, views,  de acordo com modelagem de dados solicitada, a fim de disponibilizar os dados para a ferramenta de visualização (QuickSight, a partir da próxima Sprint). Lembre-se que a origem será os dados oriundos da Trusted Zone.






Perguntas dessa tarefa
Apresentar a modelagem de dados da camada Refined. Você pode exportar seu modelo de dados na forma de imagem e registrar aqui. Lembre-se de deixá-lo disponível também no seu repositório do Github.



#### TAREFA 5


Na atividade anterior, você definiu seu modelo de dados da camada Trusted. Agora é tempo de processar os dados da camada Trusted, armazena-os na Refined, de acordo com seu modelo.



Aplicaremos novamente o Apache Spark no processo, utilizando jobs cuja origem sejam dados da camada Trusted Zone e e o destino, a camada Refined Zone.  Aqui, novamente, todos os dados serão persistidos no formato PARQUET, particionados, se necessário,  de acordo com as necessidades definidas para a camada de visualização.






Importante:



Desenvolva os jobs no Glue utilizando a opção Spark script editor. Após, na aba Job details, atente para as seguintes opções:



Worker type: Informe G 1x (opção de menor configuração).

Requested number of workers: Informe 2, que é a quantidade mínima.

Job timeout (minutes): Mantenha em 60 ou menos, se possível.








Após realizar a atividade, lembre-se de finalizar qualquer execução ativa de job para não incorrer em custos desnecessários.

Perguntas dessa tarefa
Desenvolva os jobs de processamento de acordo com as instruções. Aqui você pode apresentar prints do seu código. Lembre-se também de adicionar todo código produzido ao seu repositório no Github.