import numpy
import tkinter as tk
from tkinter import ttk
import sympy
import sys
from tkinter import messagebox

global imagen, circuito, tk, win, r1, r2, r3, r4, r5, v1, v2, vardb, messagebox, ec1, ec2, ec3, result1, result2, result3, resultva, resultvb

def generar_imagen(nombre_imagen):
    imagen=tk.PhotoImage(file=nombre_imagen)
    circuito=tk.Label(image=imagen)
    circuito.place(x=5,y=40)

def calculo_y_generar():
    if (not r1.get() or not r2.get() or not r3.get() or not r4.get() or not r5.get() or not v1.get() or not v2.get()):
        messagebox.showwarning("cuaidado","no has rellenado notas las variables")
    else:
        def metodo_nodo():
            EC1=[(1/varR1)+(1/varR2)+(1/varR3),-(1/varR3)]
            EC2=[-(1/varR3),(1/varR4)+(1/varR3)+(1/varR5)]
            V=[(varV1/varR1),(varV2/varR3)]
            matrix1= numpy.array([EC1,EC2])
            matrix2= numpy.array(V)
            matrix3= numpy.linalg.solve(matrix1,matrix2)
        def metodo_malla():
            EC1=[varR1+varR2,-varR2,0]
            EC2=[-varR2,varR2+varR3+varR4,-varR4]
            EC3=[0,-varR4,varR5+varR4]
            V=[varV1,0,varV2]
            matrix1= numpy.array([EC1,EC2,EC3])
            matrix2= numpy.array(V)
            matrix3= numpy.linalg.solve(matrix1,matrix2)
            print(matrix3)
            result1.configure(text='I1= '+str(round(matrix3[0],4)).replace(" ",'')+'A')
            result2.configure(text='I2= '+str(round(matrix3[1],4)).replace(" ",'')+'A')
            result3.configure(text='I3= '+str(round(matrix3[2],4)).replace(" ",'')+'A')
        varR1=int(r1.get())
        varR2=int(r2.get())
        varR3=int(r3.get())
        varV1=int(v1.get())
        varR4=int(r4.get())
        varR5=int(r5.get())
        varV2=int(v2.get())
        if (vardb.get()==1):
            ec1.configure(text="Ecuacion 1:     "+str(varR1+varR2)+"*(I1) - "+str(varR2)+"*(I2) = "+str(varV1))
            ec2.configure(text="Ecuacion 2:     "+str(-varR2)+"*(I1) + "+str(varR2+varR3+varR4)+"*(I2) - "+str(varR4)+"*(I2) = 0")
            ec3.configure(text="Ecuacion 3:     "+str(-varR4)+"*(I2) + "+str(varR4+varR5)+"*(I3) = "+str(varV2))
            metodo_malla()
        elif (vardb.get()==2):
            ec3.configure(text='')
            ec1.configure(text="Ecuacion 1:     "+str(1/varR1+1/varR2+1/varR3)+"*Va - "+str(1/varR3)+"*Vb = "+str(varV1/varR1))
            ec2.configure(text="Ecuacion 2:     "+str(-1/varR3)+"*Va - "+str(1/varR3+1/varR4+1/varR5)+"*Vb = "+str(varR4)+str(varV2/varR3))
        else:
            messagebox.showwarning("cuidado",'no has seleccionado un metodo de analisis')

win=tk.Tk()
win.iconbitmap('Icono.ico')
win.title("Análisis de mallas y nodos")
win.geometry('880x600')
win.configure(background='snow2')
barra=tk.Label(win,text="Circuito ",bg="dark olive green",fg="white")
barra.place(x=0,y=5,width=435, height=30)

imagen=tk.PhotoImage(file='Circuito.gif')
circuito=tk.Label(image=imagen)
circuito.place(x=0,y=35)

barra2=tk.Label(win,text="Análisis ",bg="chocolate",fg="white")
barra2.place(x=435,y=5,width=445, height=30)
vardb=tk.IntVar()
radioboton1=ttk.Radiobutton(win, variable=vardb,value=1)
radioboton1.configure(text='metodo de malla')
radioboton1.place(x=500,y=40)

