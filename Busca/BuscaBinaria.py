def binary_search(arr, x):
    """
    Realiza a busca binária em um array ordenado e retorna o índice do elemento encontrado ou -1 se não encontrado.
    """
    inicio = 0
    fim = len(arr) - 1

    while inicio <= fim:
        #meio = (inicio + fim) // 2
        meio = int((inicio + fim) / 2)

        if arr[meio] == x:
            return meio
        elif arr[meio] < x:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1
list = [1,2,3,4,5,6,7,8,9,10]
x = 8
result = binary_search(list,x)
if result != -1:
    print("Elemento encontrado no índice:", result)
else:
    print("Elemento não encontrado.")
