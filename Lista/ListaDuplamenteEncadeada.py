# Uma lista duplamente encadeada é uma variação da lista encadeada que tem referências tanto para o próximo
# elemento quanto para o elemento anterior. Em Python, você pode implementar uma lista duplamente encadeada
# criando uma classe que represente um nó e guarde referências tanto
# para o próximo quanto para o elemento anterior. Aqui está um exemplo básico de como isso pode ser feito:

class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None #proximo
        self.prev = None #anterior

class DoublyLinkedList:

    def __init__(self):
        self.head = None #L.inicio

    def append(self, data):
        """
        Add elemento no final da lista duplamente encadeada
        :rtype: object
        """
        new_node = DoublyNode(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def remove(self, key):
        current = self.head

        # Caso 1: Remoção do primeiro nó
        if current is not None and current.data == key:
            if current.next is not None:
                current.next.prev = None
            self.head = current.next
            current = None
            return

        # Caso 2: Remoção do último nó
        while current is not None and current.data != key:
            current = current.next

        if current is not None and current.next is None:
            current.prev.next = None
            current = None
            return

        # Caso 3: Remoção de um nó no meio da lista
        if current is not None:
            current.prev.next = current.next
            current.next.prev = current.prev
            current = None
            return
    def list_insert(self,data):
        x = DoublyNode(data);
        # Se lista vazia entao inserir no Inicio
        if self.head is None:
            self.head = x
            return;
        x.next = self.head;
        if self.head != None:
            self.head.prev = x;
        self.head = x
        x.prev = None

    def list_search(self,k):
        current = self.head; #x = L.inicio
        while current != None and current.data != k:
            current = current.next; #x = x.proximo
        return current;


    def print_list(self):
        """
        Printa a lista duplamente encadeada na tela.
        :rtype: object
        """
        current = self.head
        while current:
            print(current.data)
            current = current.next

if __name__ == '__main__':
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.append("A")
    doubly_linked_list.append("B")
    doubly_linked_list.append("C")
    doubly_linked_list.print_list()
    result = doubly_linked_list.list_search('B')
    print(result)
    doubly_linked_list.list_insert("Z");
    doubly_linked_list.list_insert("W");
    doubly_linked_list.print_list()

