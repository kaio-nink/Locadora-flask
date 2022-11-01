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

  query2 = ("SELECT v.id_veiculo, concat(v.marca, %s , v.modelo, %s, v.ano), v.categoria "
            "FROM Veiculo v LEFT JOIN Aluguel a ON a.id_veiculo = v.id_veiculo "
            "WHERE a.id_veiculo is null OR v.disponivel = TRUE "
            "UNION SELECT v.id_veiculo, concat(v.marca, %s , v.modelo, %s, v.ano), v.categoria "
            "FROM Veiculo AS v INNER JOIN Aluguel AS a on v.id_veiculo = a.id_veiculo "
            "WHERE (a.dataInicial > date_add(%s, interval %s day) OR date_add(a.dataInicial, interval a.numDias day) < %s)")

  params = (" "," "," "," ",initialDate, numDays, initialDate)
  vehicles = executeQuery(query2, params)

  query = ("SELECT id_cliente, nome FROM Cliente")
  clients = executeQuery(query)

  if ( vehicles == False or clients == False ):
    return
  print(vehicles)
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

@app.route('/categories')
def categories():
  query = ('SELECT * FROM Categoria_veiculo')
  result = executeQuery(query)

  if (result == False):
    return

  return render_template('categories.html', data=result)

@app.route('/registerCategory', methods=['POST'])
def registerCategory():
  category = request.form['categoria']
  dailyValue = request.form['valorDiaria']
  weeklyValue = request.form['valorSemanal']
  params = (category, dailyValue, weeklyValue)
  print(weeklyValue)
  result = callProcedure('cadastrarCategoria', params)
  if not(result):
      return "<h1>Deu ruim</h1>"
  
  return redirect(url_for('categories'))

def getRentValue(result):
  query = ('SELECT valorAluguel(%s,%s)')
  newList = []
  
  for rent in result:
    queryParams = (rent[3],rent[6])
    rentValue = executeQuery(query, queryParams)
    rent += (rentValue[0])
    newList.append(rent)

  return newList