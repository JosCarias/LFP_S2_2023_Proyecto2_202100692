import tkinter as tk

def menuPrincipal():
    menu=tk.Tk()
    menu.title("Proyecto 2")
    menu.geometry("1280x720")
    menu.resizable(False, False)

    panel=tk.Frame(menu, bg="gray", height=50,width=1240)
    panel.grid(row=0,column=0,columnspan=5,padx=5, pady=5)

    txtProyecto=tk.Label(panel,text="Proyecto 2 - 202100692",bg="gray")
    txtProyecto.config(font=10)
    txtProyecto.grid(row=0,column=0, padx=5,pady=5)

    bntAbrir=tk.Button(panel, text="Abrir", height=2, width=20)
    bntAbrir.config(font=10)
    bntAbrir.grid(row=0,column=3,padx=5,pady=5)

    bntActualizar=tk.Button(panel, text="Actualizar", height=2, width=20)
    bntActualizar.config(font=10)
    bntActualizar.grid(row=0,column=4,padx=5,pady=5)

    menuDeslizable1 = tk.Menubutton(panel, text="Reportes", relief="raised", height=2, width=20)
    menuDeslizable1.configure(font=10)
    menuDeslizable1.grid(row=0,column=5, padx=5, pady=5)

    menu1 = tk.Menu(menuDeslizable1, tearoff=0)
    menuDeslizable1['menu'] = menu1

    menu1.add_command(label="Reporte de errores:",font=10)
    menu1.add_command(label="Reporte de tokens:",font=10)
    menu1.add_command(label="Árbol de derivación:",font=10)

    txbPantalla1 = tk.Text(menu,width=90, height=39)
    txbPantalla1.grid(column=0,row=2,columnspan=3,padx=5,pady=5)

    txbPantalla2 = tk.Text(menu,width=65, height=39)
    txbPantalla2.grid(column=3,row=2,columnspan=5, padx=5,pady=5)

    menu.mainloop()
