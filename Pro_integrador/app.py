# Importacion de framework -------------------------------------------
from flask import Flask,render_template,request,redirect,url_for,flash
# Importacion de MySQL con FLASK
from flask_mysqldb import MySQL

# Inicialización del APP ó servidor ----------------------------------
app= Flask(__name__)

# Conexion de la base de datos ---------------------------------------
app.config['MYSQL_HOST']='localhost'
#app.config['MYSQL_USER']='root' # Usuario de MySQL 
#app.config['MYSQL_PASSWORD']=''  # Contraseña MySQL
#app.config['MYSQL_DB']='dbflask'  # Nombre de la base de datos
#app.secret_key='mysecretkey'
#mysql= MySQL(app)

# Declaración de las rutas hhtp://localhost:5000 ---------------------

  # Ruta principal -------------
@app.route('/')
def index():
    return render_template('registro.html')
  #Ruta secundarias ------------------------
@app.route('/Conocenos')
def inicio():
    return render_template('inicio.html')

@app.route('/EdificioA')
def edificioA():
    return render_template('edificioa.html')

@app.route('/EdificioB')
def edificioB():
    return render_template('edificiob.html')

@app.route('/EdificioC')
def edificioC():
    return render_template('edificioc.html')

@app.route('/Biblioteca')
def Biblio():
    return render_template('biblioteca.html')

@app.route('/CAPTA')
def capta():
    return render_template('capta.html')

@app.route('/CIDEA')
def cidea():
    return render_template('cidea.html')

@app.route('/LakafeUPQ')
def cafeteria():
    return render_template('cafeteria.html')

@app.route('/LT1')
def lt1():
    return render_template('LT1.html')

@app.route('/Talleres')
def talleres():
    return render_template('talleres.html')

@app.route('/Canchas')
def canchas():
    return render_template('canchas.html')

@app.route('/Registro-admision')
def registro():
    return render_template('REGISTRO_ADMISION.html')

# ruta http:localhost:500/guardar tipo POST para Insert
@app.route('/guardar')
def guardar():
    return redirect(url_for('index'))

@app.route('/eliminar')
def eliminar():
    return "Se elimino en la BD"

# Ejecución de Servidor en el Puerto 5000 ---------------------------- 
if __name__ == '__main__':
    app.run(port=5500,debug=True)
    
