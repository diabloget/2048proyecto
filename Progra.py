#importar bibliotecas
from tkinter import*
import random
import time
from threading import Thread
import threading
import os
from tkinter import messagebox

global score
score = 0

global nombre
nombre=""

global leaderboard
leaderboard = []

#Matriz principal.
global m
m=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
#m=[[16,8,4,8],[32,16,32,16],[4,8,16,4],[2,2,256,512]]

#Valor SM que selecciona sumas debido al que el profesor pidió eliminar la multiplicación ya programada.
sm=False

#Matriz traducida.
global n
n=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

#Variable de traductor por defecto.
global t
t = 0

#Valores aleatorios.
dosycuatro = (2,4)
rango=range(0,4)

#funcion para abrir el archivo de texto con la informacion del leaderboard
def crearT():
    archi=open("Leaderboard.txt","r")
    archi.close()
    
#funcion para leer el archivo con el leaderboard
def leerT():
    global leaderboard
    archi=open("Leaderboard.txt","r")
    lineas=archi.readlines()
    leaderboard = lineas
    archi.close()
    
#invocacion de funciones     
crearT()
leerT()

#funcion para guardar los datos de energia modificados en el archivo de texto y destruir la ventana 
def grabarT():
    global leaderboard
    archi=open("Leaderboard.txt","w")
   # archi.write("Navi\n")
    archi.write()
    archi.close()
    ventana.destroy()


#funcion para cargar imagen
def cargar_imagen(nombre):
    ruta = os.path.join('Images',nombre)
    imagen = PhotoImage(file = ruta)
    return imagen

#creación de la ventana principal
ventana=Tk()
ventana.title("2048 The Game")
ventana.minsize(600, 600)
ventana.resizable(width=NO,height=NO)

#creación del canvas
contenedor1=Canvas(ventana,width=605,height=605,bg="BLACK")
contenedor1.place(x=-2,y=-2)

#colocar imagenes de la patalla de inicio
inicio1 = cargar_imagen("number.gif")
Labelinicio1= Label(contenedor1, image = inicio1, bg = "BLACK")
Labelinicio1.place(x=180,y=100)

inicio2 = cargar_imagen("the game.gif")
Labelinicio2= Label(contenedor1, image = inicio2, bg = "BLACK")
Labelinicio2.place(x=140,y=200)


    

