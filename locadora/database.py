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

def closeConnection(dbConnection, dbCursor):
  dbCursor.close()
  dbConnection.close()

def callProcedure(procName: str, procParams: tuple):
  dbConnection = dbConnect()
  if (dbConnection == None):
    raise Exception('Erro na conexão com o banco de dados')
  try:
    dbCursor = dbConnection.cursor()
    dbCursor.callproc(procName, procParams)
    dbConnection.commit()

    closeConnection(dbConnection, dbCursor)
  except Exception as ex:
    print(ex)
    return False
  return True
  
def executeQuery(query, queryParams = None):
  dbConnection = dbConnect()
  if (dbConnection == None):
    raise Exception('Erro na conexão com o banco de dados')
  result = None
  try:
    dbCursor = dbConnection.cursor()
    if (queryParams == None):
      dbCursor.execute(query)
    else:
      dbCursor.execute(query, queryParams)

    result = dbCursor.fetchall()

    closeConnection(dbConnection, dbCursor)
  except Exception as ex:
    print(ex)
    return False

  return result
