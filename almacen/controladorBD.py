from tkinter import messagebox
import sqlite3
import tkinter as tk

class controladorBD:
    
    def __init__(self):
        pass
    
    def conexionBD(self):
        
        try:
            conexion = sqlite3.connect("C:/Users/jonat/OneDrive/Documentos/UPQ/6to cuatri/POOS181/almacen/DBalmacen.db")
            print("Conectado a la base de datos")
            return conexion
        
        except sqlite3.OperationalError:
            print("No se pudo conectar a la BD")
    
    def guardarProducto(self, nom, clas, mar, prec):
        
        conx = self.conexionBD()
        
        if(nom == "" or clas == "" or mar == "" or prec == ""):
           messagebox.showwarning("Cuidado!", "Ningún campo puede estar vacio")
           conx.close() 
        else:
            cursor = conx.cursor()
            datos = (nom, clas, mar, prec)
            qrInsert = "insert into TBbebidas(nombre, clasificacion, marca, precio) values(?,?,?,?)"
            
            cursor.execute(qrInsert, datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Exito!!", "Se registro la bebida")
    
    def consultasProductos(self):
        conx = self.conexionBD()
        
        cursor = conx.cursor()
        sqlConsulta = "select * from TBbebidas"
        
        cursor.execute(sqlConsulta)
        registros = cursor.fetchall()
        conx.close()
        
        return registros
    
    def consultaProducto(self, id):
        conx = self.conexionBD()
        
        if (id == ""):
            messagebox.showwarning("Cuidado", "ID vacio, escribe uno valido")
            conx.close()
        else:
            try:
                cursor = conx.cursor()
                sqlSelect = "select * from TBbebidas where id =" + id
                
                cursor.execute(sqlSelect)
                RSbebida = cursor.fetchall()
                conx.close()
                
                return RSbebida
            
            except sqlite3.OperationalError:
                print("Error de Consulta")
    
    def actualizarProducto(self, id, noment, clasent, marent, precent):
        conx = self.conexionBD()
        
        if(id == "" or noment == "" or clasent == "" or marent == "" or precent == ""):
            messagebox.showwarning("Cuidado", "ningun campo puede estar vacio")
            conx.close()
        else:
            try:
                cursor = conx.cursor()
                nom = noment
                clas = clasent
                mar = marent
                prec = precent
                sqlActuali = "UPDATE TBbebidas SET nombre=?, clasificacion=?, marca=? precio=? WHERE id=?"
                
                cursor.execute(sqlActuali, [nom, clas, mar, prec, id])
                proAct = cursor.fetchall()
                conx.commit()
                conx.close()
                messagebox.showinfo("Exito!!", "Datos de la bebida actualizados")
                
                return proAct
            
            except sqlite3.OperationalError:
                print("Error de Consulta")
    
    def eliminarProducto(self, id):
        conx = self.conexionBD()
        
        if(id == ""):
            messagebox.showwarning("Cuidado", "ningun campo puede estar vacio")
            conx.close()
        else:
            try:
                cursor = conx.cursor()
                sqlDelete = "DELETE FROM TBbebidas WHERE id=?"
                
                cursor.execute(sqlDelete, [id])
                proEli = cursor.fetchall()
                conx.commit()
                conx.close()
                messagebox.showinfo("Exito!!", "Bebida eliminada")
                
                return proEli
            
            except sqlite3.OperationalError:
                print("Error de Consulta")
        
        