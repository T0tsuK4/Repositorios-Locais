# Jogo da batalha do Dragão

Este é um jogo de batalha onde você enfrenta um dragão e deve tomar decisões para tentar derrotá-lo. O jogo utiliza a biblioteca `random` para rolar dados e `time` para simular pausas no jogo.

## Como jogar

Para jogar, execute o código em seu interpretador Python. Na batalha, você terá que escolher entre atacar o dragão ou fugir. Para atacar, digite `1` quando for solicitado a escolher sua ação. Para fugir, digite `2`. Se o dragão morrer, você ganha o jogo. Se o seu personagem morrer, você perde o jogo.

## Como funciona

A função `barra_de_carregamento(segundos)` é utilizada para simular uma barra de carregamento na tela. Ela recebe como argumento o número de segundos que deve levar para a barra chegar a 100%.

A função `roll_dice(sides)` rola um dado com o número de lados especificado no argumento `sides` e retorna um número aleatório entre 1 e esse valor.

A função `display_battle_status(player_hp, dragon_hp)` exibe na tela os pontos de vida restantes do jogador e do dragão.

A função `player_attack(player_hp, dragon_hp)` simula o ataque do jogador e retorna os pontos de vida atualizados do jogador e do dragão.

A função `dragon_attack(player_hp, dragon_hp)` simula o ataque do dragão e retorna os pontos de vida atualizados do jogador e do dragão.

No início do jogo, são definidos os pontos de vida do jogador (`player_hp`) e do dragão (`dragon_hp`). Em um loop, o jogo apresenta o dragão ao jogador e pede para que ele escolha uma ação. Se o jogador escolhe atacar, é chamada a função `player_attack()`. Se o jogador escolhe fugir, o jogo termina. Se o dragão ainda está vivo, é chamada a função `dragon_attack()`. O loop continua até que o jogador ou o dragão morram.

No final do jogo, é exibida uma mensagem informando se o jogador ganhou ou perdeu o jogo.

## Requerimentos

Este jogo requer o interpretador Python e as bibliotecas `random` e `time`.