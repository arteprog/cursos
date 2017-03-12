# PONG _ PASSO 2: LENDO OS POTENCIÔMETROS

# ARDUINO
add_library('serial') #import processing.serial.*;
add_library('arduino') #import cc.arduino.*;
POT_A = 0   # Pino que vai ser lido
POT_V = 5   # Pino que vai ser lido
SERIAL = 32  # Arduino na lista de portas seriais

#JOGADORES
MEIO_JOGADOR = 50
ESPESSURA_JOGADOR = 10

def setup():
  size(1024, 512)

  global arduino  
  # println((Arduino.list()))
  arduino = Arduino(this, Arduino.list()[SERIAL], 57600) # objeto Arduino

def draw():
  background(0) # limpa a tela

  JOGADOR_A_Y = arduino.analogRead(POT_A)/2
  fill(0,0,255)
  rect (0,
        JOGADOR_A_Y - MEIO_JOGADOR,
        ESPESSURA_JOGADOR,
        MEIO_JOGADOR*2)

  JOGADOR_V_Y = arduino.analogRead(POT_V)/2
  fill(255,0,0)
  rect (width - ESPESSURA_JOGADOR,
        JOGADOR_V_Y - MEIO_JOGADOR,
        ESP_JOGADOR,
        MEIO_JOGADOR*2)   