def EncontreMenor(Arranjo):
    if len(Arranjo) == 1:
        return Arranjo[0]
    else:
        menor = EncontreMenor(Arranjo[1:])
        if Arranjo[0] < menor:
            return Arranjo[0]
        else:
            return menor
# Testando a função EncontreMenor
print(EncontreMenor([5, 3, 8, 1, 4]))  # Deve retornar 1
print(EncontreMenor([10, 20, 5, 15]))  # Deve retornar 5
print(EncontreMenor([7, 2, 9, 3, 6]))  # Deve retornar 2