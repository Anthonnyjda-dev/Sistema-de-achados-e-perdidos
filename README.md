# Sistema de Achados e Perdidos

Este é um projeto de laboratório de programação desenvolvido em Python. A aplicação funciona em terminal e tem como finalidade principal cadastrar, pesquisar e registrar a devolução de objetos perdidos ou encontrados.

## 🚀 Funcionalidades

*   **Gestão de Cadastros:** Permite cadastrar, listar, atualizar e remover registros de objetos.
*   **Códigos Únicos:** O sistema gera automaticamente um código único para cada objeto registrado, que nunca se repete.
*   **Controle de Status:** Objetos perdidos iniciam com o status "Procurando", objetos encontrados iniciam como "Disponível", e após a entrega, passam para "Devolvido".
*   **Pesquisas Inteligentes:** É possível localizar itens por código, nome (com busca parcial e sem diferenciar maiúsculas de minúsculas), categoria, local, tipo e status.
*   **Sistema de Devolução:** Registra o nome de quem recebeu o objeto e a data exata da devolução, impedindo a entrega em duplicidade.
*   **Relatórios e Ordenação:** Exibe estatísticas gerais de itens e permite ordenar os objetos por nome, data, categoria, local ou status.

## 📂 Estrutura do Projeto

O sistema foi modularizado para separar as responsabilidades de cada parte do código:

*   `main.py`: Ponto de entrada do sistema, contendo o menu principal interativo e a integração de todos os módulos.
*   `objetos.py`: Módulo responsável pela geração de códigos, cadastro, listagem, atualização e remoção dos itens.
*   `buscas.py`: Concentra todas as lógicas de pesquisa de objetos.
*   `devolucoes.py`: Gerencia a alteração de status e os registros de entrega.
*   `relatorios.py`: Lida com a ordenação dos dados e a geração de estatísticas por categorias.
*   `validacoes.py`: Centraliza o tratamento de entradas de dados, validando textos, números e datas para evitar que o programa encerre inesperadamente.

## 🛠️ Tecnologias e Estruturas Utilizadas

Para a construção deste sistema, foram aplicados diversos conceitos fundamentais da linguagem Python:

*   **Estruturas de Dados:** Uso intensivo de Listas para armazenar objetos, Dicionários para representar os dados de cada item, e Tuplas (utilizadas para representar as datas no formato dia, mês e ano e categorias disponíveis).
*   **Controle de Fluxo:** Utilização de laços `while` para manter o menu ativo, `for` para percorrer os registros, além de `if` e `match/case` para o direcionamento das opções.
*   **Tratamento de Exceções:** Uso de `try/except` para impedir que entradas inválidas quebrem a execução da aplicação.

## 💻 Como Executar

1.  Certifique-se de ter o Python instalado em sua máquina.
2.  Clone este repositório ou baixe os arquivos da pasta do projeto.
3.  Abra o terminal, navegue até o diretório do projeto e execute o arquivo principal:
    ```bash
    python main.py
    ```

## 👥 Equipe e Prazos

*   **Desenvolvedores:** Projeto construído por um grupo de 3 integrantes, com divisão individual de tarefas.
*   **Prazo final de entrega:** 08/10/2026.