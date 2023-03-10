# Primeros pasos en Flask 

### Como requisito, tener estas herramientas: 
<li>Editor de Código: <a href="https://code.visualstudio.com/">VsCode </a> </li>
<li>Lenguaje de Programación: <a href="https://www.python.org/downloads/">python </a> </li> 

<li>Framework Flask: <a href="https://www.manualweb.net/flask/instalar-flask/"> Flask </a> </li>
<li>Documentación Flask: 
<a href="https://flask-es.readthedocs.io/quickstart/#:~:text=Para%20ejecutar%20la%20aplicaci%C3%B3n%2C%20utiliza,aplicaci%C3%B3n%20con%20la%20opci%C3%B3n%20%2Dapp%20.&text=Como%20atajo%2C%20si%20el%20archivo,tienes%20que%20usar%20%2D%2Dapp%20.">documentación de  flask </a> 
</li>
<li>Para hacer peticiones de API: <a href="https://insomnia.rest/download">insomia </a> </li> 

## crear un entorno de trabajo para flask 

### iniciamos instalando virtualenv 
```bash
pip install virtualenv
```
### creamos una carpeta para nuestro proyecto
```bash 
mkdir miproyecto
```
```bash
cd miproyecto
```
### ahora creamos el entorno virtual del proyecto - suele utilizar venv
```bash
virtualenv mientornovirtual
```
#### suelen usar cambio de mientornovirtual por venv 

### Recuerda siempre activar el entorno virtual para trabajar con flask
```bash 
source mientornovirtual/bin/activate
```
### si deseas desactivar 
```bash 
deactivate
```
## instalamos flask 
```bash
pip install Flask 
```
## creamos un archivo nuevo index.py y agregamos este codigo base: 

```py
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
```

### para correr el programa 
```bash 
flask run
```
o 
```bash
python3 index.py
```
### pero para que no estes apagando y volver a encender el servidor vamos hacer lo siguiente.

```bash 
$env:FLASK_ENV = "development"
```
o 
```bash 
export FLASK_ENV=development
```


# Para utilizar template 
<h4> primero creamos una carpeta especifica que se llame <strong> templates </strong> y debe estar al mismo nivel de la raiz y dentro de esta carpeta crear un archivo html <strong> index.html </strong> </h4>


<h4> una vez modificado todo el html, ahora importamos desde el archivo principal<code> app.py </code> y alli agregamos lo siguiente o parecido. </h4>

<h4> -- crea una nueva carpeta static y por dentro pones una structura basica de carpetas y archivos basicos de html, css, img y js.</h4> 



```py
# con rederización de otro archivo html
@app.route('/mostrar/<nombre>', methods=['GET', 'POST'])
def mostrar_nombre(nombre):
    return render_template('mostrar.html', nombre_parametro=nombre)

```

## redireccionar a paginas - desde app.py

```py
# redireccionar hacia otras paginas


@app.route('/redirect')
def mi_redirect():
    return redirect(url_for('hola_mundo'))

```
### y desde el html agregar de la siguiente manera: el que esta dentro de las comillas simples es a función de otra pagina 

```html
<a href="{{url_for('hola_mundo')}}"> Mostrar Nombre </a>
```

## Manejo de Errores de pagina - desde app.py
```py
# aqui ya no se usa route para la ruta, sino errorhandler
@app.errorhandler(404)
def pagina_error(error):
    return render_template('404.html', error=error), 404

```
### y desde el template crear un arichivo nuevo para los errores, en esta ocación 404.html y el codigo minimo es lo siguiente: 

```html
<h2>mas detalle: {{error}} </h2>
```

## Para evaluar ruta con decicíon desde index.py
```py
# ruta evaluando usuario y contraseña

@app.route('/ingreso/<usuario>/<password>')
def evaluando(usuario, password):
    # simulando base de datos
    bd_usuario = "emerson"
    bd_password = "123456"

    # evaluando si cumple
    if bd_usuario == usuario and bd_password == password:
        return "Inicio exitoso"
    else:
        return "Datos incorrectos"
    
```

## para mostrar  bucle for en html desde index.py

```py 
# bucles para listas personas
@app.route('/listaPersona')
def listaPersona():
  # lista de nombres
  personas = ['martin', 'emerson', 'juan', 'maria', 'sofia', 'lisset', 'pia']
  # se conecta con el archivo bucle.html y la variable que usara es per
  return render_template('bucle.html', per = personas)

```
### y en el archivo bucle.html
```html
<ul>
      {% for p in per %}
      <li>{{p}}</li>
      {% endfor%}
</ul>
```