radioboton2=ttk.Radiobutton(win, variable=vardb,value=2)
radioboton2.configure(text='metodo de nodos')
radioboton2.place(x=650,y=40)

label1=tk.Label(win,text="  resistencias  ",bg="olive drab",fg="white") #Ecuación 1
label1.place(x=430,y=70,width=445, height=30)

lr1=ttk.Label(win)
lr1.configure(text="R1:")
lr1.place(x=440, y=110)
r1=ttk.Entry(win)
r1.place(x=460,y=110,width=35, height=25)
lr2=ttk.Label(win)
lr2.configure(text="R2:")
lr2.place(x=500, y=110)
r2=ttk.Entry(win)
r2.place(x=520,y=110, width=35,height=25)
lr3=ttk.Label(win)
lr3.configure(text="R3:")
lr3.place(x=560,y=110)
r3=ttk.Entry(win)
r3.place(x=580,y=110,width=35,height=25)
lr4=ttk.Label(win)
lr4.configure(text="R4:")
lr4.place(x=620,y=110)
r4=ttk.Entry(win)
r4.place(x=640,y=110,width=35,height=25)
lr5=ttk.Label(win)
lr5.configure(text="R5:")
lr5.place(x=680,y=110)
r5=ttk.Entry(win)
r5.place(x=700,y=110,width=35,height=25)

label2=tk.Label(win,text="  fuentes de voltaje  ",bg="olive drab",fg="white") #Ecuación 2
label2.place(x=430,y=140,width=445, height=30)

lv1=ttk.Label(win)
lv1.configure(text="V1:")
lv1.place(x=440, y=180)
v1=ttk.Entry(win)
v1.place(x=460,y=180,width=35, height=25)
lv2=ttk.Label(win)
lv2.configure(text="V2:")
lv2.place(x=500, y=180)
v2=ttk.Entry(win)
v2.place(x=520,y=180, width=35,height=25)

Tboton1=ttk.Button(win, command=calculo_y_generar)
Tboton1.configure(text='calcular y generar')
Tboton1.place(x=700, y=240)


barra3=tk.Label(win, text="resultados", bg="dark olive green",fg="white")
barra3.place(x=0,y=290,width=880, height=30)

barra4=tk.Label(win,text="  Circuito analisados ",bg="chocolate",fg="white")
barra4.place(x=0,y=320,width=435, height=30)
barra5=tk.Label(win,text="  Plantamiento de ecuaciones  ",bg="chocolate",fg="white")
barra5.place(x=435,y=320,width=445, height=30)

barra6=tk.Label(win,text="  resultados respectivos  ",bg="chocolate",fg="white")
barra6.place(x=435,y=460,width=445, height=30)
ec3=tk.Label(win, bg="snow2",fg="black")
ec2=tk.Label(win, bg="snow2",fg="black")
ec1=tk.Label(win, bg="snow2",fg="black")
ec1.place(x=435,y=370,width=300, height=20)
ec2.place(x=435,y=390,width=340, height=20)
ec3.place(x=435,y=410,width=308, height=20)
result1=tk.Label(win, bg="snow2",fg="black")
result2=tk.Label(win, bg="snow2",fg="black")
result3=tk.Label(win, bg="snow2",fg="black")
resultva=tk.Label(win, bg="snow2",fg="black")
resultvb=tk.Label(win, bg="snow2",fg="black")
resultvR1=tk.Label(win, bg="snow2",fg="black")
resultvR2=tk.Label(win, bg="snow2",fg="black")
resultvR3=tk.Label(win, bg="snow2",fg="black")
resultvR4=tk.Label(win, bg="snow2",fg="black")
resultvR5=tk.Label(win, bg="snow2",fg="black")
result1.place(x=455,y=500)
result2.place(x=520,y=500)
result3.place(x=585,y=500)


win.mainloop()