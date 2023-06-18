from tkinter import *
from tkinter import ttk
import numpy
import random

def AgendarCitas():
    ventanaAgendarCitas = Toplevel()
    ventanaAgendarCitas.geometry("500x550")
    ventanaAgendarCitas.title("Agendar Citas")
    panel = Frame(ventanaAgendarCitas)
    panelgenero = Frame(ventanaAgendarCitas)
    panelespeci = Frame(ventanaAgendarCitas)
    panelhora = Frame(ventanaAgendarCitas)
    genero = IntVar()
    genero.set(0)
    especialidad = StringVar()
    especialidad.set("Seleccionar")
    horarios = StringVar()
    horarios.set("Seleccionar")

    def agendar():
        nombre = Enombre.get()
        nombres.append(nombre)
        edad = int(Eaño.get())
        edades.append(edad)
        identidad = int(Eidentidad.get())
        nidentidad.append(identidad)
    
        especi = especialidad.get()
        hora = horarios.get()
        
        for e in range(0,6):
            if especi == especialidades[e]:
                c=e
        for a in range(0,14):
            if hora == horario[a]:
                f=a
        if tabla[f][c] == 0:
            tabla[f][c] = identidad
            mensaje="¡Se ha agendado su cita exitosamente!"
        else:
            mensaje="El horario selecccionado ya se encuentra ocupado"
        print(tabla)

        Emensaje.delete(0,END)
        Emensaje.insert(0,mensaje)
        
    Ldatos = Label(ventanaAgendarCitas, text="Complete los Datos",font=("Arial",13), fg="black")
    Lnombre = Label(panel, text="Nombre Completo: ", pady=5).grid(row=0, column=0)
    Laño = Label(panel, text="Edad: ", pady=5).grid(row=1, column=0)
    Lidentidad = Label(panel, text="Numero de Identidad: ", pady=5).grid(row=2, column=0)
    Lespecialidad = Label(panelespeci, text='Especialidad:').grid(row=0, column=0)
    Lespeci = Label(ventanaAgendarCitas, text="¿Con que especialista desea agendar su cita?")
    entradaespeci = OptionMenu(panelespeci,especialidad,"Dermatologia","Urologia","Ginecologia","Traumatologia","Odontologia")
    entradaespeci.grid(row=0, column=1)
    Lfecha = Label(ventanaAgendarCitas, text="¿En que hora desea agendar su cita?")
    Lhorario = Label(panelhora, text="Horario:").grid(row=0, column=0)
    entradahora = OptionMenu(panelhora,horarios,"10:00 AM","10:30 AM","11:00 AM","11:30 AM","1:00 PM","1:30 PM","2:00 PM","2:30 PM","3:00 PM","3:30 PM","4:00 PM","4:30 PM","5:00 PM")
    entradahora.grid(row=0, column=1)
    etiqueta = Label(panelgenero, text='Genero:').grid(row=0, column=0)
    botongm = Radiobutton(panelgenero, text='Masculino', variable=genero, value=1)
    botongm.grid(row=0, column=1)
    botongf = Radiobutton(panelgenero, text='Femenino', variable=genero, value=2)
    botongf.grid(row=0, column=2)

    Enombre = Entry(panel, width=20)
    Enombre.grid(row=0, column=1)
    Eaño = Entry(panel, width=20)
    Eaño.grid(row=1, column=1)
    Eidentidad = Entry(panel, width=20)
    Eidentidad.grid(row=2, column=1)
    Emensaje = Entry(ventanaAgendarCitas, width=45)

    Bagendar = ttk.Button(ventanaAgendarCitas, text="Agendar Cita", width=20, command=agendar)
    cerrarventana = ttk.Button(ventanaAgendarCitas, text="Cerrar la ventana", width=20, command=ventanaAgendarCitas.destroy)

    Ldatos.pack(pady=10)
    panel.pack(pady=8)
    panelgenero.pack(pady=10)
    Lespeci.pack(pady=10)
    panelespeci.pack(pady=10)
    Lfecha.pack(pady=10)
    panelhora.pack(pady=5)
    Bagendar.pack(pady=8)
    Emensaje.pack(pady=8)
    cerrarventana.pack(pady=30)

