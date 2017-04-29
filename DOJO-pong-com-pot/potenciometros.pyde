""" 
Código para a leitura dos potenciômetros, requer biblioteca Firmata (Arduino)
Você deve ajustar o valor de SERIAL para porta USB com seu Arduino
No Linux pode ser que precise fazer `sudo chmod 666 /dev/ttyUSB0' ou equivalente.
"""

# ARDUINO
add_library('serial')  # import processing.serial.*;
add_library('arduino')  # import cc.arduino.*;
POT_AMARELO = 0   # Pino que vai ser lido controle 'jogador Amarelo'
POT_VERDE = 5   # Pino que vai ser lido controle 'jogador Verde'
SERIAL = 32  # MUDE para o índice do seu Arduino na lista de portas seriais!

# JOGADORES
MEIA_ALTURA_JOGADOR = 50  # tamanho de meia altura do jogador
LARGURA_JOGADOR = 10

def setup():
    size(600, 400)  # tamanho da tela
    global arduino
    # println((Arduino.list())) # Para ver a lista de portas seriais!
    arduino = Arduino(this, Arduino.list()[SERIAL], 57600)

def draw():
    background(0)  # limpa a tela
    
    # JOGADORES
    AMARELO_Y = arduino.analogRead(POT_AMARELO) / 2
    fill(255, 255, 0)  # Amarelo fill(vermelho->255, verde->255, azul->0)
    ellipse(MEIA_ALTURA_JOGADOR,     # ellipse( x, y, altura, largura)
            MEIA_ALTURA_JOGADOR,
            AMARELO_Y,
            AMARELO_Y)
    VERDE_Y = arduino.analogRead(POT_VERDE) / 2
    fill(0, 255, 0)  # Verde fill(vermelho->0, verde->255, azul->0)
    ellipse(width - 50,           # ellipse( x, y, altura, largura)
            MEIA_ALTURA_JOGADOR,
            VERDE_Y,
            VERDE_Y)
