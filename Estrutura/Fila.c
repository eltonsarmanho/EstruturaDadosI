#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 10

int queue[MAX_SIZE];
int inicio = 0;
int fim = -1;
int size = 0;//Tamanho

void enqueue(int value) {
    if (size == MAX_SIZE) {
        printf("Fila Cheia - Queue overflow!\n");
        return;
    }
    //fim = (fim + 1) % MAX_SIZE;
    fim = (fim + 1);

    queue[fim] = value;
    size++;
}

int dequeue() {
    /*if (size == 0) {
        printf("Fila vazia - Queue underflow!\n");
        return -1;
    }*/
    if (inicio > fim) {
        printf("Fila vazia - Queue underflow!\n");
        return -1;
    }
    int value = queue[inicio];
    //inicio = (inicio + 1) % MAX_SIZE;
    inicio = (inicio + 1);

    size--;
    return value;
}

int front()
{
    if(inicio>fim){
        printf("Fila vazia");
        return -1;}
    else
        return queue[inicio];

}

int main() {
    enqueue(1);
    enqueue(2);
    enqueue(3);
    enqueue(4);
    enqueue(5);

    int value = dequeue();
    printf("Valor Retirado: %d\n", value);

    return 0;
}