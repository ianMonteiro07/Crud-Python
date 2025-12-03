Gerenciador de Produtos 
Um sistema desktop simples para gerenciamento de produtos (CRUD), desenvolvido em Python utilizando a biblioteca gráfica Tkinter. Este projeto serve como um exemplo prático da implementação do padrão de arquitetura MVC (Model-View-Controller).
 Funcionalidades
O sistema permite realizar as operações fundamentais de gerenciamento de dados:

Adicionar: Cadastro de novos produtos com ID, Nome, Preço e Quantidade.

Listar: Visualização de todos os produtos cadastrados em uma tabela (Treeview).

Atualizar: Edição dos dados de um produto existente através do seu ID.

Remover: Exclusão de um produto do sistema através do seu ID.

Interface Gráfica: Uso de janelas e pop-ups (Messagebox) para feedback ao usuário.

Arquitetura do Projeto (MVC)
O código foi organizado seguindo estritamente o padrão de separação de responsabilidades:

Model (produto.py):

Representa a estrutura de dados (Objeto Produto).

Contém os atributos (id, nome, preco, quantidade) e métodos de acesso (Getters e Setters).

View (produtoView.py):

Responsável pela Interface Gráfica (GUI) com o usuário.

Gerencia janelas, botões, campos de entrada e a tabela de exibição.

Não contém lógica de negócio, apenas repassa as ações do usuário para o Controller.

Controller (produtoController.py):

Intermediário entre a View e o Model.

Gerencia a lista de produtos em memória.

Executa a lógica de adicionar, buscar, atualizar e remover itens da lista.

 Estrutura de Arquivos
Plaintext

projeto-produto/
│
├──  main.py              # Ponto de entrada da aplicação (Instancia o Controller e a View)
├── produto.py           # Definição da classe Produto (Model)
├── produtoController.py # Lógica de controle e manipulação da lista (Controller)
└── produtoView.py       # Interface gráfica Tkinter (View)
Pré-requisitos
Python 3.x instalado.

A biblioteca tkinter (geralmente já vem instalada por padrão com o Python).

Como Executar
Clone este repositório ou baixe os arquivos.

Certifique-se de que todos os arquivos (main.py, produto.py, produtoController.py, produtoView.py) estejam na mesma pasta.

Abra o terminal/cmd na pasta do projeto.

Execute o arquivo principal:

Cole

python main.py
Exemplo de Uso
Inserir: Digite 1 no ID, Teclado no Nome, 150.00 no Preço e 10 na Quantidade. Clique em Adicionar.

Visualizar: Clique em Listar para ver o produto na tabela.

Editar: Para alterar o preço do Teclado, preencha o ID 1, o Nome Teclado, o novo Preço 120.00 e a Quantidade 10. Clique em Atualizar.

Excluir: Digite apenas o ID 1 e clique em Remover.
