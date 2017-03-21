/* A interação da cor, por Josef Albers
 Subtração da cor, Capítulo VII 
 */

float [] cores;

void setup() {
  fullScreen();
  rectMode(CENTER);
  cores = new float[6];
  for (int i = 0; i < 6; i++) { 
    cores[i] = random(0, 255);
  }
}

void draw() {
  noStroke();
  fill(cores[0], cores[1], cores[2]);
  rect(width/4, height/2, width/2, height);
  
  fill(cores[3], cores[4], cores[5]);
  rect(width/4, height/2, width/10, height/5);
  rect(width/4+width/2, height/2, width/2, height); 
  
  fill(cores[0], cores[1], cores[2]);
  rect(width/4+width/2, height/2, width/10, height/5);
}

void keyPressed(){
  cores = new float[6];
  for (int i = 0; i < 6; i++) { 
    cores[i] = random(0, 255);
  }
}
