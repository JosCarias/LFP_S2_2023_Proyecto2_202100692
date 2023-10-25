from graphviz import Digraph

from AnalizadorLexico import listaClaves,listaRegistros, reporte


def reporteHtml():
    dot = Digraph(comment='Tabla HTML')

    tabla_html = '''<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0">'''
    tabla_html +='''<TR><TD>'''+reporte()+'''</TD></TR>'''
    
    tabla_html +='''<TR>'''
    for pos in range(len(listaClaves)):
        tabla_html += "<TD>"+str(listaClaves[pos])+ "</TD>"
    tabla_html +='''</TR>'''

    numeroDeFilas=int(((len(listaRegistros))/(len(listaClaves))))
    numeroDeColumnas=int((len(listaClaves)))

    for filas in range(numeroDeFilas):
        tabla_html +='''<TR>'''
        for columna in range(numeroDeColumnas):
            tabla_html += "<TD>"+str(listaRegistros[(filas*numeroDeColumnas)+columna])+ "</TD>"
        tabla_html +='''</TR>'''

    tabla_html +='''</TABLE>>'''

    dot.node('tabla', label=tabla_html, shape='none')
    dot.render('tabla_tabular', view=True)

