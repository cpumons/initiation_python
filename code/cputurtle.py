import turtle
import io
from PIL import Image
import os
import random

t = turtle.Turtle()


def attend(msg="Press enter to quit."):
    input(msg)


def avance(x):
    t.fd(x)


def recule(x):
    t.bk(x)


def droite(a=90):
    t.rt(a)


def gauche(a=90):
    t.lt(a)


def souleve():
    t.up()


def appuie():
    t.down()


def epaisseur(x):
    t.width(x)


def couleur_aleatoire():
    r = random.randrange(255) / 256
    g = random.randrange(255) / 256
    b = random.randrange(255) / 256

    t.pencolor((r, g, b))


def save(email=None, filename="image.png"):
    canvas = turtle.getScreen().getCanvas()
    ps = canvas.postscript(colormode="color")
    img = Image.open(io.BytesIO(ps.encode("utf-8")))
    path = os.getcwd()
    img.save(os.path.join(path, filename))
    # todo send mail


if __name__ == "__main__":
    epaisseur(3)
    couleur_aleatoire()
    avance(100)
    droite()
    couleur_aleatoire()
    avance(100)
    attend()
