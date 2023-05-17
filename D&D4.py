import random
import time
import sys

def barra_de_carregamento(segundos):
    for i in range(1, 101):
        percentual = f'{i:3d}%'
        barra = '=' * (i // 2) + '>' + ' ' * ((100 - i) // 2)
        mensagem = f'\r[{percentual}] [{barra}]'
        sys.stdout.write(mensagem)
        sys.stdout.flush()
        time.sleep(segundos / 100)

    sys.stdout.write('\n')

barra_de_carregamento(10)
print('\n\n')
print('''
          .                                                      .
        .n                   .                 .                  n.
  .   .dP                  dP                   9b                 9b.    .
 4    qXb         .       dX                     Xb       .        dXp     t
dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb
9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
 9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
  `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
    `9XXXXXXXXXXXP' `9XX'   DIE    `98v8P'  HUMAN   `XXP' `9XXXXXXXXXXXP'
        ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                        )b.  .dbo.dP'`v'`9b.odb.  .dX(
                      ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
                     dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb
                    dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                    9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                     `'      9XXXXXX(   )XXXXXXP      `'
                              XXXX X.`v'.X XXXX
                              XP^X'`b   d'`X^XX
                              X. 9  `   '  P )X
                              `b  `       '  d'
                               `             '
''')
print('\n')
def roll_dice(sides):
    return random.randint(1, sides)

def display_battle_status(player_hp, dragon_hp):
    print(f"\nVocê tem {player_hp} pontos de vida restantes.")
    print(f"O dragão tem {dragon_hp} pontos de vida restantes.")

def player_attack(player_hp, dragon_hp):
    attack_roll = roll_dice(20)
    damage = roll_dice(6) + 2
    print(f"\nVocê rolou um {attack_roll} para atacar o dragão.")
    time.sleep(1)
    if attack_roll >= 10:
        print(f"Você acertou o dragão e causou {damage} pontos de dano!")
        dragon_hp -= damage
    else:
        print("Você errou o ataque!")

    return player_hp, dragon_hp

def dragon_attack(player_hp, dragon_hp):
    attack_roll = roll_dice(20)
    damage = roll_dice(8) + 3
    print(f"\nO dragão rolou um {attack_roll} para atacar você.")
    time.sleep(1)
    if attack_roll >= 12:
        print(f"O dragão acertou você e causou {damage} pontos de dano!")
        player_hp -= damage
    else:
        print("O dragão errou o ataque!")

    return player_hp, dragon_hp

print("Jogo da batalha do Dragão!")
print('\n')
print("Você está prestes a enfrentar um dragão. Faça suas escolhas com sabedoria!")

dragon_alive = True
player_hp = 20
dragon_hp = 50

while dragon_alive and player_hp > 0:
    print("\nUm dragão aparece diante de você!")
    display_battle_status(player_hp, dragon_hp)
    choice = input("\nO que você quer fazer? (1 - Atacar / 2 - Fugir) ")
    if choice == "1":
        player_hp, dragon_hp = player_attack(player_hp, dragon_hp)
        if dragon_hp <= 0:
            print("\nParabéns! Você matou o dragão!")
            dragon_alive = False
    elif choice == "2":
        print("\nVocê fugiu da batalha, mas o dragão ainda está vivo!")
        dragon_alive = False
    else:
        print("\nEscolha inválida, tente novamente.")

    if dragon_alive:
        player_hp, dragon_hp = dragon_attack(player_hp, dragon_hp)
        if player_hp <= 0:
            print("\nVocê foi derrotado pelo dragão. Fim do jogo.")
            dragon_alive = False

print("\nFim do jogo!")
