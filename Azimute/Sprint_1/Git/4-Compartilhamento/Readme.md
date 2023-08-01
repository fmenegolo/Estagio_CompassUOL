COMPARTILHAMENTO E ATUALIZAÇÃO

- Encontrando branches (remotos)
    git fetch
        flag -a (todos)
    você é atualizado de todas as branches e tags enviados por outros devs

- Recebendo alterações
    git pull
        cada branch pode ser atualizado
        antes de inicia e boa pratica realiza-lo

- Enviando alterações
    primeiro dev
        realiza uma tarefa em uma branch via checkout
        commitar
        git push
    
    segundo dev 
        repete os passos anteriores

    terceiro dev verifica que foi adicionado duas branches
        realiza git merge
            git merge origin/<nome_branch_dev1>
            git merge origin/<nome_branch_dev2>
            git push
            testar o site com ambas altrações

- Utilizando o remote
    git remote -v
        verificar as origin's
    git remote rm origin
        remover origin
    adicionando repo remoto ao git
        git remote add origin <link>

- Trabalhando com submódulos
    funciona como um repositorio dentro de outro
    git submodule add <repo>
    verificar submodulos
        git submodule
    Adicionar submodulo
        git submodule add <link> <nome_nova_subpasta_destinataria>
            
- Atualizando submódulo
    Sempre lembrar de commitar as mudanças antes
    para enviar para repo do submodulo
        git push --recurse-submodules=on-demand