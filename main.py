"""
@author: Dev. Giovanni Venegas
@Date: 10/12/2021
@University: Instituto Politecnico Nacional

Expansion en Series de Fourier

La expansión en Series de Fourier permite representar cualquier función periódica con una suma infinita de funciones
sinusoidales. Estas funciones están compuestas por un armónico principal que oscila a la frecuencia fundamental e
infinitos armónicos que oscilan con frecuencias que son multiplos enteros de la frecuencia fundamental """

# Importamos las librerias que vamos a usar

from tkinter import *  # Se importa la librería Tkinter para Interfaces gráficas
from mpmath import ln, e, pi, cosh, sinh  # Se importan estas funciones matemáticas
from sympy import *  # Sympy permite trabajar con funciones matemáticas y aparte graficar
from tkinter import scrolledtext  # Es para la ventana de texto de los resultados
from tkinter import messagebox
import numpy as np


# Iniciamos los símbolos que se necesitaran para integrar por partes
init_printing()
x = symbols('x')
y = symbols('y')
n = symbols('n')


ventana = Tk()  # Se crea una nueva ventana
ventana.title("Series")  # Se le pone un titulo a la ventana
ventana.geometry('1200x600')  # Se define un tamaño para la ventana
ventana.resizable(width=0, height=0)  # Con esto hacemos que el usuario no pueda cambiar el tamaño de la ventana

# Un label para lo que necesitaremos ingresar
txt = Label(ventana, text="Series de Fourier ",
            font=("Arial Bold", 15))

lbl = Label(ventana, text="f(x): ",
            font=("Arial Bold", 15))

lbl2 = Label(ventana, text="Periodo min: ",
             font=("Arial Bold", 15))

lbl3 = Label(ventana, text="Periodo max: ",
             font=("Arial Bold", 15))

lbl4 = Label(ventana, text="Terminos: ",
             font=("Arial Bold", 15))

txt.grid(column=0, row=0)  # Para establecer la posición del label en la ventana
lbl.grid(column=0, row=5)
lbl2.grid(column=0, row=10)
lbl3.grid(column=0, row=15)
lbl4.grid(column=0, row=20)

# Aquí se ingresan los datos

funcion = Entry(ventana, font=("calibri 20"), width=10)
funcion.grid(row=5, column=5, columnspan=2, padx=4, pady=5)

lim_inf = Entry(ventana, font=("calibri 20"), width=10)
lim_inf.grid(row=10, column=5, columnspan=2, padx=4, pady=10)

lim_sup = Entry(ventana, font=("calibri 20"), width=10)
lim_sup.grid(row=15, column=5, columnspan=2, padx=4, pady=15)

terminos = Entry(ventana, font=("calibri 20"), width=10)
terminos.grid(row=20, column=5, columnspan=2, padx=4, pady=10)

# Botones

calcular = Button(ventana, text="Calcular", width=7, height=2, command=lambda: click_calcular())
calcular.grid(row=5, column=10, padx=15, pady=5)

borrar = Button(ventana, text="Limpiar", width=7, height=2, command=lambda: click_limpiar())
borrar.grid(row=5, column=11, padx=15, pady=5)

ayuda = Button(ventana, text="Ayuda", width=7, height=2, command=lambda: click_ayuda())
ayuda.grid(row=5, column=12, padx=15, pady=5)


# Funciones

def click_ayuda():
    messagebox.showinfo("Instrucciones",
                        "--Ejemplos para ingresar una funcion :" + '\n' + "x^2 = x**2" + '\n' + "sen(2x) = sin(2*x)" + '\n' + "cos(2x^2) = cos(2*x**2)" + '\n' + "--En limite inferior y superior ingresar los limites de integracion" + '\n' + "--En terminos ingresar el numero de terminos con la que quieres que se grafique tu serie")


def click_limpiar():
    funcion.delete(0, END)  # Con esto borramos lo que haya en el espacio de función y asi con cada Entry de la GUI
    funcion.insert(0, "")

    lim_inf.delete(0, END)
    lim_inf.insert(0, "")

    lim_sup.delete(0, END)
    lim_sup.insert(0, "")

    terminos.delete(0, END)
    terminos.insert(0, "")


