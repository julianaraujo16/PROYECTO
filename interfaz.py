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
        hora = Efecha.get()
        for e in range(0,6):
            especialis=especialidades[e]
            if especi.lower() == especialis.lower():
                c=e
        for a in range(0,14):
            h=horario[a]
            if hora.lower() == h.lower():
                f=a
        if tabla[f][c] == 0:
            tabla[f][c] = 1
            mensaje="¡Se ha agendado su cita exitosamente!"
        else:
            mensaje="El horario selecccionado ya se encuentra ocupado"

        Emensaje.delete(0,END)
        Emensaje.insert(0,mensaje)

    Lnombre = Label(panel, text="Nombre Completo: ", pady=8).grid(row=0, column=0)
    Laño = Label(panel, text="Edad: ", pady=8).grid(row=1, column=0)
    Lidentidad = Label(panel, text="Numero de Identidad: ", pady=8).grid(row=2, column=0)
    Lespeci = Label(ventanaAgendarCitas, text="¿Con que especialista desea agendar su cita?")
    Lespecin = Label(ventanaAgendarCitas, text="(Dermatologia-Urologia-Ginecologia-Traumatologia-Odontologia)")
    Lfecha = Label(ventanaAgendarCitas, text="Ingrese el que fecha desea agendar su cita")
    Lfehah = Label(ventanaAgendarCitas, text="(De 10:00 AM a 11:30 y de 1:00 PM hasta a 5:00 PM)")

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
    Lespecin.pack()
    Eespeci.pack(pady=8)
    Lfecha.pack(pady=8)
    Lfehah.pack()
    Efecha.pack(pady=8)
    Bagendar.pack(pady=8)
    Emensaje.pack(pady=8)
    cerrarventana.pack(pady=20
                       )

def ReasignarCitas():
    ventanaReasignarCitas = Toplevel()
    ventanaReasignarCitas.geometry("500x500")
    ventanaReasignarCitas.title("Reasignar Citas")
    def reagendar():
        especi = Evespeci.get()
        hora = Evfecha.get()
        for e in range(0,6):
            especialis=especialidades[e]
            if especi.lower() == especialis.lower():
                c=e
        for a in range(0,14):
            h=horario[a]
            if hora.lower() == h.lower():
                f=a
        if tabla[f][c] == 1:
            tabla[f][c] = 0
        else:
            rmensaje="El horario selecccionado no se encuentra niguna cita asignada"

        nespeci = Enuevoespeci.get()
        nhora = Enuevafecha.get()
        for e in range(0,6):
          especialis=especialidades[e]
          if nespeci.lower() == especialis.lower():
            c=e          
        for a in range(0,14):
            h=horario[a]
            if nhora.lower() == h.lower():
                f=a
        if tabla[f][c] == 0:
            tabla[f][c] = 1
            rmensaje="¡Se ha reasignado su cita exitosamente!"
        else:
            rmensaje="El horario selecccionado no se encuentra ocupado"
        Ermensaje.delete(0,END)
        Ermensaje.insert(0,rmensaje)

    Lespecin = Label(ventanaReasignarCitas, text="(Dermatologia-Urologia-Ginecologia-Traumatologia-Odontologia)")
    Lvespeci = Label(ventanaReasignarCitas, text="¿Con que especialista agendó su cita?: ")
    Lvfecha = Label(ventanaReasignarCitas, text="¿En que hora agendó su cita?")
    Lhora = Label(ventanaReasignarCitas, text="(De 10:00 AM a 11:30 y de 1:00 PM hasta a 5:00 PM)")
    Lnuevoespe = Label(ventanaReasignarCitas, text="Ingrese el especialista con el que desea agendar su nueva cita")
    Lnuevafecha = Label(ventanaReasignarCitas, text="Ingrese la hora en la que desea agendar su nueva cita")
    
    Evespeci = Entry(ventanaReasignarCitas, width=20)
    Evfecha = Entry(ventanaReasignarCitas, width=20)
    Ermensaje = Entry(ventanaReasignarCitas, width=40)
    Enuevoespeci = Entry(ventanaReasignarCitas, width=20)
    Enuevafecha = Entry(ventanaReasignarCitas, width=20)
    
    Breagendar = Button(ventanaReasignarCitas, text="Reasignar Cita", command=reagendar)
    cerrarventana = Button(ventanaReasignarCitas, text="Cerrar la ventana", command=ventanaReasignarCitas.destroy)

    Lvespeci.pack(pady=10)
    Lespecin.pack()
    Evespeci.pack(pady=10)
    Lvfecha.pack(pady=10)
    Lhora.pack()
    Evfecha.pack(pady=10)
    Lnuevoespe.pack(pady=10)
    Enuevoespeci.pack(pady=10)
    Lnuevafecha.pack(pady=10)
    Enuevafecha.pack(pady=10)
    Breagendar.pack(pady=10)
    Ermensaje.pack(pady=10)
    cerrarventana.pack(pady=20)

