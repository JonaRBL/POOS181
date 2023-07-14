from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'db_floreria'
app.secret_key='mysecretkey'
mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method == 'POST':
        Vnombre = request.form['txtNombre']
        Vcantidad = request.form['txtCantidad']
        Vprecio = request.form['txtPrecio']
        
        CG = mysql.connection.cursor()
        CG.execute('insert into tbflores(nombre,cantidad,precio) values(%s,%s,%s)',(Vnombre,Vcantidad,Vprecio))
        mysql.connection.commit()
    
    flash('El ramo fue agregado correctamente')    
    return redirect(url_for('index'))

@app.route('/consultar')
def consulta():
    CC = mysql.connection.cursor()
    CC.execute('select * from tbflores')
    conRamos = CC.fetchall()
    return render_template('consultarRamo.html',listRam = conRamos)

if __name__ == "__main__":
    app.run(port=5000, debug=True)