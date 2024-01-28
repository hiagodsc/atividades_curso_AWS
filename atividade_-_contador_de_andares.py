# ATIVIDADE FEITA COM 'for'
for i in range(20, 0, -1):
  if i == 13:
    print('Andar inexistente!')
    continue
  print(f'{i}º andar.')

print('=' * 17)
print('=' * 17)

# ATIVIDADE FEITA COM 'while'
contador = 20
while (contador > 0):
  if contador == 13:
    print('Andar inexistente!')
    contador -= 1
    continue
  print(f'{contador}º andar.')
  contador -= 1
