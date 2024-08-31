#include <stdio.h>
#include <locale.h>

int main ()
{
    setlocale(LC_ALL,"Portuguese");
    
    int x, y, res;
    printf("Digite um valor:");
    scanf_s("%i", &x);
    
    printf("Digite um segundo valor:");
    scanf_s("%i", &y);

    res = x + y;
    printf("O resultado da som de %i com %i e %i.",x, y, res);

    return 0;
}