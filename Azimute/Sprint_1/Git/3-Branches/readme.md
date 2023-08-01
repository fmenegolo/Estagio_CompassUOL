inicia a partir da branch main/master

Branch é ramificação de um projeto
    como forma de separa versões do projeto
    após finalizado as implementações, as branchs podem ser unidas (merge)
    
Facilita manutenção e diagnostico de erro ao código

- Criando e visualizando branches
    git branch <nome_da_branch>

- Deletando branches
    git branch
        flag -d ou --delete
        git branc -d <nome_da_branch>
    não é normal deletar uma branch, geralmente usado para consulta de historico
    geralmente ocorre quando ele é criado com nome errado
    
- Mudando de branch
    git checkout <nome_da_branch>
    - muda e cria o branch
        git checkout -b <nome_da_branch>
    - também é usado para dispensar mudanças de um arquivo
        git checkout <nome_do_arquivo>
    - ideal e gerar uma brant sempre da main
        lembrar de fazer pull ou comitar antes de criar branch, pois pode levar as modificações para branch nova

- Unindo branches
    git merge <nome>
        - a branche atual vai se unir ao <nome> de destino
    * Nunca de o merge nosso com a master, ela não deve ser alterada diretamente pelo git.
        salvo projeto particular.

- Stash
    git stash
    - prosseguir com outra abordagem de solução sem perder o código
        - uma forma de recomeçar sem perder o codigo (podendo recupera lo depois)
            - tipo é jogado na lixeira
            - se houve commit não é possível usar stash
             
- Recuperando stash
    - lista de stash savas
            git stash list
    - mostra as modificações da referida stash
        git stash show -p <nº>
    - aplica uma stash novamente ao branch    
            git stash apply <nº>
    
- Removendo a stash
    - Remove todas
        git stash clear
    - especifica
        git stash drop <nº>

- Utilizando tags
    um checkpoint no desenvolvimento
        git tag -a <nome> -m "msg"

- Verificando e alterando 
    git show <nome>
    - podemos trocar de tags com
        git checkout <nome>

- Enviando e compartilhando tags
    git push origin <nome>
    - quiser enviar as demais tags
        git push origin --tags