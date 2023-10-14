from collections import namedtuple 
import re

Simbolo= namedtuple("Simbolo",["valor", "linea", "columna"])
linea=1
columna=1
simbolos=[]
claves=[]
registros=[]
final=0


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

def leerClaves():
    global final
    j=0
    i=0
    clave=""
    while str(simbolos[i].valor)!="]":
        if str(simbolos[i].valor)=="[":
            j=i
        i+=1
    for pos in range(j+1,i):
        clave+=(simbolos[pos].valor)
    claves.extend(re.findall(r'"(.*?)"', clave))
    final=i
    return(claves)

def leerRegistros():
    global final
    final+=12
    registro=""
    print("-----------------------------")  
    for pos in range(final,len(simbolos)-1):
        registro+=simbolos[pos].valor
        if(str(simbolos[pos].valor)=="}"):
            registro+="\n"
    print(registro)
    return(registros)

  

print(abrirEntrada("entrada1.txt"))
leerPorSimbolo("entrada1.txt")
print(leerClaves())
print(leerRegistros())
