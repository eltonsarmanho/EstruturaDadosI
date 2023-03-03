def binary_search(arr, x):
    """
    Realiza a busca binária em um array ordenado e retorna o índice do elemento encontrado ou -1 se não encontrado.
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        #mid = (left + right) // 2
        mid = int((left + right) / 2)

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return -1
list = [1,2,3,4,5,6,7,8,9,10]
x = 11
result = binary_search(list,x)
if result != -1:
    print("Elemento encontrado no índice:", result)
else:
    print("Elemento não encontrado.")
