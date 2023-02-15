from tkinter import *

root=Tk()

miFrame=Frame(root)

miFrame.pack() #se hace esto para que le de un tamaño por defecto
operacion=""
resultado=0
# -------------- Pantalla -------------------------- #

numeroPantalla=StringVar() #

pantalla=Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1,column=1,padx=10,pady=10,columnspan=4) #columnspan sirve para alargar la celda de la pantalla
pantalla.config(background="black",fg="white",justify="right")


# -------------- pulsaciones teclado -------------------------- #

def borradoCE():
    global resultado
    numeroPantalla.set("")
    resultado=0
def numeroPulsado(num):
    global operacion
    
    if operacion != "":
        numeroPantalla.set(num)
        operacion=""
    else:
        numeroPantalla.set(numeroPantalla.get() + num)

    

# -------------- Funcion Suma -------------------------- #

def suma(num):
    global operacion    # esto se hace para que se sepa que voy a trabajar con la variable global operacion
    global resultado
    operacion="suma"
   
    if num.find(".")==True:
        operacionesComa(num)
    else:
        resultado+=int(num)
       

    numeroPantalla.set(resultado)
# -------------- Funcion para mostrar resultado -------------------------- #
def el_resultado():
    global resultado
    if type(resultado)==float or type(numeroPantalla.get())==float:
        numeroPantalla.set(resultado+float(numeroPantalla.get()))
    else:
        numeroPantalla.set(resultado+int(numeroPantalla.get()))
    
    resultado=0

def poner_punto():
    numero_a = numeroPantalla.get()
    if numero_a.count(".")==0:
        numeroPulsado(".")
# -------------- Funcion Multiplicacion -------------------------- #
def multiplicacion(num):
    global operacion
    global resultado
    operacion="multiplicacion"
    if  num.find(".")==True:
        #resultado+=float(num)
        operacionesComa(operacion,num)
    else:
        resultado*=int(num)
    numeroPantalla.set(resultado)
    
# -------------- Funcion division -------------------------- #
def division(num):
    global operacion
    global resultado
    operacion="division"
    if  num.find(".")==True:
        #resultado+=float(num)
        operacionesComa(operacion,num)
    else:
        resultado/=int(num)
    numeroPantalla.set(resultado)
    

def resta(num):
    global operacion
    global resultado
    operacion="resta"
    if  num.find(".")==True:
        #resultado+=float(num)
        operacionesComa(num)
    else:
        resultado-=int(num)
         # esto se hace para que se sepa que voy a trabajar con la variable global operacion

    numeroPantalla.set(resultado)

def operacionesComa(num):
    global operacion
    global resultado
    if operacion=="suma":
        resultado= float(resultado) + float(num)
        numeroPantalla.set(resultado)
    elif operacion=="resta":
        resultado=float(resultado) - float(num)
    elif operacion=="multiplicacion":
        resultado=float(resultado) * float(num)
    else:
        resultado=float(resultado) / float(num)

# -------------- botones fila 1 -------------------------- #

boton_7=Button(miFrame,text="7",width=3, command=lambda:numeroPulsado("7"))
boton_7.grid(row=2,column=1)

boton_8=Button(miFrame,text="8",width=3, command=lambda:numeroPulsado("8"))
boton_8.grid(row=2,column=2)

boton_9=Button(miFrame,text="9",width=3, command=lambda:numeroPulsado("9"))
boton_9.grid(row=2,column=3)

boton_div=Button(miFrame,text="/",width=3,command=lambda:division(numeroPantalla.get()))
boton_div.grid(row=2,column=4)


# -------------- botones fila 2 -------------------------- #

boton_4=Button(miFrame,text="4",width=3, command=lambda:numeroPulsado("4"))
boton_4.grid(row=3,column=1)

boton_5=Button(miFrame,text="5",width=3, command=lambda:numeroPulsado("5"))
boton_5.grid(row=3,column=2)

boton_6=Button(miFrame,text="6",width=3, command=lambda:numeroPulsado("6"))
boton_6.grid(row=3,column=3)

boton_multi=Button(miFrame,text="X",width=3, command=lambda:multiplicacion(numeroPantalla.get()))
boton_multi.grid(row=3,column=4)

# -------------- botones fila 3 -------------------------- #

boton_1=Button(miFrame,text="1",width=3, command=lambda:numeroPulsado("1"))
boton_1.grid(row=4,column=1)

boton_2=Button(miFrame,text="2",width=3, command=lambda:numeroPulsado("2"))
boton_2.grid(row=4,column=2)

boton_3=Button(miFrame,text="3",width=3, command=lambda:numeroPulsado("3"))
boton_3.grid(row=4,column=3)

boton_suma=Button(miFrame,text="+",width=3,command=lambda:suma(numeroPantalla.get()))
boton_suma.grid(row=4,column=4)

# -------------- botones fila 4 -------------------------- #

boton_0=Button(miFrame,text="0",width=3, command=lambda:numeroPulsado("0"))
boton_0.grid(row=5,column=1)

boton_coma=Button(miFrame,text=".",width=3, command=lambda:poner_punto())
boton_coma.grid(row=5,column=2)

boton_resta=Button(miFrame,text="-",width=3, command=lambda:resta(numeroPantalla.get()))
boton_resta.grid(row=5,column=3)

boton_igual=Button(miFrame,text="=",width=3, command=lambda:el_resultado())
boton_igual.grid(row=5,column=4)

# -------------- botones fila 4 -------------------------- #

boton_borrarCe=Button(miFrame,text="CE",width=3, command=lambda:borradoCE())
boton_borrarCe.grid(row=6,column=1)



root.mainloop()