#include <stdio.h>

// Função auxiliar para trocar dois elementos de posição
void troca(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Função para imprimir o array
void imprimir_array(int A[], int tamanho) {
    for (int i = 0; i < tamanho; i++) {
        printf("%d ", A[i]);
    }
    printf("\n");
}

/**
 * Função de Partição (Esquema de Lomuto).
 * Esta função recebe um array, escolhe o último elemento como pivô,
 * coloca o pivô em sua posição correta no array ordenado,
 * e posiciona todos os menores à esquerda do pivô e todos os maiores à direita.
 */
int particao(int A[], int inicio, int fim) {
    // Estratégia: o último elemento é usado como pivô
    int pivo = A[fim];
    
    // 'i' marca a fronteira onde o próximo elemento menor deve ser inserido.
    // Começa no início do sub-array.
    int i = inicio;
    
    // 'j' percorre o sub-array para encontrar elementos menores que o pivô.
    for (int j = inicio; j < fim; j++) {
        // Se um elemento menor que o pivô é encontrado...
        if (A[j] < pivo) {
            // ...troca-o com o elemento na fronteira 'i'.
            troca(&A[i], &A[j]);
            
            // ...e avança a fronteira 'i' para a próxima posição.
            i++;
        }
    }
    
    // Ao final, coloca o pivô em sua posição correta, trocando-o com A[i].
    troca(&A[i], &A[fim]);
    
    // Retorna o índice onde o pivô foi colocado.
    return i;
}

/**
 * Função principal do QuickSort que implementa a lógica recursiva.
 */
void quick_sort(int A[], int inicio, int fim) {
    if (inicio < fim) {
        // p recebe o índice do pivô que agora está na posição correta
        int p = particao(A, inicio, fim);
        
        // Ordena recursivamente a sub-lista à esquerda do pivô
        quick_sort(A, inicio, p - 1);
        
        // Ordena recursivamente a sub-lista à direita do pivô
        quick_sort(A, p + 1, fim);
    }
}

// Função principal para testar o algoritmo
int main() {
    int array_exemplo[] = {5, 3, 8, 4, 6, 2, 9, 1, 7};
    int n = sizeof(array_exemplo) / sizeof(array_exemplo[0]);
    
    printf("Array original: \n");
    imprimir_array(array_exemplo, n);
    
    quick_sort(array_exemplo, 0, n - 1);
    
    printf("\nArray ordenado: \n");
    imprimir_array(array_exemplo, n);
    
    return 0;
}