import tkinter as tk
from tkinter import *

import numpy
import random

def AgendarCitas():
    ventanaAgendarCitas = Toplevel()
    ventanaAgendarCitas.geometry("500x500")
    ventanaAgendarCitas.title("Agendar Citas")
    panel = Frame(ventanaAgendarCitas)
    def agendar():
        nombre = Enombre.get()
        nombres.append(nombre)
        año = int(Eaño.get())
        años.append(año)
        identidad = int(Eidentidad.get())
        nidentidad.append(identidad)
        especi = Eespeci.get()
        fecha = Efecha.get()
        for e in range(0,6):
            if especi == especialidades[e]:
                c=e
        for a in range(0,14):
            if fecha == horario[a]:
                f=a
        if tabla[f][c] ==0:
            tabla[f][c] = 1
            mensaje="¡Se ha agendado su cita exitosamente!"
        else:
            mensaje="El horario selecccionado ya se encuentra ocupado"
        Emensaje.delete(0,END)
        Emensaje.insert(0,mensaje)

    Lnombre = Label(panel, text="Nombre Completo: ", pady=8).grid(row=0, column=0)
    Laño = Label(panel, text="Años: ", pady=8).grid(row=1, column=0)
    Lidentidad = Label(panel, text="Numero de Identidad: ", pady=8).grid(row=2, column=0)
    Lespeci = Label(ventanaAgendarCitas, text="¿Con que especialista desea agendar su cita?: ")
    Lfecha = Label(ventanaAgendarCitas, text="Ingrese el que fecha desea agendar su cita: ")

    Enombre = Entry(panel, width=20)
    Enombre.grid(row=0, column=1)
    Eaño = Entry(panel, width=20)
    Eaño.grid(row=1, column=1)
    Eidentidad = Entry(panel, width=20)
    Eidentidad.grid(row=2, column=1)
    Eespeci = Entry(ventanaAgendarCitas, width=15)
    Efecha = Entry(ventanaAgendarCitas, width=15)
    Emensaje = Entry(ventanaAgendarCitas, width=45)

    Bagendar = Button(ventanaAgendarCitas, text="Agendar Cita", command=agendar)
    cerrarventana = Button(ventanaAgendarCitas, text="Cerrar la ventana", command=ventanaAgendarCitas.destroy)

    panel.pack(pady=8)
    Lespeci.pack(pady=8)
    Eespeci.pack(pady=8)
    Lfecha.pack(pady=8)
    Efecha.pack(pady=8)
    Bagendar.pack(pady=8)
    Emensaje.pack(pady=8)
    cerrarventana.pack(pady=8)

def ReasignarCitas():
    ventanaReasignarCitas = Toplevel()
    ventanaReasignarCitas.geometry("500x500")
    ventanaReasignarCitas.title("Reasignar Citas")
    def reagendar():
        especi = Evespeci.get()
        hora = Evfecha.get()
        for e in range(0,6):
            if especi == especialidades[e]:
                c=e
        for a in range(0,14):
            if hora == horario[a]:
                f=a
        if tabla[f][c] == 1:
            tabla[f][c] = 0
        else:
            rmensaje="El horario selecccionado no se encuentra niguna cita asignada"
        nespeci = Enuevoespeci.get()
        nhora = Enuevafecha.get()
        for e in range(0,6):
          if nespeci == especialidades[e]:
            c=e          
        for a in range(0,14):
            if nhora == horario[a]:
                f=a
        if tabla[f][c] == 0:
            tabla[f][c] = 1
            rmensaje="¡Se ha reasignado su cita exitosamente!"
        else:
            rmensaje="El horario selecccionado no se encuntra una cita asignada encuentra"
        Ermensaje.delete(0,END)
        Ermensaje.insert(0,rmensaje)

    Lvfecha = Label(ventanaReasignarCitas, text="¿En que fecha agendo su cita? ")
    Lvfecha = Label(ventanaReasignarCitas, text="¿En que fecha agendo su cita? ")
    Lvespeci = Label(ventanaReasignarCitas, text="¿Con que especialista habia agendadado su cita?: ")
    Lvfecha = Label(ventanaReasignarCitas, text="¿En que fecha agendo su cita? ")
    Lnuevafecha = Label(ventanaReasignarCitas, text="Ingrese el que fecha en la que desea agendar su nueva cita")
    
    Evespeci = Entry(ventanaReasignarCitas, width=20)
    Evfecha = Entry(ventanaReasignarCitas, width=20)
    Ermensaje = Entry(ventanaReasignarCitas, width=20)
    Enuevafecha = Entry(ventanaReasignarCitas, width=20)
    
    Breagendar = Button(ventanaReasignarCitas, text="Reasignar Cita", command=reagendar)
    cerrarventana = Button(ventanaReasignarCitas, text="Cerrar la ventana", command=ventanaReasignarCitas.destroy)

    Lvespeci.pack(pady=10)
    Evespeci.pack(pady=10)
    Lvfecha.pack(pady=10)
    Evfecha.pack(pady=10)
    Lnuevafecha.pack(pady=10)
    Enuevafecha.pack(pady=10)
    Breagendar.pack(pady=10)
    Ermensaje.pack(pady=10)
    cerrarventana.pack(pady=10)

