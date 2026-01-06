

def handshakes(n):
    #with formula == (n * (n-1))/2
    return (n * (n-1)) //2

def handshakes_without_formuala(n):
    res = 0
    for i in range(1, n):
        res = res + (n - i)

    return res


n = 4
print(handshakes_without_formuala(n))