#funcion para generar ventana de login
def newGame():
#funcion para cargar imagen
    def binary():
        global t
        t=2
    def Decimal():
        global t
        t=10
    def Octal():
        global t
        t=8
    def hexa():
        global t
        t=16
    ventana.withdraw()#desvanece la anterior ventana
    #creacion una nueva ventana 
    ventanaLogin=Toplevel()
    ventanaLogin.title("Home")
    ventanaLogin.minsize(600,600)
    ventanaLogin.resizable(width = YES, height = YES)
    #creacion de canvas
    contenedor2=Canvas(ventanaLogin,width=605,height=605,bg ="BLACK")
    contenedor2.place(x=-2,y=-2)
    def game():
        global m
        start(True)

        #funcion que mueve la matriz dependiendo de la flecha presionada
        def mover(direction):
            if(direction=="up"):
                direccional(direction)
                drawMatriz()
            if(direction=="down"):
                direccional(direction)
                drawMatriz()
            if(direction=="left"):
                direccional(direction)
                drawMatriz()
            if(direction=="right"):
                direccional(direction)
                drawMatriz()
        
        def draw():
            global m
            if(m[0][0]==0):
                print("sfgf")
            if(m[0][0]!=0):
                cMatriz1=Label(contenedor4,text="",width=100,height=100,bg = "PURPLE")
                cMatriz1.place(x=0,y=0)
            if(m[0][1]==0):
                print("sfgf")
            if(m[0][1]!=0):
                print("sfgf")
            if(m[0][2]==0):
               print("sfgf")
            if(m[0][2]!=0):
               print("sfgf")
            if(m[0][3]==0):
                print("sfgf")
            if(m[0][3]!=0):
                print("sfgf")
            if(m[1][0]==0):
                print("sfgf")
            if(m[1][0]!=0):
                print("sfgf")
            if(m[1][1]==0):
                print("sfgf")
            if(m[1][1]!=0):
                print("sfgf")
            if(m[1][2]==0):
                print("sfgf")
            if(m[1][2]!=0):
                print("sfgf")
            if(m[1][3]==0):
                print("sfgf")
            if(m[1][3]!=0):
               print("sfgf")
            if(m[2][0]==0):
                print("sfgf")
            if(m[2][0]!=0):
                print("sfgf")
            if(m[2][1]==0):
                print("sfgf")
            if(m[2][1]!=0):
                print("sfgf")
            if(m[2][2]==0):
                print("sfgf")
            if(m[2][2]!=0):
                print("sfgf")
            if(m[2][3]==0):
                print("sfgf")
            if(m[2][3]!=0):
                print("sfgf")
            if(m[3][0]==0):
                print("sfgf")
            if(m[3][0]!=0):
                print("sfgf")
            if(m[3][1]==0):
                print("sfgf")
            if(m[3][1]!=0):
                print("sfgf")
            if(m[3][2]==0):
                print("sfgf")
            if(m[3][2]!=0):
                print("sfgf")
            if(m[3][3]==0):
                print("sfgf")
            if(m[3][3]!=0):
                print("sfgf")
        #creacion una nueva ventana
        ventanaLogin.withdraw()
        ventanaGame=Toplevel()
        ventanaGame.title("2048")
        ventanaGame.minsize(600,600)
        ventanaGame.resizable(width = YES, height = YES)
        #creacion de canvas
        contenedor3=Canvas(ventanaGame,width=605,height=605,bg ="BLACK")
        contenedor3.place(x=-2,y=-2)
        contenedor4=Canvas(contenedor3,width=400,height=400,bg ="ORANGE")
        contenedor4.place(x=100,y=170)
        #distintos label
        cMatriz1=Label(contenedor4,text="",width=100,height=100,bg = "ORANGE")
        cMatriz1.place(x=0,y=0)
        cMatriz2=Label(contenedor4,text="",width=100,height=100,bg = "ORANGE")
        cMatriz2.place(x=100,y=0)
        cMatriz3=Label(contenedor4,text="",width=100,height=100,bg = "ORANGE")
        cMatriz3.place(x=200,y=0)
        cMatriz4=Label(contenedor4,text="",width=100,height=100,bg = "ORANGE")
        cMatriz4.place(x=300,y=0)
        cMatriz5=Label(contenedor4,text="",width=100,height=100,bg = "ORANGE")
        cMatriz5.place(x=0,y=100)
        cMatriz6=Label(contenedor4,text="",width=100,height=100,bg = "ORANGE")
        cMatriz6.place(x=100,y=100)
        cMatriz7=Label(contenedor4,text="",width=100,height=100,bg = "ORANGE")
        cMatriz7.place(x=200,y=100)
        cMatriz8=Label(contenedor4,text="",width=100,height=100,bg = "ORANGE")
        cMatriz8.place(x=300,y=100)
        cMatriz9=Label(contenedor4,text="",width=100,height=100,bg = "ORANGE")
        cMatriz9.place(x=0,y=200)
        cMatriz10=Label(contenedor4,text="",width=100,height=100,bg = "ORANGE")
        cMatriz10.place(x=100,y=200)
        cMatriz11=Label(contenedor4,text="",width=100,height=100,bg = "ORANGE")
        cMatriz11.place(x=200,y=200)
        cMatriz12=Label(contenedor4,text="",width=100,height=100,bg = "ORANGE")
        cMatriz12.place(x=300,y=200)
        cMatriz13=Label(contenedor4,text="",width=100,height=100,bg = "ORANGE")
        cMatriz13.place(x=0,y=300)
        cMatriz14=Label(contenedor4,text="",width=100,height=100,bg = "ORANGE")
        cMatriz14.place(x=100,y=300)
        cMatriz15=Label(contenedor4,text="",width=100,height=100,bg = "ORANGE")
        cMatriz15.place(x=200,y=300)
        cMatriz16=Label(contenedor4,text="",width=100,height=100,bg = "ORANGE")
        cMatriz16.place(x=300,y=300)

        def drawMatriz():
            matriz0=Label(contenedor4,text=m[0][0],font=("Arial", 10),fg="ORANGE",bg = "PURPLE")
            matriz0.place(x=5,y=40)
            matriz1=Label(contenedor4,text=m[0][1],font=("Arial", 10),fg="ORANGE",bg = "PURPLE")
            matriz1.place(x=105,y=40)
            matriz2=Label(contenedor4,text=m[0][2],font=("Arial", 10),fg="ORANGE",bg = "PURPLE")
            matriz2.place(x=205,y=40)
            matriz3=Label(contenedor4,text=m[0][3],font=("Arial", 10),fg="ORANGE",bg = "PURPLE")
            matriz3.place(x=305,y=40)
            matriz4=Label(contenedor4,text=m[1][0],font=("Arial", 10),fg="ORANGE",bg = "PURPLE")
            matriz4.place(x=5,y=140)
            matriz5=Label(contenedor4,text=m[1][1],font=("Arial", 10),fg="ORANGE",bg = "PURPLE")
            matriz5.place(x=105,y=140)
            matriz6=Label(contenedor4,text=m[1][2],font=("Arial", 10),fg="ORANGE",bg = "PURPLE")
            matriz6.place(x=205,y=140)
            matriz7=Label(contenedor4,text=m[1][3],font=("Arial", 10),fg="ORANGE",bg = "PURPLE")
            matriz7.place(x=305,y=140)
            matriz8=Label(contenedor4,text=m[2][0],font=("Arial", 10),fg="ORANGE",bg = "PURPLE")
            matriz8.place(x=5,y=240)
            matriz9=Label(contenedor4,text=m[2][1],font=("Arial", 10),fg="ORANGE",bg = "PURPLE")
            matriz9.place(x=105,y=240)
            matriz10=Label(contenedor4,text=m[2][2],font=("Arial", 10),fg="ORANGE",bg = "PURPLE")
            matriz10.place(x=205,y=240)
            matriz11=Label(contenedor4,text=m[2][3],font=("Arial", 10),fg="ORANGE",bg = "PURPLE")
            matriz11.place(x=305,y=240)
            matriz12=Label(contenedor4,text=m[3][0],font=("Arial", 10),fg="ORANGE",bg = "PURPLE")
            matriz12.place(x=5,y=340)
            matriz13=Label(contenedor4,text=m[3][1],font=("Arial", 10),fg="ORANGE",bg = "PURPLE")
            matriz13.place(x=105,y=340)
            matriz14=Label(contenedor4,text=m[3][2],font=("Arial", 10),fg="ORANGE",bg = "PURPLE")
            matriz14.place(x=205,y=340)
            matriz15=Label(contenedor4,text=m[3][3],font=("Arial", 10),fg="ORANGE",bg = "PURPLE")
            matriz15.place(x=305,y=340)
        drawMatriz()


        #funciones lambda para ejecutar el movimiento de la matriz
        ventanaGame.bind("<Up>", lambda x:mover("up"))
        ventanaGame.bind("<Down>", lambda x:mover("down"))
        ventanaGame.bind("<Left>", lambda x:mover("left"))
        ventanaGame.bind("<Right>", lambda x:mover("right"))



        
