def sequential_search(arr, x):
    """
    Realiza a busca sequencial em um array e retorna o índice do elemento encontrado ou -1 se não encontrado.
    """
    for i in range(len(arr)):
        if arr[i] == x:
            return i

    return -1

arr = [1, 3, 5, 7, 9]
x = 5

result = sequential_search(arr, x)
if result != -1:
    print("Elemento encontrado no índice:", result)
else:
    print("Elemento não encontrado.")
