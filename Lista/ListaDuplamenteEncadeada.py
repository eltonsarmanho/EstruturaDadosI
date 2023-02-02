# Uma lista duplamente encadeada é uma variação da lista encadeada que tem referências tanto para o próximo
# elemento quanto para o elemento anterior. Em Python, você pode implementar uma lista duplamente encadeada
# criando uma classe que represente um nó e guarde referências tanto
# para o próximo quanto para o elemento anterior. Aqui está um exemplo básico de como isso pode ser feito:

class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = DoublyNode(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def print_list(self):
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