#include <stdio.h>
#include <stdlib.h> // Necessário para malloc() e free()

/**
 * Procedimento para intercalar (merge) dois sub-arrays A[esq..meio] e A[meio+1..dir]
 * de volta para o array principal A.
 */
void intercalar(int A[], int esq, int meio, int dir) {
    // --- Criar vetores temporários ---
    int i, j, k;
    int n1 = meio - esq + 1;
    int n2 = dir - meio;

    // Alocar memória para os vetores temporários
    int* E = (int*)malloc(n1 * sizeof(int));
    int* D = (int*)malloc(n2 * sizeof(int));

    // Verificar se a alocação de memória foi bem-sucedida
    if (E == NULL || D == NULL) {
        printf("Erro na alocação de memória!\n");
        exit(1); // Encerra o programa se a memória não puder ser alocada
    }

    // --- Copiar dados para os vetores temporários E[] e D[] ---
    for (i = 0; i < n1; i++) {
        E[i] = A[esq + i];
    }
    for (j = 0; j < n2; j++) {
        D[j] = A[meio + 1 + j];
    }

    // --- Intercalar os vetores temporários de volta para A[esq..dir] ---
    i = 0;    // Índice inicial do primeiro sub-array (E)
    j = 0;    // Índice inicial do segundo sub-array (D)
    k = esq;  // Índice inicial do sub-array mesclado (em A)

    while (i < n1 && j < n2) {
        if (E[i] <= D[j]) {
            A[k] = E[i];
            i++;
        } else {
            A[k] = D[j];
            j++;
        }
        k++;
    }

    // --- Copiar o restante dos elementos de E[], se houver ---
    while (i < n1) {
        A[k] = E[i];
        i++;
        k++;
    }

    // --- Copiar o restante dos elementos de D[], se houver ---
    while (j < n2) {
        A[k] = D[j];
        j++;
        k++;
    }

    // Liberar a memória alocada para os vetores temporários
    free(E);
    free(D);
}

/**
 * Função principal do MergeSort que ordena A[esq..dir] usando o procedimento intercalar.
 */
void merge_sort(int A[], int esq, int dir) {
    if (esq < dir) {
        // Encontra o ponto do meio para evitar overflow para esq e dir grandes
        int meio = esq + (dir - esq) / 2;

        // Ordena a primeira e a segunda metade
        merge_sort(A, esq, meio);
        merge_sort(A, meio + 1, dir);

        // Intercala as duas metades ordenadas
        intercalar(A, esq, meio, dir);
    }
}

// Função auxiliar para imprimir o array
void imprimir_array(int A[], int tamanho) {
    for (int i = 0; i < tamanho; i++) {
        printf("%d ", A[i]);
    }
    printf("\n");
}

// Função main para testar o algoritmo
int main() {
    int array_exemplo[] = {12, 11, 13, 5, 6, 7, 2};
    int n = sizeof(array_exemplo) / sizeof(array_exemplo[0]);

    printf("Array original: \n");
    imprimir_array(array_exemplo, n);

    merge_sort(array_exemplo, 0, n - 1);

    printf("\nArray ordenado: \n");
    imprimir_array(array_exemplo, n);

    return 0;
}