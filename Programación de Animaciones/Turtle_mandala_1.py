import turtle
import random

# Configuración de la ventana

ventana = turtle.Screen()
ventana.setup(width=800,height=600)
ventana.bgcolor('black')

colores = ['red','blue','orange','yellow','magenta','purple','peru','ivory','dark orange']

# Objetos Turtle

luna = turtle.Turtle()
luna.speed(100)
luna.hideturtle()

estrella = turtle.Turtle()
estrella.speed(100)
estrella.hideturtle()

texto = turtle.Turtle()
texto.speed(100)
texto.hideturtle()

# Funciones

def dibujar_luna(pos,color):
    x,y = pos

    luna.color(color)
    luna.begin_fill()
    luna.penup()
    luna.goto(x,y)
    luna.pendown()
    luna.circle(50)
    luna.end_fill()

def dibujar_estrella(x,y,color,longitud):	
    estrella.color(color)

    estrella.penup()
    estrella.goto(x,y)
    estrella.pendown()

    estrella.begin_fill()
    for i in range(5):
        estrella.forward(longitud)
        estrella.right(144)
        estrella.forward(longitud)
    estrella.end_fill()

def posicion_aleatoria():
    return random.randint(-390,390), random.randint(-200,290)

def longitud_aleatoria():
    return random.randint(5,25)

def escribir_texto(color):
    texto.color(color)

    texto.penup()
    texto.goto(-180,-270)
    texto.pendown()
    estilo = ('Stencil Std Bold',50,'normal')
    texto.write('Buenas Noches',font=estilo,move=True)

# Programa principal

dibujar_luna((-300,170),'white')
dibujar_luna((-278,183),'black')

while True:
    color = random.choice(colores)
    x ,y = posicion_aleatoria()
    longitud = longitud_aleatoria()

    dibujar_estrella(x,y,color,longitud)
    escribir_texto(color)
    # luna.clear()

turtle.done()
