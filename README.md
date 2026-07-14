# Sistema de Gestão para Assistência Técnica

Sistema web desenvolvido para facilitar o gerenciamento de uma assistência técnica de celulares, notebooks e equipamentos eletrônicos.

O projeto permite cadastrar clientes, aparelhos, peças e ordens de serviço, ajudando no controle dos atendimentos e no acompanhamento de cada reparo.

## Funcionalidades

* Cadastro de clientes
* Cadastro de aparelhos
* Criação de ordens de serviço
* Registro do defeito informado pelo cliente
* Controle do status do reparo
* Registro de peças utilizadas
* Controle de valores do serviço
* Consulta do histórico de atendimentos
* Área administrativa para gerenciamento dos dados

## Tecnologias utilizadas

* Python
* Django
* HTML
* CSS
* JavaScript
* Bootstrap
* SQLite

## Status do projeto

🚧 Projeto em desenvolvimento.

Funcionalidades que ainda serão adicionadas:

* Login de usuários
* Controle de estoque
* Geração de orçamento
* Impressão da ordem de serviço
* Envio de atualizações pelo WhatsApp
* Dashboard com indicadores
* Cadastro de empresas
* Separação dos dados por assistência técnica

## Como executar o projeto

### 1. Clone o repositório

```bash
git clone LINK_DO_SEU_REPOSITORIO
```

### 2. Entre na pasta do projeto

```bash
cd nome-do-projeto
```

### 3. Crie um ambiente virtual

```bash
python -m venv venv
```

### 4. Ative o ambiente virtual

No Windows:

```bash
venv\Scripts\activate
```

No Linux, macOS ou GitHub Codespaces:

```bash
source venv/bin/activate
```

### 5. Instale as dependências

```bash
pip install -r requirements.txt
```

### 6. Execute as migrações

```bash
python manage.py migrate
```

### 7. Inicie o servidor

```bash
python manage.py runserver
```

Acesse no navegador:

```text
http://127.0.0.1:8000/
```

## Objetivo do projeto

Este projeto foi criado com o objetivo de praticar desenvolvimento web com Python e Django e, futuramente, transformar o sistema em uma solução SaaS para pequenas assistências técnicas.

## Aprendizados

Durante o desenvolvimento deste projeto, estou praticando:

* Criação de models no Django
* Relacionamento entre tabelas
* Criação de views e URLs
* Templates com HTML
* Formulários e requisições POST
* Django Admin
* Banco de dados
* Git e GitHub

## Autor

**Cristian Lucas Santos Moura**

* GitHub: [Cristian-luc](https://github.com/Cristian-luc)
* LinkedIn: [Cristian Lucas](https://www.linkedin.com/in/cristian-lucas-110420ba)

## Licença

Este projeto foi desenvolvido para fins de estudo e portfólio.

