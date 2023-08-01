ADMINISTRAÇÃO DO REPOSITÓRIO

*- Limpando arquivos untracked
    para arquivos que são gerados automaticamente
        Ou todos que você não utilizou git add
    git clean
        flag -f
            forçar ação

- Otimizando o repositório (garbage collector)
    git gc
        Ele identifica arquivos que não são mais necessários e os exclui
        Pode melhorar a performace

- Chegando integridade de arquivos (File System ChecK)
    git fsck
        Verifica possíveis corrupções em arquivos

- Reflog
    git reflog 
        mapeia todas as mudanças do repo
    da para avanças e retroceder atraves do hash do reflof pelo git reset
        
- Recuperando arquivos com reflog
    git reset --hard <hash>
        da para avanças e retroceder através do hash do reflof pelo git reset
    git stash
    *Lembrando: o reflog expira com o tempo! (default: 30 dias)

- Transformando o repo para arquivo
    git archive --format zip --output <main>_files.zip <main>
        salva arquivo .zip da branch especifica