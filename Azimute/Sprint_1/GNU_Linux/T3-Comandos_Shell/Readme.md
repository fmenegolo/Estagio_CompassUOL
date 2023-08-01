MANIPULAÇÃO DE CONTEÚDOS COM COMANDOS SHELL

- Visualizadores de texto

    cat [arquivo]
        exibe todo conteudo do arquivo em texto

    more [arquivo]
        corre pagina a pagina aparece porcentagem para concluir, ele nao volta

    less [arquivo]
        ja é possivel navegar por todo o conteudo do texto oe voltar ou pesquisar linha com "/" e voltar com Shift + N

    head [arquivo]
        visualiza as primeiras linhas do arquivo (default: 10)
        flag -n [nº]
            mostra número especifico de linhas
    
    tail [arquivo]
        visualiza as ultimas linhas do arquivo ( default: 10)
        flag -n [nº]
            mostra número especifico de linhas 

        flag -f
            permanece aberto na tela e atualiza a visualização caso houver alteração
            ex.: tail -f /var/log/auth.log

- Redirecionadores

    - Entrada Padrão stdin

        “>”: Envia a saída para um arquivo ou dispositivo, porém, se o 
arquivo já existir, o seu conteúdo é sobrescrito.

        “>>”: Envia a saída para um arquivo ou dispositivo, porém, se o 
arquivo já existir, a saída do comando é ADICIONADA no final do arquivo 
especificado.

    - Saida padrão stdout

        “<”: Faz com que determinado comando receba algo como entrada

        “<<”: Utilizado para determinar o final de um “bloco” de dados

    - Saida de erro padrão stderr

        “2>”: Envia apenas os sinais de erro para um arquivo ou dispositivo, 
porém, se o arquivo já existir, o seu conteúdo é sobrescrito.

        “2>>”: Envia apenas os sinais de erro para um arquivo ou 
dispositivo, porém, se o arquivo já existir, a saída (apenas os erros) será 
ADICIONADA no final do arquivo

     “/dev/null” é um arquivo especial que descarta toda informação enviada para ele, além de 
não retornar nenhuma informação caso seja acessado

- Concatenação de comandos

    Para realizar a concatenação, devemos utilizar dutos (duto = PIPE = | )
        “pegar” a saída de um comando e utilizá-la como “entrada” para o comando seguinte

    - Conectores e Operadores
        Ponto e vírgula “;” para execução de comandos em sequência
            não há relação entre sucesso das execuções ou não

        Operador “&&” (AND), caso o primeiro comando execute com sucesso (código de retorno = 0), o 
segundo comando também será executado

    Operador “||” (OR), caso o primeiro comando não execute com sucesso (código de retorno ≠ 0), o segundo comando será executado. RESUMINDO, quando um dos comandos for executado com sucesso, os comandos seguintes não são verificados

Filtros de conteúdo
    interceptar e filtrar conteúdo que iriam para stdout
    - $ greep <opções> [string_ou_regex] [arquivo_ou_caminho]
        - processa conteudo linha a linha e exibe as que possuir string especifica
        flag -v
            executa o inverso, ou seja as linhas que nao possuir string especificada
        flag -r 
            executa de forma recursiva, ou seja enta em cada arquid de cada diretório e subdiretório
        falg -i
            ignora o case-sensitive
    - $ dmesg
        visualizar o hardware carregado na inicialização
    - $ egreep
        permite uso de uma expresão regular (REGEX) para buscas mais elaboradas
    - $ wc
        contador de palavras (word count)
            apresenta linhas, palavras e caracteres
    - $ cut
        realiza recortes em conteúdo
            flag -d
                delimitador 
            flag -f
                campo que deseja visualizar (Field)
            flag --output-delimiter="<string_REGEX>"
                adiciona uma string no entre delimitador
    - $ tr "<string_REGEX>"
        traduz um sinal ou caracterer por outro
        flag -d deleta a string da saída
    - $ sort
        ordena em ordem alfabetica
    - $ uniq
        exibe penas uma ocorrencia no caso houver strings repetidas
    - $ nl
        enumera as saidas decada linha
    
    - $ awk -F, '{<condição>}' <nome_arquivo>
            -flag F
                indica que realizara um filto
        tambem funciona como limitador e aceita concatenação de stings e quebra de linhas na condição
    - $ sed 's/<expressão>t/<outra>/g'
        substitui uma expressão de saida por outra
            - /g atua em todas a expressões existentes
    - $ diff <arquivo_x> <arquivo_y>
        comparador de arquivos e verifica a diferença entre eles

Meta caracter
    - "^" => inicio de uma linha 


Empacotadores e Compactadores

    usado tambem em rotinas de backup

    - $ zip <opções> [caminho_do_arquivo] [arquivos_a_ser_compactados]
        compacta arquivos
        flag -r 
            atua de forma recursiva, a fim de inserir pastas e subpastas
    
    - $ unzip <arquivo>.zip
        descompacta arquivo zip
            flag -d <diretorio_destino>
                determina o destino onde será descompactado
    - $ tar <opções> [arquivo] <opções||caminho_a_ser_compactado>
        pode empacotar sem realizar compressão 
        utiliza padrão "gzip",bzip" e "compress" de empacotamento
