import tkinter as tk
import math
import operator

calc = tk.Tk()
calc.title("Calculadora")
calc.geometry("520x580")
calc.config(bg="gray")

visor = tk.Entry(calc, bg="lightgray", width=500, font=("Arial", 24), justify="right")
visor.pack(side="top", padx=10, pady=10)

framebotoes = tk.Frame(calc, bg="darkgray", width=500, height=500)
framebotoes.pack(side="top", pady=15)

calculo = []

def calculos():
    stringcalculo = "".join(calculo)
    vetorcalculo = stringcalculo.split(" ")
    vetorcalculo = [x for x in vetorcalculo if x != ""]

    def continuarcalculo(vetorcalculo):
        
        if vetorcalculo[1] == "+" or vetorcalculo[1] == "-" or vetorcalculo[1] == "*" or vetorcalculo[1] == "/":
            oper = vetorcalculo[1]
            num1 = float(vetorcalculo[0])
            num2 = float(vetorcalculo[2])
            ops = {
                "+": operator.add,
                "-": operator.sub,
                "*": operator.mul,
                "/": operator.truediv
            }
            try:
                resultado = ops[oper](num1, num2)
                
                if 0 <= 3 < len(vetorcalculo):
                    print(vetorcalculo[3])
                    vetorcalculo = vetorcalculo[3:]
                    vetorcalculo.insert(0, resultado)
                    continuarcalculo(vetorcalculo=vetorcalculo)
                else:
                    visor.delete(0, tk.END)
                    visor.insert(0, resultado)

            except ValueError:
                print("erro")

        elif vetorcalculo[0] == "log":
            num1 = float(vetorcalculo[1])
            resultado = math.log10(num1)
            visor.delete(0, tk.END)
            visor.insert(0, resultado)

            if 0 <= 2 < len(vetorcalculo):
                print(vetorcalculo[2])
                vetorcalculo = vetorcalculo[2:]
                vetorcalculo.insert(0, resultado)
                continuarcalculo(vetorcalculo=vetorcalculo)
            else:
                visor.delete(0, tk.END)
                visor.insert(0, resultado)

        elif vetorcalculo[1] == "!":
            num1 = int(vetorcalculo[0])
            resultado = math.factorial(num1)
            visor.delete(0, tk.END)
            visor.insert(0, resultado)

            if 0 <= 2 < len(vetorcalculo):
                print(vetorcalculo[2])
                vetorcalculo = vetorcalculo[2:]
                vetorcalculo.insert(0, resultado)
                continuarcalculo(vetorcalculo=vetorcalculo)
            else:
                visor.delete(0, tk.END)
                visor.insert(0, resultado)

        elif vetorcalculo[0] == "√":
            num1 = float(vetorcalculo[1])
            resultado = math.sqrt(num1)
            visor.delete(0, tk.END)
            visor.insert(0, resultado)

            if 0 <= 2 < len(vetorcalculo):
                print(vetorcalculo[2])
                vetorcalculo = vetorcalculo[2:]
                vetorcalculo.insert(0, resultado)
                continuarcalculo(vetorcalculo=vetorcalculo)
            else:
                visor.delete(0, tk.END)
                visor.insert(0, resultado)

    continuarcalculo(vetorcalculo=vetorcalculo)

def bitao(botaop):
    global calculo
    caracteres = enumerate(calculo)
    if botaop == "=":
        if caracteres == 0:
            visor.delete(0, tk.END)
            visor.insert(0, "Coloque um cálculo!")
        else:
            calculos()
    
    elif botaop == "CE":
        if caracteres == 0:
            visor.delete(0, tk.END)
            visor.insert(0, "Coloque um cálculo!")
        else:
            calculo = []
    else:
        calculo.append(botaop)
        visor.delete(0, tk.END)
        visor.insert(0, "".join(calculo))

botoes = ["CE", " ! ", " √ ", " log ", "7", "8", "9", " / ", "5", "6", "7", " * ", "1", "2", "3", " - ", ".", "0", " + ", "="]

for i in range(4):
    framebotoes.columnconfigure(i, weight=1)
for i in range(5):
    framebotoes.rowconfigure(i, weight=1)

for i, botao in enumerate(botoes):
    linha = i // 4
    coluna = i % 4
    botao = tk.Button(framebotoes, text=botao, font=("Arial", 40), command=lambda b=botao: bitao(b))
    botao.grid(row=linha, column=coluna, sticky="nsew", padx=5, pady=5)



calc.mainloop()