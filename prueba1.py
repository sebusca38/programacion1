import tkinter
import numpy as np
from scipy import signal as sp
import matplotlib.pylab as plt
def señal_seno():
    amplitud = 1
    periodo = np.pi


    t = np.arange(-1, 10, 0.001)
    funcion = ((sp.square(2 * t)) * (amplitud / 2.0)) + (amplitud / 2.0)

    plt.plot(t, funcion, lw=2)
    plt.grid()
    plt.annotate('Pi', xy = (np.pi, 1), xytext = (np.pi, 1.1))
    plt.annotate('Pi/2', xy = (np.pi / 2.0, 1), xytext = (np.pi / 2.0, 1.1))
    plt.ylabel('Amplitud')
    plt.xlabel('Tiempo(t)')
    plt.ylim(-1,2)
    plt.xlim(-0.5, 4)
    plt.show()
def señal_seno1():
    
    amplitud = 1
    periodo = np.pi


    t = np.arange(-1, 10, 0.001)
    funcion = ((sp.square(2 * t)) * (amplitud / 2.0)) + (amplitud / 2.0)

    plt.plot(t, funcion, lw=2)
    plt.grid()
    plt.annotate('Pi', xy = (np.pi, 1), xytext = (np.pi, 1.1))
    plt.annotate('Pi/2', xy = (np.pi / 2.0, 1), xytext = (np.pi / 2.0, 1.1))
    plt.ylabel('Amplitud')
    plt.xlabel('Tiempo(t)')
    plt.ylim(-1,2)
    plt.xlim(-0.5, 4)
    plt.show()
def señal_seno2():
    amplitud = 1
    periodo = np.pi


    t = np.arange(-1, 10, 0.001)
    funcion = ((sp.square(2 * t)) * (amplitud / 2.0)) + (amplitud / 2.0)

    plt.plot(t, funcion, lw=2)
    plt.grid()
    plt.annotate('Pi', xy = (np.pi, 1), xytext = (np.pi, 1.1))
    plt.annotate('Pi/2', xy = (np.pi / 2.0, 1), xytext = (np.pi / 2.0, 1.1))
    plt.ylabel('Amplitud')
    plt.xlabel('Tiempo(t)')
    plt.ylim(-1,2)
    plt.xlim(-0.5, 4)
    plt.show()

app=tkinter.Tk()
app.geometry("400x400")
boton1=tkinter.Button(app, command=señal_seno)
boton1.configure(text="olo")
boton1.pack()
boton2=tkinter.Button(app, command=señal_seno1)
boton2.configure(text="olo")
boton2.pack()
boton3=tkinter.Button(app, command=señal_seno2)
boton3.configure(text="olo")
boton3.pack()
app.mainloop()