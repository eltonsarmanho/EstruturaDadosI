#include <stdio.h>
#include <stdlib.h>



void encontreMaior()
{
    int A[] = {4,3,5,1};
    int n = sizeof(A)/sizeof(A[0]);
    int maior = A[0];
    for(int i = 1; i < n; i++)
    {
        if(A[i] > maior)
            maior = A[i];
    }
    printf("Maior valor: %d\n", maior);
}

void palindromo()
{
    char str[100];
    printf("Digite uma string: ");
    scanf("%s", str);
    
    int len = 0;
    while (str[len] != '\0') {
        // Incrementa o comprimento da string até encontrar o caractere nulo.
        // O caractere nulo ('\0') indica o final da string.
        // Portanto, o loop continua até que len aponte para esse caractere.
        // Isso é útil para determinar o tamanho da string sem usar funções de biblioteca.
        // A variável len é incrementada a cada iteração do loop.
        // Assim, ao final do loop, len conterá o número de caracteres na string.
        // Isso é uma maneira comum de calcular o comprimento de uma string em C.
        len++;
    }
    
    int isPalindrome = 1;
    for (int i = 0; i < len / 2; i++) {
        if (str[i] != str[len - i - 1]) {
            // Se os caracteres correspondentes não forem iguais,
            // a string não é um palíndromo.
            // A variável isPalindrome é definida como 0 (falso).
            // O loop é interrompido, pois já sabemos que a string não é um palíndromo.
            // A comparação é feita entre o caractere na posição i e o caractere na posição len - i - 1.
            // Isso verifica se os caracteres correspondentes do início e do final da string são iguais.
            isPalindrome = 0;
            break;
        }
    }
    
    if (isPalindrome) {
        printf("A string eh um palindromo.\n");
    } else {
        printf("A string nao eh um palindromo.\n");
    }
}



int main() {
    

    palindromo();
    return 0;
}