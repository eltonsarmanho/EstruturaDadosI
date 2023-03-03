
def mdc(x,y):
    if y == 0:
        return x;
    return mdc(y,x%y);


print(mdc(12,18))