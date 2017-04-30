# Pong com potenciômetros, versão dojo
Atividade inspirada na metodologia [Coding Dojo](https://pt.wikipedia.org/wiki/Coding_Dojo), na qual participantes experimentam *baby steps* em direção à solução de um desafio, todos circulando, se revezando, no papéis de piloto e co-piloto, com trocas a cada 5 minutos.

<img src="imgs/arduino-foto-joao-adriano-freitas.jpg" style="float:right" width=400px alt="Foto: João Adriano Freitas 29/4/2017" />

0. **[Preparação]** [Instalar Processing Modo Python](villares.github.io/como-instalar-o-processing-modo-python/), baixar no próprio IDE do Processing a biblioteca Firmata(Arduino). Conectar um Arduino preparado com o sketch [Firmata All Inputs](https://github.com/firmata/arduino/blob/master/examples/AllInputsFirmata/AllInputsFirmata.ino) ao computador com cabo USB. Conectar os pinos centrais de dois potenciômetros aos pinos A0 e A5 do Arduino (um em cada). Os outros dois pinos de cada potenciômetro, devem ir em GND e em +5V respectivamente (confira na imagem).
1. **[Primeiro desafio]** Alterar o código em `potenciometros.pyde`, que inicialmente produz dois círculos com os tamanhos controlados pelos potenciômetros, para obtermos dois jogadores retangulares que se movem verticalmente;ado 
2. **[Desafio Final]** Transferir o código de leitura dos potenciômetros via Arduino, do arquivo anterior, para fazer com que o jogo em `pong-sem-potenciometros.pyde` passe a ter os seus jogadores controlados pelos potenciômetros.
