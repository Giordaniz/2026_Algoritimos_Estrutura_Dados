txt = "python"
print( txt[ 3:] )
print( txt[ 1 : 3:] )
print( txt[ :: -1] )
print( "th" in txt)
print( "ab" in txt)
txt_maiusculo = txt.upper()
print( txt_maiusculo.lower())
print( txt.upper() )
txt = "PyThOn"
print( txt.swapcase() )
txt = "algoritimo e estruturas"
print( txt.capitalize() )
print ( txt.title() )
txt = " python "
txt2 = "-" + txt.strip() + "-"  
print(txt2)
txt2 = "-" + txt.lstrip() + "-"
print(txt2)  
txt2 = "-" + txt.rstrip() + "-"  
print(txt2)
url = "http://senacrs.com.br"
print( url.removeprefix("http://") )
print( url.removesuffix(".com.br").removeprefix("http://") )

txt= "python"
print( txt.find( "ho" ) )
txt = "algoritmo"
print( txt.rfind("o") )
print( txt.find("o") )
print( txt.count("o") )
txt3 = "algotimo"
print( txt3.replace("ti" , "rit"))
print( txt )
print( txt.translate( str.maketrans( "o" , "0" ) ))
lista = "Jon;camila;talascado"
print( lista.split(";") )
separador = "-"
print( separador.join( ["kayanne" , "cauê gabriel cruz palmeiro" , "Niela"] ) )

print( txt.isalpha() )
txt += '123'
print( txt )
print( txt.isalpha() )
print( txt.isalnum() )
print( txt.isnumeric() )
txt = "Python"
print( "tudo minusculo: " , txt.islower() )
print( "tudo maiusculo:" , txt.isupper() )

txt = " "
print( txt.isspace())