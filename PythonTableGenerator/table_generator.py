import numpy as np

'''
    Para representar as 15 cartas do jogo, serão usados os números de 1 a 15, 
    onde cada um representa, respectivamente:
    
    1 -| Castiçal
    2 -| Corda
    3 -| Faca
    4 -| Revólver

    5 -| Cozinha
    6 -| Hall
    7 -| Sala de Estar
    8 -| Sala de Jantar
    9 -| Spa

    10 -| Green
    11 -| Mustard
    12 -| Peacock
    13 -| Plum
    14 -| Scarlet
    15 -| White
'''

def gerar_crime():
    arma = np.random.randint(1, 5)
    lugar = np.random.randint(5, 10)
    suspeito = np.random.randint(10, 16)
    crime = np.array([arma, lugar, suspeito])
    return crime

def gerar_evidencias(crime):
    # Cria um array de números de 1 a 15
    pistas = np.arange(1, 16)
    
    # Vou remover os valores do crime do array de evidencias
    # A mascara vai ser um array que vai armazenar os elementos de pista que não estiverem em crime
    mascara = ~np.isin(pistas, crime)
    evidencias = pistas[mascara]
    return evidencias

def gerar_jogadores(evidencias):
    jogador0 = np.random.choice(evidencias, size=3, replace=False)
    evidencias = evidencias[~np.isin(evidencias, jogador0)]
    
    jogador1 = np.random.choice(evidencias, size=3, replace=False)
    evidencias = evidencias[~np.isin(evidencias, jogador1)]
    
    jogador2 = np.random.choice(evidencias, size=3, replace=False)
    evidencias = evidencias[~np.isin(evidencias, jogador2)]

    jogador3 = np.random.choice(evidencias, size=3, replace=False)
    evidencias = evidencias[~np.isin(evidencias, jogador3)]
    
    jogador0.sort()
    jogador1.sort()
    jogador2.sort()
    jogador3.sort()

    jogadores = np.array([jogador0, jogador1, jogador2, jogador3]) 
    
    return jogadores

def gerar_tabela(jogadores):
    tabela_jogador0 = np.arange(1, 16)
    mascara = np.isin(tabela_jogador0, jogadores[0])
    tabela_jogador0[mascara] = 1  
    tabela_jogador0[~mascara] = -1  

    tabela_jogador1 = np.arange(1, 16)
    mascara = np.isin(tabela_jogador1, jogadores[1])
    tabela_jogador1[mascara] = 1  
    tabela_jogador1[~mascara] = -1  

    tabela_jogador2 = np.arange(1, 16)
    mascara = np.isin(tabela_jogador2, jogadores[2])
    tabela_jogador2[mascara] = 1  
    tabela_jogador2[~mascara] = -1  
    
    tabela_jogador3 = np.arange(1, 16)
    mascara = np.isin(tabela_jogador3, jogadores[3])
    tabela_jogador3[mascara] = 1  
    tabela_jogador3[~mascara] = -1  
    
    tabela_geral = np.array([tabela_jogador0, tabela_jogador1, tabela_jogador2, tabela_jogador3])

    return tabela_geral

def imprimir_tabela(tabela_geral):
    tabela = ''
    for i in range(15):
        if i == 0:
            tabela += f'Castiçal({i+1})         | '
        elif i == 1:
            tabela += f'Corda({i+1})            | '
        elif i == 2:
            tabela += f'Faca({i+1})             | '
        elif i == 3:
            tabela += f'Revólver({i+1})         | '
        elif i == 4:
            tabela += f'Cozinha({i+1})          | '
        elif i == 5:
            tabela += f'Hall({i+1})             | '
        elif i == 6:
            tabela += f'Sala de Estar({i+1})    | '
        elif i == 7:
            tabela += f'Sala de Jantar({i+1})   | '
        elif i == 8:
            tabela += f'Spa({i+1})              | '
        elif i == 9:
            tabela += f'Green({i+1})           | '
        elif i == 10:
            tabela += f'Mustard({i+1})         | '
        elif i == 11:
            tabela += f'Peacock({i+1})         | '
        elif i == 12:
            tabela += f'Plum({i+1})            | '
        elif i == 13:
            tabela += f'Scarlet({i+1})         | '
        elif i == 14:
            tabela += f'White({i+1})           | '
        for j in range(4):
            if tabela_geral[j][i] == 1 or tabela_geral[j][i] == 0:
                tabela += ' '+ str(tabela_geral[j][i])+ " | "
            else:
                tabela += str(tabela_geral[j][i])+ " | "
                        
        tabela += '\n'
    print(tabela)

def corromper_tabela(tabela_geral, chance1, chance_menos1):
    for i in range(15):
        for j in range(1,4):
            if tabela_geral[j][i] == 1:
                if np.random.randint(0, 101) < chance1:
                    tabela_geral[j][i] = 0
            elif tabela_geral[j][i] == -1:
                if np.random.randint(0, 101) < chance_menos1:
                    tabela_geral[j][i] = 0
    return tabela_geral;


def main():   
    crime = gerar_crime()
    evidencias = gerar_evidencias(crime)
    jogadores = gerar_jogadores(evidencias)
    tabela_geral = gerar_tabela(jogadores)

    print("Crime:\t", crime, "\n")
    print("Jogadores:\n", jogadores, '\n')
    print('Tabela\n')
    imprimir_tabela(tabela_geral)

    tabela_corrompida = corromper_tabela(tabela_geral, 10, 10)
    print('Tabela Corrompida\n')
    imprimir_tabela(tabela_corrompida)

if __name__ == "__main__":
    main()