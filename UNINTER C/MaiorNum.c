#include <stdio.h>
#include <locale.h>

int main () 
{
    setlocale(LC_ALL,"Portuguese");
    
    int num1, num2;

    printf("Digite o primeiro numero: ");
    scanf_s("%d", &num1);
    
    printf("Digite o primeiro numero: ");
    scanf_s("%d", &num2);
    
    if (num1 > num2) 
    {
        printf("Numero 1 eh maior que numero 2!");
    }
    else 
    {
        printf("Numero 2 eh maior que o numero 1");
    }
      
    return 0;
}