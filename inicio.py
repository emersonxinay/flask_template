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
