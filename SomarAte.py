def SomarAte(n):
    if n == 1:
        return 1
    else:
        return n + SomarAte(n - 1)

def Fatorial(n):
    if n == 1:
        return 1
    else:
        return n * Fatorial( n-1 )
    

print (SomarAte(5))
print (Fatorial(5))


