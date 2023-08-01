ANÁLISES E INSPEÇÃO

- Exibindo informações
    Informaões das branchs e commits
        git show
    podendo ser tambem usado para tags
        git show <tag>

- Exibindo diferenças (branchs)
    branch atual com repo remoto
        git diff
    branch atual com outra branch especifica
        git diff <nome_da_branch>
    diferença entre arquivos
        git diff <arquivo_1> <arquivo_2>

- Log resumido
    git shortlog
        commit será unido por nome do autor
    esse comando é a nivel de projeto
        ou seja não importa em que branch estiver o resultado e o mesmo

- Utilizando o describe*
    Verifica todas as tags do nosso projeto
        git describe --tags
    flag --all
        recebemos também a referência das tags