from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
  return 'buenas buenas buenas'

@app.route('/operasBas', methods=['GET', 'POST'])
def operasBas():
  if request.method == 'POST':
    num1 = request.form.get('num1')
    num2 = request.form.get('num2')
    return "<h2> la suma es: {}".format(str(int(num1)+int(num2)))
  elsif: 
        return '''
        <form/Action="/operaas" method="POST">
        <label> N1:</label>
        <input> type="text" name="num1"></br></br>
          <label> N1:</label>

        <input> type="text" name="num2"></br></br>
        <input> type="submit" value="suma"></br></br>
        <input> type="submit" value="Resta"></br></br>
        <input> type="submit" value="Multiplicar"></br></br>
        <input> type="submit" value="dividir"></br></br>

        </form>
        '''
    elsif: 


if _name_ == '_main_':
  app.run(debug=True, port=8000)