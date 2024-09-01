#include <stdio.h>
#include <locale.h>

int main () {
    setlocale(LC_ALL,"Portuguese");
    
    int x = 0;
    while (x <= 100)
    {
        if(x % 2 == 0)
        {
            printf("O número %i é par!", x);
        }
        else
        {
            printf("O número %i é impar!", x);
        }
        x++;
    }
    
    return 0;
}

/*int main () {
    setlocale(LC_ALL,"Portuguese");
    
    for(int x = 0; x <= 100; x++)
    {
        if(x % 2 == 0)
        {
            printf("O número %i é par!", x);
        }
        else
        {
            printf("O número %i é impar!", x);
        }
        x++;
    }
    
    return 0;
}*/


