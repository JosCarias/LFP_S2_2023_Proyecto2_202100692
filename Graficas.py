from graphviz import Digraph
from AnalizadorLexico import *

def grafica():

    dot = Digraph(comment='Árbol Simple')

    dot.node("Claves", "Claves")

    for pos in range(len(listaClaves)):
        dot.node(listaClaves[pos], listaClaves[pos])

    for pos in range(len(listaClaves)):
        dot.edge("Claves", listaClaves[pos]) 

    dot.node("Registros", "Registros")

    numeroDeFilas=int(((len(listaRegistros))/(len(listaClaves))))

    for filas in range(numeroDeFilas):
        nodo=""
        for columna in range(len(listaClaves)):
            nodo+=(str(listaRegistros[(filas*len(listaClaves))+columna])+" ")
        dot.node(nodo,nodo)
        dot.edge("Registros",nodo)

    dot.node("imprimir", "imprimir")

    for pos in range(len(listaMensajes)):
        nodo=str(listaMensajes[pos])
        print(nodo)
        dot.node(nodo,nodo)
        dot.edge("imprimir",nodo)

    dot.node("imprimirln", "imprimirln")

    for pos in range(len(listaMensajes)):
        nodo=str(listaMensajesln[pos])
        print(nodo)
        dot.node(nodo,nodo)
        dot.edge("imprimirln",nodo)

        
    

    dot.node("Árbol de derivación", "Árbol de derivación")

    dot.edge("Árbol de derivación", "Claves")
    
    dot.edge("Árbol de derivación", "Registros")
    
    dot.edge("Árbol de derivación", "imprimir")

    dot.edge("Árbol de derivación", "imprimirln")
    
    dot.render('arbol', view=True)