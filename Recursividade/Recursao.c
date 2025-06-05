
#include <stdio.h>
#include <stdlib.h>



int fatorial(int n)
{
    if(n==0)//Caso Base
        return 1;
    if(n>0)//Passo Indutivo
        return n*fatorial(n-1);
}

int fibonacci(int n)
{
    if(n==0)
        return 0;
    if(n==1)
        return 1;

    if(n>1)
        return fibonacci(n-1)+fibonacci(n-2);

}

int main()
{
    int n = 4;
    printf("Fatorial %d = %d \n",n,fatorial(n));
    return 0;
}
