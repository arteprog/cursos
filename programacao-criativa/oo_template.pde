MeuNome meu_nome;

void setup() {
  size(600, 400);
  rectMode(CENTER);
  meu_nome = new MeuNome(100, 100, 50);
}

void draw() {
  background(128);
  meu_nome.desenha();  
  meu_nome.move();
}

class MeuNome {
  float x, y, vx, vy, tamanho;
  color cor;
  MeuNome(float px, float py, float ptam) {
    x = px;
    y = py;
    tamanho = ptam;
    cor = color(255);
    vx = random(-2, 2);
    vy = random(-2, 2);
  }
  void desenha() {
    if (dist(mouseX, mouseY, x, y)<tamanho/2) {
      fill(255, 0, 0);
      rect(x, y, tamanho, tamanho);
    } else {
      fill(cor);
      ellipse ( x, y, tamanho, tamanho);
    }
  }
  void move() {
    x = x + vx;
    y = y + vy;
    if (x < 0 || x > width) { 
      vx = -vx;
    }
    if (y < 0 || y > height) { 
      vy = -vy;
    }
  }
}
