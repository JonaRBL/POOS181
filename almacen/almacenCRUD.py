from tkinter import *
from tkinter import ttk
import tkinter as tk

from controladorBD import *

controlador = controladorBD()

def ejecutaInsert():
    controlador.guardarProducto(varNom.get(), varClas.get(), varMar.get(), varPrec.get())

def ejecutaConsulta():
    consult = controlador.consultasProductos()
    
    tabla.delete(*tabla.get_children())
    for beb in consult:
        tabla.insert("", tk.END, text = "", values = beb)

def ejecutaActualizar():
    rsBebida = controlador.consultaProducto(varID.get())
    if(rsBebida):
        controlador.actualizarProducto(varID.get(), varaNom.get(), varaClas.get(), varaMar.get(), varaPrec.get())
    else:
        messagebox.showinfo("No encontrado", "Bebida no registrada en la BD")

def ejecutaBusqueda():
    rsProducto = controlador.consultaProducto(varID2.get())
    
    textBus2.delete("1.0", "end")
    for beb in rsProducto:
        cadena = str(beb[0])+" "+ beb[1]+" "+ beb[2]+" "+ str(beb[3])
    
    if(rsProducto):
        textBus2.insert("0.0", cadena)
    else:
        messagebox.showinfo("No encontrado", "Bebida no registrada en la BD")

def ejecutaEliminar():
    sel = messagebox.askyesno("Elimiar Bebida", "Seguro que desea eliminar la bebida?")
    if (sel == True):
        
        try:
            controlador.eliminarProducto(varID2.get())
        except sqlite3.OperationalError:
            print("Error de Consulta")
        
ventana = Tk()
ventana.title("CRUD almacen")
ventana.geometry("500x300")

panel = ttk.Notebook(ventana)
panel.pack(fill= "both", expand = "yes")

pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)
pestana4 = ttk.Frame(panel)
pestana5 = ttk.Frame(panel)

#PESTAÑA1:alta de bebidas
titulo = Label(pestana1, text = "Alta de Bebidas", fg = "blue", font = ("Modern", 18)).pack()

varNom = tk.StringVar()
lblNom = Label(pestana1, text = "Nombre: ").pack()
txtNom = Entry(pestana1, textvariable = varNom).pack()

varClas = tk.StringVar()
lblClas = Label(pestana1, text = "Clasificacion: ").pack()
txtClas = Entry(pestana1, textvariable = varClas).pack()

varMar = tk.StringVar()
lblMar = Label(pestana1, text = "Marca: ").pack()
txtMar = Entry(pestana1, textvariable = varMar).pack()

varPrec = tk.StringVar()
lblPrec = Label(pestana1, text = "Precio: ").pack()
txtPrec = Entry(pestana1, textvariable = varPrec).pack()

btnGuardar = Button(pestana1, text = "Guardar bebida", command = ejecutaInsert).pack()

#PESTAÑA2: Consultar bebidas
titulo2 = Label(pestana2, text = "Consultar Bebidas", fg = "red", font = ("Modern", 18)).pack()

btnConsulta = Button(pestana2, text = "Consulta", command = ejecutaConsulta).pack()

columns = ("id", "nombre", "clasificacion", "marca", "precio")

tabla = ttk.Treeview(pestana2, columns = columns, show = "headings")

tabla.column("id", anchor=tk.W, width=50)
tabla.column("nombre", anchor=tk.W, width=150)
tabla.column("clasificacion", anchor=tk.W, width=150)
tabla.column("marca", anchor=tk.W, width=150)
tabla.column("precio", anchor=tk.W, width=150)

tabla.heading("id", text = "ID", )
tabla.heading("nombre", text = "NOMBRE")
tabla.heading("clasificacion", text = "CLASIFICACION")
tabla.heading("marca", text = "MARCA")
tabla.heading("precio", text = "PRECIO")

tabla.pack()

#PESTAÑA3:Actualizar bebida
titulo4 = Label(pestana3, text = "Actualizar Bebida", fg = "red", font = ("Modern", 18)).pack()

varID = tk.StringVar()
varaNom = tk.StringVar()
varaClas = tk.StringVar()
varaMar = tk.StringVar()
varaPrec = tk.StringVar()
lblid = Label(pestana3, text = "Identificador de producto: ").pack()
txtid = Entry(pestana3, textvariable = varID).pack()
lanNom = Label(pestana3, text = "Nuevo Nombre de Bebida: ").pack()
txNom = Entry(pestana3, textvariable = varaNom).pack()
lanClas = Label(pestana3, text = "Nueva Clasificacion: ").pack()
txClas = Entry(pestana3, textvariable = varaClas).pack()
lanMar = Label(pestana3, text = "Nueva Marca: ").pack()
txMar = Entry(pestana3, textvariable = varaMar).pack()
lanPrec = Label(pestana3, text = "Nuevo precio: ").pack()
txPrec = Entry(pestana3, textvariable = varaPrec).pack()

btnActuali = Button(pestana3, text = "Actualizar", command = ejecutaActualizar).pack()

#PESTAÑA4:Eliminar bebida
titulo4 = Label(pestana4, text = "Eliminar Bebida", fg = "red", font = ("Modern", 18)).pack()

varID2 = tk.StringVar()
lblid = Label(pestana4, text = "Identificador de bebida: ").pack()
txtid = Entry(pestana4, textvariable = varID2).pack()

btnBusqueda = Button(pestana4, text = "Buscar", command = ejecutaBusqueda).pack()

subBus2 = Label(pestana4, text = "Registrada:", fg = "blue", font = ("Modern", 18)).pack()
textBus2 = tk.Text(pestana4, height = 2, width = 52)
textBus2.pack()

btnBusqueda = Button(pestana4, text = "eliminar", command = ejecutaEliminar).pack()

panel.add(pestana1, text = "Alta de Bebidas")
panel.add(pestana2, text = "Consultar Bebidas")
panel.add(pestana3, text = "Actualizar Bebida")
panel.add(pestana4,text = "Eliminar Bebida")

ventana.mainloop()