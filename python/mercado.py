import mysql.connector
from mysql.connector import errorcode
import sys
from datetime import date

def makeConnection(usr, pswd, h, bd):
    try:
        con = mysql.connector.connect(user=usr, password=pswd, host=h, database=bd)
        print("CONEXÃO ESTABELECIDA !!")
        return con
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_CHANGE_USER_ERROR:
            print("Usuário ou senha invalida !")
            sys.exit(-1)
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            print("BD não encontrado !")
            sys.exit(-1)

def cadastrarCliente(con, id_cliente, nome, cpf):
    cur = con.cursor()
    sql = ("insert into cliente(id_cliente, nome, cpf) values(%s, %s, %s)")
    dados = (id_cliente, nome, cpf)
    cur.execute(sql, dados)
    con.commit()
    con.close()
    print("Cliente inserido com sucesso !!")


def cadastrarProduto(con, id_produto, nome, preco_unitario, qtd):
    cur = con.cursor()
    sql = ("insert into produto(id_produto, nome, preco_unitario, qtd) values(%s, %s, %s, %s)")
    dados = (id_produto, nome, preco_unitario, qtd)
    cur.execute(sql, dados)
    con.commit()
    con.close()
    print("Produto inserido com sucesso !!")

def buscaCliente(con, p_nome):
    cur = con.cursor()
    sql = "select * from cliente where nome like %s"
    dados = [p_nome+"%"]
    cur.execute(sql, dados)
    tuplas = cur.fetchall() #recuperar todas as tuplas da consulta
    cur.close()
    return tuplas

def buscaProduto(con):
    cur = con.cursor()
    sql = "select * from produto"
    cur.execute(sql)
    tuplas = cur.fetchall() #recuperar todas as tuplas da consulta
    cur.close()
    return tuplas

def cadastrarVenda(con, id_compra, id_cliente, id_produto, qtd_venda):
    p_nome = input("Nome do clliente:\n")
    clientes = buscaCliente(con, p_nome)
    for i in clientes:
        print("ID: {}, NOME: {},  CPF: {}".format(i[0], i[1], i[2]))

    print("PRODUTOS:\n")
    produtos = buscaProduto(con)
    for j in produtos:
        print("ID: {}, NOME: {}, PRECO_UNIT: {}, QTD: {}".format(j[0], j[1], j[2], j[3]))
    
    cur = con.cursor()
    sql = "update produto set qtd = qtd - %s where id_produto = %s"
    dados = (qtd_venda, id_produto)
    cur.execute(sql, dados)

    data_venda = date.today()

    sql = "insert into compras(id_compra, id_cliente, id_produto, data_venda, qtd_venda) values(%s, %s, %s, %s, %s)"
    dados = (id_compra, id_cliente, id_produto, data_venda, qtd_venda)
    cur.execute(sql, dados)
    con.commit()
    con.close()
    print("Compra feita com sucesso")


if __name__ == '__main__':
    conn = makeConnection('harison', '12345', 'localhost', 'mercado')

    while(True):
        print("*********************************")
        print("1- Cadastrar cliente\n2- Cadastrar produto\n3- Cadastrar venda\n4- Sair\n")
        print("*********************************")
        
        choice = input()

        if choice == '1':
            id_cliente = int(input("Entre com o id do cliente\n"))
            nome = input("Entre com o nome do cliente\n")
            cpf = int(input("Entre com o cpf do cliente\n"))
            cadastrarCliente(conn, id_cliente, nome, cpf)
        elif choice == '2':
            id_produto = int(input("Entre com o id do produto\n"))
            nome = input("Entre com o nome do produto\n")
            preco_unitario = float(input("Entre com o preco unitario\n"))
            qtd = int(input("Entre com a quantidade\n"))
            cadastrarProduto(conn, id_produto, nome, preco_unitario, qtd)

        elif choice == '3':
            id_compra = int(input("Entre com o id da compra\n"))
            id_cliente = int(input("Entre com o id do cliente\n"))
            id_produto = int(input("Entre com o id do produto\n"))
            qtd_venda = int(input("Entre com o qtd do produto\n"))
            cadastrarVenda(conn, id_compra, id_cliente, id_produto, qtd_venda)

        elif choice == '4':
            print("Saindo !!")
            conn.close()
            sys.exit()
        else:
            print("Opção Inválida !")

    
