from datetime import date
from flask import Flask, render_template, request, redirect, url_for

from database import callProcedure, executeQuery

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
  initialDate = request.args.get('dataInicial')
  numDays = request.args.get('numDias')

  if (initialDate == None and numDays == None):
    initialDate = date.today()
    numDays = 1

  query = ("SELECT id_veiculo, concat(marca, %s , modelo, %s, ano), categoria "
          "from Veiculo "
          "where disponivel = TRUE OR id_veiculo NOT IN ("
            "SELECT id_veiculo "
            "from Aluguel "
            "where adddate(dataInicial, numDias) >= %s)")
  params = (" ", " ", initialDate)
  vehicles = executeQuery(query, params)

  query = ("SELECT id_cliente, nome FROM Cliente")
  clients = executeQuery(query)

  if ( vehicles == False or clients == False ):
    return

  return render_template('index.html', initialDate=initialDate, numDays=numDays, vehicles=vehicles, clients=clients)

@app.route('/registerRent', methods=['POST'])
def registerRent():
  idVehicle = request.form['idVeiculo']
  idClient = request.form['idCliente']
  initalDate = request.form['dataReserva']
  numDays = request.form['diasReserva']
  params = (idClient, idVehicle, initalDate, numDays)

  result = callProcedure('cadastrarAluguel', params)
  if (not(result)):
    return

  return redirect(url_for('index'))

@app.route('/rents')
def rents():
  query = ("SELECT * FROM relatorioAluguel")
  result = executeQuery(query)
  if ( result == False ):
    return
  result = getRentValue(result)
  print(result)

  return render_template('rent.html', data=result)

@app.route('/payRent', methods=['POST'])
def payRent():
  idClient = request.form['id_cliente']
  idVehicle = request.form['id_veiculo']
  initialDate = request.form['dataInicial']
  params = (idClient, idVehicle, initialDate)
  
  result = callProcedure('pagarAluguel', params)
  if not(result):
      return "<h1>Deu ruim</h1>"
  
  return redirect(url_for('rents'))

@app.route('/client')
def client():
  query = ("SELECT * FROM Cliente")
  result = executeQuery(query)

  if (result == False):
    return

  return render_template('client.html', data=result)

@app.route('/registerClient', methods=['POST'])
def registerClient():
  name = request.form['nome']
  phone = request.form['telefone']
  params = (name, phone)

  result = callProcedure('cadastrarCliente', params)
  if not(result):
    return "<h1>Deu ruim</h1>"

  return redirect(url_for('client'))
  

@app.route('/vehicles')
def vehicles():
  query = ("SELECT * FROM Veiculo")
  vehicles = executeQuery(query, None)

  query = ("SELECT categoria FROM Categoria_veiculo")
  categories = executeQuery(query)

  if (vehicles == False or categories == False):
    return

  return render_template('vehicles.html', data=vehicles, categories=categories)


@app.route('/registerVehicle', methods=['POST'])
def registerVehicle():
  brand = request.form['marca']
  model = request.form['modelo']
  year = request.form['ano']
  category = request.form['tipo']
  params = (brand, model, category, year)
  
  result = callProcedure('cadastrarVeiculo', params)
  if not(result):
      return "<h1>Deu ruim</h1>"
  
  return redirect(url_for('vehicles'))

@app.route('/test')
def test():
  return render_template('test.html')

def getRentValue(result):
  query = ('SELECT valorAluguel(%s,%s)')
  newList = []
  
  for rent in result:
    queryParams = (rent[3],rent[6])
    rentValue = executeQuery(query, queryParams)
    rent += (rentValue[0])
    newList.append(rent)

  return newList