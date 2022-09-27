from crypt import methods
from tkinter.messagebox import NO
from flask import Flask, render_template, request
import mysql.connector
from mysql.connector import errorcode
import sys

app = Flask(__name__) #Cria uma instancia do gateway

#criar conexão com bd
def get_db_con():
    try:
        con = mysql.connector.connect(user="harison", password="12345", host="localhost", database="mercado")
        print("CONEXÃ ESTABELECIDA !",file=sys.stdout)
        return con
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_CHANGE_USER_ERROR:
            print("Usuário ou senha invalida !", file=sys.stdout)
            return None
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            print("BD não encontrado !", file=sys.stdout)
            return None

# @app.route() é a forma que o flask mapea  URL de requisições HTTP para funções
@app.route('/')
def index():
    return render_template('base.html')

@app.route('/form_cad_cli')
def getFormCadastroCliente():
    return render_template('form_cad_cli.html')


@app.route('/cadastrar_cliente', methods=['POST'])
def cadstrarCliente():
    con = get_db_con()
    if con == None:
        return "<h1>DEU MERDA</h1>"
    else:
        cur = con.cursor()
        sql = "insert into cliente(id_cliente, nome, cpf) values(%s, %s, %s)"
        id_cliente =  int(request.form['id'])
        nome = request.form['nome']
        cpf = request.form['cpf']

        cur.execute(sql, (id_cliente, nome, cpf))
        con.commit()
        cur.close()
        con.close()
        return "<h1>CADASTRO FEITO COM SUCESSO !!</h1>"

@app.route('/form_cad_prod')
def getFormCadastroProduto():
    return render_template('form_cad_prod.html')

@app.route('/cadastrar_produto', methods=['POST'])
def cadstrarProduto():
    con = get_db_con()
    if con == None:
        return "<h1>DEU MERDA</h1>"
    else:
        cur = con.cursor()
        sql = "insert into produto(id_produto, nome, preco_unitario, qtd) values(%s, %s, %s, %s)"
        id_produto =  int(request.form['id'])
        nome = request.form['nome']
        preco_unitario = float(request.form['preco_unitario'])
        qtd = int(request.form['qtd'])

        cur.execute(sql, (id_produto, nome, preco_unitario, qtd))
        con.commit()
        cur.close()
        con.close()
        return "<h1>CADASTRO FEITO COM SUCESSO !!</h1>"