def VerCitas():
    ventanaVerCitas = Toplevel()
    ventanaVerCitas.geometry("900x900")
    ventanaVerCitas.title("Ver Citas")
    cerrarventana = Button(ventanaVerCitas, text="Cerrar la ventana", command=ventanaVerCitas.destroy)
    cerrarventana.pack(pady=10)

def VerCitaslibres():
    ventanaVerCitasl = Toplevel()
    ventanaVerCitasl.geometry("400x400")
    ventanaVerCitasl.title("Ver Citas Libres")
    
    def citaslibresE():
        especialista=Eespecialista.get()
        for e in range(0,6):
            especialis=especialidades[e]
            if especialista.lower() == especialis.lower():
                c=e
        libre = 0
        for j in range(1,6,1):
            for i in range(1,14,1):
              if j == c:
                if tabla[i][j] == 0:
                    libre+=1
                    mensajee=libre
        Emensajee.delete(0,END)
        Emensajee.insert(0,mensajee)

    def citaslibresH():
        hora=Ehora.get()
        for a in range(0,14):
            h=horario[a]
            if hora.lower() == h.lower():
                f=a
        libre = 0
        for j in range(1,6,1):
            for i in range(1,14,1):
                if i == f:
                    if tabla[i][j] == 0:
                        libre+=1
        mensajeh=libre
        Emensajeh.delete(0,END)
        Emensajeh.insert(0,mensajeh)
        
    Lespe = Label(ventanaVerCitasl, text="Especialista")
    Lho = Label(ventanaVerCitasl, text="Horario")
    Lespecialista = Label(ventanaVerCitasl, text="¿De que especialista desea saber el total citas libres?")
    Lhora = Label(ventanaVerCitasl, text="¿De que hora desea saber el total citas libres?")

    Eespecialista = Entry(ventanaVerCitasl, width=20)
    Ehora = Entry(ventanaVerCitasl, width=20)
    Emensajee = Entry(ventanaVerCitasl, width=10)
    Emensajeh = Entry(ventanaVerCitasl, width=10)
    libresespe = Button(ventanaVerCitasl, text="Ver Citas libres", command=citaslibresE)
    libreshora = Button(ventanaVerCitasl, text="Ver Citas libres", command=citaslibresH)
    cerrarventana = Button(ventanaVerCitasl, text="Cerrar la ventana", command=ventanaVerCitasl.destroy)
    Lespe.pack()
    Lespecialista.pack(pady=5)
    Eespecialista.pack()
    libresespe.pack(pady=10)
    Emensajee.pack(pady=10)
    Lho.pack()
    Lhora.pack(pady=5)
    Ehora.pack(pady=10)
    libreshora.pack(pady=10)
    Emensajeh.pack()
    cerrarventana.pack(pady=30)

