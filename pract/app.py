#importación del framework
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

#Inicializacion del APP
app = Flask(__name__)

#Configuracion de la conexion
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'dbflask'
app.secret_key='mysecretkey'
mysql = MySQL(app)

#declaracion de ruta http://localhost:5000
@app.route('/')
def index():
    CC = mysql.connection.cursor()
    CC.execute('select * from tbalbums')
    conAlbums = CC.fetchall()
    #print(conAlbums)
    return render_template('index.html',listAlbums = conAlbums)

#ruta http:localhost:5000/guardar tipo POST para Insert
@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method == 'POST':
        
        #pasamos a variables el contenido de los inputs
        Vtitulo = request.form['txtTitulo']
        Vartista = request.form['txtArtista']
        Vanio = request.form['txtAnio']
        
        #conectar a la bd y ejecutar el insert
        CS = mysql.connection.cursor()
        CS.execute('insert into tbalbums(titulo,artista,anio) values(%s,%s,%s)',(Vtitulo,Vartista,Vanio))
        mysql.connection.commit()
        
    flash('El album fue agregado correctamente')
    return redirect(url_for('index'))

@app.route('/editar/<id>')
def editar(id):
    CID = mysql.connection.cursor()
    CID.execute('select * from tbalbums where id = %s', (id,))
    consulId = CID.fetchone()
    return render_template('editarAlbum.html', album = consulId)

@app.route('/actualizar/<id>', methods=['POST'])
def actualizar(id):
    if request.method == 'POST':
        vartitulo = request.form['txtTitulo']
        varartista = request.form['txtArtista']
        varanio = request.form['txtAnio']
        
        CA = mysql.connection.cursor()
        CA.execute('update tbalbums set titulo= %s,artista= %s,anio= %s where id= %s', (vartitulo,varartista,varanio,id))
        mysql.connection.commit()
        
    flash('El album se actualizo correctamente'+' '+ vartitulo)
    return redirect(url_for('index'))

@app.route('/eliminar')
def eliminar():
    return "Se elimino en la BD"

#Ejecucion del servidor en el puerto 5000
if __name__ == "__main__":
    app.run(port=5000, debug=True)