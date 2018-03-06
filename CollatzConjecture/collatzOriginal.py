
def collatzOriginal(n):
    print 'n = {}'.format(n)
    if n == 1 : return n
    if n % 2 == 0 : 
        n = n / 2
        return collatzOriginal(n)
    else :
        n = 3 * n + 1
        return collatzOriginal(n)

def collatzOrigWith4(n):
    print 'n = {}'.format(n)
    if n == 1 : return n
    if n % 2 == 0 : 
        n = n / 2
        return collatzOrigWith4(n)
    else :
        n = 3 * (n - 1) + 4
        return collatzOrigWith4(n)


def collatzTwoToX(n, x):
    print 'n = {}'.format(n)
    if n == 1 : return n
    if n % 2 == 0 : 
        n = n / 2
        return collatzTwoToX(n, x)
    else :
        n = (2**x - 1) * (n - 1) + 2**x
        return collatzTwoToX(n, x)

if __name__ == "__main__":
    print "collatzOriginal.py"
    
    n = long('9')
    print 'For n = {} the Collatz original result is {}'.format(n,collatzOriginal(n))

    n = long('9')
    print 'For n = {} the collatz with 4 result is {}'.format(n,collatzOrigWith4(n))

    n = long('9')
    x = 2
    print 'For n = {} the collatz 2 to the X (x={}) result is {}'.format(n,x,collatzTwoToX(n, 2))
    n = long('9')

    x = 2
    print 'For n = {} the collatz 2 to the X (x={}) result is {}'.format(n,x,collatzTwoToX(n, x))

    x = 3
    print 'For n = {} the collatz 2 to the X (x={}) result is {}'.format(n,x,collatzTwoToX(n, x))
    n = long('13')
# 7, 11, 15 all on same line