def ReasignarCitas():
    ventanaReasignarCitas = Toplevel()
    ventanaReasignarCitas.geometry("500x600")
    ventanaReasignarCitas.title("Reasignar Citas")
    paneldatos = Frame(ventanaReasignarCitas)
    vespecialidad = StringVar()
    vespecialidad.set("Seleccionar")
    vhorarios = StringVar()
    vhorarios.set("Seleccionar")
    nespecialidad = StringVar()
    nespecialidad.set("Seleccionar")
    nhorarios = StringVar()
    nhorarios.set("Seleccionar")

    def reagendar():
        identidad = Eidentidad.get()
        especi = vespecialidad.get()
        hora = vhorarios.get()
        for e in range(0,6):
            if especi == especialidades[e]:
                c=e
        for a in range(0,14):
            if hora == horario[a]:
                f=a
        if tabla[f][c] != 0:
            tabla[f][c] = 0
        else:
            rmensaje="El horario selecccionado no se encuentra niguna cita asignada"
        print(tabla)

        nuevoespeci = nespecialidad.get()
        nuevahora = nhorarios.get()
        for e in range(0,6):
          if nuevoespeci == especialidades[e]:
            c=e          
        for a in range(0,14):
            if nuevahora == horario[a]:
                f=a
        if tabla[f][c] == 0:
            tabla[f][c] = identidad
            rmensaje="¡Se ha reasignado su cita exitosamente!"
        else:
            rmensaje="El horario selecccionado se encuentra ocupado"
        print(rmensaje)
        print(tabla)

        Ermensaje.delete(0,END)
        Ermensaje.insert(0,rmensaje)

    Lvespeci = Label(ventanaReasignarCitas, text="¿Con que especialista agendó su cita?: ")
    Lletrero = Label(ventanaReasignarCitas, text='Cita Posteriormente Agendada',font=("Arial",13), fg="black")
    Lespeci = Label(ventanaReasignarCitas, text="¿Con que especialista desea agendar su cita?")
    entradavespeci = OptionMenu(ventanaReasignarCitas,vespecialidad,"Dermatologia","Urologia","Ginecologia","Traumatologia","Odontologia")
    entradavhora = OptionMenu(ventanaReasignarCitas,vhorarios,"10:00 AM","10:30 AM","11:00 AM","11:30 AM","1:00 PM","1:30 PM","2:00 PM","2:30 PM","3:00 PM","3:30 PM","4:00 PM","4:30 PM","5:00 PM")
    Lvhora = Label(ventanaReasignarCitas, text="¿En que hora agendó su cita?")
    Lnuevacita = Label(ventanaReasignarCitas, text="Reasignación de Cita",font=("Arial",13), fg="black")
    Lidentidad = Label(paneldatos, text="Numero de Identidad: ", pady=2).grid(row=0, column=0) 
    Lnuevoespe = Label(ventanaReasignarCitas, text="¿Con que especialista desea agendar su nueva cita")
    entradanuevoespeci = OptionMenu(ventanaReasignarCitas,nespecialidad,"Dermatologia","Urologia","Ginecologia","Traumatologia","Odontologia")
    entradanuevahora = OptionMenu(ventanaReasignarCitas,nhorarios,"10:00 AM","10:30 AM","11:00 AM","11:30 AM","1:00 PM","1:30 PM","2:00 PM","2:30 PM","3:00 PM","3:30 PM","4:00 PM","4:30 PM","5:00 PM")
    Lnuevafecha = Label(ventanaReasignarCitas, text="¿A que hora desea agendar su nueva cita?")
    
    Eidentidad = Entry(paneldatos, width=20)
    Eidentidad.grid(row=0, column=1)
    Ermensaje = Entry(ventanaReasignarCitas, width=40)
    
    Breagendar = ttk.Button(ventanaReasignarCitas, text="Reasignar Cita", width=20, command=reagendar)
    cerrarventana = ttk.Button(ventanaReasignarCitas, text="Cerrar la ventana", width=20, command=ventanaReasignarCitas.destroy)

    Lletrero.pack(pady=10)
    paneldatos.pack(pady=8)
    Lvespeci.pack(pady=8)
    entradavespeci.pack()
    Lvhora.pack(pady=10)
    entradavhora.pack(pady=7)
    Lnuevacita.pack(pady=9)
    Lnuevoespe.pack(pady=7)
    entradanuevoespeci.pack()
    Lnuevafecha.pack(pady=7)
    entradanuevahora.pack()
    Breagendar.pack(pady=15)
    Ermensaje.pack(pady=8)
    cerrarventana.pack(pady=30)

