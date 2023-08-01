COMANDOS BÁSICOS


- select
    Selecionar colunas de tabelas
        select qual_coluna 
        from nome_do_squema.nome_da_tabela

    -- Ex. 1 => Seleção de uma única coluna

        select email 
        from sales.customers

    -- Ex. 2  => Seleção de mais de uma única coluna

        select email, first_name
        from sales.customers

    --Ex. 3 => todas as colunas
        -- "*" coringa representa todos os dados contidos

        select *
        from sales.customers


- distinct
    remover linhas duplicadas
        select distinct qual_coluna 
        from nome_do_squema.nome_da_tabela
    
    -- Ex. 1 comparar tabela com e sem distinct

        select brand
        from sales.products
        -- total 333 linhas

        select distinct brand
        from sales.products
        -- total 40 linhas

    -- Ex. 2 seleção mais de uma coluna com distinct
        -- neste caso ira mostras todas as combinações distintas

        select distinct brand, model_year
        from sales.products
        -- total 184 linhas

- where
    filtra a tabela de acordo com a condição estipulada
        select qual_coluna 
        from nome_do_squema.nome_da_tabela
        where condição_for_verdadeira

    -- Ex. 1 filtro de condição unica

        select email, state 
        from sales.customers
        where state = 'SC' -- Case Sensitive -- String usa aspas simples

        -- verificando informações da coluna
        select distinct state
        from sales.customers

    -- Ex. 2 filtro mais de uma condição

        select email, state 
        from sales.customers
        where state = 'SC' or state = 'MS' --aceita uso operadores logicos

    -- Ex. 3 filtro de uma condição com data

        select email, state, birth_date
        from sales.customers
        where (state = 'SC' or state = 'MS') and birth_date < '1991-12-28' 
            -- aceita tambem data sem separação por hífem

        -- verificando informações da coluna	
        select distinct birth_date
        from sales.customers

- order by
    Ordenar seleção confome definido
        select qual_coluna 
        from nome_do_squema.nome_da_tabela
        where condição_for_verdadeira
        order by coluna_a_ser_ordenada
    
    -- Ex. 1 ordenação valores numericos

	    select *
	    from sales.products
	    order by price desc -- desc = ordem decrescente
	

    -- Ex. 2 ordenação de texto
        -- crescente seguem ordem alfabetica
        select distinct state 
        from sales.customers
        order by state

- limit
    limita o numer ode linhas exibido na consulta
        select qual_coluna 
        from nome_do_squema.nome_da_tabela
        where condição_for_verdadeira
        order by coluna_a_ser_ordenada
        limit numero_de_linhas

    -- Ex. 1 seleção simples das N primeiras linas

        select *
        from sales.funnel
        limit 10 -- desc = ordem decrescente
	

-- Ex. 2 seleção limit e orderby
   
	select * 
	from sales.products
	order by price desc
	limit 10

- DESAFIO

    -- EXERCÍCIOS ######################################################################

        -- (Exercício 1) Selecione os nomes de cidade distintas que existem no estado de
        -- Minas Gerais em ordem alfabética (dados da tabela sales.customers)
            
            select distinct city, state
            from sales.customers
            where state = 'MG' 

            select distinct state
            from sales.customers

        -- (Exercício 2) Selecione o visit_id das 10 compras mais recentes efetuadas
        -- (dados da tabela sales.funnel)

            select paid_date, visit_id
            from sales.funnel
            where paid_date > '1-1-1' 
            order by paid_date desc
            limit 10


            select *
            from sales.funnel


        -- (Exercício 3) Selecione todos os dados dos 10 clientes com maior score nascidos
        -- após 01/01/2000 (dados da tabela sales.customers)


            select first_name, score
            from sales.customers
            where birth_date > '2000-01-01' 
            order by score desc
            limit 10


            select birth_date
            from sales.customers

End