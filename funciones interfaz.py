import numpy
import random
especialidades=["Especia","Dermatologia","Urologia","Ginecologia","Traumatologia","Odontologia"]
horario=["Horario","10:00 AM","10:30 AM","11:00 AM","11:30 AM","1:00 PM","1:30 PM","2:00 PM","2:30 PM"
         ,"3:00 PM","3:30 PM","4:00 PM","4:30 PM","5:00 PM"]
tabla= numpy.empty((14,6),dtype='object')
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

print("1-Agendar, 2-Reagendar, 3-Mostar Tabla, 4-Estadicticas Hora, 5-Estadicticas Especialista")
print("6-Ver citas, 7-CitaslibresE, 8-citaslibresE, 9-Especialista Mayor")
nombres=[]
nombres.append("Nombres")
edades=[]
edades.append("Años")
nidentidad=[]
nidentidad.append("Identidad")

def agendar():
    nombre = input("Nombre Completo: ")
    nombres.append(nombre)
    edad = input("Edad: ")
    edades.append(edad)
    identidad = int(input("Numero de Identidad: "))
    nidentidad.append(identidad)
    especi = input("¿Con que especialista desea agendar su cita?: ")
    hora = input("Ingrese el que fecha desea agendar su cita: ")
    for e in range(0,6):
      if especi == especialidades[e]:
        c=e
    for a in range(0,14):
      if hora == horario[a]:
        f=a
    if tabla[f][c] == 0:
      tabla[f][c] = identidad
      print("Se ha agendado su cita exitosamente con",especi,"a las",hora)
    else:
      print("El horario selecccionado ya se encuentra ocupado\n")
    print(tabla)
    
def reagendar():
    identidad = int(input("Numero de Identidad: "))
    especi = input("¿Con que especialista agendo su cita?: ")
    hora = input("Ingrese en que hora agendo su cita: ")
    for e in range(0,6):
      if especi == especialidades[e]:
        c=e
    for a in range(0,14):
      if hora == horario[a]:
        f=a
    if tabla[f][c] != 0:
      tabla[f][c] = 0
    else:
      print("El horario selecccionado no se encuentra niguna cita asignada\n")
    print(tabla)
    
    nuevoespeci = input("\n¿Con que especialista desea agendar su nueva cita?: ")
    nuevohora = input("Ingrese a que hora desea agendar su nueva cita: ")
    for e in range(0,6):
      if nuevoespeci == especialidades[e]:
        c=e
    for a in range(0,14):
      if nuevohora == horario[a]:
        f=a
    if tabla[f][c] == 0:
      tabla[f][c] = identidad
      print("Se ha agendado su cita exitosamente")
    else:
      print("El horario selecccionado ya se encuentra ocupado\n")
    print(tabla)
    
def estadisticashora():
    es = input("De cual es especilistas desea ver las estadisticas: ")
    for e in range(0,6):
      if es == especialidades[e]:
        c=e
    suma=0
    for j in range(1,6,1):
      for i in range(1,14,1):
        if j == c:
          if tabla[i][j] != 0:
            suma+=1
            porcen=(suma/13)*100
            redondea=round(porcen,2)
    print(redondea)
  
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
  print(porcentajesH)
  mayor=max(porcentajesH)
  pos=porcentajesH.index(mayor)
  ho=horario[pos]
  print(mayor)
  print(pos)
  print(ho)
  
def estadisticasespecia():
    es = input("De cual es especilistas desea ver las estadisticas: ")
    for e in range(0,6):
      if es == especialidades[e]:
        c=e
    suma=0
    for j in range(1,6,1):
      for i in range(1,14,1):
        if j == c:
          if tabla[i][j] != 0:
            suma+=1
            porcen=(suma/13)*100
            redondea=round(porcen,2)
    print(redondea)
    
def estadisticashora():
  suma=0
  hora = input("De cual hora desea ver las estadisticas: ")
  for a in range(0,14):
    if hora == horario[a]:
      f=a
  for i in range(1,14,1):
    for j in range(1,6,1):
      if i == f:
        if tabla[i][j] != 0:
          suma+=1
          porcentaje=(suma/5)*100
          redondea=round(porcentaje,2)
    print(redondea)
    
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
      print(mayor)
      print(pos)
      print(esp)

def vercitas():
    citas = 0
    citaslista = ""
    identidad = int(input("Digite su Numero de Identidad: "))

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
          citas = citas + 1
          citaslista = citaslista + tabla[0][j] + "; " + tabla[i][0] + "\n"
    print(citas)
    print(citaslista)


def citaslibresE():
  especialista = input("¿De que especialista desea saber las citas libres? ")
  for e in range(0,6):
    if especialista == especialidades[e]:
      c=e
  libre = 0
  for j in range(1,6,1):
    for i in range(1,14,1):
      if j == c:
        if tabla[i][j] == 0:
          libre+=1
  print("La especialidades de",especialista,"tiene",libre,"citas libres")

def citaslibresH():
  hora = input("¿De que horario desea saber las citas libres? ")
  for a in range(0,14):
    if hora == horario[a]:
      f=a
  libre = 0
  for j in range(1,6,1):
    for i in range(1,14,1):
      if i == f:
        if tabla[i][j] == 0:
          libre+=1
  print("En el horario de",hora,"se encuentran",libre,"cita/s libre/s")

op=0
while op != 11:
  op = int(input("Digite una opcion "))
  if op == 1:
    agendar()
  if op == 2:
    reagendar()
  if op == 3:
    print(tabla)
  if op == 4:
    estadisticashora()
  if op == 5:
    estadisticasespecia()
  if op == 6:
    vercitas()
  if op == 7:
    citaslibresE()
  if op == 8:
    citaslibresH()
  if op == 9:
    estadisticasespeciamayor()