#
def funcion_impar():
    fun = funcion.get()  # La variable fun recibe lo que hay en el espacio de la función en la GUI.
    f = eval(fun)  # la nueva variable f almacena la evaluación de fun para que esté representada matemáticamente.

    limi = lim_inf.get()  # La variable limi recibe lo que hay en el espacio del periodo min en la GUI.
    li = eval(limi)  # la nueva variable li almacena la evaluación de limi para que esté representada matemáticamente.

    lims = lim_sup.get()  # La variable lims recibe lo que hay en el espacio del periodo máximo en la GUI.
    ls = eval(lims)  # la nueva variable ls almacena la evaluación de lims para que esté representada matemáticamente.

    term = terminos.get()  # La variable term recibe lo que hay en el espacio de los términos en la GUI.
    t = eval(term)  # la nueva variable t almacena la evaluación de term para que esté representada matemáticamente.

    txt = scrolledtext.ScrolledText(ventana, width=90, height=15)
    txt.grid(column=13, row=30)

    ao = (integrate(f, (x, li, ls))) * (2 / ls)
    # integramos la función que ingrese el usuario (f) en función de x con los límites de integración (li,ls)
    # multiplicamos por 1 sobre L

    # Usamos la función pprint para mostrar ao

    an = 0
    # an es 0 ya que es la funcion para la opcion de senos.

    bn = integrate((f) * sin((n * pi * x) / ls), (x, li, ls)) * (2 / ls)
    # Integramos la función que ingrese el usuario (f) en función de x con los límites de integración (li,ls)...
    # ... Multiplicada por sen((n*pi*x)/pi) como dice la fórmula para an
    # multiplicamos por 1 sobre L

    seriebn = []  # serie bn es una lista que almacenara los datos de la serie
    for i in range(1, t + 1):  # con un ciclo for de 1 a términos
        seriebn.append(integrate((f) * sin((n * x * pi) / pi), (x, li, ls)).subs(n, i) * (1 / ls))
        # Como indica la fórmula, la función .subs cambia la n por cada uno de los términos
        # Solo es bn porque es la opción de senos

    seriebn.reverse()

    txt.insert(INSERT, "f(x) es una función impar por lo que la serie se resolverá usando senos")

    txt.insert(INSERT, '\n')
    txt.insert(INSERT, '\n')
    txt.insert(INSERT, "Coeficientes de Fourier----------------- ")
    txt.insert(INSERT, "a0 = ")
    txt.insert(INSERT, ao)
    txt.insert(INSERT, '\n')
    txt.insert(INSERT, "---------------------------- ")
    txt.insert(INSERT, '\n')

    txt.insert(INSERT, "an = ")
    txt.insert(INSERT, an)

    txt.insert(INSERT, '\n')
    txt.insert(INSERT, "---------------------------- ")
    txt.insert(INSERT, "b0-bn:")
    txt.insert(INSERT, '\n')

    for element in seriebn:
        txt.insert(INSERT, element)
        txt.insert(INSERT, '\n')

    # Calculamos las series con el número de términos que haya ingresado el usuario
    serie = (ao / 2)  # Inicia como indica la formula con a0/2
    for i in range(1, t + 1):  # con un ciclo for que va de 1 a términos
        serie = serie + (an * cos((n * pi * x) / pi)).subs(n, i)  # La fórmula de an, sin embargo siempre será 0
    for j in range(1, t + 1):  # Otro ciclo de 1 a términos para bn
        serie = serie + (bn * sin((n * pi * x) / pi)).subs(n, j)  # Con la formula para bn
        # la función .subs cambia "n" por cada número en términos.

    txt.insert(INSERT, '\n')

    txt.insert(INSERT, "Serie = ")
    txt.insert(INSERT, serie)

    colores = ["#00cc44",  # Verde
               "#ff0000"  # Rojo
               ]

    txt.insert(INSERT, "Serie = ")
    txt.insert(INSERT, serie)
    plotting = plot(f, serie, ylim=(-10, 10), xlim=(-10, 10), title="f(x):Azul , Serie (Expansion):Rojo",
                    show=False)  # Usando el módulo para gráficas de sympy
    plotting[0].line_color = "b"
    plotting[1].line_color = "r"
    plotting.show()