def VerCitas():
    ventanaVerCitas = Toplevel()
    ventanaVerCitas.geometry("400x300")
    ventanaVerCitas.title("Ver Citas")
    cerrarventana = Button(ventanaVerCitas, text="Cerrar la ventana", command=ventanaVerCitas.destroy)

    cerrarventana.pack(pady=10)

def VerCitaslibres():
    ventanaVerCitasl = Toplevel()
    ventanaVerCitasl.geometry("400x300")
    ventanaVerCitasl.title("Ver Citas Libres")
    def citaslibresE():
      for e in range(0,6):
        if especialista == especialidades[e]:
          c=e
      libre = 0
      for j in range(1,6,1):
        for i in range(1,14,1):
          if j == c:
            if tabla[i][j] == 0:
              libre+=1
      mensajee="La especialidades de",especialista,"tiene",libre,"citas libres"
      Ermensajee.delete(0,END)
      Ermensajee.insert(0,mensajee)
    def citaslibresH():
      for a in range(0,14):
        if hora == horario[a]:
          f=a
      libre = 0
      for j in range(1,6,1):
        for i in range(1,14,1):
          if i == f:
            if tabla[i][j] == 0:
              libre+=1
      mensajeh="En el horario seleccionado se encuentran",libre,"cita/s libre/s"
      Ermensajeh.delete(0,END)
      Ermensajeh.insert(0,mensajeh)
    Lespecialista  = Label(ventanaVerCitasl, text="¿De que especialista desea saber las citas libres?")
    Lhora = Label(ventanaVerCitasl, text="¿De que horario desea saber las citas libres?")

    Eespecialista = Entry(ventanaVerCitasl, width=20)
    Ehora = Entry(ventanaVerCitasl, width=20)
    Emensajee = Entry(ventanaVerCitasl, width=20)
    Emensajeh = Entry(ventanaVerCitasl, width=20)
    libresespe = Button(ventanaVerCitasl, text="Ver Citas libres del Espacialista", command=citaslibresE)
    libreshora = Button(ventanaVerCitasl, text="Ver Citas libres del Horario", command=citaslibresH)
    #cerrarventana = Button(ventanaVerCitasl, text="Cerrar la ventana", command=VerCitaslibres.destroy)

    Lespecialista.pack(pady=10)
    Eespecialista.pack(pady=10)
    libresespe.pack(pady=10)
    Emensajee.pack(pady=10)
    Lhora.pack(pady=10)
    Ehora.pack(pady=10)
    libreshora.pack(pady=10)
    Emensajeh.pack(pady=10)
    cerrarventana.pack(pady=8)

