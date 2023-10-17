from collections import namedtuple 

Simbolo= namedtuple("Simbolo",["valor", "linea", "columna"])
linea=1
columna=1
simbolos=[]
listaRegistros=[]
listaClaves=[]
listaErrores=[]
listaMensajes=[]
listaMensajesln=[]


def abrirEntrada(ruta):
    salida="Contenido completo:\n"
    with open(ruta, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()
    
    salida+=(contenido)
    return salida

def leerPorSimbolo(ruta):
    global columna,linea
    salida="Analisis lexico:\n"
    with open(ruta, 'r', encoding='utf-8') as archivo:
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
    i = 0
    claves = False
    clave = ""
    palabraClave = ""
    sublista = ["C", "l", "a", "v", "e", "s"]  
    while i < len(simbolos):
        if all(simbolos[i + j].valor == sublista[j] for j in range(len(sublista))):
            palabraClave = "Claves"  
        if palabraClave == "Claves" and simbolos[i].valor == "[":
            claves = True
            palabraClave = ""            
        if claves==True:
            #caso 1 " "
            if simbolos[i].valor=='"' and simbolos[i+1].valor=='"':
                clave+=simbolos[i].valor
                listaErrores.append("falta una ,: "+ clave)
                clave=""
                i+=1
            #caso 2 clave,"
            if simbolos[i].valor!='"' and simbolos[i+1].valor==",":
                clave+=simbolos[i].valor
                listaErrores.append('''falta una " al final: '''+ clave)
                clave=""
                i+=2
            #caso 3 clave]
            if simbolos[i].valor!='"' and simbolos[i+1].valor=="]":
                clave+=simbolos[i].valor
                listaErrores.append('''falta una " al final: '''+ clave)
                clave=""
                break
            #caso 4 [clave
            if simbolos[i].valor=='[' and simbolos[i+1].valor!='"':
                error=""
                while simbolos[i].valor!='"':
                    error+=simbolos[i+1].valor                   
                    i+=1
                listaErrores.append('''falta una " al inicio: '''+error)           
                clave = ""
                i+=2
            #caso 5 ,clave
            if simbolos[i].valor==',' and simbolos[i+1].valor!='"':
                error=""
                while simbolos[i].valor!='"':
                    error+=simbolos[i+1].valor                   
                    i+=1
                listaErrores.append('''falta una " al inicio: '''+error)           
                i+=1
            #para eliminar [ de mas
            if simbolos[i].valor=='[' and simbolos[i+1].valor=='"':
                i+=1
            #mundo perfecto y su final
            if simbolos[i].valor==',':
                listaClaves.append(clave)
                clave=""
                i+=1
            if simbolos[i].valor==']':
                listaClaves.append(clave)
                clave=""
            clave += simbolos[i].valor         
        if palabraClave == "" and simbolos[i].valor == "]":
            claves = False        
        i+=1
    for pos in range(len(listaClaves)):
        print(listaClaves[pos])
    for pos in range(len(listaErrores)):
        print(listaErrores[pos])
        
    return listaClaves

def leerRegistros():
    i = 0
    registros = False
    registro = ""
    palabraregistro = ""
    sublista = ["r", "e", "g", "i", "s", "t", "r", "o", "s"]  
    while i < len(simbolos):
        if all(simbolos[i + j].valor == sublista[j] for j in range(len(sublista))):
            palabraregistro = "registros"  
        if palabraregistro == "registros" and simbolos[i].valor == "[":
            registros = True
            palabraregistro = "" 
        if registros==True:
            if simbolos[i].valor == '{':
                i+=1
            if simbolos[i].valor == '[':
                i+=2
            if simbolos[i].valor == '}' and simbolos[i+1].valor == '{':
                listaRegistros.append(registro)
                registro = ""
                i+=2 
            if simbolos[i].valor == '}' and simbolos[i+1].valor == ']':
                listaRegistros.append(registro)
                break 
            if simbolos[i].valor == ',':
                listaRegistros.append(registro)
                registro = "" 
            else:
                registro += simbolos[i].valor                
                  
        if palabraregistro == "" and simbolos[i].valor == "]":
            listaRegistros.append(registro[:-1])
            registros = False      
        i += 1  

    listaRegistros.pop(0)
    for elemento in range(len(listaRegistros)):
        print(str(elemento+1)+" "+listaRegistros[elemento])

    

    return listaRegistros

def leerImprimir():
    i = 0
    imprimir = False
    mensaje = ""
    palabraImprimir = ""
    sublista = ["i", "m", "p", "r", "i", "m", "i", "r","("]
    while i < len(simbolos):
        if all(simbolos[i + j].valor == sublista[j] for j in range(len(sublista))):
            palabraImprimir = "imprimir"
        if palabraImprimir == "imprimir" and simbolos[i].valor == "(":
            imprimir = True
            palabraImprimir = ""
        if imprimir == True:
            if simbolos[i].valor == '"':
                mensaje = ""
                i += 1
                while i < len(simbolos) and simbolos[i].valor != '"':
                    mensaje += simbolos[i].valor
                    i += 1
                if simbolos[i].valor == '"':
                    listaMensajes.append(mensaje)
        if palabraImprimir == "" and simbolos[i].valor == ")":
            imprimir = False

        i += 1
    mensaje=""
    for elemento in range(len(listaMensajes)):
        mensaje+=(listaMensajes[elemento])
    print(mensaje)

def leerImprimirln():
    i = 0
    imprimir = False
    mensaje = ""
    palabraImprimir = ""
    sublista = ["i", "m", "p", "r", "i", "m", "i", "r","l","n"]
    while i < len(simbolos):
        if all(simbolos[i + j].valor == sublista[j] for j in range(len(sublista))):
            palabraImprimir = "imprimirln"
        if palabraImprimir == "imprimirln" and simbolos[i].valor == "(":
            imprimir = True
            palabraImprimir = ""
        if imprimir == True:
            if simbolos[i].valor == '"':
                mensaje = ""
                i += 1
                while i < len(simbolos) and simbolos[i].valor != '"':
                    mensaje += simbolos[i].valor
                    i += 1
                if simbolos[i].valor == '"':
                    listaMensajesln.append(mensaje)
        if palabraImprimir == "" and simbolos[i].valor == ")":
            imprimir = False

        i += 1

    for elemento in range(len(listaMensajesln)):
        print(listaMensajesln[elemento])



print("--------------------------------")
(abrirEntrada("entrada1.txt"))
print("--------------------------------")
(leerPorSimbolo("entrada1.txt"))
#print("--------------------------------")
#(leerClaves())
#print("--------------------------------")
#(leerRegistros())
#print("--------------------------------")
#leerImprimir()
#print("--------------------------------")
#leerImprimirln()




