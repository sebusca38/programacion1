'''
nombre="analisis de nodo y malla"(en un circuito particular)
version=1.0
descripcion="es una app que calcula atraves de algoritmos de los metodos de malla y nodos las corrientes o voltajes que se nesesiten"
autores="Enrique Ramirez, Daniel Mendez, Pedro Galdames, Matias, Luis"
email="enrique.ramirez@alumnos.uach.cl"
url_proyecto="https://github.com/sebusca38/programacion1/trabajo_final.py"
'''
#importaremos las librerias correspondientes que se ocuparan en el software
import numpy
#le decimos a python que tk es lo mismo tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sys
#declaramos variables que ocuparemos ya sea dentro de una funcion o en el codigo principal de la app
global imagen, circuito, tk, win, r1, r2, r3, r4, r5, v1, v2, vardb, messagebox, ec1, ec2, ec3, result1, result2, result3, resultva, resultvb, imagen2, imagen1, circuito_resultante
#creamos una funcion que se encargara de procesar todos los datos
#ademas de resolve y mostrar las ecuaciones y los datos resultantes pedidos
def calculo_y_generar():
    #primero tenemos que saber si ninguna variable esta vacia
    #por que podria ocasionar un error en los metodos que ocuparemos
    #(nodos y mallas)
    if (not r1.get() or not r2.get() or not r3.get() or not r4.get() or not r5.get() or not v1.get() or not v2.get()):
        #si las variables estan  vacias se le informaran al usuario
        messagebox.showwarning("Cuidado","no has rellenado todas las variables")
    else:
        #en caso de que no esten vacias las variables o entry
        #procedemos a crear funciones dentro dela funcion por que seran llamadas unicamente aqui
        def metodo_nodo():
            #creamos dos listas que seran nuestras filas en la matriz(2x2)
            EC1=[(1/varR1)+(1/varR2)+(1/varR3),-(1/varR3)]
            EC2=[-(1/varR3),(1/varR4)+(1/varR3)+(1/varR5)]
            #procedemos a crear una lista que sera nuestra matriz(2x1)
            V=[(varV1/varR1),(varV2/varR3)]
            #llamamos a nuestra libreria que se encargara de crear las respectivas matrices
            matrix1= numpy.array([EC1,EC2])
            matrix2= numpy.array(V)
            #llamamos de nuevo a la libreria para resolver el sistema
            matrix3= numpy.linalg.solve(matrix1,matrix2)
            #el resultado se nos entraga en una nueva lista
            #le mostramos los resultado al usuario
            result3.configure(text='')
            result1.configure(text='Va= '+str(round(matrix3[0],4)).replace(" ",'')+'V')
            result2.configure(text='Vb= '+str(round(matrix3[1],4)).replace(" ",'')+'V')
        def metodo_malla():
            #creamos tres listas que seran nuestras filas en la matriz(3x3)
            EC1=[varR1+varR2,-varR2,0]
            EC2=[-varR2,varR2+varR3+varR4,-varR4]
            EC3=[0,-varR4,varR5+varR4]
            #procedemos a crear una lista que sera nuestra matriz(3x1)
            V=[varV1,0,varV2]
            #llamamos a nuestra libreria que se encargara de crear las respectivas matrices
            matrix1= numpy.array([EC1,EC2,EC3])
            matrix2= numpy.array(V)
            #llamamos de nuevo a la libreria para resolver el sistema
            matrix3= numpy.linalg.solve(matrix1,matrix2)
            #el resultado se nos entraga en una nueva lista
            #le mostramos los resultado al usuario
            result1.configure(text='I1= '+str(round(matrix3[0],4)).replace(" ",'')+'A')
            result2.configure(text='I2= '+str(round(matrix3[1],4)).replace(" ",'')+'A')
            result3.configure(text='I3= '+str(round(matrix3[2],4)).replace(" ",'')+'A')
        #tenemos que proteger a la app de errores
        #la funcion es que en el caso de que el usuario ingrese letras, se le avise al usuario que cometio ese error
        try:
            #si no hubo ningun error en el ingresado de datos entonces
            #proceguimos a obtener los valores ingresados
            varR1=int(r1.get())
            varR2=int(r2.get())
            varR3=int(r3.get())
            varV1=int(v1.get())
            varR4=int(r4.get())
            varR5=int(r5.get())
            varV2=int(v2.get())
            #nuestro objeto vardb se encargara de decirnos que metodo selecciono
            if (vardb.get()==1):
                #metodo malla
                ec1.configure(text="Ecuacion 1:     "+str(varR1+varR2)+"*(I1) - "+str(varR2)+"*(I2) = "+str(varV1))
                ec2.configure(text="               Ecuacion 2:     "+str(-varR2)+"*(I1) + "+str(varR2+varR3+varR4)+"*(I2) - "+str(varR4)+"*(I2) = 0")
                ec3.configure(text="   Ecuacion 3:   0 I1  "+str(-varR4)+"*(I2) + "+str(varR4+varR5)+"*(I3) = "+str(varV2))
                metodo_malla()
                circuito_resultante.configure(image=imagen1)
            elif (vardb.get()==2):
                #metodo nodo
                ec3.configure(text='')
                ec1.configure(text="Ecuacion 1:     "+str(round((1/varR1+1/varR2+1/varR3),4))+"*Va - "+str(round((1/varR3),4))+"*Vb = "+str(round((varV1/varR1),4)))
                ec2.configure(text="    Ecuacion 2:     "+str(round((-1/varR3),4))+"*Va - "+str(round((1/varR3+1/varR4+1/varR5),4))+"*Vb = "+str(varR4)+str(round((varV2/varR3),4)))
                metodo_nodo()
                circuito_resultante.configure(image=imagen2)
            else:
                #en caso de que no alla seleccionado alguno entonces se le avisara
                messagebox.showwarning("cuidado",'no has seleccionado un metodo de analisis')
        except ValueError:
            #se le avisara al usuario que coloco datos erronios
            messagebox.showwarning("Cuidado",'Solo puedes colocar variables numericas')

