import mysql.connector


def criar_conexao(host, usuario, senha, banco):
    try:
        return mysql.connector.connect(host=host, user=usuario, password=senha, database=banco)
    except Exception as e:
        raise e


def fechar_conexao(con):
    return con.close()
