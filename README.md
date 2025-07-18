# Agenda de Eventos Dinâmica

Uma plataforma web completa e interativa para gerenciamento de eventos, construída com Python e Flask. O projeto permite o cadastro de usuários, participação em eventos e gerenciamento manual de listas de participantes.

## 🚀 Sobre o Projeto

Este projeto é uma aplicação web full-stack que evoluiu de um simples catálogo para uma plataforma de eventos dinâmica. Ele permite que administradores gerenciem eventos e suas listas de participantes, enquanto usuários cadastrados podem interagir, confirmando ou cancelando sua presença. A interface foi cuidadosamente desenhada para ser moderna, intuitiva e responsiva.

## ✨ Funcionalidades

-   **CRUD Completo de Eventos:** Crie, visualize, edite e delete eventos com informações detalhadas.
-   **Sistema de Usuários Completo:**
    -   **Cadastro:** Novos usuários podem criar suas próprias contas.
    -   **Autenticação:** Sistema de login seguro para proteger as rotas administrativas.
-   **Sistema de Participação Interativo:**
    -   **Inscrição/Cancelamento:** Usuários logados podem se inscrever e cancelar sua participação nos eventos com um único clique.
    -   **Gerenciamento Manual:** Administradores podem adicionar participantes manualmente (mesmo que não sejam usuários cadastrados) através de um campo de tags moderno.
    -   **Visualização Clara:** Uma janela modal exibe a lista completa de participantes de cada evento, mantendo a interface principal limpa.
-   **Upload de Imagens:** Associe uma imagem de capa a cada evento.
-   **Interface Moderna e Responsiva:** Construída com Bootstrap, a aplicação oferece uma ótima experiência em desktops, tablets e celulares.

## 🛠️ Tecnologias Utilizadas

-   **Back-end:**
    -   ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
    -   ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
    -   **SQLAlchemy:** ORM para interação com o banco de dados.
    -   **Flask-Bcrypt:** Para criptografia de senhas.
    -   **WTForms & WTForms-SQLAlchemy:** Para criação e validação de formulários.

-   **Front-end:**
    -   ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
    -   ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
    -   ![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
    -   **Tagify.js:** Para o campo de inserção de participantes.

-   **Banco de Dados:**
    -   ![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)

## ⚙️ Configuração e Instalação

Para rodar este projeto localmente, siga os passos abaixo:

**1. Pré-requisitos:**
   -   Python 3 instalado.
   -   MySQL Server instalado e rodando.

**2. Clone o Repositório:**
   ```bash
   git clone [https://github.com/MatheusW14/PlataformaDeEventos.git](https://github.com/MatheusW14/PlataformaDeEventos.git)
   cd nome-do-repositorio

3. Instale as Dependências:
Crie um ambiente virtual (recomendado) e instale as bibliotecas necessárias.

# Criar ambiente virtual
python -m venv venv

# Ativar o ambiente virtual
# No Windows:
venv\Scripts\activate
# No macOS/Linux:
source venv/bin/activate

# Instalar as dependências
pip install Flask Flask-SQLAlchemy Flask-WTF Flask-Bcrypt mysql-connector-python WTForms-SQLAlchemy

4. Configure o Banco de Dados:

Abra os arquivos config.py e prepara_banco.py.

Altere o usuario e a senha do banco de dados para corresponder às suas credenciais do MySQL.

5. Crie e Popule o Banco de Dados:
Execute o script prepara_banco.py para criar o banco de dados e as tabelas.

python prepara_banco.py

6. Rode a Aplicação:

flask run

Acesse a aplicação no seu navegador em http://127.0.0.1:5000.

🗂️ Estrutura do Projeto
/
├── lista_eventos.py    # Arquivo principal que inicializa a aplicação Flask
├── config.py           # Configurações da aplicação (banco, chave secreta)
├── models.py           # Modelos de dados do SQLAlchemy (Eventos, Usuarios, Participantes)
├── helpers.py          # Funções auxiliares e classes de formulários (WTForms)
├── prepara_banco.py    # Script para inicializar o banco de dados
├── views_eventos.py    # Rotas relacionadas ao CRUD de eventos e participação
├── views_user.py       # Rotas de autenticação e cadastro de usuários
├── static/             # Arquivos estáticos (CSS, JS)
└── templates/          # Arquivos HTML (Jinja2)

Desenvolvido com 💻 por Matheus C. M.