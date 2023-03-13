from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def home():
    result = 0.0
    return render_template('index.html', result=result)
@app.route('/press_button', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        operation = None
        button_value = request.form['button']
        result = float(request.form.get('result', 0))
        num1 = result
        if button_value == 'C':
            result = 0.0
            operation = None
        elif button_value == 'borrar':
            operation = None
            result = request.form.get('result',0)
            result = result[:-1]  # eliminar el último carácter
            if result == '':
                result = 0.0
        elif button_value == 'suma':
            operation = 1
            num1 = result
            result = float(request.form.get("",0))
            result = 0.0  # reiniciar result
        elif button_value == 'minus':
            operation = 2
            num1 = result
            result = float(request.form.get("",0))

        elif button_value == 'multi':
            operation = 3
            num1 = result
            result = float(request.form.get("",0))

        elif button_value == 'dividir':
            operation = 4
            num1 = result
            result = float(request.form.get("",0))
        elif button_value == 'igual':
            num2 = result
            match operation:
                case 1:
                    result = num1+num2
                case 2:
                    result = num1-num2
                case 3:
                    result = num1*num2
                case 4:
                    result = num1 / num2
        else:
            result = result * 10 + float(button_value)
    else:
        result = 0

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
