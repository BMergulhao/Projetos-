#include <stdio.h>
#include <math.h>

// Calculo do delta: Δ = b2 – 4ac
float calDelta(float a, float b, float c) {
    return pow(b, 2) - 4 * a * c;  
// pow calcula o valor de um número elevado ao quadrado
}

// Calculo do zero:  x = – b ± √Δ / 2a
// sqrt retorna a raiz quadrada
float zero(float a, float b, float delta) {
    return (-b + sqrt(delta)) / (2 * a); 
}

// Resultado
void resultado(float x1, float x2) {
    printf("A equação possui dois resultados reais: %.2f e %.2f\n", x1, x2);
}

// Verifica se tem resultados reais. Delta != 0
// Se x for um valor negativo, sqrt retornará um NaN indefinido
void verReal(float delta) {
    if (delta < 0) {
        printf("A equação não possui resultados reais.\n");
    } else {
        printf("A equação possui resultados reais.\n"); 
    }
}

int main() {
    float a, b, c, delta;

    printf("Digite os coeficientes a, b e c: \n");
    printf("a: ");
    scanf("%f", &a);
    printf("b: ");
    scanf("%f", &b);
    printf("c: ");
    scanf("%f", &c);

    delta = calDelta(a, b, c);

    verReal(delta);

    if (delta > 0) {
        float x1 = zero(a, b, delta);
        float x2 = zero(a, b, -delta);
        resultado(x1, x2);
    }

    return 0;
}
