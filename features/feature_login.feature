# language: pt

Funcionalidade: Login Swag Labs

    Esquema do Cenário: Login bem sucedido

        Dado que esteja na página de login
        Quando preencher "<email>" e "<senha>" corretos
        E clicar no botão de login
        Então deve ser mostrado uma lista de produtos

        Exemplos:
            | email          | senha          |
            | standard_user  | secret_sauce   |
            | problem_user   | secret_sauce   |