def funcion_general():
    fun = funcion.get()  # La variable fun recibe lo que hay en el espacio de la función en la GUI.
    f = eval(fun)  # la nueva variable f almacena la evaluación de fun para que esté representada matemáticamente.

    limi = lim_inf.get()  # La variable limi recibe lo que hay en el espacio de limite inferior en la GUI
    li = eval(limi)  # La nueva variable li almacena la evaluacion de limi para conocer el valor

    lims = lim_sup.get()  # La variable lims recive lo que hay en el espacio de limite superior en la GUI
    ls = eval(lims)  # La nueva variable ls almacena la evaluacion de lims para conocer el valor.

    term = terminos.get()  # La variable term recibe lo que hay en el espacio de terminos en la GUI
    t = eval(term)  # La nueva variable t, almacena la evaluacion de term para concoer el valor

    txt = scrolledtext.ScrolledText(ventana, width=70, height=15)
    txt.grid(column=13, row=30)

    ao = (integrate(f, (x, li, ls))) * (1 / ls)
    # integramos la funcion que ingrese el usuario (f) en funcion de x con los limites de integracion (li,ls)
    # multiplicamos por 1 sobre L

    an = integrate((f) * cos((n * pi * x) / ls), (x, li, ls)) * (1 / ls)
    # integramos la funcion que ingrese el usuario (f) en funcion de x con los limites de integracion (li,ls)...
    # ... Multiplicada por cos((n*pi*x)/pi) como dice la formula para an
    # multiplicamos por 1 sobre L

    bn = integrate((f) * sin((n * pi * x) / ls), (x, li, ls)) * (1 / ls)
    # integramos la funcion que ingrese el usuario (f) en funcion de x con los limites de integracion (li,ls)...
    # ... Multiplicada por sen((n*pi*x)/pi) como dice la formula para an
    # multiplicamos por 1 sobre L

    seriebn = []  # seriebn es una lista
    for i in range(1, t + 1):  # Se usa un ciclo for que va de 1 a terminos, para calcular cada dato
        seriebn.append(integrate((f) * sin((n * x * pi) / pi), (x, li, ls)).subs(n, i) * (1 / ls))
        # Se ingresa a la lista cada termino, que se calcula con la formula, con la funcion .subs se cambia el valor de n...
        # ... por cada uno de los terminos y se multiplica por 1/ls como indica la formula.

    seriean = []  # seriean en otra lista
    for i in range(1, t + 1):  # Se usa un ciclo for que va de 1 a terminos, para calcular cada dato
        seriean.append(integrate((f) * cos((n * pi * x) / pi), (x, li, ls)).subs(n, i) * (1 / ls))
        # Se ingresa a la lista cada termino, que se calcula con la formula, con la funcion .subs se cambia el valor de n...
        # ... por cada uno de los terminos y se multiplica por 1/ls como indica la formula.

    seriean.reverse()
    seriebn.reverse()
    txt.insert(INSERT, "f(x) es una función general ")
    txt.insert(INSERT, '\n')
    txt.insert(INSERT, "Coeficientes de Fourier----------------- ")
    txt.insert(INSERT, '\n')
    txt.insert(INSERT, "a0 = ")
    txt.insert(INSERT, ao)

    txt.insert(INSERT, '\n')
    txt.insert(INSERT, '\n')
    txt.insert(INSERT, "---------------------------- ")
    txt.insert(INSERT, '\n')
    txt.insert(INSERT, "a0-an:")
    txt.insert(INSERT, '\n')

    for element in seriean:
        txt.insert(INSERT, element)
        txt.insert(INSERT, '\n')

    txt.insert(INSERT, '\n')
    txt.insert(INSERT, "---------------------------- ")
    txt.insert(INSERT, '\n')
    txt.insert(INSERT, "b0-bn:")
    txt.insert(INSERT, '\n')

    for element in seriebn:
        txt.insert(INSERT, element)
        txt.insert(INSERT, '\n')

    # Calculamos la series con el numero de terminos que haya ingresado el usuario
    serie = (ao / 2)  # serie es una lista, inicia como indica la formula con a0/2
    for i in range(1, t + 1):  # Con un for vamos a iterar de acuerdo al numero de terminos.
        serie = serie + (an * cos((n * pi * x) / pi)).subs(n, i)  # Se aplica la formula de series de fourier para an
    for j in range(1, t + 1):  # Otro for para calcular los terminos de bn
        serie = serie + (bn * sin((n * pi * x) / pi)).subs(n, j)  # Se aplica la formula de series de fourier para bn

    txt.insert(INSERT, '\n')
    txt.insert(INSERT, '\n')

    colores = ["#00cc44",  # Verde
               "#ff0000"  # Rojo
               ]
    txt.insert(INSERT, "---------------------------- ")
    txt.insert(INSERT, '\n')
    txt.insert(INSERT, "Serie = ")
    txt.insert(INSERT, serie)
    plotting = plot(f, serie, ylim=(-10, 10), xlim=(-10, 10), title="f(x):Azul , Serie (Expansion):Rojo", show=False)
    # Usando el modulo para graficas de sympy
    plotting[0].line_color = "b"  # Para la funcion se utiliza el color azul y por eso se pone "b" (blue)
    plotting[1].line_color = "r"  # Para la funcion se utiliza el color rojo y por eso se pone "r" (red)
    plotting.show()  # Se muestra la gráfica