#creamos nuestra ventana con tkinter y la personalisamos
win=tk.Tk()
win.iconbitmap('Icono.ico')
win.title("Análisis de mallas y nodos")
win.geometry('880x600')
win.configure(background='snow2')
#declaramos las variables que guardaran el valor de los datos de la app
vardb=tk.IntVar()
#llamamos a la imagenes que ocuparemos a nuestro programas
#se debe colocar la ruta donde estan hubicadas las imagenes
imagen=tk.PhotoImage(file='C:\\Users\\quico\\Desktop\\taller3\\trabajo1\\Circuitos\\Circuito.gif')
imagen1=tk.PhotoImage(file='C:\\Users\\quico\\Desktop\\taller3\\trabajo1\\Circuitos\\Circuito_Mallas.GIF')
imagen2=tk.PhotoImage(file='C:\\Users\\quico\\Desktop\\taller3\\trabajo1\\Circuitos\\Circuito_Nodos.GIF')
#declaramos y colocamos nuestras imagen sin analisar
circuito=tk.Label(image=imagen)
circuito.place(x=0,y=30)
#declaramos los abjetos que van a ir dentro de nuestra ventana
barra=tk.Label(win,text="Circuito ",bg="dark olive green",fg="white")
barra2=tk.Label(win,text="Análisis ",bg="chocolate",fg="white")
radioboton1=ttk.Radiobutton(win, variable=vardb,value=1)
radioboton2=ttk.Radiobutton(win, variable=vardb,value=2)
label1=tk.Label(win,text="  resistencias   (ohms) ",bg="olive drab",fg="white")
lr1=ttk.Label(win)
r1=ttk.Entry(win)
lr2=ttk.Label(win)
r2=ttk.Entry(win)
lr3=ttk.Label(win)
r3=ttk.Entry(win)
lr4=ttk.Label(win)
r4=ttk.Entry(win)
lr5=ttk.Label(win)
r5=ttk.Entry(win)
label2=tk.Label(win,text="  Fuentes de voltaje  (volts)",bg="olive drab",fg="white")
lv1=ttk.Label(win)
v1=ttk.Entry(win)
lv2=ttk.Label(win)
v2=ttk.Entry(win)
Tboton1=ttk.Button(win, command=calculo_y_generar)#obs aqui llamamos a nuestra funcion
barra3=tk.Label(win, text="Resultados", bg="dark olive green",fg="white")
barra4=tk.Label(win,text="  Circuito analisados ",bg="chocolate",fg="white")
barra5=tk.Label(win,text="  Plantamiento de ecuaciones  ",bg="chocolate",fg="white")
barra6=tk.Label(win,text="  Resultados respectivos  ",bg="chocolate",fg="white")
ec3=tk.Label(win, bg="snow2",fg="black")
ec2=tk.Label(win, bg="snow2",fg="black")
ec1=tk.Label(win, bg="snow2",fg="black")
result1=tk.Label(win, bg="snow2",fg="black")
result2=tk.Label(win, bg="snow2",fg="black")
result3=tk.Label(win, bg="snow2",fg="black")
circuito_resultante=tk.Label(win)
#configuramos los objetos de la ventana
barra.configure(bd=1 ,relief="solid")
barra2.configure(bd=1,relief="solid")
barra3.configure(bd=1,relief="solid")
barra4.configure(bd=1,relief="solid")
barra5.configure(bd=1,relief="solid")
barra6.configure(bd=1,relief="solid")
label1.configure(bd=1,relief="solid")
label2.configure(bd=1,relief="solid")
radioboton1.configure(text='Metodo de malla')
radioboton2.configure(text='Metodo de nodos')
lr1.configure(text="R1:")
lr2.configure(text="R2:")
lr3.configure(text="R3:")
lr4.configure(text="R4:")
lr5.configure(text="R5:")
lv1.configure(text="V1:")
lv2.configure(text="V2:")
Tboton1.configure(text='Calcular y generar')
#colocamos los objetos anteriormente configurados en la ventana
barra.place(x=0,y=0,width=435, height=30)
barra2.place(x=435,y=0,width=445, height=30)
radioboton1.place(x=500,y=40)
radioboton2.place(x=650,y=40)
label1.place(x=430,y=65,width=450, height=30)
lr1.place(x=440, y=105)
r1.place(x=460,y=105,width=35, height=25)
lr2.place(x=500, y=105)
r2.place(x=520,y=105, width=35,height=25)
lr3.place(x=560,y=105)
r3.place(x=580,y=105,width=35,height=25)
lr4.place(x=620,y=105)
r4.place(x=640,y=105,width=35,height=25)
lr5.place(x=680,y=105)
r5.place(x=700,y=105,width=35,height=25)
label2.place(x=430,y=135,width=450, height=30)
lv1.place(x=440, y=180)
v1.place(x=460,y=180,width=35, height=25)
v2.place(x=520,y=180, width=35,height=25)
Tboton1.place(x=700, y=240)
barra3.place(x=0,y=285,width=880, height=30)
barra4.place(x=0,y=315,width=435, height=30)
barra5.place(x=435,y=315,width=445, height=30)
barra6.place(x=435,y=455,width=445, height=30)
ec1.place(x=440,y=370,width=300, height=20)
ec2.place(x=440,y=390,width=340, height=20)
ec3.place(x=440,y=410,width=308, height=20)
result1.place(x=455,y=500)
result2.place(x=520,y=500)
result3.place(x=585,y=500)
circuito_resultante.place(x=0,y=350)
#mostramos ejecutamos nuestra ventana
win.mainloop()
'''
nombre="analisis de nodo y malla"(en un circuito particular)
version=1.0
descripcion="es una app que calcula atraves de algoritmos de los metodos de malla y nodos las corrientes o voltajes que se nesesiten"
autores="Enrique Ramirez, Daniel Mendez, Pedro Galdames, Matias, Luis"
email="enrique.ramirez@alumnos.uach.cl"
url_proyecto="https://github.com/sebusca38/programacion1/trabajo_final.py"
'''