# PONG _ PASSO 4: GAME OVER!

# ARDUINO
add_library('serial') #import processing.serial.*;
add_library('arduino') #import cc.arduino.*;
POT_A = 0   # Pino que vai ser lido controle 'jogador Amarelo'
POT_V = 5   # Pino que vai ser lido controle 'jogador Verde'
SERIAL = 0  # MUDE para o índice do seu Arduino na lista de portas seriais!

# JOGADORES
MEIO_JOGADOR = 50  # Meia altura do jogador
ESPESSURA_JOGADOR = 10  

# BOLA
BOLA_TAMANHO = 20

def setup():
    size(600, 400) # tamanho da tela
    
    global arduino
    # println((Arduino.list())) # Para ver a lista de portas seriais!
    arduino = Arduino(this, Arduino.list()[SERIAL], 57600)
    
    # BOLA
    global BOLA_X, BOLA_Y, BOLA_VEL_X, BOLA_VEL_Y
    BOLA_X, BOLA_Y = width / 2, height / 2  # Bola no meio da tela
    BOLA_VEL_X, BOLA_VEL_Y = 0, 0  # Bola parada

def draw():
    background(0) # limpa a tela

    #JOGADORES
    JOGADOR_A_Y = arduino.analogRead(POT_A) / 2  # lê o potenciômetro A
    fill(255, 255, 0)  # cor de preenchimento amarelo (vermelho=255, verde=255, azul=0) 
    rect (0,  # posição x do retângulo
          JOGADOR_A_Y - MEIO_JOGADOR,  # posição y do retângulo
          ESPESSURA_JOGADOR,  # largura do retângulo
          MEIO_JOGADOR*2)     # altura do retângulo
    JOGADOR_V_Y = arduino.analogRead(POT_V) / 2  # lê o potenciômetro B
    fill(0, 255, 0)  # cor de preenchimento verde (vermelho=0, verde=255, azul=0)
    rect (width - ESPESSURA_JOGADOR,  # x
          JOGADOR_V_Y - MEIO_JOGADOR, # y
          ESPESSURA_JOGADOR,  # largura
          MEIO_JOGADOR * 2)   # altura

    # BOLA
    global BOLA_X, BOLA_Y, BOLA_VEL_X, BOLA_VEL_Y
    BOLA_X = BOLA_X + BOLA_VEL_X  # atualiza posição horizontal (x) da bola
    BOLA_Y = BOLA_Y + BOLA_VEL_Y  # atualiza posição vertical (y) da bola
    fill(255)  # cor de preenchimento branco, equivale a (255, 255, 2550 
    ellipse(BOLA_X, BOLA_Y, BOLA_TAMANHO, BOLA_TAMANHO)  # desenha a bola
    if BOLA_X < 0:  # Se a bola sair da tela pela esquerda
        if JOGADOR_A_Y - MEIO_JOGADOR < BOLA_Y < JOGADOR_A_Y + MEIO_JOGADOR:
            BOLA_VEL_X = -BOLA_VEL_X
        else:
            BOLA_VEL_X, BOLA_VEL_Y = 0, 0
    if BOLA_X > width:  # Se a bola sair da tela pela direita
        if JOGADOR_V_Y - MEIO_JOGADOR < BOLA_Y < JOGADOR_V_Y + MEIO_JOGADOR:
            BOLA_VEL_X = -BOLA_VEL_X
        else:
            BOLA_VEL_X, BOLA_VEL_Y = 0, 0        
    if BOLA_Y < 0:  # Se a bola sair da tela por cima
        BOLA_VEL_Y = -BOLA_VEL_Y    
    if BOLA_Y > height:  # Se a bola sair da tela por baixo
        BOLA_VEL_Y = -BOLA_VEL_Y    

def keyPressed(): # 'reset' quando apertar uma tecla
    global BOLA_X, BOLA_Y, BOLA_VEL_X, BOLA_VEL_Y
    BOLA_X, BOLA_Y = width / 2, height / 2  # Bola no meio da tela
    BOLA_VEL_X = (-4, 4)[int(random(2))]  # Sorteio da velocidade horizontal da bola
    BOLA_VEL_Y = (-4, 4)[int(random(2))]  # Sorteio da velocidade vertical da bola
    
# FIM
