# language: pt

Funcionalidade: Produtos Magazine Luiza

    Esquema do Cenário: Exibir resultados corretos para a pesquisa de produto

        Dado que esteja na página inicial da Magalu
        Quando preencher "<produto>" na barra de pesquisa
        E clicar para pesquisar
        Então deve ser exibida uma lista com "<produto>" de acordo com a pesquisa

        Exemplos:
            | produto     |
            | relógio     |
            # | geladeiras  |
