
class Nodo:
    def __init__(self, valor):
        self.chave = valor
        self.proximo = None #proximo
        self.anterior = None #anterior

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.inicio = None;

    def list_search(self,k):
        x = self.inicio;
        while x != None and x.chave != k:
            x = x.proximo;
        return x;

    def list_insert(self,data):
        x = Nodo(data);
        # Se lista vazia entao inserir no Inicio
        if self.inicio is None:
            self.inicio = x
            return;
        x.proximo = self.inicio;
        if self.inicio != None:
            self.inicio.anterior = x;
        self.inicio = x
        x.anterior = None

    def print_list(self):
        """
        Printa a lista duplamente encadeada na tela.
        :rtype: object
        """
        current = self.inicio
        while current:
            print(current.chave)
            current = current.proximo

    def list_delete(self,x):
        current = self.inicio;
        while current != None:
            if current.chave == x:
                if current.anterior is not None:
                    current.anterior.proximo = current.proximo
                else:
                    self.inicio = current.proximo
                if current.proximo is not None:
                    current.proximo.anterior = current.anterior
                return
            current = current.proximo;


        return x;


if __name__ == '__main__':
    lista = ListaDuplamenteEncadeada()
    lista.list_insert("A")
    lista.list_insert("B")
    lista.list_insert("C")
    lista.print_list()
    result = lista.list_search('B')
    print(result)
    lista.list_delete("A")
    lista.print_list()

