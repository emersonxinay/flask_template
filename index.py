from flask import Flask, render_template, request, redirect, url_for

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

# decicón con if
@app.route('/saludo/<saludar>')
def saludar(saludar):
  return render_template('condicion.html', saludo = saludar)

# herencias 
@app.route('/perfil')
def perfil():
  return render_template('perfil.html')

@app.route('/blog')
def blog():
  return render_template('blog.html')

# rutas para formularios 
@app.route('/formulario')
def formulario():
  
  return render_template('formulario.html')

# el bienenido despues de hacer click en boton de enviar de formulario
@app.route('/bienvenido')
def bienvenido():
  # para usar con get, para obtener datos desde consola
  name = request.args.get('name')
  correo = request.args.get('correo')
  print(name, correo)
  return render_template('bienvenido.html')


if __name__ == '__main__':
    app.run(debug=True)
