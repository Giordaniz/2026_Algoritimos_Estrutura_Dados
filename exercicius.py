# 1 potenciação
def potencia(n, p):
    if p == 0:
        return 1
    else: 
        return n * potencia(n, p -1)
    
print (potencia(2, 4))

#2 contagem regressiva
import time
def contagem( x ):
    time.sleep( 1 )
    if x == 0:
        print("fim")
    else:
        print( x )
        contagem( x - 1 )

contagem(10)

#3 inverter string
def inverString( s ):
    if len( s ) <= 1:
        return s
    return inverString( s[1:] ) + s[0]

print( inverString("Insano") )