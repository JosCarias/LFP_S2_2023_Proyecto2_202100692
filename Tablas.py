from graphviz import Digraph

def reporteHtml():
    dot = Digraph(comment='Tabla HTML')

    tabla_html = '''<
    <TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0">
        <TR>
            <TD>Reporte HTML de abarrotería 1</TD>
        </TR>
        <TR>
            <TD>codigo</TD>
            <TD>producto</TD>
            <TD>precio_compra</TD>
            <TD>precio_venta</TD>
            <TD>stock</TD>
        </TR>
        
        <TR>
            <TD>1</TD>
            <TD>2</TD>
            <TD>3</TD>
            <TD>4</TD>
            <TD>5</TD>
        </TR>
    </TABLE>
    >'''

    dot.node('tabla', label=tabla_html, shape='none')
    dot.render('tabla_tabular', view=True)

reporteHtml()