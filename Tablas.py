from graphviz import Digraph

from AnalizadorLexico import *


def reporteHtml():
    dot = Digraph(comment='Tabla HTML')

    tabla_html = '''<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0">'''
    tabla_html +='''<TR><TD>Reporte HTML de abarrotería 1</TD></TR>'''
    tabla_html +='''<TR>'''

    for pos in range(len(claves)):
        tabla_html += "<TD>"+str(claves[pos])+ "</TD>"

    tabla_html +='''</TR>'''
    tabla_html +='''</TABLE>>'''

    dot.node('tabla', label=tabla_html, shape='none')
    dot.render('tabla_tabular', view=True)

reporteHtml()