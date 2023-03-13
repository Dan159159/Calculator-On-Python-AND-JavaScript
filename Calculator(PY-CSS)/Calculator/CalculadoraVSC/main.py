from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def home():
    result = 0.0
    return render_template('index.html', result=result)
@app.route('/Calculator-BY:Dan', methods=['POST','GET'])
def index():
    result = 0.0
    operation = None
    result = float(request.form.get('result', 0))
    num2=0.0

    if request.method == 'POST':
        button_value = request.form['button']
        result = float(request.form.get('result', 0))
        num1=float(request.form.get('result',0))
        print(f"Primer resultado : {result}")
        print(f"Variable num1 : {num1}")
        print(f"")
        if button_value == 'C':
            result = 0.0
            num1=result
            operation = None
        elif button_value == 'borrar':
            num1=result
            result = request.form.get('result',0)
            result = result[:-1]  # eliminar el último carácter
            operation = None
        elif button_value == 'suma':
            num1=result
            result = 0.0  # reiniciar result
            operation = 'plus'
            print(f"resultado : {result}")
            print(f"Variable num1 : {num1}")
            print(f"Variable num2 : {num2}")
            print(f"Operation : {operation}")
            if button_value == 'igual':
                num2 = float(request.form.get('result', 0))
                print(f"resultado igual : {result}")
                print(f"Variable num1 igual : {num1}")
                print(f"Variable num2 igual : {num2}")
                print(f"Operation igual : {operation}")
                match operation:
                    case 'suma':
                        result = num1 + num2
                    case 'minus':
                        result = num1 - num2
                    case 'multi':
                        result = num1 * num2
                    case 'div':
                        result = num1 / num2
        elif button_value == 'minus':
            num1=result
            operation = 'minus'
            num1 = result
            result = float(request.form.get("",0))

        elif button_value == 'multi':
            operation = 'multi'
            num1 = result
            result = float(request.form.get("",0))

        elif button_value == 'dividir':
            operation = 'div'
            num1 =float(request.form.get('result'))
            result = float(request.form.get("",0))
        elif button_value == 'igual':
            num2 = float(request.form.get('result', 0))
            print(f"resultado igual : {result}")
            print(f"Variable num1 igual : {num1}")
            print(f"Variable num2 igual : {num2}")
            print(f"Operation igual : {operation}")
            match operation:
                case 'suma':
                    result = num1 + num2

                case 'minus':
                    result = num1-num2
                case 'multi':
                    result = num1*num2
                case 'div':
                    result = num1 / num2

        else:
            result = result *10+ float(button_value)
    else:
        result = 0

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
