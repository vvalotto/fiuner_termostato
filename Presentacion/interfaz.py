import tkinter as tk


principal = tk.Tk()
# width x height + x_offset + y_offset:
principal.geometry("600x300+0+0")


var_climatizador = tk.StringVar()
var_bateria = tk.StringVar()
var_temperatura = tk.StringVar()


# visualizacion climatizador
titulo_climatizador = tk.Label(principal,
                               text="Climatizador")
titulo_climatizador.place(x=0, y=0, width=300, height=75)

estado_climatizador = tk.Label(principal,
                               text="estado",
                               textvariable=var_climatizador,
                               fg='White', bg='Black')
estado_climatizador.place(x=0, y=75, width=300, height=75)


# visualizacion climatizador
titulo_bateria = tk.Label(principal,
                          text="Batería")
titulo_bateria.place(x=0, y=150, width=300, height=75)

nivel_bateria = tk.Label(principal,
                        text="nivel",
                        textvariable=var_bateria,
                        fg='White', bg='Blue')
nivel_bateria.place(x=0, y=225, width=300, height=75)

#visualizacion Temperatura
titulo_temperatura = tk.Label(principal, text="Temperatura")
titulo_temperatura.place(x=300, y=0, width=300, height=75)

valor_temperatura = tk.Label(principal, text="24", font=("Arial", 80),
                             fg="White", bg="Red")
valor_temperatura.place(x=350, y=50, width=200, height=200)

var_climatizador.set("Apagado")
var_bateria.set("Normal")


principal.mainloop()