import turtle

#Ventana

ventana = turtle.Screen()
ventana.bgcolor("white")

#Crea tortuga

emoji = turtle.Turtle()
emoji.speed(5)
emoji.pensize(3)

#Circulo amarillo
emoji.penup()
emoji.goto(0,-100)
emoji.pendown()
emoji.color("yellow")
emoji.begin_fill()
emoji.circle(100)
emoji.end_fill()

#Ojos 
emoji.penup()
emoji.goto(-40,30)
emoji.pendown()
emoji.color("black")
emoji.begin_fill()
emoji.circle(5)
emoji.end_fill()

emoji.penup()
emoji.goto(40,30)
emoji.pendown()
emoji.color("black")
emoji.begin_fill()
emoji.circle(5)
emoji.end_fill()

#Boca

emoji.penup()
emoji.goto(-60,-20)
emoji.pendown()
emoji.right(90)
emoji.color("black")
emoji.pensize(3)
emoji.circle(60,180)

#Mensaje

emoji.penup()
emoji.goto(0,-150)
emoji.pendown()
emoji.write("Feliz día", align="center", font=("Arial",20,"normal"))

#Cierre
turtle.done()







