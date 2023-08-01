COMANDOS PARA GERENCIAMENTO DO SISTEMA E DO HARDWARE

- Comandos para coletar informações do sistema
    Exibe informações sobre o sistema instalado
        - $ Uname -a
            Flag "-a" (all)
        - na maioria dos casos não exibe a versão da distro
            - é possível verificar em um arquivo dentro de "/etc" via cat
    
    Exibe por quanto tempo a maquina está ligada e afins
        - $ uptime
            - veremos mais afundo em comando "top"
    
    Exibe informações da utilização da RAM e SWAP 
        - $ free -m
            Flag -m , -g ou -k => para mudar fundo de escala (exibir em Mb, Gb ou Kb)
            flag -s nº => atualizar status a cada nº em segundos
        - mais informações no arquivo "/proc/meminfo" via cat

    Informações sobre discos
        espaço livre/utilizado
            - $ df -h
                
        tamanho ocupado de arquivos ou diretórios
            - $ du -hs /etc
                flag -s => mostra tamanho total do ditetório/arquivo

        flag -h => forma inteligivel (humam readable)
    
    Informações sobre arquivos
        exibe o tipo do arquivo
            - $ file <nome_do_arquivo>

    Informações de acessos (logons)
        informações sobre os usuarios conectados seu tempo ocioso e processo em execução
            - $ w
        quais usuarios estão logados, en qual terminal, quando efetuou o logon, e seu ip caso for remoto    
            - $ who
        qual usuario logado no terminal atual
            - $ whoami       

- Configurações de rede e resumo sobre conectividade no Virtual Box
    - verificat um ip atual ou configurar um para determinado adaptador (antigo)
        - $ ifconfig <interface>
            <interface> verifica uma determiada interface 
        - $ ifconfig <interface> [X.X.X.X] netmask [Y.Y.Y.Y]
            Atribui um ip a determinada interface
    - modifica rotas ou Default Gateway
        - $ route add default gw [X.X.X.X]
        Exibe rotas existentes
            - $ route -n
    - Comandos acima são voláteis
    - comando "ip" (novo)
        - $ ip [ OPTIONS ] OBJECT { COMMAND | help }
            - $ ip addr add [X.X.X.X] dev <interface>
            Exibe rotas existentes
            - $ ip route 

- Comandos relacionados a Hardware
    exibe todo hardware carregado pela inicialização do sistema
        - $ dmesg 
    exibe info do chiset e dispositivos PCI
        - $ lspci
    exibe inf de disp. USB
        - $ lsusb
    exime módulos (drivers) carregados no sistema
        - $ lsmod
            instalar ou carregar novo módulo
                - $ insmod [arquivo] <opções>
            remover módulo
                - $ rmmod <nome_do_modulo>
    Diretório "/proc"
        - Diretório Virtual 
            - não é possivel gravar ou criar arquivos aqui
            - porém podemos visualizar o conteudo destes via cat
    Listar todos disp de armazenamento
        - $ fdisk -l
