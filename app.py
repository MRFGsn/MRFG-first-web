import turtle
from flask import Flask
app = Flask(__name__)

@app.route('/')


Sl=turtle.getscreen()
S=turtle.Turtle()
turtle.bgcolor('black')
S.speed(3)
S.penup()
S.pen(pencolor='red',fillcolor='red',pensize='4')
S.lt(180)
S.fd(200)
S.rt(90)
S.fd(500)
S.rt(90)
S.pendown()
S.fd(400)
S.goto(0,400)
S.lt(45)
S.goto(200,300)
S.goto(-200,300)

L=S.clone()
L.pen(pencolor='blue',fillcolor='blue',pensize='4')
L.penup()
L.rt(135)
L.fd(30)
L.pendown()
L.lt(90)
L.fd(400)
L.rt(90)
L.fd(170)
L.rt(90)
L.fd(200)
L.rt(90)
L.fd(160)
L.goto(-200,70)
L.penup()
L.lt(180)
L.fd(30)

J=L.clone()
J.pen(pencolor='purple',fillcolor='purple',pensize='4')
J.pendown()
J.lt(90)
J.fd(400)
J.rt(90)
J.fd(150)
J.penup()
J.bk(150)
J.lt(90)
J.bk(180)
J.pendown()
J.rt(90)
J.fd(120)
J.penup()
J.bk(120)
J.rt(90)
J.fd(220)
J.lt(90)

K=J.clone()
K.pen(pencolor='aqua',fillcolor='aqua',pensize='4')
K.fd(180)
K.pendown()
K.lt(90)
K.fd(400)
K.rt(90)
K.fd(220)
K.rt(90)
K.fd(50)
K.penup()
K.fd(350)
K.rt(90)
K.fd(220)
K.pendown()
K.rt(180)
K.fd(220)
K.lt(90)
K.fd(200)
K.lt(90)
K.fd(105)
K.rt(180)
K.fd(120)
K.rt(90)
K.fd(150)
K.penup()
K.fd(100)
K.rt(90)
K.bk(50)
K.pendown()

A=K.clone()
A.pen(pencolor='purple',fillcolor='purple',pensize='4')
A.fd(1000)
A.rt(90)

P=A.clone()
P.pen(pencolor='red',fillcolor='red',pensize='4')
P.fd(500)
P.rt(90)

E=P.clone()
E.pen(pencolor='aqua',fillcolor='aqua',pensize='4')
E.fd(1000)
E.rt(90)

X=E.clone()
X.pen(pencolor='blue',fillcolor='blue',pensize='4')
X.fd(500)
X.rt(90)




if __name__ == "__main__":
    app.run()
