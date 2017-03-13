# PONG _ PASSO 4: GAME OVER!

# ARDUINO
add_library('serial') #import processing.serial.*;
add_library('arduino') #import cc.arduino.*;
POT_A = 0   # Pino que vai ser lido controle 'jogador Amarelo'
POT_V = 5   # Pino que vai ser lido controle 'jogador Verde'
SERIAL = 5  # Arduino na lista de portas seriais

# JOGADORES
MEIO_JOGADOR = 50
ESPESSURA_JOGADOR = 10

# BOLA
BOLA_TAMANHO = 20

def setup():
    size(600, 400) # tamanho da tela
    
    global arduino
    # println((Arduino.list()))
    arduino = Arduino(this, Arduino.list()[SERIAL], 57600)
    
    # BOLA
    global BOLA_X, BOLA_Y, BOLA_VEL_X, BOLA_VEL_Y
    BOLA_X, BOLA_Y = width / 2, height / 2
    BOLA_VEL_X, BOLA_VEL_Y = 0, 0

def draw():
    background(0) # limpa a tela

    #JOGADORES
    JOGADOR_A_Y = arduino.analogRead(POT_A) / 2
    fill(255, 255, 0) # Amarelo
    rect (0,
          JOGADOR_A_Y - MEIO_JOGADOR,
          ESPESSURA_JOGADOR,
          MEIO_JOGADOR*2)
    JOGADOR_V_Y = arduino.analogRead(POT_V) / 2
    fill(0, 255, 0) # Verde
    rect (width - ESPESSURA_JOGADOR,
          JOGADOR_V_Y - MEIO_JOGADOR,
          ESPESSURA_JOGADOR,
          MEIO_JOGADOR * 2)   

    # BOLA
    global BOLA_X, BOLA_Y, BOLA_VEL_X, BOLA_VEL_Y
    BOLA_X = BOLA_X + BOLA_VEL_X
    BOLA_Y = BOLA_Y + BOLA_VEL_Y
    fill(255)
    ellipse(BOLA_X, BOLA_Y, BOLA_TAMANHO, BOLA_TAMANHO)
    if BOLA_X < 0:
        if JOGADOR_A_Y - MEIO_JOGADOR < BOLA_Y < JOGADOR_A_Y + MEIO_JOGADOR:
            BOLA_VEL_X = -BOLA_VEL_X
        else:
            BOLA_VEL_X, BOLA_VEL_Y = 0, 0
    if BOLA_X > width:
        if JOGADOR_V_Y - MEIO_JOGADOR < BOLA_Y < JOGADOR_V_Y + MEIO_JOGADOR:
            BOLA_VEL_X = -BOLA_VEL_X
        else:
            BOLA_VEL_X, BOLA_VEL_Y = 0, 0        
    if BOLA_Y < 0:
        BOLA_VEL_Y = -BOLA_VEL_Y    
    if BOLA_Y > height:
        BOLA_VEL_Y = -BOLA_VEL_Y    

def keyPressed(): # 'reset' quando apertar uma tecla
    global BOLA_X, BOLA_Y, BOLA_VEL_X, BOLA_VEL_Y
    BOLA_X, BOLA_Y = width / 2, height / 2
    BOLA_VEL_X = (-4, 4)[int(random(2))] 
    BOLA_VEL_Y = (-4, 4)[int(random(2))]
