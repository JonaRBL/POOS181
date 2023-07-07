from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'db_fruteria'
app.secret_key='mysecretkey'
mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method == 'POST':
        
        Vfruta = request.form['txtFruta']
        Vtemporada= request.form['txtTemporada']
        Vprecio = request.form['txtPrecio']
        Vstock = request.form['txtStock']
        
        CS = mysql.connection.cursor()
        CS.execute('insert into tbfrutas(fruta,temporada,precio,stock) values(%s,%s,%s,%s)',(Vfruta,Vtemporada,Vprecio,Vstock))
        mysql.connection.commit()
        
    flash('La fruta fue agregado correctamente')
    return redirect(url_for('index'))

@app.route('/consulta')
def consulta():
    CC = mysql.connection.cursor()
    CC.execute('select * from tbfrutas')
    conFruts = CC.fetchall()
    return render_template('consultarFruta.html',listFrut = conFruts)

@app.route('/editar/<id>')
def editar(id):
    CID = mysql.connection.cursor()
    CID.execute('select * from tbfrutas where id = %s', (id,))
    consulId = CID.fetchone()
    return render_template('editarFruta.html', fruta = consulId)

@app.route('/actualizar/<id>', methods=['POST'])
def actualizar(id):
    if request.method == 'POST':
        varfruta = request.form['txtFruta']
        vartemporada = request.form['txtTemporada']
        varprecio = request.form['txtPrecio']
        varstock = request.form['txtStock']
        
        CA = mysql.connection.cursor()
        CA.execute('update tbfrutas set fruta= %s,temporada= %s,precio= %s,stock= %s where id= %s', (varfruta,vartemporada,varprecio,varstock,id))
        mysql.connection.commit()
        
    flash('El registro se actualizo correctamente'+' '+ varfruta)
    return redirect(url_for('consulta'))

@app.route('/pasar/<id>')
def pasar(id):
    CAP = mysql.connection.cursor()
    CAP.execute('select * from tbfrutas where id = %s', (id,))
    consulId2 = CAP.fetchone()
    return render_template('borrarFruta.html', fruta2 = consulId2)

@app.route('/eliminar/<id>', methods=['POST'])
def eliminar(id):
    if request.method == 'POST':
        CA = mysql.connection.cursor()
        CA.execute('delete from tbfrutas where id= %s', (id))
        mysql.connection.commit()
    
    flash('El registro se elimino correctamente')
    return redirect(url_for('consulta'))

@app.route('/consultaNom', methods=['POST'])
def consultaNom():
    varbuscar = request.form['txtBuscar']
    CC = mysql.connection.cursor()
    CC.execute('select * from tbfrutas where fruta LIKE %s',(f'%{varbuscar}%',))
    conFrut = CC.fetchall()
    return render_template('consultaNombre.html',listFruts = conFrut)

@app.route('/consultan')
def consultan():
    return render_template('consultaNombre.html')

#Ejecucion del servidor en el puerto 5000
if __name__ == "__main__":
    app.run(port=5000, debug=True)