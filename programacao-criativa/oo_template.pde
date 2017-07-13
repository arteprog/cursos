// Substitua MeuNome pelo seu nome da classe (com a inicial maiúscula)
MeuNome objeto_teste;

void setup() {
  size(600, 400);
  rectMode(CENTER);
  objeto_teste = new MeuNome(100, 100, 50);
}

void draw() {
  background(128);
  objeto_teste.desenha();  
  objeto_teste.move();
}

// Substitua MeuNome pelo seu nome da classe (com a inicial maiúscula)
class MeuNome {
  float x, y, vx, vy, tamanho;
  color cor;
  // Aqui vai o construtor de novos objetos da sua classe
  MeuNome(float px, float py, float ptam) {
    x = px;
    y = py;
    tamanho = ptam;
    cor = color(255);
    vx = random(-2, 2);
    vy = random(-2, 2);
  }
  void desenha() {
    // Aqui você desenha o seu objeto (este exemplo muda com o mouse perto)
    if (dist(mouseX, mouseY, x, y)<tamanho/2) {
      // com o mouse perto
      fill(255, 0, 0);
      rect(x, y, tamanho, tamanho);
    } else {
      // com o mouse longe
      fill(cor);
      ellipse ( x, y, tamanho, tamanho);
    }
  }
  // Aqui você define como seu objeto se move
  void move() {
    x = x + vx;
    y = y + vy;
    // este exemplo inverte a velocidade quando bate nas bordas
    if (x < 0 || x > width) { 
      vx = -vx;
    }
    if (y < 0 || y > height) { 
      vy = -vy;
    }
  }
}
