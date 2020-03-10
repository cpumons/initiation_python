import turtle
import io
from PIL import Image
import os
import random

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

t = turtle.Turtle()
t.shape("turtle")
#t.color('green')


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


def sauver(email=None, filename="image.png", envoyer=False):
    canvas = t.getscreen().getcanvas()
    ps = canvas.postscript(colormode="color")
    img = Image.open(io.BytesIO(ps.encode("utf-8")))
    path = os.getcwd()
    img.save(os.path.join(path, filename))
    # todo send mail

    if not envoyer:
        return
    
    fromaddr = "adresse email" # a completer
    toaddr = email

    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Ton dessin réalisé à l'atelier de CPUMons !"
    
    body="Salut !\n Tu trouvera en pièce jointe le dessin que tu as réalisé avec notre petite tortue Turtle !\n\n A bientôt ! La team CPUMons\n "
    msg.attach(MIMEText(body, 'plain'))
    
    attachment=open(filename, "rb")
    p=MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p) 
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p)

    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls()
    s.login(fromaddr, "mot de passe") # a completer
    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)
    s.quit() 


    

if __name__ == "__main__":
    epaisseur(3)
    couleur_aleatoire()
    avance(100)
    droite()
    couleur_aleatoire()
    avance(100)
    attend()