def funcion_par():
    fun = funcion.get()  # La variable fun recibe lo que hay en el espacio de la funcion en la GUI.
    f = eval(fun)  # la nueva variable f almacena la evaluación de fun para que este representada matemáticamente.

    limi = lim_inf.get()  # La variable limi recibe lo que hay en el espacio de la funcion en la GUI.
    li = eval(limi)  # la nueva variable li almacena la evaluacion de limi para que este representada matematicamente.

    lims = lim_sup.get()  # La variable lims recibe lo que hay en el espacio de la funcion en la GUI.
    ls = eval(lims)  # la nueva variable ls almacena la evaluacion de lims para que este representada matematicamente.

    term = terminos.get()  # La variable term recibe lo que hay en el espacio de la funcion en la GUI.
    t = eval(term)  # la nueva variable t almacena la evaluacion de term para que este representada matematicamente.

    txt = scrolledtext.ScrolledText(ventana, width=70, height=15)
    txt.grid(column=13, row=30)

    lt = ls * -1

    ao = (integrate(f, (x, li, ls))) * (2 / ls)
    # integramos la funcion que ingrese el usuario (f) en función de x con los limites de integracion (li,ls)
    # multiplicamos por 1 sobre L

    # Usamos la funcion pprint para mostrar ao

    an = integrate((f) * cos(n * x), (x, li, ls)) * (2 / ls)
    # integramos la funcion que ingrese el usuario (f) en funcion de x con los limites de integracion (li,ls)...
    # ... Multiplicada por cos((n*pi*x)/pi) como dice la formula para an
    # multiplicamos por 1 sobre L

    bn = 0
    # bn es 0 ya que es la opcion para cosenos

    seriean = []  # seriean es una lista que almacenara la serie, solo an ya que es la opcion de cosenos
    for i in range(1, t + 1):  # Se utiliza un ciclo for de 1 a terminos
        seriean.append(integrate((f) * cos((n * x * pi) / pi), (x, li, ls)).subs(n, i) * (1 / ls))
        # la funcion .subs cambia la "n" por cada uno de los terminos (1,2,3....n)

    seriean.reverse()
    txt.insert(INSERT, "f(x) es una función par por lo que la serie se resolverá usando senos")
    txt.insert(INSERT, "El inervalo se extendera a (-p,p) y se resolvera usando cosenos")

    txt.insert(INSERT, '\n')

    txt.insert(INSERT, "a0-an:")
    txt.insert(INSERT, '\n')

    for element in seriean:
        txt.insert(INSERT, element)
        txt.insert(INSERT, '\n')

    txt.insert(INSERT, '\n')

    txt.insert(INSERT, "bn = ")
    txt.insert(INSERT, bn)
    txt.insert(INSERT, '\n')

    # Calculamos la series con el numero de terminos que haya ingresado el usuario
    serie = (ao / 2)  # La serie inicia como indica la formula con a0/2
    for i in range(1, t + 1):  # Con un ciclo for que va de 1 a terminos
        serie = serie + (an * cos((n * pi * x) / ls)).subs(n,
                                                           i)  # se le va sumando a la serie cada dato segun la formula
    for j in range(1, t + 1):  # Otro for para bn, aunque en este caso siempre sera 0 ya que es la opcion por cosenos.
        serie = serie + (bn * sin((n * pi * x) / ls)).subs(n, j)

    txt.insert(INSERT, '\n')

    txt.insert(INSERT, "Serie = ")
    txt.insert(INSERT, serie)

    colores = ["#00cc44",  # Verde
               "#ff0000"  # Rojo
               ]

    plotting = plot(f, serie, ylim=(-10, 10), xlim=(-10, 10), title="f(x)-Azul , Serie (Expansion)-Rojo", show=False)
    # Usando el modulo para graficas de sympy
    plotting[0].line_color = "b"  # el color azul para la funcion y se pone "b"(blue)
    plotting[1].line_color = "r"  # el color rojo para la serie y se pone "r"(red)
    plotting.show()  # Para mostrar la ventana de la grafica


def click_calcular():
    fun = funcion.get()
    f = eval(fun)

    limi = lim_inf.get()
    li = eval(limi)

    lims = lim_sup.get()
    ls = eval(lims)

    term = terminos.get()
    t = eval(term)

    if li != 0:
        funcion_general()

    if li == 0:
        ingresar()


def ingresar():
    ventana2 = Tk()  # Se crea una nueva ventana
    ventana2.title("Opciones")  # Se le pone un titulo a la ventana
    ventana2.geometry('300x70')  # Se define un tamaño para la ventana
    ventana2.resizable(width=0, height=0)  # Con esto hacemos que el usuario no pueda cambiar el tamaño de la ventana

    lbl5 = Label(ventana2, text="Elija una opcion:",
                 font=("Arial Bold", 10))

    lbl5.grid(column=0, row=15)

    calcularcos = Button(ventana2, text="Cosenos", width=7, height=2, command=lambda: funcion_par())
    calcularcos.grid(row=15, column=5, padx=15, pady=5)

    calcularsen = Button(ventana2, text="Senos", width=7, height=2, command=lambda: funcion_impar())
    calcularsen.grid(row=15, column=10, padx=15, pady=5)


ventana.mainloop()  # Esta función reconoce todo lo que estamos haciendo con la ventana y es necesaria para verla