#distintos label  
    LabelName= Label(contenedor2,text="Introduzca su nombre",fg="WHITE",bg = "BLACK")
    LabelName.place(x=420,y=125)
    LabelBase= Label(contenedor2,text="Seleccione la base en la que desea jugar",fg="WHITE",bg = "BLACK")
    LabelBase.place(x=380,y=200)
#creacion de un cuadro de texto
    namePlayer=Entry(contenedor2, width = 20)
    namePlayer.place(x=420,y=150)
#distintos botones
    binario=Button(contenedor2,text="Binario",command=binary,width=10,bg="ORANGE")
    binario.place(x=400,y=250)
    octal=Button(contenedor2,text="Octal",command=Octal,width=10,bg="ORANGE")
    octal.place(x=500,y=250)
    decimal=Button(contenedor2,text="Decimal",command=Decimal,width=10,bg="ORANGE")
    decimal.place(x=400,y=300)
    hexadecimal=Button(contenedor2,text="Hexadecimal",command=hexa,width=10,bg="ORANGE")
    hexadecimal.place(x=500,y=300)
    inicioI=cargar_imagen("inicio.gif")
    inicioButton=Button(contenedor2,text="Start",command=game,font=("Blackader ITC", 30),bg="PURPLE")
    inicioButton.place(x=430,y=350)








    

#boton para abrir ventana de login
startImage = cargar_imagen("start.gif")
newgame=Button(contenedor1,image=startImage,command=newGame,width=200,height=100,bg="ORANGE")
newgame.place(x=200,y=380)

#Función que busca generar dos valores aleatorios al presionar el botón "start"
def start(x):
    if(x==True):
        threading.Thread(target=gameover_2,args=[300]).start()
        gen_aux(m, 0)
        return traductor(m,0,0)
    else:
        print("Fuck")

#Auxiliar para generar uno o dos valores (2 o 4) de forma aleatoria.
def gen_aux(m, cont):
    a=random.choice(rango)
    b=random.choice(rango)
    c=random.choices(dosycuatro, weights=[77, 23], k=1)
    if(cont==2):
        return m
    if(m[a][b]==0):
        m[a][b]=c[0]
        return gen_aux(m, cont+1)
    else:
        return gen_aux(m, cont)

