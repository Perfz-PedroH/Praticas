#include <stdio.h>
#include <locale.h>

int main ()
{
    setlocale(LC_ALL,"Portuguese");
    
    int x, y;
    char op;

    printf("Digite a operação desejada:");
    scanf_s("%c", &op);

    printf("Digite o primeiro valor:");
    scanf_s("%i", &x);
    printf("Digite o segundo valor valor:");
    scanf_s("%i", &y);

    switch (op) //
    {
    case '+':
        printf("%i + %i = %i", x, y, x + y);
        break;
    case '-':
        printf("%i - %i = %i", x, y, x - y);
        break;
    case '*':
        printf("%i * %i = %i", x, y, x * y);
        break;
    case '/':
        printf("%i / %i = %i", x, y, x / y);
        break;
    default: //equivale ao elif do python
        printf("Opção inválida!");
        break;
    }
      
    return 0;
}