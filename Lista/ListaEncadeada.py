class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def list_search(self,k):
        current = self.head; #x = L.inicio
        while current != None and current.data != k:
            current = current.next; #x = x.proximo
        return current;

    def append(self, data):
        """
        Add elemento no final da lista simplesmente encadeada
        :rtype: object
        """
        new_node = Node(data)
        #Se lista vazia entao inserir no Inicio
        if self.head is None:
            self.head = new_node
            return;
        current = self.head #
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.append("A")
    linked_list.append("B")
    linked_list.append("C")
    linked_list.print_list()
    result = linked_list.list_search('Z')
    print(result)
