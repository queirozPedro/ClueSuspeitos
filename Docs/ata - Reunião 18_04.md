## Exemplos de problema de teoria de jogos que foi resolvido com lógica: 

Muddy Children Faces: https://medium.com/maths-dover/muddy-children-puzzle-variation-personal-research-4909e85fcf34

Jogo de xadrez: https://repositorio.ufrn.br/jspui/bitstream/123456789/22563/1/AndreQuintilianoBezerraSilva_DISSERT.pdf

## Formatação das regras do jogo:
    + 4 jogadores;
    + 1o a acusar obriga os outros a acusarem

## IA:
    a) Construção de um banco de regras por jogador:
        + Cada jogador constrói sua visão de mundo baseado nas cartas iniciais;
        + Cada pergunta e cada resposta traz novas regras a todos os jogadores;
    b) Construção de jogadores coerentes: Jogadores que interagem corretamente com os outros mas não necessariamente com a melhor resposta para si.
    c) Permissão de um jogador humano.
    d) Propor um método de chute.

## Propostas matemáticas (conjecturas)
    a) O jogo tem **resolução**?
    
    b) Quantos movimentos o jogo possui? Mínimo e máximo.
    
    c) Quais as melhores cartas para início de jogo?
    
    d) Quais as piores cartas para início de jogo?
    
    e) Como gerar jogos a explorar as dificuldades do jogo. 
    Distribuição de cartas, elaboração do crime.****
    
    f) Quantas combinações tem a alternativa anterior?
    Crime: C(4,1) * C(5,1) * C(6,1) = 120
    C(12, 3) * C(9, 3) * C(6, 3) * C(3, 3) = 220*84*20*1
    120*220*84*20*1 = 44.352.000 de configurações iniciais de um jogo.