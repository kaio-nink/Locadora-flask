import mysql.connector as connector
from mysql.connector import errorcode

USER = "root"
PASSWORD = "root"
HOST = "localhost"
DATABASE = "Locadora"

def dbConnect():
  try:
    conn = connector.connect(
      user=USER,
      password=PASSWORD,
      host=HOST,
      database=DATABASE)
    return conn

  except connector.Error as err:
    print("Erro na conexão:")

    if (err.errno == errorcode.ER_ACCESS_DENIED_ERROR):
      print("Usuário ou senha incorreto(s)")

    if (err.errno == errorcode.ER_BAD_DB_ERROR):
      print("Banco de dados não encontrado")
      
    return None
