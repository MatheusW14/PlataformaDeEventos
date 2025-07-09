import mysql.connector
from mysql.connector import errorcode
from flask_bcrypt import generate_password_hash

print("Conectando...")
try:
    conn = mysql.connector.connect(host="localhost", user="root", password="admin")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Existe algo errado no nome de usuário ou senha")
    else:
        print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `jogoteca`;")
cursor.execute("CREATE DATABASE `jogoteca`;")
cursor.execute("USE `jogoteca`;")


TABLES = {}

TABLES["Eventos"] = (
    """
    CREATE TABLE `eventos` (
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `nome` varchar(50) NOT NULL,
        `data` date NOT NULL,
        `tema` varchar(40) NOT NULL,
        `descricao` varchar(200) NOT NULL,
        PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
    """
)

TABLES["Usuarios"] = (
    """
    CREATE TABLE `usuarios` (
        `nome` varchar(20) NOT NULL,
        `nickname` varchar(20) NOT NULL,
        `senha` varchar(100) NOT NULL,
        PRIMARY KEY (`nickname`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
    """
)

TABLES["Participantes"] = (
    """
    CREATE TABLE `participantes` (
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `nome` varchar(100) NOT NULL,
        `evento_id` int(11) NOT NULL,
        PRIMARY KEY (`id`),
        FOREIGN KEY (`evento_id`) REFERENCES `eventos` (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
    """
)


for tabela_nome in TABLES:
    tabela_sql = TABLES[tabela_nome]
    try:
        print(f"Criando tabela {tabela_nome}:", end=" ")
        cursor.execute(tabela_sql)
        print("OK")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("Já existe.")
        else:
            print(err.msg)


usuario_sql = "INSERT INTO usuarios (nome, nickname, senha) VALUES (%s, %s, %s)"
usuarios = [
    ("Bruno Divino", "BD", generate_password_hash("alohomora").decode("utf-8")),
    ("José Roberto", "Beto", generate_password_hash("algoritmo").decode("utf-8")),
]
cursor.executemany(usuario_sql, usuarios)

conn.commit()

eventos_sql = (
    "INSERT INTO eventos (nome, data, tema, descricao) VALUES (%s, %s, %s, %s)"
)
eventos = [
    (
        "Festa de Lançamento",
        "2024-10-25",
        "Tecnologia",
        "Lançamento do nosso novo produto.",
    ),
    (
        "Conferência Anual",
        "2024-11-15",
        "Negócios",
        "Encontro anual de parceiros e clientes.",
    ),
    (
        "Workshop de Python",
        "2025-01-20",
        "Educação",
        "Aprenda Python do zero com nossos especialistas.",
    ),
]
cursor.executemany(eventos_sql, eventos)

conn.commit()

cursor.close()
conn.close()

print("\nBanco de dados e tabelas criados com sucesso!")
