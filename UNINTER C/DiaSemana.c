#include <stdio.h>
#include <locale.h>

//Programa que informa o dia da semana baseado em um numero
int main ()
{
    setlocale(LC_ALL,"Portuguese");
    
    int numero;

    printf("Digite o valor numerico do dia da semana desejada: ");
    scanf_s ("%i", &numero);

    switch (numero)
    {
    case 1:
        printf("Domingo!");
        break;

    case 2:
        printf("Segunda!");
        break;

    case 3:
        printf("Terca!");
        break;

    case 4:
        printf("Quarta!");
        break;

    case 5:
        printf("Quinta!");
        break;

    case 6:
        printf("Sexta!");
        break;

    case 7:
        printf("Sabado!");
        break;
    
    default:
        printf("Numero incorreto!");
    }
      
    return 0;
}