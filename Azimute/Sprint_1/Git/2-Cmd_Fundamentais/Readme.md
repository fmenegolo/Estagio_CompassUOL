- criando repositório
    git init

- enviar nossos repos
    touch text.txt
    git add text.txt
    git commit -m "first commit"
- adiciona origem
    git remote add origin https://github.com/FabricioMenegolo/Compasso.git
    
    git push -u origin main
            visualizar origens
            git remote -v
        remover origem
            git remote rm origin

- Verificando mudanças do projeto
    git status

- Adicionando arquivos ao projeto
    - arquivo único
        git add nomeArquivo.ext
    - diversos arquivo
        git add .

- Salvando alterações do projeto
    git commit -a -m "mensagem"
        - arquivo especifico
            commit nomeArquivo.ext -m "mensagem"
            
- Enviando código ao repo remoto    
    git push

- Recebendo as mudanças
    git pull

- Clonando repositórios via HTTPS
    git clone https://github.com/usuario/repo.git

- Removendo arquivos do repo
    git rm nomeArquivo.ext

- Histórico de alterações
    git log
    - sair
        Ctrl + C; ou
        Ctrl + Q; ou
        :q


- Renomeando ou mover arquivos
    git mv nomeArquivo.ext pasta/destino/nomeArquivo.ext
        - é possivel renomear o arquivo também
            git mv pasta/destino/nomeArquivo.ext pasta/destino/nome_novo.ext

- Desfazendo alterações
    -git checkout pasta/destino/nomeArquivo.ext

- Ignorando arquivos no projeto
    - cria um arquivo
        .gitignore
        - inserir nome do arquivo ou pasta a ser ignorado
            - para pastas
                nomeDaPasta/*

- Desfazendo todas as alterações
    git reset --hard origin/main
    - Flag --hard
        remove todas as mudanças e retorna ao estado inicial
    - origin/main
        qual vai ser sua referência
