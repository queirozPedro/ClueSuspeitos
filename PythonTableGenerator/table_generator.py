import numpy as np

'''
    Geração de jogos em tabelas para estudo do Jogo Clue
    Para representar as 15 cartas do jogo, serão usados os números de 1 a 15, 
    onde cada um representa, respectivamente:
    
    1 -> Castiçal
    2 -> Corda
    3 -> Faca
    4 -> Revólver

    5 -> Cozinha
    6 -> Hall
    7 -> Sala de Estar
    8 -> Sala de Jantar
    9 -> Spa

    10 -> Green
    11 -> Mustard
    12 -> Peacock
    13 -> Plum
    14 -> Scarlet
    15 -> White
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
    
    tabela = np.array([tabela_jogador0, tabela_jogador1, tabela_jogador2, tabela_jogador3])

    return tabela

def gerar_string_tabela(tabela):
    string = ''
    for i in range(15):
        if i == 0:
            string += f'Castical({i+1})         | '
        elif i == 1:
            string += f'Corda({i+1})            | '
        elif i == 2:
            string += f'Faca({i+1})             | '
        elif i == 3:
            string += f'Revolver({i+1})         | '
        elif i == 4:
            string += f'Cozinha({i+1})          | '
        elif i == 5:
            string += f'Hall({i+1})             | '
        elif i == 6:
            string += f'Sala de Estar({i+1})    | '
        elif i == 7:
            string += f'Sala de Jantar({i+1})   | '
        elif i == 8:
            string += f'Spa({i+1})              | '
        elif i == 9:
            string += f'Green({i+1})           | '
        elif i == 10:
            string += f'Mustard({i+1})         | '
        elif i == 11:
            string += f'Peacock({i+1})         | '
        elif i == 12:
            string += f'Plum({i+1})            | '
        elif i == 13:
            string += f'Scarlet({i+1})         | '
        elif i == 14:
            string += f'White({i+1})           | '
        for j in range(4):
            if tabela[j][i] == 1 or tabela[j][i] == 0:
                string += ' '+ str(tabela[j][i])+ " | "
            else:
                string += str(tabela[j][i])+ " | "
                        
        string += '\n'
    return(string)

def corromper_tabela(tabela, chance1, chance_menos1):
    for i in range(15):
        for j in range(1,4):
            if tabela[j][i] == 1:
                if np.random.randint(0, 100) < chance1:
                    tabela[j][i] = 0
            elif tabela[j][i] == -1:
                if np.random.randint(0, 100) < chance_menos1:
                    tabela[j][i] = 0
    return tabela;

def gerar_tabelas_txt():
    
    print("Caracteristicas do Arquivo Txt")
    
    quant_tabelas = int(input("Quantidade de Tabelas: "))
    chance1 = int(input("Probabilidade de 1 ser corrompido(0 a 100): "))
    chance_menos1 = int(input("Probabilidade de -1 ser corrompido(0 a 100): "))
    nome_arquivo = f'{quant_tabelas}_jogos_com_{chance1}%_para_1_e_{chance_menos1}%_para_-1.txt'
    
    with open(nome_arquivo, 'w') as arquivo:
        for i in range(quant_tabelas):

            crime = gerar_crime()
            evidencias = gerar_evidencias(crime)
            jogadores = gerar_jogadores(evidencias)
            tabela = corromper_tabela(gerar_tabela(jogadores), chance1, chance_menos1)

            linhas = [
                f'Jogo {i+1} de {quant_tabelas}\n',
                f'{chance1}% de chance de corromper o 1\n',
                f'{chance_menos1}% de chance de corromper o -1\n\n',
                f'Crime: {crime}\n',
                f'Cartas dos Jogadores\n',
                f'  Jogador {0}: {jogadores[0]}\n',
                f'  Jogador {1}: {jogadores[1]}\n',
                f'  Jogador {2}: {jogadores[2]}\n',
                f'  Jogador {3}: {jogadores[3]}\n\n',
                f'Tabela Corrompida \n',
                gerar_string_tabela(tabela),
                '\n\n\n'
            ]

            arquivo.writelines(linhas)
    print("Arquivo Gerado com Sucesso")

def gerar_tabelas_tex():
    print("Caracteristicas do Arquivo LaTex")
    
    quant_tabelas = int(input("Quantidade de Tabelas: "))
    chance1 = int(input("Probabilidade de 1 ser corrompido(0 a 100): "))
    chance_menos1 = int(input("Probabilidade de -1 ser corrompido(0 a 100): "))
    nome_arquivo = f'{quant_tabelas}_jogos_com_{chance1}%_para_1_e_{chance_menos1}%_para_-1.tex'

    with open(nome_arquivo, 'w') as arquivo:
        
        texto = [
            r'\documentclass{article}',
            r'\usepackage{graphicx} % Required for inserting images',
            r'\usepackage[portuguese]{babel}',
            r'\usepackage[utf8]{inputenc}',
            r'\usepackage[T1]{fontenc}',
            r'\begin{document}'
        ]

        for n in range(quant_tabelas):
            crime = gerar_crime()
            evidencias = gerar_evidencias(crime)
            jogadores = gerar_jogadores(evidencias)
            tabela = corromper_tabela(gerar_tabela(jogadores), chance1, chance_menos1)

            cartas = [
                "01 - Castical", "02 - Corda", "03 - Faca", "04 - Revolver",
                "05 - Cozinha", "06 - Hall", "07 - Sala de Estar", "08 - Sala de Jantar",
                "09 - Spa", "10 - Green", "11 - Mustard", "12 - Peacock",
                "13 - Plum", "14 - Scarlet", "15 - White"
            ]

            texto.extend([
                r'\begin{table}[!htb]',
                r'\begin{tabular}{|l|l|l|l|l|}',
                r'\hline',
                r'Cartas & Jogador 0 & Jogador 1 & Jogador 2 & Jogador 3 \\ \hline'
            ])

            for i in range(15):
                linha = cartas[i]
                for j in range(4):
                    linha += f' & {tabela[j][i]}'
                linha += r' \\ \hline'
                texto.append(linha)

            texto.extend([
                r'\end{tabular}',
                r'\end{table}'
            ])

        texto.append(r'\end{document}')

        arquivo.writelines('\n'.join(texto))

def main(): 
    # gerar_tabelas_txt()  
    gerar_tabelas_tex()

if __name__ == "__main__":
    main()