def VerCitas():
    ventanaVerCitas = Toplevel()
    ventanaVerCitas.geometry("400x500")
    ventanaVerCitas.title("Ver Citas")
    panelidentidad = Frame(ventanaVerCitas)
    paneldatos = Frame(ventanaVerCitas)
    panelcita = Frame(ventanaVerCitas)

    def citas():
        citas = 0
        citaslista = ""
        identidad = int(Eidentidad.get())
        for i in range(1,len(nidentidad),1):
            if identidad == nidentidad[i]:
              lugar=i
        nombre=nombres[lugar]
        edad=edades[lugar]
        print(nombre)
        print(edad)
        
        for i in range(1,14,1):
          for j in range(1,6,1):
            if identidad == tabla[i][j]:
              citas+=1
              citaslista = citaslista + tabla[0][j] + " a las " + tabla[i][0] + "\n"
        print(citas)
        print(citaslista)
        
        Enombre.delete(0,END)
        Enombre.insert(0,nombre)
        Eedad.delete(0,END)
        Eedad.insert(0,edad)
        Ecantidad.delete(0,END)
        Ecantidad.insert(0,citas)
        Ecitas.delete(0,END)
        Ecitas.insert(0,citaslista)

    Letiqueta = Label(ventanaVerCitas, text="Sus Citas",font=("Arial",13), fg="black")
    Laviso = Label(ventanaVerCitas, text="Ingrese su Numero de Identidad")
    Lidentidad = Label(panelidentidad, text="Identidad: ").grid(row=0,column=0)
    Ldatos = Label(ventanaVerCitas, text="Datos del Paciente",font=("Arial",13), fg="black")
    Lnombre = Label(paneldatos, text="Nombre: ").grid(row=0,column=0)
    Ledad = Label(paneldatos, text="Edad: ").grid(row=1,column=0)
    Lcita = Label(ventanaVerCitas, text="")
    Lcantidad = Label(panelcita, text="Cantidad de Citas:").grid(row=0,column=0)
    Lcita = Label(ventanaVerCitas, text="Informacion Citas",font=("Arial",13), fg="black")

    Eidentidad = Entry(panelidentidad, width=15)
    Eidentidad.grid(row=0,column=1)
    Enombre = Entry(paneldatos, width=15)
    Enombre.grid(row=0,column=1)
    Eedad = Entry(paneldatos, width=15)
    Eedad.grid(row=1,column=1)
    Ecantidad = Entry(panelcita, width=10)
    Ecantidad.grid(row=0,column=1)
    Ecitas = Entry(ventanaVerCitas, width=30)

    vcitas = ttk.Button(ventanaVerCitas, text="Encontrar", width=20, command=citas)
    cerrarventana = ttk.Button(ventanaVerCitas, text="Cerrar la ventana", width=20, command=ventanaVerCitas.destroy)

    Letiqueta.pack(pady=7)
    Laviso.pack()
    panelidentidad.pack(pady=10)
    vcitas.pack(pady=7)
    Ldatos.pack(pady=10)
    paneldatos.pack(pady=10)
    Lcita.pack(pady=10)
    panelcita.pack(pady=10)
    Ecitas.pack(pady=10)
    cerrarventana.pack(pady=30)

