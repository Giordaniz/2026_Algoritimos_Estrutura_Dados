carro01 = {
    "Modelo" : "Doblo", "ano" : 2006
}

carro02 = {
    "Modelo" : "Renegade" , "ano" : 2021
}

carro03 = {
    "Modelo" : "Pulse", "ano" : 2024
}

carro03["placa"] : "676767"
#print( carro03 )

frota = carro01, carro02
carro01["Modelo"] = "Uno Mille"
#print( frota )
#frota[0] = carro03
#
def calcular(X, Y):
    return X+Y, X-Y, X*Y, X/Y     

result = calcular( 6, 7 )
#print ( result )
a, b, c, d = result
print( "Soma: ", a )
print( "Subtração: ", b )
print( "Multiplicação: ", c )
print( "Divisão: ", d )

print("----------------------------------")
def printarNome(X):
    print( "Nome: " , X )

def somarValores( Valores ):
    total = 0
    for N in Valores:
        total += N
        return total
    
numeros = ( (6,7) , [2,3,7] , [10,20,30,50] )
somas = map( somarValores , numeros )
print ( list(somas) )
nomes = "Jão" , "Marya" , "jon"
X = map( printarNome , nomes ) 
list( X )
