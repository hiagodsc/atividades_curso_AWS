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
