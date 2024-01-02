"""
Faça uma função calculadora de dois números com três parâmetros: 
os dois primeiros serão os números da operação e o terceiro será 
a entrada que definirá a operação a ser executada. Considera a 
seguinte definição:
1. Soma
2. Subtração
3. Multiplicação
4. Divisão

Caso seja inserido um número de operação que não exista, o 
resultado deverá ser 0.
"""

def calculadora(num1, num2, operacao):
    if operacao == '+':
        return f'{numero1} + {numero2} = {numero1+numero2}'
    elif operacao == '-':
        return f'{numero1} - {numero2} = {numero1-numero2}'
    elif operacao == 'x':
        return f'{numero1} x {numero2} = {numero1*numero2}'
    elif operacao == '/':
        return f'{numero1} / {numero2} = {numero1/numero2}'
    else:
        return '0'

numero1 = 5
numero2 = 5
operacao = 'f'
resultado = calculadora(numero1, numero2, operacao)
print(resultado)