def Estadisticas():
    ventanaEstadisticas = Toplevel()
    ventanaEstadisticas.geometry("600x600")
    ventanaEstadisticas.title("Estadisticas")
    panelmayor1=Frame(ventanaEstadisticas)
    panelmayor2=Frame(ventanaEstadisticas)
    panelresultadosmator1=Frame(ventanaEstadisticas)
    panelresultadosmator2=Frame(ventanaEstadisticas)

    def estadisticasespecialista():
        esp = Eespecialista.get()
        for e in range(0,6):
            especialis=especialidades[e]
            if esp.lower() == especialis.lower():
                c=e
        suma=0
        for j in range(1,6,1):
            for i in range(1,14,1):
                if j == c:
                    suma+=tabla[i][j]
                    porcen=(suma/13)*100
                    redondeado=round(porcen,2)

        Emensajeep.delete(0,END)
        Emensajeep.insert(0,redondeado)
        
    def estadisticashora():
        hora = Ehorario.get()
        for a in range(0,14):
            h=horario[a]
            if hora.lower() == h.lower():
                f=a
        suma=0
        for i in range(1,14,1):
            for j in range(1,6,1):
                if i == f:
                    suma+=tabla[i][j]
                    porcentaje=(suma/5)*100
                    redondea=round(porcentaje,2)
        Emensajehp.delete(0,END)
        Emensajehp.insert(0,redondea)
        
    def estadisticasespeciamayor():
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
        
        Emensajemen.delete(0,END)
        Emensajemen.insert(0,esp)
        Emensajemem.delete(0,END)
        Emensajemem.insert(0,mayor)
        
    def estadisticashoramayor():
          suma1=0
          suma2=0
          suma3=0
          suma4=0
          suma5=0
          suma6=0
          suma7=0
          suma8=0
          suma9=0
          suma10=0
          suma11=0
          suma12=0
          suma13=0
          porcentajesH=[0]*14
          for i in range(1,14,1):
            for j in range(1,6,1):
              if i == 1:
                suma1+=tabla[i][j]
                porcentaje=(suma1/5)*100
              if i == 2:
                suma2+=tabla[i][j]
                porcentaje=(suma2/5)*100
              if i == 3:
                suma3+=tabla[i][j]
                porcentaje=(suma3/5)*100
              if i == 4:
                suma4+=tabla[i][j]
                porcentaje=(suma4/5)*100
              if i == 5:
                suma5+=tabla[i][j]
                porcentaje=(suma5/5)*100
              if i == 6:
                suma6+=tabla[i][j]
                porcentaje=(suma6/5)*100
              if i == 7:
                suma7+=tabla[i][j]
                porcentaje=(suma7/5)*100
              if i == 8:
                suma8+=tabla[i][j]
                porcentaje=(suma8/5)*100
              if i == 9:
                suma9+=tabla[i][j]
                porcentaje=(suma9/65)*100
              if i == 10:
                suma10+=tabla[i][j]
                porcentaje=(suma10/5)*100
              if i == 11:
                suma11+=tabla[i][j]
                porcentaje=(suma11/5)*100
              if i == 12:
                suma12+=tabla[i][j]
                porcentaje=(suma12/5)*100
              if i == 13:
                suma13+=tabla[i][j]
                porcentaje=(suma13/5)*100
            redondeado = round(porcentaje,2)
            porcentajesH[i]=redondeado
          mayor=max(porcentajesH)
          pos=porcentajesH.index(mayor)
          ho=horario[pos]
          Emensajemhh.delete(0,END)
          Emensajemhh.insert(0,ho)
          Emensajemhm.delete(0,END)
          Emensajemhm.insert(0,mayor)

    Lespecialist = Label(ventanaEstadisticas,text="Porcentaje de citas por Especialistas",pady=10)
    Lespecialista = Label(ventanaEstadisticas,text="¿De que especialista desea saber el porcentaje?")
    Lhorar = Label(ventanaEstadisticas,text="Porcentaje de citas por Horario",pady=10)
    Lmayores = Label(ventanaEstadisticas,text="¿Desea saber que especialista tiene mayor numero de citas registradas?")
    Lmayorho = Label(ventanaEstadisticas,text="¿Desea saber que horario tiene el mayor numero de citas registradas?")
    Lhorario = Label(ventanaEstadisticas,text="¿De que horario desea saber el porcentaje?")
    Lnombreesm = Label(panelresultadosmator1,text="Especialistas").grid(row=0,column=0)
    Lespem = Label(panelresultadosmator1,text="Porcentaje %").grid(row=1,column=0)
    Lhoram = Label(panelresultadosmator2,text="Hora").grid(row=0,column=0)
    Lhorariom = Label(panelresultadosmator2,text="Porcentaje %").grid(row=1,column=0)

    Eespecialista = Entry(ventanaEstadisticas,width=20)
    Ehorario = Entry(ventanaEstadisticas,width=20)
    Emensajee = Entry(ventanaEstadisticas,width=20)
    Emensajeep = Entry(ventanaEstadisticas,width=15)
    Emensajeh = Entry(ventanaEstadisticas,width=20)
    Emensajehp = Entry(ventanaEstadisticas,width=15)
    Emensajeme = Entry(ventanaEstadisticas,width=10)
    Emensajemh = Entry(ventanaEstadisticas,width=10)
    Emensajemen = Entry(panelresultadosmator1,width=13)
    Emensajemen.grid(row=0,column=1)
    Emensajemem = Entry(panelresultadosmator1,width=10)
    Emensajemem.grid(row=1,column=1)
    Emensajemhh = Entry(panelresultadosmator2,width=10)
    Emensajemhh.grid(row=0,column=1)
    Emensajemhm = Entry(panelresultadosmator2,width=10)
    Emensajemhm.grid(row=1,column=1)

    cerrarventana = Button(ventanaEstadisticas, text="Cerrar la ventana", command=ventanaEstadisticas.destroy)
    botonEh = Button(ventanaEstadisticas,text="Ver %", command=estadisticashora)
    botonEe = Button(ventanaEstadisticas,text="Ver %", command=estadisticasespecialista)
    botonMes = Button(panelmayor1,text="Si", width=7, command=estadisticasespeciamayor).grid(row=0,column=0)
    botonMen = Button(panelmayor1,text="No", width=7).grid(row=0,column=1)
    botonMhs = Button(panelmayor2,text="Si", width=7, command=estadisticashoramayor).grid(row=0,column=0)
    botonMhn = Button(panelmayor2,text="No", width=7).grid(row=0,column=1)

    Lespecialist.pack()
    Lespecialista.pack()
    Eespecialista.pack(pady=5)
    botonEe.pack(pady=5)
    Emensajee.pack(pady=5)
    Lmayores.pack(pady=5)
    panelmayor1.pack(pady=5)
    panelresultadosmator1.pack(pady=5)
    Lhorar.pack()
    Lhorario.pack()
    Ehorario.pack(pady=8)
    botonEh.pack(pady=8)
    Emensajehp.pack(pady=5)
    Lmayorho.pack(pady=5)
    panelmayor2.pack(pady=5)
    panelresultadosmator2.pack(pady=5)
    cerrarventana.pack(pady=20)
    
gui = Tk()
gui.title("Ventana principal")
gui.geometry("600x500")
panelBotones = Frame(gui)

titulo = Label(gui,text="Hospital Universidad del Valle", font=20, pady=20)
especialidades=["Especia","Dermatologia","Urologia","Ginecologia","Traumatologia","Odontologia"]
horario=["Horario","10:00 AM","10:30 AM","11:00 AM","11:30 AM","1:00 PM","1:30 PM","2:00 PM","2:30 PM"
         ,"3:00 PM","3:30 PM","4:00 PM","4:30 PM","5:00 PM"]
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
for i in range(1,14,1):
  for j in range(1,6,1):
    tabla[i][j]=random.randint(0,1)
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
botonA.pack(pady=10)
botonR.pack(pady=10)
botonC.pack(pady=10)
botonCl.pack(pady=10)
botonE.pack(pady=10)
