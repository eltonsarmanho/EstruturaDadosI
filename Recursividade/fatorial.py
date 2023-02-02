
def fatorial(n):
    if(n==0):
        return 1
    else:
        return n*fatorial(n-1);

if __name__ == '__main__':
    n= 4;
    print("Fatorial de {0} = {1}".format(n,fatorial(n)));

