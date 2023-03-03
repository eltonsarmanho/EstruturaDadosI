class Fila:
    def __init__(self, tamanho_maximo):
        self.tamanho_maximo = tamanho_maximo
        self.fila = []
        self.inicio = 0
        self.fim = -1

    def queue_empty(self):
        return self.fim < self.inicio

    def queue_isFull(self):
        return len(self.fila) == self.tamanho_maximo

    def enqueue(self, valor):
        if not self.queue_isFull():
            self.fim += 1
            self.fila.insert(self.fim,valor)
            #self.fila.append(valor)
    def dequeue(self):
        if not self.queue_empty():
            valor = self.fila[self.inicio]
            self.inicio += 1
            return valor
        else: print("Fila vazia")

    def print_front(self):
        if not self.queue_empty():
            #return self.fila[self.inicio]
            print(self.fila[self.inicio])
            print("\n");

    def print_queue(self):
        if not self.queue_empty():
             for indice in range(self.inicio,self.tamanho_maximo):
                print(self.fila[indice], end=" ")
             print("\n");
        else: print("[]")


if __name__ == '__main__':
    fila = Fila(5)
    fila.enqueue(1)
    fila.enqueue(2)
    fila.enqueue(3)
    fila.enqueue(4)
    fila.enqueue(5)
    fila.enqueue(10)

    fila.print_queue();
    fila.print_front()  # exibe o primeiro elemento da fila (1)

    fila.dequeue()
    fila.print_queue();
    fila.dequeue()
    fila.print_queue();
    fila.dequeue()
    fila.print_queue();
    fila.dequeue()
    fila.print_queue();
    fila.dequeue()
    fila.print_queue();
    fila.dequeue()
    fila.print_queue();
    fila.dequeue()
    fila.print_queue();


