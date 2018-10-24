from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *

resolutionX = 1200
resolutionY = 600
janela = Window(resolutionX,resolutionY)
janela.set_title("Pong")

global velx, vely, velPad, cont, pady, padx, pad1y, pad1x, pad2y, pad2x

fundo = GameImage("imagens/fundo.jpg")
fundo.draw()

bola = Sprite("imagens/bola.png")
bola.set_position(((resolutionX / 2) - 20) , ((resolutionY / 2) - 20))

pad1 = Sprite("imagens/pad.jpg")
pad1x = 0
pad1y = (resolutionY / 2) - 20
pad1.set_position(pad1x,pad1y)

pad2 = Sprite("imagens/pad.jpg")
pad2x = resolutionX - 30
pad2y = (resolutionY / 2) - 20
pad2.set_position(pad2x,pad2y)

teclado = Window.get_keyboard()


velx = 300
vely = 300
velPad = 400
cont = 0



#def movimento():

#def colisao():

while(True):
    fundo.draw()


    # Movimentação da bolinha
    bola.x += velx * janela.delta_time()
    bola.y += vely * janela.delta_time()

    #Comandos do teclado
    if (teclado.key_pressed("W")):
        if pad1y > 0:
            pad1y = pad1y - velPad * janela.delta_time()
            pad1.set_position(pad1x, pad1y)

    if (teclado.key_pressed("S")):
        if (pad1y + 150) < resolutionY:
            pad1y = pad1y + velPad * janela.delta_time()
            pad1.set_position(pad1x, pad1y)


    if (teclado.key_pressed("UP")):
        if pad2y > 0:
            pad2y = pad2y - velPad * janela.delta_time()
            pad2.set_position(pad2x, pad2y)

    if (teclado.key_pressed("DOWN")):
        if (pad2y + 150) < resolutionY:
            pad2y = pad2y + velPad * janela.delta_time()
            pad2.set_position(pad2x, pad2y)



    # Colisão com as paredes
    if (bola.y + 40) > 600 or bola.y < 0:
        vely = -vely

    if (bola.x < 0):
        bola.set_position((resolutionX / 2), (resolutionY / 2))
        vely = 300
        velx = 300
    if (bola.x + 40) > resolutionX:
        bola.set_position((resolutionX / 2), (resolutionY / 2))
        velx = -300
        vely = 300

    # Colisão com os pads
    if (bola.collided_perfect(pad2)):
        velx = -velx
        cont += 1
        if (cont % 2) == 0 and cont < 15:
            velx += 100
            vely += 100
            # Falta fazer um limite

    if (bola.collided_perfect(pad1)):
        velx = abs(velx)
        cont += 1
        if (cont % 2) == 0 and cont < 15:
            velx += 100
            vely += 100

    pad1.draw()
    pad2.draw()
    bola.draw()
    janela.update()