
def fib(n):
    #Caso base 1
    if(n==0):
        return 0;
    if(n==1):#Caso base 2
        return 1;
    return fib(n-1)+fib(n-2)
if __name__ == '__main__':
    print(fib(2))