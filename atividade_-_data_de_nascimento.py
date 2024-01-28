while True:
    try:
        nome = input('Qual o seu nome completo? ')
        ano_nascimento = int(input('Em que ano você nasceu? '))
        ano_atual = 2024
        if ano_nascimento >= 1922 and ano_nascimento <= 2023:
            idade = ano_atual - ano_nascimento
            print(f'Seu nome completo é: {nome}.')
            if idade == 1:
                print(f'Você irá completar {idade} ano em 2024.')
            else: 
                print(f'Você irá completar {idade} anos em 2024.')
        else:
            print('Ano de nascimento inválido!!')
    except:
        print('Caracter incorreto!')
            