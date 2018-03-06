
def collatzTwoToX(n, x):
    if n == 1 : return n
    if n % 2 == 0 : 
        n = n / 2
        return n
    elif n % 3 == 0 :
        n = n / 3
        return n
    else :
        n = (2**x - 1) * (n - 1) + 2**x
        #n = 3 * (n - 1) + 2**x # this does NOT work, has cycles)
        return n

def processCollatz(n, x):
    print "processing n = {}, x = {}".format(n, x)
    counter = 0
    while n > 1:
        n = collatzTwoToX(n, x)
        counter += 1
        if counter < 100:
            print "step: {}, n = {}".format(counter, n)
        else:
            if counter % 1000 == 0: print ".",
            if counter > 100000: 
                print "counter limit reached, last n = {}".format(n)
                break

if __name__ == "__main__":
    print "collatzWithPattern.py"
    
    n = long('9')
    x = 2
    processCollatz(n, x)

    n = long('9')
    x=3
    processCollatz(n, x)

    n = long('17')
    x=3
    processCollatz(n, x)
    
    n = long('15')
    x=3
    processCollatz(n, x)
    
    n = long('17')
    x=4
    processCollatz(n, x)
    
    n = long('13')
    x=5
    processCollatz(n, x)