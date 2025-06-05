#include <stdio.h>
#include <stdlib.h>
#include<stdbool.h>
#define MAX_SIZE 10

int stack[MAX_SIZE];
int top = -1;

bool stack_empty()
{
    if(top == 0)
        return true;
    else return false;
}
void push(int x) {
    if (top == MAX_SIZE - 1) {
        printf("Pilha cheia - Stack overflow!\n");
        return;
    }
    top++;
    stack[top] = x;
}

int pop() {
    if (stack_empty()) {
        printf("Pilha vazia - Stack underflow!\n");
        return -1;
    }
    else
    {
        top--;
        return stack[top+1];
    }

}

int main() {
    push(1);
    push(2);
    push(3);
    push(4);
    push(5);

    int value = pop();
    printf("valor retirado da pilha: %d\n", value);

    return 0;
}

