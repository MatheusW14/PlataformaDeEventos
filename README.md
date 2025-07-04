# Agenda de Eventos

Um sistema web completo para gerenciamento e visualização de eventos, desenvolvido com Python, Flask e MySQL.

## 🚀 Sobre o Projeto

Este projeto é uma aplicação web full-stack que permite a criação, visualização, edição e exclusão (CRUD) de eventos. A plataforma possui um sistema de autenticação de usuários para garantir que apenas pessoas autorizadas possam modificar o conteúdo, além de uma interface moderna e responsiva para a visualização dos eventos.

## ✨ Funcionalidades

- **Visualização de Eventos:** A página inicial exibe todos os eventos cadastrados em um layout de cards moderno.
- **Gerenciamento de Eventos:**
  - **Criar:** Adicionar novos eventos com nome, data, tema, descrição e uma imagem de capa.
  - **Editar:** Atualizar as informações de um evento existente.
  - **Deletar:** Remover um evento do catálogo.
- **Autenticação de Usuários:** Sistema de login seguro para proteger as rotas de criação, edição e exclusão.
- **Upload de Imagens:** Funcionalidade para associar uma imagem de capa a cada evento, com pré-visualização no formulário.
- **Interface Responsiva:** O design se adapta a diferentes tamanhos de tela, desde desktops até celulares, graças ao uso do framework Bootstrap.

## 🛠️ Tecnologias Utilizadas

### Back-end:
- Python
- Flask
- SQLAlchemy (ORM)
- Flask-Bcrypt (Criptografia de senhas)
- WTForms (Formulários e validações)
- MySQL

### Front-end:
- HTML5
- CSS3
- Bootstrap
- JavaScript

## ⚙️ Configuração e Instalação

### 1. Pré-requisitos:

- Python 3 instalado.
- MySQL Server instalado e rodando.

### 2. Clone o Repositório:

```bash
git clone https://github.com/MatheusW14/PlataformaDeEventos.git
cd PlataformaDeEventos
```

### 3. Instale as Dependências:

Crie um ambiente virtual (recomendado) e instale as bibliotecas necessárias.

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar o ambiente virtual
# No Windows:
venv\Scripts\activate
# No macOS/Linux:
source venv/bin/activate

# Instalar as dependências
pip install Flask Flask-SQLAlchemy Flask-WTF Flask-Bcrypt mysql-connector-python
```

### 4. Configure o Banco de Dados:

Abra os arquivos `config.py` e `prepara_banco.py` e altere o usuário e a senha do banco de dados conforme suas credenciais do MySQL.

```python
# Exemplo em config.py
SQLALCHEMY_DATABASE_URI = "...usuario='seu_user', senha='sua_senha'..."
```

### 5. Crie e Popule o Banco de Dados:

Execute o script `prepara_banco.py` para criar o banco de dados `lista_eventos` e as tabelas `eventos` e `usuarios`.

```bash
python prepara_banco.py
```

**Credenciais padrão de usuário para teste:**

- Usuário: BD | Senha: alohomora
- Usuário: Beto | Senha: algoritmo
- Usuário: Matheus | Senha: aluno

### 6. Rode a Aplicação:

```bash
flask run
```

Acesse a aplicação no seu navegador em `http://127.0.0.1:5000`.

## 🗂️ Estrutura do Projeto

```
/
├── lista_eventos.py    # Arquivo principal que inicializa a aplicação Flask
├── config.py           # Configurações da aplicação (banco, chave secreta)
├── models.py           # Modelos de dados do SQLAlchemy (Eventos, Usuarios)
├── helpers.py          # Funções auxiliares e classes de formulários (WTForms)
├── prepara_banco.py    # Script para inicializar o banco de dados
├── views_eventos.py    # Rotas relacionadas ao CRUD de eventos
├── views_user.py       # Rotas de autenticação de usuário
├── static/             # Arquivos estáticos
│   ├── css/            # Folhas de estilo
│   └── js/             # Scripts JavaScript
└── templates/          # Arquivos HTML (Jinja2)
    ├── template.html   # Layout base
    ├── lista.html      # Página principal com a lista de eventos
    ├── login.html      # Página de login
    ├── novo.html       # Formulário para criar novo evento
    └── editar.html     # Formulário para editar evento
```

---

Desenvolvido com 💻 por Matheus C.
