Após desenvolver cada exercício localmente, realize o registro nas respectivas tarefas das respostas. Além disso, lembre-se de adicionar todo código ao seu repositório no GitHub para que o monitor(a) possa avaliá-lo posteriormente.

Perguntas dessa tarefa
1. Construa uma imagem a partir de um arquivo de instruções (Dockerfile) que execute o código carguru.py. Após, execute um container a partir da imagem criada.

Registre aqui o conteúdo de seu arquivo Dockerfile e o comando utilizado para execução do container.
 R: 
    Dockerfile:
        FROM python:3
        WORKDIR /app
        COPY . .
        CMD ["python", "carguru.py"]

    Comandos:
        >docker build . 
        >docker image ls 
        >docker run --name atv1 <ID-Image>

2. É possível reutilizar containers? Em caso positivo, apresente o comando necessário para reiniciar um dos containers parados em seu ambiente Docker? Não sendo possível reutilizar, justifique sua resposta.
    R: 
        Sim, docker start <id-ou-nome_do_container-parado_contidos-na-listagem_[docker ps -a]>

3. Agora vamos exercitar a criação de um container que permita receber inputs durante sua execução. Seguem as instruções.
-- Criar novo script Python que implementa o algoritmo a seguir:

1 - Receber uma string via input

2 - Gerar o hash  da string por meio do algoritmo SHA-1

3 - Imprimir o hash em tela, utilizando o método hexdigest

4 - Retornar ao passo 1
-- Criar uma imagem Docker chamada mascarar-dados que execute o script Python criado anteriormente

--  Iniciar um container a partir da imagem, enviando algumas palavras para mascaramento

-- Registrar o conteúdo do script Python, arquivo Dockerfile e comando de inicialização do container neste espaço.
    R:
        *Script Python:*

        import hashlib

        while True:
            string = input("Digite uma string para gerar o hash: ")
            
            gerar_hash = hashlib.sha1()
            gerar_hash.update(string.encode())
            
            imprimir_hash_hexdigest = gerar_hash.hexdigest()
            
            print(f"O hash SHA-1 da string '{string}' é: {imprimir_hash_hexdigest}")

        *Dockerfile:*

        FROM python:3
        WORKDIR /app
        COPY . .
        CMD ["python", "script.py"]

        *Comandos:*

        ❯ docker build -t mascarar-dados .
        ❯ docker run -it --name atv3 mascarar-dados  

Fazer download dos arquivos de recursos