# PONG _ PASSO 0: A BOLA

# BOLA
BOLA_TAMANHO = 20

def setup():
    size(600, 400) # tamanho da tela
    # BOLA
    global BOLA_X, BOLA_Y, BOLA_VEL_X, BOLA_VEL_Y
    BOLA_X, BOLA_Y = width/2, height/2
    BOLA_VEL_X, BOLA_VEL_Y = 0, 0

def draw():
    background(0) # limpa a tela

    # BOLA
    global BOLA_X, BOLA_Y, BOLA_VEL_X, BOLA_VEL_Y
    BOLA_X = BOLA_X + BOLA_VEL_X
    BOLA_Y = BOLA_Y + BOLA_VEL_Y
    fill(255)
    ellipse(BOLA_X, BOLA_Y, BOLA_TAMANHO, BOLA_TAMANHO)
    if BOLA_X < 0:
        BOLA_VEL_X = -BOLA_VEL_X    
    if BOLA_X > width:
        BOLA_VEL_X = -BOLA_VEL_X    
    if BOLA_Y < 0:
        BOLA_VEL_Y = -BOLA_VEL_Y    
    if BOLA_Y > height:
        BOLA_VEL_Y = -BOLA_VEL_Y    

def keyPressed():  # 'reset' quando apertar uma tecla
    global BOLA_X, BOLA_Y, BOLA_VEL_X, BOLA_VEL_Y
    BOLA_X, BOLA_Y = width/2, height/2
    BOLA_VEL_X = (-4,4)[int(random(2))] 
    BOLA_VEL_Y = (-4,4)[int(random(2))]
