# Pong com potenciômetros, versão dojo
[Instalar Processing Modo Python](villares.github.io/como-instalar-o-processing-modo-python/), baixar no próprio IDE do Processing a biblioteca Firmata(Arduino). Conectar um Arduino ao computador com cabo USB. Instalar no Arduino o sketch 'Firmata All Inputs'. Conectar os pinos centrais de dois potenciômetros aos pinos A0 e A5 do Arduino (um em cada). Quanto aos outros dois pinos de cada potenciômetro, um vai em GND e o outro em +5V.

0. Atividade inspirada na metodologia [Coding Dojo](https://pt.wikipedia.org/wiki/Coding_Dojo), na qual participantes experimentam *baby steps* - piloto e co-piloto, trocas a cada 5min;
1. Primeiro alterar o código `potenciometros.pyde` de círculos para jogadores retangulares que se movem na vertical;
2. Finalmente transferir o código de leitura dos potenciômetros para o `pong-sem-potenciometros.pyde`.
