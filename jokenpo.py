from random import randint
from time import sleep

opcoes = ['Pedra', 'Papel', 'Tesoura']
pc = randint(0,2)
print('''Opções de jogada :

[0] Pedra
[1] Papel
[2] Tesoura
''')

voce = int(input('Escolha uma das opção de jogada: '))

try:

  print('Jo')
  sleep(1)
  print('Ken')
  sleep(1)
  print('Pô')
  sleep(2)
  print('- ' * 15)
  print(f'PC escolheu: {opcoes[pc]}')
  print(f'Você escolheu: {opcoes[voce]}')
  print('- ' * 15)

except:

  print("Você deve escolher uma opção válida.")

if voce == pc:
    print("Empate!")
elif (voce == 1 and pc == 3) or \
    (voce == 2 and pc == 1) or \
    (voce == 3 and pc == 2):
    print("Você ganhou!")
else:
    print("Computador ganhou!")