## condición if desde index.py
```py
@app.route('/saludo/<saludar>')
def saludar(saludar):
  return render_template('condicion.html', saludo = saludar)
```
### y ahora if desde condición.html
```html
<div>
      <h1>iniciando {{saludo}}</h1>
      {% if saludo == 'hola'%}
      <h2>Hola como estas</h2>
      {% else %}
      <h2>bueno, chauuu!</h2>

      {%endif%}
    </div>
```

## herencia de pagina o poner uno de raíz

### en python
```py
```

### en html base
```html
<div>
    <h1>Sección Navegación</h1>
    <a href="/blog">Blog</a>
    <a href="/perfil">Perfil</a>
  </div>

  {% block content %}


  {% endblock%}

  <footer>
    <h3>Esto es el footer</h3>
  </footer>
```
### en html que hereda 
```html 
<!-- con esto hereda  -->
{% extends 'base.html' %}

<!-- inicia el bloque -->
{% block content %}
<!-- Aqui personalizas tu pagina heredada  -->
<h1>hola este es mi perfil</h1>


{% endblock %}
<!-- fin del bloque heredado -->

```
## para que sea mas dinamico las url y no dependa de si mismo sino que herede
```html
<div>
    <h1>Sección Navegación</h1>
    <a href="{{url_for('blog')}}">Blog</a>
    <a href="{{url_for('perfil')}}">Perfil</a>
  </div>
```



## Si queremos que los titulos cambien su nombre por pagina 
```html
<!-- en el archivo base -->
<title>{% block title %} inicio {%endblock%}</title>

```
```html
<!-- en el archivo heredado -->
<title>{% block title %} inicio {%endblock%}</title>
```

### tips para generar html desde el h1 al h3, y otros. 
h$[title=items$]{Titulo $}*3 

## Formularios 
### en archivo index.py
```py 
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

```

### y en achivos html de formulario y bienvenido
#### en formulario.html
```html
{% extends 'base.html' %}

{% block content %}
<h1>Formulario de Registros</h1>
<!-- cuando hacemos click se ira a la pagina bienvenido.hmtl  -->
<form action="{{url_for('bienvenido')}}" method="GET">
  Nombre: <input type="text" name="name">
  <br>
  correo: <input type="text" name="correo">
  <br>
  <input type="submit" value="Enviar Datos">
  <br>

</form>
{% endblock%}

```

#### en archivo bienvenido.html
```html
{% extends 'base.html' %} 
{% block content %}
<h1>registro exitoso</h1>
{% endblock%}
```

## pagina para errores al buscar en la pestaña del navegador
### en el index.py
```py
@app.errorhandler(404)
def paginaNoEncontrada(e):

    return render_template('404.html'), 404

```

### en el 404.html 
```html
{% extends 'base.html' %} {% block content %}
<h1>pagina no econtrada!</h1>
<p>revisa la url</p>

{% endblock%}
```

## validación de datos del formulario, desde index.py al enviar desde el boton

```py
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
```

# FlaskForm 
<a href="https://flask-wtf.readthedocs.io/en/0.15.x/install/"> doc Instalación FlaskForm </a>

```bash
pip install -U Flask-WTF
```

## desde un nuevo archivo inicio.py 
```py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask import Flask, render_template
app = Flask(__name__)

app.config['SECRET_KEY'] = 'miclavesecreta'


class Formulario(FlaskForm):
    nombre = StringField('nombre')
    estado = SubmitField('estado')


@app.route('/', methods=['GET', 'POST'])
def inicio():
    nombre = ''
    estado = False
    formulario = Formulario()
    if formulario.validate_on_submit():
        estado = True
        nombre = formulario.nombre.data
        formulario.nombre.data = ''

    return render_template('inicio.html', estado=estado, nombre=nombre, formulario=formulario)


if __name__ == '__main__':
  # para poder ver los errores si los hubiera
    app.run(debug=True)

```

## desde templates/inicio.html
```html 
{% if estado %}

<p>hola bienvenido {{nombre}}</p>

{% else %}

<p>No estas en mi base de datos registrate</p>

{%endif%}

<form method="POST" action="">
  {{formulario.hidden_tag()}} 
  {{formulario.nombre.label}} {{formulario.nombre}}
  {{formulario.estado}}
</form>

```












