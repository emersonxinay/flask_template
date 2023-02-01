from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# ruta base para usar render_template
@app.route('/')
def index():
  return render_template('index.html')

# ruta hacia otro lado ejm: login.html
@app.route('/login')
def login():
  nombre = "emerson"
  edad = 20
  
  return render_template('login.html', name = nombre, age = edad)


# diccionarios 
@app.route('/diccionario')
def diccionario():
  dic = {"nombre":"emerson", "edad":"20", "ciudad":"Santiago"}
  
  return render_template('login.html', diccionario = dic)

# bucles para listas personas
@app.route('/listaPersona')
def listaPersona():
  # lista de nombres
  personas = ['martin', 'emerson', 'juan', 'maria', 'sofia', 'lisset', 'pia']
  # se conecta con el archivo bucle.html y la variable que usara es per
  return render_template('bucle.html', per = personas)


if __name__ == '__main__':
    app.run(debug=True)
