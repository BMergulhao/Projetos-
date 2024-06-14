#include <stdio.h>

int main () {
  float tamArquivo, velNet, tempDown; // Considerando que 1 MB = 8 Megabits e 1 min = 60 s

   // Solicita o tamanho do arquivo em MB ao usuário
   printf ("Insira o tamanho do arquivo em MB:");
   scanf ("%f", &tamArquivo);
   
   // Solicita a velocidade de um link de Internet em Mbps
   printf ("Insira a velocidade de um link de Internet em Mbps:");
   scanf ("%f", &velNet);

  // Calcule e informe o tempo aproximado do dowload em minutos 
  // 1º converter o tamanho do arquivo de MB para Megabits e 2º dividir pela velocidade em Mbps.
 // Finalmente, convertendo de segundos para minutos.
tempDown = (tamArquivo * 8) / velNet / 60;  
  printf("O tempo aproximado do dowload em minutos é: %.2f min\n", tempDown);

    return 0;
}


