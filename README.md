Nome do Projeto: Lista de Produtos Interativa

Descrição:
Este projeto consiste em uma aplicação web interativa para exibir uma lista de produtos. A lista de produtos é apresentada em uma interface amigável, permitindo a filtragem dos produtos com base no número ou nome do produto. A aplicação utiliza o framework Flask para o desenvolvimento do backend e o Jinja2 como mecanismo de template para renderizar as páginas HTML.

Funcionalidades Gerais:

Exibição de uma lista de produtos com informações como nome, quantidade e valor.
Barra de pesquisa que permite filtrar os produtos com base no número ou nome.
Layout responsivo que se adapta a diferentes tamanhos de tela.
Detalhes Técnicos:

Linguagem de Programação: Python
Framework Web: Flask
Mecanismo de Template: Jinja2
Bibliotecas Utilizadas:
Flask: Framework web para Python.
Flask-CORS: Extensão para permitir requisições cross-origin.
Estrutura de Pastas:
bash
Copy code
/app
  /static
    /fotos
      produto1.jpg
      produto2.jpg
      ...
  /templates
    index.html
  app.py
Instalação de Bibliotecas:
bash
Copy code
pip install Flask Flask-CORS
Como Executar o Projeto:

Certifique-se de ter o Python e o pip instalados no seu sistema.
Instale as bibliotecas necessárias executando o comando acima.
Navegue até o diretório do projeto.
Execute o arquivo app.py com o comando:
bash
Copy code
python app.py
Acesse a aplicação em um navegador no endereço http://127.0.0.1:5000/.
Observação: Este projeto é voltado para fins educacionais e pode ser expandido com recursos adicionais, como persistência de dados, autenticação de usuários, entre outros.

Jônatas Mascarenhas Lima