#Función que alterna entre suma o multiplicación según su valor de verdad.
def SoM(x,y):
    if(sm==True):
        res = y*y
        return res
    else:
        res = y*2
        findScore(res)
        return res

def asignar():
    global m
    lista=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    return asignar_aux(lista,0,0)

def asignar_aux(lista,i,j):
    global m
    if(i==3 and j==3):
        a=m[i][j]
        lista[i][j] = a
        return lista
    if(j<3):
        a=m[i][j]
        lista[i][j] = a
        j+=1
        return asignar_aux(lista,i,j)
    if(j==3):
        a=a=m[i][j]
        lista[i][j] = a
        j=0
        i+=1
        return asignar_aux(lista,i,j)
    

def cambios(a,b,c,d,e,f,g,h,i,j,k,l,x,n,o,p):
    if (a==m[0][0] and b==m[0][1] and c==m[0][2] and d==m[0][3] and e==m[1][0] and f==m[1][1] and g==m[1][2] and h==m[1][3] and i==m[2][0] and j==m[2][1]
        and k==m[2][2] and l==m[2][3] and x==m[3][0] and n==m[3][1] and o==m[3][2] and p==m[3][3]):
        return False
    else:
        return True
    
#Función encargada de llamar a las auxiliares de cada movimiento (up,down,right,left), generar un valor aleatorio, actualiar la variable n a la traducción correcta.
def direccional(x):
    a=asignar()
    if(x=="up"):
        f_up_aux(m,0,1,0)
        if(a!=m):
            gen_aux(m,1)
        if(gameover_1(0,0)==False):
            traductor(0,0)
            return gameover(True)
        if(TryWin(m,0,0)==True):
            return win(True)

        return traductor(m,0,0)
    if(x=="down"):
        a=asignar()
        f_down_aux(m,0,2,0)
        if(a!=m):
            gen_aux(m,1)
        if(gameover_1(0,0)==False):
            traductor(m,0,0)
            return gameover(True)
        if(TryWin(m,0,0)==True):
            return win(True)

        return traductor(m,0,0)
    if(x=="right"):
        a=asignar()
        f_r_aux(m,2,0,0)
        if(a!=m):
            gen_aux(m,1)
        if(gameover_1(0,0)==False):
            traductor(m,0,0)
            return gameover(True)
        if(TryWin(m,0,0)==True):
            return win(True)

        return traductor(m,0,0)
    if(x=="left"):
        a=asignar()
        f_l_aux(m,1,0,0)
        if(a!=m):
            gen_aux(m,1)
        if(gameover_1(0,0)==False):
            traductor(m,0,0)
            return gameover(True)
        if(TryWin(m,0,0)==True):
            return win(True)

        return traductor(m,0,0)

#Traductor universal (binario, octal y hexadecimal)
def traductor(m,a,b):
    global n
    global t
    if(a==4):
        return n
    if(b==4):
        return traductor(a+1,0)
    if(t==2):
        n[a][b] = binario_aux(m[a][b])
        return traductor(a,b+1)
    if(t==8):
        n[a][b] = octal_aux(m[a][b])
        return traductor(a,b+1)
    if(t==16):
        n[a][b] = hexadecimal_aux(m[a][b])
        return traductor(a,b+1)
    else:
        n=m
        return n

#Función encargada de pasar valores de decimal a binario.
def binario(x):
    if(x<0):
        print("La variable es menor que 0")
    else:
        return binario_aux(x)