def Estadisticas():
    ventanaEstadisticas = Toplevel()
    ventanaEstadisticas.geometry("400x300")
    ventanaEstadisticas.title("Estadisticas")
    def estadisticasespecia():
        suma1=0
        suma2=0
        suma3=0
        suma4=0
        suma5=0
        porcentajesE=[0]*6
        for j in range(1,6,1):
          for i in range(1,14,1):
            if j == 1:
              suma1+=tabla[i][j]
              porcentaje=(suma1/13)*100
            if j == 2:
              suma2+=tabla[i][j]
              porcentaje=(suma2/13)*100
            if j == 3:
              suma3+=tabla[i][j]
              porcentaje=(suma3/13)*100
            if j == 4:
              suma4+=tabla[i][j]
              porcentaje=(suma4/13)*100
            if j == 5:
              suma5+=tabla[i][j]
              porcentaje=(suma5/13)*100
          redondeado=round(porcentaje,2)
          porcentajesE[j]=redondeado
        mayor=max(porcentajesE)
        pos=porcentajesE.index(mayor)
        esp=especialidades[pos]
        print(mayor)
        print(pos)
        print(esp)
        Emensajee.delete(0,END)
        Emensajee.insert(0,)
        
    Lespecialista = Label(ventanaEstadisticas,text="¿De que especialista desea saber las estadisticas?")
    Lhorario = Label(ventanaEstadisticas,text="¿De que horario desea saber las estadisticas?")
    Eespecialista = Entry(ventanaEstadisticas,width=20)
    Ehorario = Entry(ventanaEstadisticas,width=20)
    Emensajee = Entry(ventanaEstadisticas,width=20)
    Emensajeep = Entry(ventanaEstadisticas,width=20)
    Emensajeh = Entry(ventanaEstadisticas,width=20)
    Emensajehp = Entry(ventanaEstadisticas,width=20)
    cerrarventana = Button(ventanaEstadisticas, text="Cerrar la ventana", command=ventanaEstadisticas.destroy)
    botonEh = Button(ventanaEstadisticas,text="Ver Estadisticas por Hora", font=8, command=Estadisticashora)
    botonEe = Button(ventanaEstadisticas,text="Ver Estadisticas por Especialista", font=8, command=estadisticasespecia).grid(row=0, column=1)
    Lespecialista.pack(pady=8)
    Eespecialista.pack(pady=8)
    botonEe.pack(pady=8)
    Emensajee.pack(pady=8)
    Emensajep.pack(pady=8)
    Lhorario.pack(pady=8)
    Ehorario.pack(pady=8)
    botonEh.pack(pady=8)
    cerrarventana.pack(pady=8)
    
gui = Tk()
gui.title("Ventana principal")
gui.geometry("600x500")
panelBotones = Frame(gui)

titulo = Label(gui,text="Hospital Universidad del Valle", font=20)
especialidades=["Especia","Dermatologia","Urologia","Ginecologia","Traumatologia","Odontologia"]
horario=["Horario","10:00 AM","10:30 AM","11:00 AM","11:30 AM","1:00 PM","1:30 PM","2:00 PM","2:30 PM",
         "3:00 PM","3:30 PM","4:00 PM","4:30 PM","5:00 PM"]
tabla = numpy.empty((14,6),dtype='object')
tabla[0][0]= "Horar/Espe"
tabla[0][1]= "Dermatologia"
tabla[0][2]= "Urologia"
tabla[0][3]= "Ginecologia"
tabla[0][4]= "Traumatologia"
tabla[0][5]= "Odontologia"
tabla[1][0]= "10:00 AM"
tabla[2][0]= "10:30 AM"
tabla[3][0]= "11:00 AM"
tabla[4][0]= "11:30 AM"
tabla[5][0]= "1:00 PM"
tabla[6][0]= "1:30 PM"
tabla[7][0]= "2:00 PM"
tabla[8][0]= "2:30 PM"
tabla[9][0]= "3:00 PM"
tabla[10][0]= "3:30 PM"
tabla[11][0]= "4:00 PM"
tabla[12][0]= "4:30 PM"
tabla[13][0]= "5:00 PM"
nombres=[]
nombres.append("Nombres")
años=[]
años.append("Años")
nidentidad=[]
nidentidad.append("Identidad")

botonA = Button(gui,text="Agendar Cita", font=3, command=AgendarCitas)
botonR = Button(gui,text="Reasignar Citas", font=8, command=ReasignarCitas)
botonC = Button(gui,text="Ver sus Citas", font=8, command=VerCitas)
botonCl = Button(gui,text="Ver sus Citas Libres", font=8, command=VerCitaslibres)
botonE = Button(gui,text="Estadisticas", font=8, command=Estadisticas)

titulo.pack(pady=10) 
botonA.pack(pady=8)
botonR.pack(pady=8)
botonC.pack(pady=10)
botonCl.pack(pady=10)
botonE.pack(pady=5)


