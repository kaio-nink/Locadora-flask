from flask import Flask, render_template


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
  return render_template('client.html')

@app.route('/cars')
def cars():
  return render_template('cars.html')

@app.route('/test')
def test():
  return render_template('test.html')