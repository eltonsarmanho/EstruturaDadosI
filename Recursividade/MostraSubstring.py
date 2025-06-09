def showSubstringRecursiva(s,n):
    if n == 1:
        return s[0]
    else:
        return showSubstringRecursiva(s, n - 1) + "\n" +s[:n]
    
# Testando a função showSubstringRecursiva

print(showSubstringRecursiva("dog", len("dog")))  