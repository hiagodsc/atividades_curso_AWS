# ATIVIDADE FEITA COM 'while'
contador = 20
while (contador > 0):
  if contador == 13:
    print('Andar inexistente!')
    contador -= 1
    continue
  elif contador == 15:
    print('Andar inexistente!')
    contador -= 1
    continue

  print(f'{contador}º andar.')
  contador -= 1
