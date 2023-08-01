Processamento -  Camada Trusted



A camada Trusted de um data lake corresponde àquela em que os dados encontram-se limpos e são confiáveis. É resultado da integração das diversas fontes de origem, que encontram-se na camada anterior, que chamamos de Raw.



Aqui faremos uso do Apache Spark no processo, integrando dados existentes na camada Raw Zone. O objetivo é gerar uma visão padronizada dos dados, persistida no S3,  compreendendo a Trusted Zone do data lake.  Nossos jobs Spark serão criados por meio do AWS Glue.



Todos os dados serão persistidos na Trusted no formato PARQUET, particionados por data de criação do tweet  ou data de coleta do TMDB (dt=<ano\mês\dia> exemplo: dt=2018\03\31). A exceção fica para os dados oriundos do processamento batch (CSV), que não precisam ser particionados.



Iremos separar o processamento em dois jobs: o primeiro, para carga histórica, será responsável pelo processamento dos arquivos CSV  e o segundo, para carga de dados do Twitter/TMDB. Lembre-se que suas origens serão os dados existentes na RAW Zone.




Importante:



Desenvolva os jobs no Glue utilizando a opção Spark script editor.  Após, na aba Job details, atente para as seguintes opções:



Worker type: Informe G 1x (opção de menor configuração).

Requested  number of workers: Informe 2, que é a quantidade mínima.

Job timeout (minutes): Mantenha em 60 ou menos, se possível.








Após realizar a atividade, lembre-se de finalizar qualquer execução ativa de job para não incorrer em custos desnecessários.

Perguntas dessa tarefa
Realize as atividades conforme as instruções. Neste espaço, você pode adicionar prints dos jobs criados. Contudo, lembre-se de adicionar todo código elaborado no seu repositório do Github.