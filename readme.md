# Desafio Técnico: Ecommerce
- ## Descrição
    ### O objetivo é construir uma API robusta para a gestão de produtos de um e-commerce, mas com um nível de complexidade elevado. Além de CRUD (Create, Read, Update, Delete), a API deverá fornecer recursos como filtragem avançada, paginação, relacionamento com outras entidades (como fornecedores e avaliações de clientes) e um algoritmo de recomendações de produtos.
<br>

- ## Como executar o projeto
    - #### Requisitos: Docker e Git.

````
1 - clonar o projeto
    git clone https://github.com/joaomateuus/drf-ecommerce.git

2 - Entrar no diretorio do projeto
    cd drf-ecommerce

3 - Rodar o docker build para construir a imagem da nossa api
    docker build .

4 - Subir os serviços, api e db com docker compose
    docker-compose up -d --build

5 - Rodar o migrate para criar nossas tabelas do bd
    docker-compose exec web python manage.py migrate

6 - Rodar o comando para popular a tabela de produtos e seus relacionamentos
    docker-compose exec web python manage.py runscript load
````
### Aguarde até que os contêineres sejam iniciados. Após a conclusão, você poderá acessar a aplicação no navegador:
- Aplicação Django: http://localhost:8000
<br>
<br>

## Estrutura da Aplicação
- ### Account: App que contém toda a parte de autenticação e base para lógica de controle de usuários e permissões.
    - Base url: http://localhost:8000/account/
- ### Core: App que contém as principais entidades e funções alinhadas a lógica de négocio da aplicação.
    - Base url: http://localhost:8000/api/v1/
<br>
<br>

## Autenticação
### Criando um usuário
- #### Podemos criar um usuario na nossa aplicação pelo endpoint de usuários que para requisições POST é livre e também pelo cli do django.
````
POST: http://localhost:8000/account/users/
{
    {
		"id": 5,
		"email": "tiao@email.com",
		"full_name": "Tião da Silva",
		"is_superuser": false,
		"is_staff": false,
		"last_login": null
	}
}

Ou

docker-compose exec web python manage.py createsuperuser

````


### Autenticação
- #### Como solicitado a autenticação padrão é realizada por meio do oauth0, na qual podemos adquirir o access e refresh token por meio do endpoint: http://localhost:8000/o/token/
`````
client_id=ogvzCRSRP8hbpcuvTp7LeeilIcnN1qLaT8cv8O25
client_secret=QuoBkDujQm361CrRAWwVHF6hjeIqUzFg2bWs9xpRb9JHm4DjPQnG9fhkAAxmTuXZs8TRsms4S9OLP8rd47HUdtazfOmmftBqejXbPyhwhPN1qWEUsr3NwV6ElrVRYAyS

# Exemplo de como fazer a requisição do token pela ferramenta curl:
curl -X \ 
    POST http://localhost:8000/o/token/ \
        -H "content-type: application/x-www-form-urlencoded" \
        -d "grant_type=password&client_id=<your client id>\
        &client_secret=<your client secret>\
        &username=<your username>\
        &password=<your password>"

# Payload de Resposta:
{"expires_in": 36000, "refresh_token": <your refresh token>, "access_token": <your access token>, "token_type": "Bearer", "scope": "read write groups"}
`````
#### Ápos ser autenticado e recebermos os tokens e é necessario anexar o acess token ao header de cada requisição para acessar as rotas protegidas

#### Também é possível se autenticar normalmente pelo django admin, somente acessar a url de admin: http://localhost:8000/admin/ e logar com as credenciais de um usuário admin (superuser ou is_staff) que também irá ser possível acessar as rotas protegidas.

<br>

## Rotas
### Account
- #### http://localhost:8000/account/users/
    - Enpoint de usuarios
- #### http://localhost:8000/account/user_adresses/
    - Enpoint com as informações de endereço do usuário

### Core
- #### http://localhost:8000/api/v1/categories/
    - Endpoint de produto.
- #### http://localhost:8000/api/v1/sub_categories/
    - Endpoint das sub categorias de produto.
- #### http://localhost:8000/api/v1/products/
    - Endpoint de produto.
- #### http://localhost:8000/api/v1/orders/
    - Endpoint das ordems de produto.
- #### http://localhost:8000/api/v1/orders/
    - Endpoint das ordems de produto.
- #### http://localhost:8000/api/v1/order_items/
    - Endpoint dos items de cada ordem de produto.

