import tkinter as tk

def digitar_0():
    visor.insert(tk.END, "0")

def digitar_1():
    visor.insert(tk.END, "1")

def digitar_2():
    visor.insert(tk.END, "2")

def digitar_3():
    visor.insert(tk.END, "3")

def digitar_4():
    visor.insert(tk.END, "4")

def digitar_5():
    visor.insert(tk.END, "5")

def digitar_6():
    visor.insert(tk.END, "6")

def digitar_7():
    visor.insert(tk.END, "7")

def digitar_8():
    visor.insert(tk.END, "8")

def digitar_9():
    visor.insert(tk.END, "9")

def digitar_ponto():
    visor.insert(tk.END, ".")

def limpar():
    visor.delete(0, tk.END)

def delete():
    if visor.get():
        visor.delete(len(visor.get()) - 1, tk.END)

def somar():
    visor.insert(tk.END, "+")

def subtrair():
    visor.insert(tk.END, "-")

def multiplicar():
    visor.insert(tk.END, "*")

def dividir():
    visor.insert(tk.END, "/")

def calcular():
    expressao = visor.get()

    if not expressao:
        return

    try:
        if not all(c in "0123456789.+-*/ " for c in expressao):
            raise ValueError()

        resultado = eval(expressao, {"__builtins__": {}}, {})
        limpar()
        visor.insert(tk.END, str(resultado))

    except Exception:
        limpar()
        visor.insert(tk.END, "Erro")


janela = tk.Tk()
janela.title("Teclado da calculadora")

visor = tk.Entry(janela, width=30, justify="right")
visor.grid(row=0, column=0, columnspan=4, padx=5, pady=5)


botao_0 = tk.Button(janela, text="0", width=6, command=digitar_0)
botao_0.grid(row=5, column=0, columnspan=2, sticky="we", padx=2, pady=2)

botao_1 = tk.Button(janela, text="1", width=6, command=digitar_1)
botao_1.grid(row=4, column=0, padx=2, pady=2)

botao_2 = tk.Button(janela, text="2", width=6, command=digitar_2)
botao_2.grid(row=4, column=1, padx=2, pady=2)

botao_3 = tk.Button(janela, text="3", width=6, command=digitar_3)
botao_3.grid(row=4, column=2, padx=2, pady=2)

botao_4 = tk.Button(janela, text="4", width=6, command=digitar_4)
botao_4.grid(row=3, column=0, padx=2, pady=2)

botao_5 = tk.Button(janela, text="5", width=6, command=digitar_5)
botao_5.grid(row=3, column=1, padx=2, pady=2)

botao_6 = tk.Button(janela, text="6", width=6, command=digitar_6)
botao_6.grid(row=3, column=2, padx=2, pady=2)

botao_7 = tk.Button(janela, text="7", width=6, command=digitar_7)
botao_7.grid(row=2, column=0, padx=2, pady=2)

botao_8 = tk.Button(janela, text="8", width=6, command=digitar_8)
botao_8.grid(row=2, column=1, padx=2, pady=2)

botao_9 = tk.Button(janela, text="9", width=6, command=digitar_9)
botao_9.grid(row=2, column=2, padx=2, pady=2)

botao_c = tk.Button(janela, text="C", width=6, command=limpar)
botao_c.grid(row=1, column=0, padx=2, pady=2)

botao_delete = tk.Button(janela, text="⌫", width=6, command=delete)
botao_delete.grid(row=1, column=1, padx=2, pady=2)

botao_dividir = tk.Button(janela, text="÷", width=6, command=dividir)
botao_dividir.grid(row=1, column=2, padx=2, pady=2)

botao_multiplicar = tk.Button(janela, text="x", width=6, command=multiplicar)
botao_multiplicar.grid(row=1, column=3, padx=2, pady=2)

botao_subtrair = tk.Button(janela, text="-", width=6, command=subtrair)
botao_subtrair.grid(row=2, column=3, padx=2, pady=2)

botao_somar = tk.Button(janela, text="+", width=6, command=somar)
botao_somar.grid(row=3, column=3, padx=2, pady=2)

botao_ponto = tk.Button(janela, text=".", width=6, command=digitar_ponto)
botao_ponto.grid(row=5, column=2, padx=2, pady=2)

botao_igual = tk.Button(janela, text="=", width=6, command=calcular)
botao_igual.grid(row=4, column=3, rowspan=2, sticky="ns", padx=2, pady=2)

janela.mainloop()