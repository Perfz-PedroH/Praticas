#include <stdio.h>
#include <locale.h>

int main ()
{
    setlocale(LC_ALL,"Portuguese");
    
    float preco1, preco2, preco3;

    printf("Digite o preco do primeiro produto: ");
    scanf_s("%f", &preco1);

    printf("Digite o preco do segundo produto: ");
    scanf_s("%f", &preco2);

    printf("Digite o preco do terceiro produto: ");
    scanf_s("%f", &preco3);

    if ((preco1 < preco2) && (preco1 < preco3)) 
    {
        printf("O produto 1 eh mais barato!");
    }
    else if ((preco2 < preco1) && (preco2 < preco3))
    {
        printf("O produto 2 eh mais barato!");
    }
    else 
    {
        printf("O produto 3 eh mais barato!");
    }
    return 0;
}