INTRODUÇÃO AO SHELL E COMANDOS BÁSICOS

O Shell
    é o interpretador de comandos do Linux

comandos
    Encerrar um terminal
        - exit
        - logout
        - CTRL + D

    Reiniciar o sistema
        - reboot 
        - init 6
        - CTRL + ALT + DEL (reinicia)

    Desligar sistema
        - shutdown -h now
        - init 0
        - halt
        - poweroff
    
    orientação/ajuda
        Exibe um manual sobre um comando
            - man [comando]
            - [comando] --help
            - info [comando]
        Exibe o calendário de um mês/ano desejado
            - Cal <mês> <ano>
        Altera data e hora do sistema
            -  date <mês><dia><hora><ano>
    
    Navegação
        Lista o conteúdo de um diretório
            -  ls <opção> <argumento/caminho>
        Alterna entre diretórios
            - cd [diretório_desejado]
    
    Manipulação de arquivos e diretórios
        Cria um novo diretório
            - mkdir [nome_do_diretório]
                - flag -p
                    cria também subdiretórios
                - criar multiplos diretorios com nomes semelhantes
                    mkdir <nome_para_diretorio>{02,03,04}
        Apagar diretórios vazios
            - rmdir [diretório]
        Apaga arquivos ou diretórios com conteúdo
            - rm [arquivo]
                - flag -rf 
                    exclusao de modo Recursivo e Forçado
        Move ou renomeia arquivos
            - mv [origem] [destino]
        Copia arquivos e diretórios
            - cp <opção> [origem] [destino]
                - flag -r
                    copia o diretorio de modo Recursivo
        Cria arquivos de texto puro
            - touch [nome_do_arquivo]
                - flag -t
                    Timestamp determina a data de criação
        Cria Links simbólicos (atalhos)
            -  ln -s [origem] [link_destino]                
        Procura arquivos no sistema de arquivos
            - find <caminho> <opção> [nome_desejado]
        Mostra o quanto de espaço em disco que está sendo utilizado
            - du <opção> <caminho> 
                - flag -hs
                    forma sumarisada           
        Mostra a estrutura de diretórios em “árvore”
            - tree <caminho>
        altera q execução de um comando adiicionando as flags que vao ser executadas por padrão
            - Alias [comando]="[comando] --[flag]"
            
Teclas - atalhos
    Shift + PageUp = sobe pagina
    Shift + PageDown = desce pagina
    Ctrl + L = clear
    Tab = pode autocompletar determinados comando 
    Alt + F1 (ao F6) = alterna sessões em ambiente de texto
    Alt + F7 (ao F8) = alterna sessões em ambientes gráficos
    CTRL+A = mover o cursor para o início da linha
    CTRL+E = mover o cursor para o fim da linha
    CTRL+R = iniciar uma “busca” a um comando já executado
    Caractere ~ (til) = atalho para o diretório pessoal de usuário

Diretórios
    / => Raiz do sistema operacional (análogo ao “C:” de um sistema Windows).
    
    /boot => Contém arquivos necessários para a inicialização do sistema.
    
    /etc => Arquivos de configuração do sistema e de serviços de rede (pacotes) instalados (por padrão).
    
    /bin => Contém os programas/comandos básicos do sistema para uso dos usuários.
    
    /sbin => Contém os programas/comandos acessíveis pelo super usuário (root) para administração do sistema.
    
    /var => Contém os logs do sistema e dados de spool de impressora e cache.
    
    /root =>  Diretório do usuário root, o administrador do sistema.
    
    /home => Diretório que contém os subdiretórios de cada usuário (análogo ao “Users” ou o antigo “Documents and Settings”).
    
    /dev => Permite acesso aos dispositivos do sistema.
    
    /lib => Bibliotecas compartilhadas pelos programas do sistema e módulos do kernel.
    
    /proc => Sistema de arquivos do kernel. Este diretório não existe em seu disco rígido, ele é criado pelo kernel e usado por diversos programas que fazem sua leitura. Através de seu conteúdo podemos verificar configurações do sistema ou modificar o funcionamento de dispositivos através de alterações em seus arquivos (como a função de roteamento).
    
    /usr => Contém arquivos e aplicativos de usuários do sistema, “documentações” do sistema, entre outros tipos de arquivo.

Caracteristicas exibição do LS
    1ª coluna - Permissões de acesso
        R = leitura (Read)
        W = gravação (Write)
        X = execução (eXecute) 
        sendo:
            3 primeiras do usuario root (proprietario)
            3 segintes do grupo proprietario
            3 ultimas de qualquer outro usuario
    2ª coluna - inodes de cada objeto
    3ª coluna - usuario proprietario
    4ª coluna - grupo proprietario
    5ª coluna - tamanho de cada objeto
    6ª coluna - data de criação do objeto
        quando aparece a hora quer dizer que foi criado/alterado no ano corrente
    7ª coluna - o objeto
flag -h 
    human-readable
        