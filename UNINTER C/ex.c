#include <stdio.h>
#include <locale.h>

int main ()
{
    setlocale(LC_ALL,"Portuguese");
    
    int x = 10;
    
    x = x + 1; //x++;
      
    return 0;
}