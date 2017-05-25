// Exemplo de como carregar dados de um arquivo CSV externo

Table tabela;
String  URL = "https://docs.google.com/spreadsheets/d/1cdwfpjI9OEM1_Cd4djzdMqBiu82Q36eMSJLDLR9cz24/pub?gid=0&single=true&output=csv";

void setup() {
  size(200, 200);
  tabela = loadTable(URL, "header, csv");
  println(tabela.getRowCount() + " linhas na tabela"); 
  for (TableRow row : tabela.rows()) {
    float x = row.getFloat("x");
    float y = row.getFloat("y");
    float tamanho = row.getFloat("tamanho");
    int R = row.getInt("R");
    int G = row.getInt("G");
    int B = row.getInt("B");
    fill(R, G, B);
    ellipse(x, y, tamanho, tamanho);
  }
}
