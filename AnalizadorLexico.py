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
    #for pos in range(len(listaClaves)):
    #    print(listaClaves[pos])
    #for pos in range(len(listaErrores)):
    #    print(listaErrores[pos])
        
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
    #for elemento in range(len(listaRegistros)):
    #    print(str(elemento)+" "+listaRegistros[elemento])

    

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

def leerConteo():
    i = 0
    conteo=""
    sublista = ["c","o","n","t","e","o"]
    while i < len(simbolos):
        if all(simbolos[i + j].valor == sublista[j] for j in range(len(sublista))):
            conteo = "conteo"
        if conteo == "conteo":
            print("Numero de registros: "+str(len(listaRegistros)))
            break
        i += 1  

def leerDatos():
    i = 0
    datos=""
    sublista = ["d","a","t","o","s"]
    tabla_html =""
    while i < len(simbolos):
        if all(simbolos[i + j].valor == sublista[j] for j in range(len(sublista))):
            datos = "datos"
        if datos == "datos":
            tabla_html +='|'
            for pos in range(len(listaClaves)):
                tabla_html += str(listaClaves[pos])+ "|"
            tabla_html +='\n'
            numeroDeFilas=int(((len(listaRegistros))/(len(listaClaves))))
            numeroDeColumnas=int((len(listaClaves)))

            for filas in range(numeroDeFilas):
                tabla_html +='|'
                for columna in range(numeroDeColumnas):
                    tabla_html += str(listaRegistros[(filas*numeroDeColumnas)+columna])+ "|"
                tabla_html +='\n'
            break
        i += 1  
    print(tabla_html)   

def Promedio(palabra):
    posicion=0
    promedio=0
    palabra=palabra
    while listaClaves[posicion]!=palabra:
        posicion+=1
    for pos in range(posicion,len(listaRegistros,), len(listaClaves)):
        primer_caracter = listaRegistros[pos][0]
        if listaRegistros[pos][0]==primer_caracter=='"':
            print("Esta columna es de tipo string: "+listaClaves[posicion])
            break
        promedio+=float((listaRegistros[pos]))
    numeroDeFilas=int(((len(listaRegistros))/(len(listaClaves))))
    print("El promedio de "+str(listaClaves[posicion])+" es: "+str(promedio/numeroDeFilas))

def leerPromedio():
    i = 0
    imprimir = False
    mensaje = ""
    palabraImprimir = ""
    sublista = ["p", "r", "o", "m", "e", "d", "i", "o"]
    while i < len(simbolos):
        if all(simbolos[i + j].valor == sublista[j] for j in range(len(sublista))):
            palabraImprimir = "promedio"
        if palabraImprimir == "promedio" and simbolos[i].valor == "(":
            imprimir = True
            palabraImprimir = ""
        if imprimir == True:
            if simbolos[i].valor != '(':
                mensaje+=simbolos[i].valor 
            if simbolos[i].valor == '"' and simbolos[i+1].valor == ')':
                imprimir = False
        if palabraImprimir == "" and simbolos[i].valor == ")":
            imprimir = False   
        i += 1

    Promedio(mensaje)
            
       
        
def contarSi(clave,valor):
    posicion=0
    existencia=0
    while listaClaves[posicion]!=clave:
        posicion+=1

    for pos in range(posicion,len(listaRegistros,), len(listaClaves)):
        primer_caracter = listaRegistros[pos][0]
        if listaRegistros[pos][0]==primer_caracter=='"':
            print("Esta columna es de tipo string: "+listaClaves[posicion])
            break
        if float(listaRegistros[pos])== valor:           
            existencia+=1  
    print("La registros que cumplen esta condicon son: "+str(existencia))

def leerContarSi():
    i = 0
    valor=""
    imprimir = False
    valor=""
    palabraImprimir = ""
    sublista = ["c", "o", "n", "t", "a","r", "s", "i"]
    while i < len(simbolos):
        if all(simbolos[i + j].valor == sublista[j] for j in range(len(sublista))):
            palabraImprimir = "contarSi"
        if palabraImprimir == "contarSi" and simbolos[i].valor == "(":
            imprimir = True
            palabraImprimir = ""
        if imprimir == True and palabraImprimir=="":
            if simbolos[i].valor == "(" and simbolos[i+1].valor == '"':
                i+=1
                while i < len(simbolos) and simbolos[i].valor != ",":
                    palabraImprimir += simbolos[i].valor
                    i+= 1
            if simbolos[i].valor == "," and valor=="":
                i+=1
                while i < len(simbolos) and simbolos[i].valor != ")":
                    valor += simbolos[i].valor
                    i+= 1           
        if palabraImprimir == "" and simbolos[i].valor == ")":
            imprimir = False
        i += 1
    contarSi(palabraImprimir,float(valor))

def sumar(palabra):
    posicion=0
    suma=0
    while listaClaves[posicion]!=palabra:
        posicion+=1
    for pos in range(posicion,len(listaRegistros,), len(listaClaves)):
        primer_caracter = listaRegistros[pos][0]
        if listaRegistros[pos][0]==primer_caracter=='"':
            print("Esta columna es de tipo string: "+listaClaves[posicion])
            break
        suma+=float((listaRegistros[pos]))
    print("El suma de "+str(listaClaves[posicion])+" es: "+str(suma))

