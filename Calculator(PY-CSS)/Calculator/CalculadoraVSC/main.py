from flask import Flask, render_template, request

app = Flask(__name__)
# Funciones para las operaciones
def suma(num1, num2):
    result = num1 + num2
def resta(num1, num2):
    result = num1 - num2
    return result
def dividir(num1, num2):
    result = num1 / num2
    return result
def multi(num1, num2):
    result = num1 * num2
    return result
# La primera pagina que nos saldra
@app.route('/')
def home():
    result = 0
    return render_template('index.html', result=result)
# La pagina saldra cuando en el ocurra onaction='/press_button' en el html
@app.route('/press_button', methods=['GET', 'POST'])
def index():
    num1 = 0
    num2 = 0
    operation=''
    result = 0
    # Cuando post devolvamos en float el resultado con el value del boton
    # Post the value of the button on the html
    if request.method == 'POST':
        # Recoger el valor value='' del html// Get the value='' for the html
        button_value = request.form['button']
        # Mostrar el resultado en pantalla concadenando con el anterior resultado//Show the result concatenate the result
        result = float(request.form.get('result', 0))
        num1 = result
        if button_value == 'C':
            result = 0
        elif button_value == 'borrar':
            result = request.form.get('result',0)
            result = result[:-1]  # eliminar el último carácter
            if result == '':
                result = 0.0
        elif button_value == 'suma':
            operation = 'suma'
            num1 = result
            result = float(request.form.get("",0))
            result = 0.0  # reiniciar result
        elif button_value == 'minus':
            operation = 'minus'
            num1 = result
            result = float(request.form.get("",0))

        elif button_value == 'multi':
            operation = 'multi'
            num1 = result
            result = float(request.form.get("",0))

        elif button_value == 'dividir':
            operation = 'dividir'
            num1 = result
            result = float(request.form.get("",0))
        elif button_value == 'igual':
            num2 = result
            if operation == 'suma':
                result = float(request.form.get('result', suma(num1, num2)))
            elif operation == 'minus':
                result = float(resta(num1, num2))
            elif operation == 'multi':
                result = multi(num1, num2)
            elif operation == 'dividir':
                result = dividir(num1, num2)
        else:
            result = result * 10 + float(button_value)
    else:
        result = 0

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
