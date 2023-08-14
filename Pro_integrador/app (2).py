# Importacion de framework -------------------------------------------
from flask import Flask,render_template,request,redirect,url_for,flash
# Importacion de MySQL con FLASK
from flask_mysqldb import MySQL
from datetime import datetime 

# Inicialización del APP ó servidor ----------------------------------
app= Flask(__name__)

# Conexion de la base de datos ---------------------------------------
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root' # Usuario de MySQL 
app.config['MYSQL_PASSWORD']=''  # Contraseña MySQL
app.config['MYSQL_DB']='bdproyecto'  # Nombre de la base de datos
app.secret_key='mysecretkey'
mysql= MySQL(app)

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

@app.route('/LT')
def lt1():
    return render_template('LT1.html')

@app.route('/Talleres')
def talleres():
    return render_template('talleres.html')

@app.route('/Canchas')
def canchas():
    return render_template('canchas.html')

@app.route('/admision')
def registroproceso():
    return render_template('ADMISION.html')

@app.route('/proceso')
def proceso():
    return render_template('proceso.html')

@app.route('/registrar', methods=['POST'])
def registrar():
    if request.method == 'POST':
# Pasamos a variables el contenido de los input
        Vnombre = request.form['txtnombre']
        Vcorreo = request.form['txtcorreo']

        # Validamos que los campos no estén vacíos
        if Vnombre == "" or Vcorreo == "":
            flash('No se puede registrar un envío con campos vacíos')
            return render_template('registro.html')
        else:
            # Conectar y ejecutar el insert
            CS = mysql.connection.cursor()
            CS.execute('insert into registro(nombre,correo) values (%s,%s)',(Vnombre,Vcorreo))
            mysql.connection.commit()
            return redirect(url_for('inicio')) 

# ruta http:localhost:500/guardar tipo POST para Insert
@app.route('/guardar-proceso', methods=['POST'])
def guardarproceso():
     if request.method == 'POST':
# Pasamos a variables el contenido de los input
        Varnombre = request.form['txtNombre']
        Varcorreo = request.form['txtemail']
        Vardireccion = request.form['txtDireccion']
        Vartelefono = request.form['txtTelefono']
        Varfecha = request.form['Fecha_Registro']
        Varcarrera = request.form['txtcarrera']

        # Validamos que los campos no estén vacíos
        if Varnombre == "" or Varcorreo == "" or Vardireccion == "" or Vartelefono == "" or Varfecha == "":
            flash('No se puede enviar campos vacíos')
            return render_template('proceso.html')
        else:
            # Conectar y ejecutar el insert
            CS = mysql.connection.cursor()
            CS.execute('insert into proceso(nombre,email,direccion,telefono,fecha,carrera) values (%s,%s,%s,%s,%s,%s)',(Varnombre,Varcorreo,Vardireccion,Vartelefono,Varfecha,Varcarrera))
            mysql.connection.commit()
            flash('Tu registro se registró correctamente')
            return redirect(url_for('proceso')) 
# Ejecución de Servidor en el Puerto 5000 ---------------------------- 
if __name__ == '__main__':
    app.run(port=5500,debug=True)
    
