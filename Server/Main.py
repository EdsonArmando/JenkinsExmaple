from os import close
from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '201701029'
app.config['MYSQL_DB'] = 'Ejemplo'

mysql = MySQL(app)

@app.route('/insertar', methods=['POST'])
def insert():
    contenido = request.json
    nombre = contenido['name']
    apellido = contenido['lastname']
    print(nombre, apellido)
    cursor = mysql.connection.cursor()
    cursor.execute('''INSERT INTO Persona(name,lastname) VALUES(%s, %s) ''',(nombre, apellido))
    mysql.connection.commit()
    cursor.close()
    return '200'

@app.route('/',methods=['GET'])
def index():
    return 'Funciona Flask'

@app.route('/getaAll',methods=['GET'])
def personas():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute(''' SELECT * FROM Persona ''')
        rows = cursor.fetchall()
        return jsonify(rows)
    except Exception as e:
        print('Error: '+e)
    finally:
        cursor.close()
app.run(host='0.0.0.0',debug=True)