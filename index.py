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

    return render_template('login.html', name=nombre, age=edad)


# diccionarios
@app.route('/diccionario')
def diccionario():
    dic = {"nombre": "emerson", "edad": "20", "ciudad": "Santiago"}

    return render_template('login.html', diccionario=dic)

# bucles para listas personas


@app.route('/listaPersona')
def listaPersona():
    # lista de nombres
    personas = ['martin', 'emerson', 'juan', 'maria', 'sofia', 'lisset', 'pia']
    # se conecta con el archivo bucle.html y la variable que usara es per
    return render_template('bucle.html', per=personas)

# decicón con if


@app.route('/saludo/<saludar>')
def saludar(saludar):
    return render_template('condicion.html', saludo=saludar)

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
    # simulando base de datos
    user = "emerson"
    user_correo = "xinay@gmail.com"
    # para usar con get, para obtener datos desde consola cuando hacen click en submit del formulario
    name = request.args.get('name')
    correo = request.args.get('correo')

    # tomando decición
    if name == user and correo == user_correo:
        return render_template('bienvenido.html')
    else:
        return '<h1> Datos Incorrectos </h1>'


# pagina apara errores al buscar en la pestaña
@app.errorhandler(404)
def paginaNoEncontrada(e):

    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
