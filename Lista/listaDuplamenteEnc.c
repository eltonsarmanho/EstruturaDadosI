#include <stdio.h>
#include <stdlib.h>

struct node {
   int chave;
   struct node *anterior;
   struct node *proximo;
};

struct node *head = NULL;//Nosso L.inicio ou L.head
struct node *tail = NULL;//Pode servir para alguma coisa - Mantem referencia no final da lista

/*
Nesse método fiz retorno da Posicao do elemento.
Entao tive que fazer pequena alteracao no codigo.
Porem eh a mesma abstracao do pseudocodigo
*/
int list_search(int k)
{
   struct node *x = head;//x = L.inicio
   int indice = 0;
   while(x != NULL) {
      if(x->chave == k)
        return indice;
      indice = indice + 1;
      x = x->proximo;
   }
   return -1;
}

void list_insert(int value) {
   //Criacao do Nodo
   struct node *x = (struct node*) malloc(sizeof(struct node));
   x->chave = value;
   x->anterior = NULL;
   x->proximo = NULL;

   if(head == NULL) {
      head = x;//L.inicio = x
      //tail = x;
   } else {
      x->proximo = head;
      if(head != NULL)
        head->anterior = x;
      head = x;
      x->anterior = NULL;
   }
}

//add final da lista
void append(int value) {
   struct node *new_node = (struct node*) malloc(sizeof(struct node));
   new_node->chave = value;
   new_node->anterior = NULL;
   new_node->proximo = NULL;
   if(head == NULL) {
      head = new_node;
      tail = new_node;
   } else {
      tail->proximo = new_node;
      new_node->anterior = tail;
      tail = new_node;
   }
}

void list_delete(int x)
{

   struct node *current = head;//x = L.inicio
   while(current != NULL) {
      if(current->chave == x)
      {
        if(current->anterior != NULL)
            current->anterior->proximo = current->proximo;
        else head = current->proximo;

        if (current->proximo != NULL)
            current->proximo->anterior = current->anterior;
      }//Fim do IF

    current = current->proximo;
   }//Fim do While
}



void print_list() {
   struct node *temp = head;
   while(temp != NULL) {
      printf("%d ", temp->chave);
      temp = temp->proximo;
   }
}

int main() {

   list_insert(1);
   list_insert(2);
   list_insert(3);
   list_insert(4);
   list_insert(5);
   list_delete(3);
   print_list();
   int resultado = list_search(4);
   printf("\nPosicao do elemento %d \n",resultado);

   return 0;
}

