import mysql.connector
from mysql.connector import errorcode

try:
    con = mysql.connector.connect(user='harison', password='12345', host='localhost', database='mercado')
    print("CONEXÃO ESTABELECIDA !!")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_CHANGE_USER_ERROR:
        print("Usuário ou senha invalida !")
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        print("BD não encontrado !")
    
cur = con.cursor()

#chama o procedimento armazenado
resultado = cur.callproc('addCliente', [2234, 'sogro do bill', '24561'])
con.commit()
print(resultado)
con.close()