def leerSuma():
    i = 0
    imprimir = False
    mensaje = ""
    palabraImprimir = ""
    sublista = ["s", "u", "m", "a"]
    while i < len(simbolos):
        if all(simbolos[i + j].valor == sublista[j] for j in range(len(sublista))):
            palabraImprimir = "suma"
        if palabraImprimir == "suma" and simbolos[i].valor == "(":
            imprimir = True
            palabraImprimir = ""
        if imprimir == True:
            if simbolos[i].valor != '(':
                mensaje+=simbolos[i].valor 
            if simbolos[i].valor == '"' and simbolos[i+1].valor == ')':
                imprimir = False
        if palabraImprimir == "" and simbolos[i].valor == ")":
            imprimir = False   
        i += 1

    sumar(mensaje)

def max(palabra):
    posicion=0
    max=0
    while listaClaves[posicion]!=palabra:
        posicion+=1
    for pos in range(posicion,len(listaRegistros,), len(listaClaves)):
        primer_caracter = listaRegistros[pos][0]
        if listaRegistros[pos][0]==primer_caracter=='"':
            print("Esta columna es de tipo string: "+listaClaves[posicion])
            break
        if float(listaRegistros[pos])> max:
            max=float(listaRegistros[pos])
    print("El valor max de "+str(listaClaves[posicion])+" es: "+str(max))

def leerMax():
    i = 0
    imprimir = False
    mensaje = ""
    palabraImprimir = ""
    sublista = ["m", "a", "x"]
    while i < len(simbolos):
        if all(simbolos[i + j].valor == sublista[j] for j in range(len(sublista))):
            palabraImprimir = "max"
        if palabraImprimir == "max" and simbolos[i].valor == "(":
            imprimir = True
            palabraImprimir = ""
        if imprimir == True:
            if simbolos[i].valor != '(':
                mensaje+=simbolos[i].valor 
            if simbolos[i].valor == '"' and simbolos[i+1].valor == ')':
                imprimir = False
        if palabraImprimir == "" and simbolos[i].valor == ")":
            imprimir = False   
        i += 1

    max(mensaje)

def min(palabra):
    posicion=0
    min=0
    while listaClaves[posicion]!=palabra:
        posicion+=1

    min=listaRegistros[posicion]
    for pos in range(posicion,len(listaRegistros,), len(listaClaves)):
        primer_caracter = listaRegistros[pos][0]
        if listaRegistros[pos][0]==primer_caracter=='"':
            print("Esta columna es de tipo string: "+listaClaves[posicion])
            break
        if float(listaRegistros[pos])< float(min):
            min=(listaRegistros[pos])
    print("El valor min de "+str(listaClaves[posicion])+" es: "+str(min))

def leerMin():
    i = 0
    imprimir = False
    mensaje = ""
    palabraImprimir = ""
    sublista = ["m", "i", "n"]
    while i < len(simbolos):
        if all(simbolos[i + j].valor == sublista[j] for j in range(len(sublista))):
            palabraImprimir = "max"
        if palabraImprimir == "max" and simbolos[i].valor == "(":
            imprimir = True
            palabraImprimir = ""
        if imprimir == True:
            if simbolos[i].valor != '(':
                mensaje+=simbolos[i].valor 
            if simbolos[i].valor == '"' and simbolos[i+1].valor == ')':
                imprimir = False
        if palabraImprimir == "" and simbolos[i].valor == ")":
            imprimir = False   
        i += 1

    min(mensaje)

def reporte():
    i = 0
    mensaje = ""
    palabraImprimir = ""
    sublista = ["e", "x", "p", "o", "r", "t", "a", "r", "R", "e", "p", "o", "r", "t", "e"]
    
    while i < len(simbolos):
        if all(simbolos[i + j].valor == sublista[j] for j in range(len(sublista))):
            palabraImprimir = "exportarReporte"
        if palabraImprimir == "exportarReporte" and simbolos[i].valor == "(":
            palabraImprimir = ""
            i += 1
            while i < len(simbolos) and simbolos[i].valor != '"':
                mensaje += simbolos[i].valor
                i += 1
            if mensaje:  
                mensaje = mensaje.strip(");") 

        i += 1
    return mensaje

def errores():
    salida=""
    for pos in range(len(listaErrores)):
        salida+=listaErrores[pos]+"\n"
    return salida

#print("--------------------------------")
#(abrirEntrada("entrada2.txt"))
#print("--------------------------------")
#(leerPorSimbolo("entrada2.txt"))
##print("--------------------------------")
#(leerClaves())
##print("--------------------------------")
#(leerRegistros())
#print("--------------------------------")
##leerImprimir()
#print("--------------------------------")
##leerImprimirln()
#print("--------------------------------")
##leerConteo()
#print("--------------------------------")
##leerDatos()
#print("--------------------------------")
##leerPromedio()
#print("--------------------------------")
##leerContarSi()
#print("--------------------------------")
##leerSuma()
#print("--------------------------------")
##leerMax()
#print("--------------------------------")
##leerMin()
#print("--------------------------------")
##reporte()
#print("--------------------------------")
#print(errores())







