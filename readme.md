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

## Para evaluar ruta con decicíon 
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












