#include <stdio.h>
#include <locale.h>

int main () {
    setlocale(LC_ALL,"Portuguese");
    
    int x;
    printf("Digite um valor para testarmos: ");
    scanf_s("%i", &x);

    if (x % 2 == 0)
    {
        printf("O número é par!");
    }
    else 
    {
        printf("O número é ímpar!");
    }
      
    return 0;
}