from collections import namedtuple 

Simbolo= namedtuple("Simbolo",["valor", "linea", "columna"])
linea=1
columna=1
simbolos=[]

def abrirEntrada(ruta):
    salida="Contenido completo:\n"
    with open(ruta, 'r') as archivo:
        contenido = archivo.read()
    
    salida+=(contenido)
    return salida

def leerPorSimbolo(ruta):
    global columna,linea
    salida="Analisis lexico:\n"
    with open(ruta, 'r') as archivo:
        for lineas in archivo:
            for caracter in lineas:
                if caracter.isspace():
                    columna=1                 
                else:
                    simbolo = Simbolo(caracter, linea, columna)
                    simbolos.append(simbolo)
                    columna += 1
            linea+=1 
            
    for simbolo in simbolos:
        salida+=(f"Fila {simbolo.linea}, Columna {simbolo.columna}, Token {simbolo.valor}\n")
    return salida

print(abrirEntrada("entrada1.txt"))
print(leerPorSimbolo("entrada1.txt"))