def VerCitaslibres():
    ventanaVerCitasl = Toplevel()
    ventanaVerCitasl.geometry("400x450")
    ventanaVerCitasl.title("Ver Citas Libres")
    panelespecialista=Frame(ventanaVerCitasl)
    panelhorario=Frame(ventanaVerCitasl)
    especialidad = StringVar()
    especialidad.set("Seleccionar")
    horarios = StringVar()
    horarios.set("Seleccionar")

    def citaslibresE():
        especialista=especialidad.get()
        for e in range(0,6):
            if especialista == especialidades[e]:
                c=e
        libre = 0
        for j in range(1,6,1):
            for i in range(1,14,1):
              if j == c:
                if tabla[i][j] == 0:
                    libre+=1
        mensajee=libre
        print(mensajee)
        Emensajee.delete(0,END)
        Emensajee.insert(0,mensajee)

    def citaslibresH():
        hora=horarios.get()
        for a in range(0,14):
            if hora == horario[a]:
                f=a
        libre = 0
        for j in range(1,6,1):
            for i in range(1,14,1):
                if i == f:
                    if tabla[i][j] == 0:
                        libre+=1
        mensajeh=libre
        print(mensajeh)
        Emensajeh.delete(0,END)
        Emensajeh.insert(0,mensajeh)

    Letiqueta = Label(ventanaVerCitasl, text="Citas No Reservadas",font=("Arial",13), fg="black")
    Lespe = Label(panelespecialista, text="Especialista").grid(row=0,column=0)
    Lho = Label(panelhorario, text="Horario").grid(row=0,column=0)
    Lespecialista = Label(ventanaVerCitasl, text="¿De que especialista desea saber el total citas libres?")
    entradaespeci = OptionMenu(panelespecialista,especialidad,"Dermatologia","Urologia","Ginecologia","Traumatologia","Odontologia")
    entradaespeci.grid(row=0,column=1)
    Lhora = Label(ventanaVerCitasl, text="¿De que hora desea saber el total citas libres?")
    entradahora = OptionMenu(panelhorario,horarios,"10:00 AM","10:30 AM","11:00 AM","11:30 AM","1:00 PM","1:30 PM","2:00 PM","2:30 PM","3:00 PM","3:30 PM","4:00 PM","4:30 PM","5:00 PM")
    entradahora.grid(row=0,column=1)
    Emensajee = Entry(ventanaVerCitasl, width=10)
    Emensajeh = Entry(ventanaVerCitasl, width=10)
    
    libresespe = ttk.Button(ventanaVerCitasl, text="Ver Citas libres", width=20, command=citaslibresE)
    libreshora = ttk.Button(ventanaVerCitasl, text="Ver Citas libres", width=20, command=citaslibresH)
    cerrarventana = ttk.Button(ventanaVerCitasl, text="Cerrar la ventana", width=20, command=ventanaVerCitasl.destroy)

    Letiqueta.pack(pady=7)
    Lespecialista.pack(pady=5)
    panelespecialista.pack(pady=7)
    libresespe.pack(pady=6)
    Emensajee.pack(pady=7)
    Lhora.pack(pady=5)
    panelhorario.pack(pady=7)
    libreshora.pack(pady=6)
    Emensajeh.pack(pady=5)
    cerrarventana.pack(pady=30)

