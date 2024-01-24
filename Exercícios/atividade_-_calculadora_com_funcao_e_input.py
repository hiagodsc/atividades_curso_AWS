"""
Faça uma função calculadora que os números e as operações serão
feitas pelo usuário. O código deve ficar rodando infinitamente
até que o usuário escolha a opção de sair. No início, o 
programa mostrará a seguinte lista de operações:

1: Soma
2: Subtração
3: Multiplicação
4: Divisão
0: Sair

Digite o número para a operação correspondente e caso o usuário 
introduza qualquer outro, o sistema deve mostrar a mensagem 
“Essa opção não existe” e voltar ao menu de opções.

Após a seleção, o sistema deve pedir para o usuário inserir o 
primeiro e segundo valor, um de cada. Depois precisa executar 
a operação e mostrar o resultado na tela. Quando o usuário 
escolher a opção “Sair”, o sistema irá parar.

É necessário que o sistema mostre as opções sempre que finalizar 
uma operação e mostrar o resultado. 
"""
def calculadora():
     
    while True:
        try: 
            numero1 = float(input('Digite um número: '))
            numero2 = float(input('Digite outro número: '))
            print('[1] Soma | [2] Subtração | [3] Multiplicação | [4] Divisão | [0] Sair')
            operacao = int(input('Escolha uma opção: '))
            
            if operacao == 1:
                print(f'{numero1} + {numero2} = {numero1+numero2}')
                print('CALCULADORA')
                continue

            elif operacao == 2:
                print(f'{numero1} - {numero2} = {numero1-numero2}')
                print('CALCULADORA')

            elif operacao == 3:
                print(f'{numero1} x {numero2} = {numero1*numero2}')
                print('CALCULADORA')

            elif operacao == 4:
                print(f'{numero1} / {numero2} = {numero1/numero2}')
                print('CALCULADORA')

            elif operacao == 0:
                print('Finalizando a calculadora...')
                break
                
        except:
            print('Operação inválida!')
            print('CALCULADORA')

print('CALCULADORA')
calculadora()