def binario_aux(x):
    a=""
    if(x//2>0):
        b= x-(2*(x//2))
        a+=str(b)
        return binario_aux(x//2) + a
    else:
        a+=str(x)
        return a

#Función encargada de pasar valores de decimal a octal.
def octal(x):
    if(x>0 or x==0):
        return octal_aux(x)
    else:
        print("El valor no es un numero, es negativo o es float")
def octal_aux(x):
    a=""
    if(x//8>0):
        b = x-(8*(x//8))
        a += str(b)
        return octal_aux(x//8) + a
    else:
        a += str(x)
        return a

#Función encargada de pasar valores de decimal a hexadecimal.
def hexadecimal(x):
    if(x>0 or x==0):
        return hexadecimal_aux(x)
    else:
        print("El valor no es un numero, es negativo o es float")
def hexadecimal_aux(x):
    a=""
    if(x//16>0):
        b = x-(16*(x//16))
        if(b<10):
            a += str(b)
            return hexadecimal_aux(x//16) + a
        else:
            if(b==10):
                a += "a"
                return hexadecimal_aux(x//16) + a
            if(b==11):
                a += "b"
                return hexadecimal_aux(x//16) + a
            if(b==12):
                a += "c"
                return hexadecimal_aux(x//16) + a
            if(b==13):
                a += "d"
                return hexadecimal_aux(x//16) + a
            if(b==14):
                a += "e"
                return hexadecimal_aux(x//16) + a
            else:
                a += "f"
                return hexadecimal_aux(x//16) + a
    else:
        if(x<10):
            a += str(x)
            return a
        else:
            if(x==10):
                a += "a"
                return a
            if(x==11):
                a += "b"
                return a
            if(x==12):
                a += "c"
                return a
            if(x==13):
                a += "d"
                return a
            if(x==14):
                a += "e"
                return a
            else:
                a += "f"
                return a

#Auxiliar encargada la flecha derecha.
def f_r_aux(m,cc,cf,cn):
    if(cf==4):
        return m
    if(cc>0):
        if(cc==2):
            if(m[cf][cc+1]==0):
                y = m[cf][cc]
                m[cf][cc+1] = y
                m[cf][cc] = 0
                return f_r_aux(m,cc-1,cf,cn)
            if(m[cf][cc+1]==m[cf][cc]):
                y = m[cf][cc]
                m[cf][cc+1]= SoM(sm,y)
                m[cf][cc] = 0
                return f_r_aux(m,cc-1,cf,1)
            else:
                return f_r_aux(m,cc-1,cf,cn)
        if(cc==1):
            if(m[cf][cc+1]==0 and m[cf][cc+2]==0):
                y = m[cf][cc]
                m[cf][cc+2] = y
                m[cf][cc] = 0
                return f_r_aux(m,cc-1,cf,cn)
            if(m[cf][cc+1]==0):
                if(m[cf][cc+2]==m[cf][cc] and cn==0):
                    y = m[cf][cc]
                    m[cf][cc+2]= SoM(sm,y)
                    m[cf][cc] = 0
                    return f_r_aux(m,cc-1,cf,cn)
                else:
                    y = m[cf][cc]
                    m[cf][cc+1] = y
                    m[cf][cc] = 0
                    return f_r_aux(m,cc-1,cf,cn)
            if(m[cf][cc+1]==m[cf][cc]):
                y = m[cf][cc]
                m[cf][cc+1]= SoM(sm,y)
                m[cf][cc] = 0
                return f_r_aux(m,cc-1,cf,2)
            else:
                return f_r_aux(m,cc-1,cf,cn)
    else:
        if(m[cf][cc+1]==0 and m[cf][cc+2]==0 and m[cf][cc+3]==0):
            y = m[cf][cc]
            m[cf][cc+3] = y
            m[cf][cc] = 0
            return f_r_aux(m,2,cf+1,0)
        if(m[cf][cc+1]==0 and m[cf][cc+2]==0):
            if(m[cf][cc+3]==m[cf][cc] and cn==0):
                y = m[cf][cc]
                m[cf][cc+3]= SoM(sm,y)
                m[cf][cc] = 0
                return f_r_aux(m,2,cf+1,0)
            else:
                y = m[cf][cc]
                m[cf][cc+2] = y
                m[cf][cc] = 0
                return f_r_aux(m,2,cf+1,0)
        if(m[cf][cc+1]==0):
            if(m[cf][cc+2]==m[cf][cc] and cn!=2):
                y = m[cf][cc]
                m[cf][cc+2]= SoM(sm,y)
                m[cf][cc] = 0
                return f_r_aux(m,2,cf+1,0)
            else:
                y = m[cf][cc]
                m[cf][cc+1] = y
                m[cf][cc] = 0
                return f_r_aux(m,2,cf+1,0)
        if(m[cf][cc+1]==m[cf][cc]):
            y = m[cf][cc]
            m[cf][cc+1]= SoM(sm,y)
            m[cf][cc] = 0
            return f_r_aux(m,2,cf+1,0)
        else:
            return f_r_aux(m,2,cf+1,0)


#Auxiliar encargada la flecha arriba.
def f_up_aux(m,cc,cf,cn):
    if(cc==4):
        return m
    if(cf<3):
        if(cf==1):
            if(m[cf-1][cc]==0):

                y = m[cf][cc]
                m[cf-1][cc] = y
                m[cf][cc] = 0
                return f_up_aux(m,cc,cf+1,cn)
            if(m[cf-1][cc]==m[cf][cc]):
                y = m[cf][cc]
                m[cf-1][cc]= SoM(sm,y)
                m[cf][cc] = 0
                return f_up_aux(m,cc,cf+1,1)
            else:
                return f_up_aux(m,cc,cf+1,cn)
        if(cf==2):
            if(m[cf-1][cc]==0 and m[cf-2][cc]==0):
                y = m[cf][cc]
                m[cf-2][cc] = y
                m[cf][cc] = 0
                return f_up_aux(m,cc,cf+1,cn)
            if(m[cf-1][cc]==0):
                if(m[cf-2][cc]==m[cf][cc] and cn==0):
                    y = m[cf][cc]
                    m[cf-2][cc]= SoM(sm,y)
                    m[cf][cc] = 0
                    return f_up_aux(m,cc,cf+1,cn)
                else:
                    y = m[cf][cc]
                    m[cf-1][cc] = y
                    m[cf][cc] = 0
                    return f_up_aux(m,cc,cf+1,cn)
            if(m[cf-1][cc]==m[cf][cc]):
                y = m[cf][cc]
                m[cf-1][cc]= SoM(sm,y)
                m[cf][cc] = 0
                return f_up_aux(m,cc,cf+1,2)
            else:
                return f_up_aux(m,cc,cf+1,cn)
    else:
        if(m[cf-1][cc]==0 and m[cf-2][cc]==0 and m[cf-3][cc]==0):
            y = m[cf][cc]
            m[cf-3][cc] = y
            m[cf][cc] = 0
            return f_up_aux(m,cc+1,1,0)
        if(m[cf-1][cc]==0 and m[cf-2][cc]==0):
            if(m[cf-3][cc]==m[cf][cc] and cn==0):
                y = m[cf][cc]
                m[cf-3][cc]= SoM(sm,y)
                m[cf][cc] = 0
                return f_up_aux(m,cc+1,1,0)
            else:
                y = m[cf][cc]
                m[cf-2][cc] = y
                m[cf][cc] = 0
                return f_up_aux(m,cc+1,1,0)
        if(m[cf-1][cc]==0):
            if(m[cf-2][cc]==m[cf][cc] and cn!=2):
                y = m[cf][cc]
                m[cf-2][cc]= SoM(sm,y)
                m[cf][cc] = 0
                return f_up_aux(m,cc+1,1,0)
            else:
                y = m[cf][cc]
                m[cf-1][cc] = y
                m[cf][cc] = 0
                return f_up_aux(m,cc+1,1,0)
        if(m[cf-1][cc]==m[cf][cc]):
            y = m[cf][cc]
            m[cf-1][cc]= SoM(sm,y)
            m[cf][cc] = 0
            return f_up_aux(m,cc+1,1,0)
        else:
            return f_up_aux(m,cc+1,1,0)

#Auxiliar encargada de flecha izquierda.
def f_l_aux(m,cc,cf,cn):
    if(cf==4):
        return m
    if(cc<3):
        if(cc==1):
            if(m[cf][cc-1]==0):
                y = m[cf][cc]
                m[cf][cc-1] = y
                m[cf][cc] = 0
                return f_l_aux(m,cc+1,cf,cn)
            if(m[cf][cc-1]==m[cf][cc]):
                y = m[cf][cc]
                m[cf][cc-1]= SoM(sm,y)
                m[cf][cc] = 0
                return f_l_aux(m,cc+1,cf,1)
            else:
                return f_l_aux(m,cc+1,cf,cn)
        if(cc==2):
            if(m[cf][cc-1]==0 and m[cf][cc-2]==0):
                y = m[cf][cc]
                m[cf][cc-2] = y
                m[cf][cc] = 0
                return f_l_aux(m,cc+1,cf,cn)
            if(m[cf][cc-1]==0):
                if(m[cf][cc-2]==m[cf][cc] and cn==0):
                    y = m[cf][cc]
                    m[cf][cc-2]= SoM(sm,y)
                    m[cf][cc] = 0
                    return f_l_aux(m,cc+1,cf,cn)
                else:
                    y = m[cf][cc]
                    m[cf][cc-1] = y
                    m[cf][cc] = 0
                    return f_l_aux(m,cc+1,cf,cn)
            if(m[cf][cc-1]==m[cf][cc]):
                y = m[cf][cc]
                m[cf][cc-1]= SoM(sm,y)
                m[cf][cc] = 0
                return f_l_aux(m,cc+1,cf,2)
            else:
                return f_l_aux(m,cc+1,cf,cn)
    else:
        if(m[cf][cc-1]==0 and m[cf][cc-2]==0 and m[cf][cc-3]==0):
            y = m[cf][cc]
            m[cf][cc-3] = y
            m[cf][cc] = 0
            return f_l_aux(m,1,cf+1,0)
        if(m[cf][cc-1]==0 and m[cf][cc-2]==0):
            if(m[cf][cc-3]==m[cf][cc] and cn==0):
                y = m[cf][cc]
                m[cf][cc-3]= SoM(sm,y)
                m[cf][cc] = 0
                return f_l_aux(m,1,cf+1,0)
            else:
                y = m[cf][cc]
                m[cf][cc-2] = y
                m[cf][cc] = 0
                return f_l_aux(m,1,cf+1,0)
        if(m[cf][cc-1]==0):
            if(m[cf][cc-2]==m[cf][cc] and cn!=2):
                y = m[cf][cc]
                m[cf][cc-2]= SoM(sm,y)
                m[cf][cc] = 0
                return f_l_aux(m,1,cf+1,0)
            else:
                y = m[cf][cc]
                m[cf][cc-1] = y
                m[cf][cc] = 0
                return f_l_aux(m,1,cf+1,0)
        if(m[cf][cc-1]==m[cf][cc]):
            y = m[cf][cc]
            m[cf][cc-1]= SoM(sm,y)
            m[cf][cc] = 0
            return f_l_aux(m,1,cf+1,0)
        else:
            return f_l_aux(m,1,cf+1,0)

#Auxiliar encargada de la flecha abajo.
def f_down_aux(m,cc,cf,cn):
    if(cc==4):
        return m
    if(cf>0):
        if(cf==2):
            if(m[cf+1][cc]==0):
                y = m[cf][cc]
                m[cf+1][cc] = y
                m[cf][cc] = 0
                return f_down_aux(m,cc,cf-1,cn)
            if(m[cf+1][cc]==m[cf][cc]):
                y = m[cf][cc]
                m[cf+1][cc]= SoM(sm,y)
                m[cf][cc] = 0
                return f_down_aux(m,cc,cf-1,1)
            else:
                return f_down_aux(m,cc,cf-1,cn)
        if(cf==1):
            if(m[cf+1][cc]==0 and m[cf+2][cc]==0):
                y = m[cf][cc]
                m[cf+2][cc] = y
                m[cf][cc] = 0
                return f_down_aux(m,cc,cf-1,cn)
            if(m[cf+1][cc]==0):
                if(m[cf+2][cc]==m[cf][cc] and cn==0):
                    y = m[cf][cc]
                    m[cf+2][cc]= SoM(sm,y)
                    m[cf][cc] = 0
                    return f_down_aux(m,cc,cf-1,cn)
                else:
                    y = m[cf][cc]
                    m[cf+1][cc] = y
                    m[cf][cc] = 0
                    return f_down_aux(m,cc,cf-1,cn)
            if(m[cf+1][cc]==m[cf][cc]):
                y = m[cf][cc]
                m[cf+1][cc]= SoM(sm,y)
                m[cf][cc] = 0
                return f_down_aux(m,cc,cf-1,2)
            else:
                return f_down_aux(m,cc,cf-1,cn)
    else:
        if(m[cf+1][cc]==0 and m[cf+2][cc]==0 and m[cf+3][cc]==0):
            y = m[cf][cc]
            m[cf+3][cc] = y
            m[cf][cc] = 0
            return f_down_aux(m,cc+1,2,0)
        if(m[cf+1][cc]==0 and m[cf+2][cc]==0):
            if(m[cf+3][cc]==m[cf][cc] and cn==0):
                y = m[cf][cc]
                m[cf+3][cc]= SoM(sm,y)
                m[cf][cc] = 0
                return f_down_aux(m,cc+1,2,0)
            else:
                y = m[cf][cc]
                m[cf+2][cc] = y
                m[cf][cc] = 0
                return f_down_aux(m,cc+1,2,0)
        if(m[cf+1][cc]==0):
            if(m[cf+2][cc]==m[cf][cc] and cn!=2):
                y = m[cf][cc]
                m[cf+2][cc]= SoM(sm,y)
                m[cf][cc] = 0
                return f_down_aux(m,cc+1,2,0)
            else:
                y = m[cf][cc]
                m[cf+1][cc] = y
                m[cf][cc] = 0
                return f_down_aux(m,cc+1,2,0)
        if(m[cf+1][cc]==m[cf][cc]):
            y = m[cf][cc]
            m[cf+1][cc]= SoM(sm,y)
            m[cf][cc] = 0
            return f_down_aux(m,cc+1,2,0)
        else:
            return f_down_aux(m,cc+1,2,0)

#Función encargada de declarar la condición de derrota por movimiento.
#Salida: Si el jugador aún puede jugar retorna un True, si perdió; retorna un False.
def gameover_1(cf,cc):
    global m
    if(cf==4):
        return False
    #Verificaciones para la primera y última fila.
    if(cf==0 or cf==3):
        #Esquinas.
        if(cf==0 and cc==0):
            if(m[cf+1][cc]==0 or m[cf+1][cc]==m[cf][cc]) or (m[cf][cc+1]==0 or m[cf][cc+1]==m[cf][cc]):
                return True
            else:
                return gameover_1(cf,cc+1)
        if(cf==0 and cc==3):
            if(m[cf+1][cc]==0 or m[cf+1][cc]==m[cf][cc] or m[cf][cc-1]==0 or m[cf][cc-1]==m[cf][cc]):
                return True
            else:
                return gameover_1(cf+1,0)
        if(cf==3 and cc==0):
            if(m[cf-1][cc]==0 or m[cf-1][cc]==m[cf][cc] or m[cf][cc+1]==0 or m[cf][cc+1]==m[cf][cc]):
                return True
            else:
                return gameover_1(cf,cc+1)
        if(cf==3 and cc==3):
            if(m[cf-1][cc]==0 or m[cf-1][cc]==m[cf][cc] or m[cf][cc-1]==0 or m[cf][cc-1]==m[cf][cc]):
                return True
            #Al llegar al else el jugador perdió.
            else:
                return gameover_1(cf+1,0)
        #Techo centro o base centro.
        if(cc==1 or cc==2):
            if(cf==0):
                if(m[cf][cc-1]==0 or m[cf][cc-1]==m[cf][cc] or m[cf][cc+1]==0 or m[cf][cc+1]==m[cf][cc] or m[cf+1][cc]==0 or m[cf+1][cc]==m[cf][cc]):
                    return True
                else:
                    return gameover_1(cf,cc+1)
            if(cf==3):
                if(m[cf][cc-1]==0 or m[cf][cc-1]==m[cf][cc] or m[cf][cc+1]==0 or m[cf][cc+1]==m[cf][cc] or m[cf-1][cc]==0 or m[cf-1][cc]==m[cf][cc]):
                    return True
                else:
                    return gameover_1(cf,cc+1)
    #Verificaciones para las filas centrales.
    else:
        #Lateral izquierdo central.
        if(cc==0):
            if(m[cf-1][cc]==0 or m[cf-1][cc]==m[cf][cc] or m[cf+1][cc]==0 or m[cf+1][cc]==m[cf][cc] or m[cf][cc+1]==0 or m[cf][cc+1]==m[cf][cc]):
                return True
            else:
                return gameover_1(cf,cc+1)
        #Lateral derecho central.
        if(cc==3):
            if(m[cf-1][cc]==0 or m[cf-1][cc]==m[cf][cc] or m[cf+1][cc]==0 or m[cf+1][cc]==m[cf][cc] or m[cf][cc-1]==0 or m[cf][cc-1]==m[cf][cc]):
                return True
            else:
                return gameover_1(cf+1,0)
        #Cuadrado central.
        if(cc==1 or cc==2):
            if(m[cf-1][cc]==0 or m[cf-1][cc]==m[cf][cc] or m[cf+1][cc]==0 or m[cf+1][cc]==m[cf][cc] or m[cf][cc+1]==0 or m[cf][cc+1]==m[cf][cc] or m[cf][cc-1]==0 or m[cf][cc-1]==m[cf][cc]):
                return True
            else:
                return gameover_1(cf,cc+1)

#Condición para perder debido al límite de tiempo.
def gameover_2(s):
    if(s==0):
        return gameover(True)
    else:
        time.sleep(1)
        return gameover_2(s-1)

#Acciones del gameover.
def gameover(x):
    global score
    if (x==True):
        nombre = ""
        print("Gameover my dude, your score is:", score)

#Auxiliar para ver si ya se ganó.
def TryWin(m,a,b):
    if(a==4):
        return False
    if(m[a][b]==2048):
        return True
    else:
        if(b!=3):
            return TryWin(m,a,b+1)
        else:
            return TryWin(m,a+1,0)

def win(x):
    if (x==True):
        score="Perfect Score"

#Función que se encarga de encontrar la puntuación
def findScore(res):
    global score
    score += res