def Estadisticas():
    ventanaEstadisticas = Toplevel()
    ventanaEstadisticas.geometry("600x650")
    ventanaEstadisticas.title("Estadisticas")
    panelmayor1=Frame(ventanaEstadisticas)
    panelmayor2=Frame(ventanaEstadisticas)
    panelresultadosmator1=Frame(ventanaEstadisticas)
    panelresultadosmator2=Frame(ventanaEstadisticas)
    especialidad = StringVar()
    especialidad.set("Seleccionar")
    horarios = StringVar()
    horarios.set("Seleccionar")

    def estadisticasespecialista():
        especialista = especialidad.get()
        for e in range(0,6):
            if especialista == especialidades[e]:
                c=e
        suma=0
        for j in range(1,6,1):
            for i in range(1,14,1):
                if j == c:
                    if tabla[i][j] != 0:
                        suma+=1
                        porcen=(suma/13)*100
                        redondeado=round(porcen,2)
        print(redondeado)
        Emensajep.delete(0,END)
        Emensajep.insert(0,redondeado)
        
    def estadisticashora():
        hora = horarios.get()
        for a in range(0,14):
            if hora == horario[a]:
                f=a
        suma=0
        for i in range(1,14,1):
            for j in range(1,6,1):
                if i == f:
                    if tabla[i][j] != 0:
                        suma+=1
                        porcentaje=(suma/5)*100
                        redondea=round(porcentaje,2)
        print(redondea)
        Emensajehp.delete(0,END)
        Emensajehp.insert(0,redondea)
        
    def estadisticasEspeciaMayor():
          suma1=0
          suma2=0
          suma3=0
          suma4=0
          suma5=0
          porcentajesE=[0]*6
          for j in range(1,6,1):
            for i in range(1,14,1):
              if j == 1:
                if tabla[i][j] != 0:
                  suma1+=1
                  porcentaje=(suma1/13)*100
              if j == 2:
                if tabla[i][j] != 0:
                  suma2+=1
                  porcentaje=(suma2/13)*100
              if j == 3:
                if tabla[i][j] != 0:
                  suma3+=1
                  porcentaje=(suma3/13)*100
              if j == 4:
                if tabla[i][j] != 0:
                  suma4+=1
                  porcentaje=(suma4/13)*100
              if j == 5:
                if tabla[i][j] != 0:
                  suma5+=1
                  porcentaje=(suma5/13)*100
            redondeado=round(porcentaje,2)
            print("La especialidades de",especialidades[j],"tiene un",redondeado,"% citas agendadas")
            porcentajesE[j]=redondeado
          mayor=max(porcentajesE)
          pos=porcentajesE.index(mayor)
          esp=especialidades[pos]
          Emensajemen.delete(0,END)
          Emensajemen.insert(0,esp)
          Emensajemem.delete(0,END)
          Emensajemem.insert(0,mayor)
          
    def estadisticasHoraMayor():
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
            if tabla[i][j] != 0:
              suma1+=1
              porcentaje=(suma1/5)*100
          if i == 2:
            if tabla[i][j] != 0:
              suma2+=1
              porcentaje=(suma2/5)*100
          if i == 3:
            if tabla[i][j] != 0:
              suma3+=1
              porcentaje=(suma3/5)*100
          if i == 4:
            if tabla[i][j] != 0:
              suma4+=1
              porcentaje=(suma4/5)*100
          if i == 5:
            if tabla[i][j] != 0:
              suma5+=tabla[i][j]
              porcentaje=(suma5/5)*100
          if i == 6:
            if tabla[i][j] != 0:
              suma6+=1
              porcentaje=(suma6/5)*100
          if i == 7:
            if tabla[i][j] != 0:
              suma7+=1
              porcentaje=(suma7/5)*100
          if i == 8:
            if tabla[i][j] != 0:
              suma8+=1
              porcentaje=(suma8/5)*100
          if i == 9:
            if tabla[i][j] != 0:
              suma9+=1
              porcentaje=(suma9/65)*100
          if i == 10:
            if tabla[i][j] != 0:
              suma10+=1
              porcentaje=(suma10/5)*100
          if i == 11:
            if tabla[i][j] != 0:
              suma11+=1
              porcentaje=(suma11/5)*100
          if i == 12:
            if tabla[i][j] != 0:
              suma12+=1
              porcentaje=(suma12/5)*100
          if i == 13:
            if tabla[i][j] != 0:
              suma13+=1
              porcentaje=(suma13/5)*100
        redondeado = round(porcentaje,2)
        print("A las",tabla[i][0],"se registra un",redondeado,"% de citas agendadas")
        porcentajesH[i]=redondeado
      mayor=max(porcentajesH)
      pos=porcentajesH.index(mayor)
      ho=horario[pos]
      Emensajemhh.delete(0,END)
      Emensajemhh.insert(0,ho)
      Emensajemhm.delete(0,END)
      Emensajemhm.insert(0,mayor)

    Lespecialist = Label(ventanaEstadisticas,text="Porcentaje de Citas por Especialistas",font=("Arial",13), fg="black",pady=10)
    Lespecialista = Label(ventanaEstadisticas,text="¿De que especialista desea saber el porcentaje?")
    entradaespeci = OptionMenu(ventanaEstadisticas,especialidad,"Dermatologia","Urologia","Ginecologia","Traumatologia","Odontologia")
    Lhorar = Label(ventanaEstadisticas,text="Porcentaje de Citas por Horario",font=("Arial",13), fg="black",pady=10)
    Lmayores = Label(ventanaEstadisticas,text="¿Desea saber que especialista tiene mayor numero de citas registradas?")
    Lmayorho = Label(ventanaEstadisticas,text="¿Desea saber que horario tiene el mayor numero de citas registradas?")
    entradahora = OptionMenu(ventanaEstadisticas,horarios,"10:00 AM","10:30 AM","11:00 AM","11:30 AM","1:00 PM","1:30 PM","2:00 PM","2:30 PM","3:00 PM","3:30 PM","4:00 PM","4:30 PM","5:00 PM")
    Lhorario = Label(ventanaEstadisticas,text="¿De que hora desea saber el porcentaje?")
    Lnombreesm = Label(panelresultadosmator1,text="Especialistas: ").grid(row=0,column=0)
    Lespem = Label(panelresultadosmator1,text=" con ").grid(row=0,column=2)
    Lespep = Label(panelresultadosmator1,text=" % ").grid(row=0,column=4)
    Lhoram = Label(panelresultadosmator2,text="Hora:").grid(row=0,column=0)
    Lespem = Label(panelresultadosmator2,text=" con ").grid(row=0,column=2)
    Lhorariom = Label(panelresultadosmator2,text=" % ").grid(row=0,column=4)

    Emensajep = Entry(ventanaEstadisticas,width=15)
    Emensajehp = Entry(ventanaEstadisticas,width=15)
    Emensajemh = Entry(ventanaEstadisticas,width=10)
    Emensajemen = Entry(panelresultadosmator1,width=13)
    Emensajemen.grid(row=0,column=1)
    Emensajemem = Entry(panelresultadosmator1,width=7)
    Emensajemem.grid(row=0,column=3)
    Emensajemhh = Entry(panelresultadosmator2,width=10)
    Emensajemhh.grid(row=0,column=1)
    Emensajemhm = Entry(panelresultadosmator2,width=7)
    Emensajemhm.grid(row=0,column=3)

    botonEh = ttk.Button(ventanaEstadisticas,text="Ver %", width=10, command=estadisticashora)
    botonEe = ttk.Button(ventanaEstadisticas,text="Ver %", width=10, command=estadisticasespecialista)
    botonMes = ttk.Button(panelmayor1,text="Si", width=7, command=estadisticasEspeciaMayor).grid(row=0,column=0)
    botonMen = ttk.Button(panelmayor1,text="No", width=7).grid(row=0,column=1)
    botonMhs = ttk.Button(panelmayor2,text="Si", width=7, command=estadisticasHoraMayor).grid(row=0,column=0)
    botonMhn = ttk.Button(panelmayor2,text="No", width=7).grid(row=0,column=1)
    cerrarventana = Button(ventanaEstadisticas, text="Cerrar la ventana", width=20, command=ventanaEstadisticas.destroy)

    Lespecialist.pack(pady=10)
    Lespecialista.pack()
    entradaespeci.pack()
    botonEe.pack(pady=5)
    Emensajep.pack(pady=5)
    Lmayores.pack(pady=5)
    panelmayor1.pack(pady=5)
    panelresultadosmator1.pack(pady=5)
    Lhorar.pack(pady=10)
    Lhorario.pack()
    entradahora.pack(pady=5)
    botonEh.pack(pady=5)
    Emensajehp.pack(pady=5)
    Lmayorho.pack(pady=5)
    panelmayor2.pack(pady=5)
    panelresultadosmator2.pack(pady=5)
    cerrarventana.pack(pady=30)
    
root = Tk()
root.title("Ventana principal")
root.geometry("600x500")

titulo = ttk.Label(root,text="Hospital Universidad del Valle", font=('Courier', 18, 'bold'))

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
print(tabla)

nombres=[]
nombres.append("Nombres")
edades=[]
edades.append("Años")
nidentidad=[]
nidentidad.append("Identidad")

botonA = ttk.Button(root,text="Agendar Cita", width=20, command=AgendarCitas)
botonR = ttk.Button(root,text="Reasignar Citas", width=20, command=ReasignarCitas)
botonC = ttk.Button(root,text="Ver sus Citas", width=20, command=VerCitas)
botonCl = ttk.Button(root,text="Ver Citas Libre", width=20, command=VerCitaslibres)
botonE = ttk.Button(root,text="Estadisticas", width=20, command=Estadisticas)

titulo.pack(pady=40) 
botonA.pack(pady=15)
botonR.pack(pady=15)
botonC.pack(pady=15)
botonCl.pack(pady=15)
botonE.pack(pady=15)
root.mainloop()
