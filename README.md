Calculadora científica em python com tkinter (interface gráfica)
A calculadora pega o cálculo por meio dos botões e coloca em um vetor, e exibe para o usuário
depois transforma esse vetor em uma string para depois transformar em outro vetor com o cálculo
Resumindo: # ["1", "0", " + ", "1", "0"]
           # "10 + 10"
           # ["10", "+", "10"]

Depois calcula de acordo com a ordem da esquerda para a direita:
           # ["1", "+", "10", "+", "1"]
           - 1 + 10 = 11, entao
           # ["11", "+", "1"]
           - e assim por diante

E após isso mostra para o usuário o resultado
