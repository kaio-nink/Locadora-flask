from flask import Flask, render_template, request, redirect, url_for

from database import dbConnect


app = Flask(__name__)


# @app.route('/')
# def index():
#   conn = dbConnect()
#   if (conn == None):
#     return "<h1>Deu erro</h1>"
#   return "<h1>Deu certo</h1>"
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/client')
def client():
  dbConn = dbConnect()
  if (dbConn == None):
    return "<h1>Erro ao conectar com o BD</h1>"

  cursor = dbConn.cursor()
  cursor.execute(("SELECT * FROM Cliente"))
  data = cursor.fetchall()
  cursor.close()
  dbConn.close()

  return render_template('client.html', data=data)

@app.route('/registerClient', methods=['POST'])
def registerClient():
  dbConn = dbConnect()
  if (dbConn == None):
    return "<h1>Erro ao cadastrar cliente</h1>"

  name = request.form['nome']
  phone = request.form['telefone']

  cursor = dbConn.cursor()
  cursor.callproc('cadastrarCliente', (name, phone))
  dbConn.commit()

  cursor.close()
  dbConn.close()
  
  return redirect(url_for('client'))

@app.route('/cars')
def cars():
  return render_template('cars.html')

@app.route('/registerCar', methods=['POST'])
def registerCar():
  dbConn = dbConnect()
  if (dbConn == None):
    return "<h1>Erro ao cadastrar cliente</h1>"

  brand = request.form['marca']
  model = request.form['modelo']
  year = request.form['ano']
  type = request.form['tipo']

  cursor = dbConn.cursor()
  cursor.callproc('cadastrarCarro', (type, model, brand, year, True))
  dbConn.commit()
  
  cursor.close()
  dbConn.close()
  
  return redirect(url_for('client'))

@app.route('/test')
def test():
  return render_template('test.html')