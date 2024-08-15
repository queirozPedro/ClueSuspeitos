from sklearn.neural_network import MLPClassifier
import numpy as np

'''
    Geração de jogos em tabelas para estudo do Jogo Clue Card
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
    '''
    Método que gera o crime.
    '''
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
    '''
    Vai receber um array com as evidencias e distribuir elas entre os jogadores
    Retorna uma matriz (array de array) de jogadorse 'jogadores[]' e suas cartas 'jogadores[][]'
    '''
    jogadores = []

    for i in range(4):
        jogador = np.random.choice(evidencias, size=3, replace=False)
        evidencias = evidencias[~np.isin(evidencias, jogador)]
        jogador.sort()
        jogadores.append(jogador)

    jogadores = np.array(jogadores)

    return jogadores


def gerar_tabela(jogadores):
    tabela_aux = []

    for i in range(4):
        tabela_jogador_np = np.arange(1, 16)
        mascara = np.isin(tabela_jogador_np, jogadores[i])
        tabela_jogador_np[mascara] = 1
        tabela_jogador_np[~mascara] = -1
        tabela_jogador = tabela_jogador_np.tolist()
        tabela_aux.append(tabela_jogador)

    tabela = np.array(tabela_aux)

    return tabela.tolist()

def gerar_string_tabela(tabela):

    cartas = [
        "01 - Castical       ", "02 - Corda          ", "03 - Faca           ", "04 - Revolver       ",
        "05 - Cozinha        ", "06 - Hall           ", "07 - Sala de Estar  ", "08 - Sala de Jantar ",
        "09 - Spa            ", "10 - Green          ", "11 - Mustard        ", "12 - Peacock        ",
        "13 - Plum           ", "14 - Scarlet        ", "15 - White          "
    ]

    string = ''

    for i in range(15):
        string += f'|{cartas[i] }|'
        for j in range(4):
            if tabela[j][i] == 1 or tabela[j][i] == 0:
                string += ' '+ str(tabela[j][i])+ " |"
            else:
                string += str(tabela[j][i])+ " |"
                        
        string += '\n'
    return(string)

def gerar_string_tabela_detalhada(tabela, chance1, chance_menos1, crime):

    cartas = [
        "01 - Castical       ", "02 - Corda          ", "03 - Faca           ", "04 - Revolver       ",
        "05 - Cozinha        ", "06 - Hall           ", "07 - Sala de Estar  ", "08 - Sala de Jantar ",
        "09 - Spa            ", "10 - Green          ", "11 - Mustard        ", "12 - Peacock        ",
        "13 - Plum           ", "14 - Scarlet        ", "15 - White          "
    ]

    string = f'\nCrime: {crime}\nChance de corromper o  1: {chance1}\nChance de corromper o -1: {chance_menos1}\n\n'

    for i in range(15):
        string += f'|{cartas[i] }|'
        for j in range(4):
            if tabela[j][i] == 1 or tabela[j][i] == 0:
                string += ' '+ str(tabela[j][i])+ " |"
            else:
                string += str(tabela[j][i])+ " |"
                        
        string += '\n'
    return(string)


def corromper_tabela(tabela, chance1, chance_menos1):
    '''
    Método que corrompe uma tabela. Recebe a tabela junto as chances de corromper o 
    número 1 e o -1. Retorna a tabela corrompida. 
    '''
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
    '''
    Método que gera as tabelas em txt
    '''
    
    print("Caracteristicas do Arquivo Txt")
    
    quant_tabelas = int(input("Quantidade de Tabelas: "))
    chance1 = int(input("Probabilidade de 1 ser corrompido(0 a 100): "))
    chance_menos1 = int(input("Probabilidade de -1 ser corrompido(0 a 100): "))
    nome_arquivo = f'{quant_tabelas}_jogos_com_{chance1}%_para_1_e_{chance_menos1}%_para_-1.txt'

    cartas = [
        "Castical(01)", "Corda(02)", "Faca(03)", "Revolver(04)",
        "Cozinha(05)", "Hall(06)", "Sala de Estar(07)", "Sala de Jantar(08)",
        "Spa(09)", "Green(10)", "Mustard(11)", "Peacock(12)",
        "Plum(13)", "Scarlet(14)", "White(15)"
    ]

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
                f'Crime: {cartas[crime[0]-1]}, {cartas[crime[1]-1]}, {cartas[crime[2]-1]}\n',
                f'Jogador 0: {cartas[jogadores[0][0]-1]}, {cartas[jogadores[0][1]-1]}, {cartas[jogadores[0][2]-1]}\n',
                f'Jogador 1: {cartas[jogadores[1][0]-1]}, {cartas[jogadores[1][1]-1]}, {cartas[jogadores[1][2]-1]}\n',
                f'Jogador 2: {cartas[jogadores[2][0]-1]}, {cartas[jogadores[2][1]-1]}, {cartas[jogadores[2][2]-1]}\n',
                f'Jogador 3: {cartas[jogadores[3][0]-1]}, {cartas[jogadores[3][1]-1]}, {cartas[jogadores[3][2]-1]}\n\n',
                f'Tabela Corrompida \n',
                gerar_string_tabela(tabela),
                '\n\n\n'
            ]

            arquivo.writelines(linhas)
    print("Arquivo Gerado com Sucesso")


def gerar_tabelas_tex():
    '''
    Método que gera as tabelas em LaTex
    '''
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
            r'\begin{document}',
            r'\title{Teste de Corrupcao de Dados}'
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

            linha = r'\section{Jogo '+ str(n+1)+ ' de ' + str(quant_tabelas) +'}'

            texto.append(linha)

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
                r'\end{table}',
                '\\ \\'
            ])

        texto.append(r'\end{document}')

        arquivo.writelines('\n'.join(texto))

def gerar_jogo_arquivo():
    crime = gerar_crime()
    evidencias = gerar_evidencias(crime)
    jogadores = gerar_jogadores(evidencias)
    tabela = gerar_tabela(jogadores)
    
    linhas = [
        f'Caracteristicas do Jogo'
        f'Crime: {crime}\n'
        f'Evidencias: {evidencias}\n'
        f'Jogadores:\n{jogadores}\n\n'
    ]

    tabela_arma = []
    for i in range(4):
        for j in range(4):
            tabela_arma.append(tabela[i][j])

    tabela_lugar = []
    for i in range(4):
        for j in range(4,9):
            tabela_lugar.append(tabela[i][j])

    tabela_suspeito = []
    for i in range(4):
        for j in range(9,15):
            tabela_suspeito.append(tabela[i][j])

    with open ('arquivo.txt', 'w') as arquivo:
        linhas.extend([
            f'Tabela\n{tabela}\nTamanho: {len(tabela)} por {len(tabela[0])}\n\n',
            f'Tabela Arma\n{tabela_arma}\nTamanho: {len(tabela_arma)}\n\n',
            f'Tabela Lugar\n{tabela_lugar}\nTamanho: {len(tabela_lugar)}\n\n',
            f'Tabela Suspeito\n{tabela_suspeito}\nTamanho: {len(tabela_suspeito)}\n\n'
        ])
        arquivo.writelines(linhas) 

def criar_cenario(chance1, chance_menos1):
    '''
    O método criar_cenario, cria o cenario do crime e retorna o array do crime e a tabela já corrompida.
    '''
    crime = gerar_crime()
    return crime, corromper_tabela(gerar_tabela(gerar_jogadores(gerar_evidencias(crime))), chance1, chance_menos1)

def treinar():
    print(f"\n\nCaracteristicas do Treino")
    quant_dados_jogos = int(input("Quantidade de Jogos para Treinamento: "))
    quant_palpites = int(input("Quantidade de Palpites Automáticos: "))
    print(f"Informações adicionais")
    chance1 = int(input("Chance de Corromper o 1: "))
    chance_menos1 = int(input("Chance de Corromper o -1: "))

    clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(16, 1), random_state=1)
    clf1 = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(20, 1), random_state=1)
    clf2 = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(24, 1), random_state=1)

    # Os itens nomeados com X serão as tabelas com 0, 1 e -1 referentes aos jogadores.
    arma_X = []
    lugar_X = []
    suspeito_X = []
    # Os itens nomeados com y serão as respostas dos crimes.
    arma_y = []
    lugar_y = []
    suspeito_y = []

    # Base de dados
    for n in range(quant_dados_jogos):
        # Vou criar o crime e a tabela
        crime, tabela = criar_cenario(chance1, chance_menos1)
        # Distribuir o crime em seu respectivos y
        arma_y.append(crime[0])
        lugar_y.append(crime[1])
        suspeito_y.append(crime[2])

        # Divide um array para cada tipo de carta
        # Um array com as informações de armas
        tabela_aux = []
        for i in range(4):
            for j in range(4):
                tabela_aux.append(tabela[i][j])
        arma_X.append(tabela_aux)
        # Um array com as informações de lugares
        tabela_aux = []
        for i in range(4):
            for j in range(4,9):
                tabela_aux.append(tabela[i][j])
        lugar_X.append(tabela_aux)
        # Um array com as informações de suspeitos
        tabela_aux = []
        for i in range(4):
            for j in range(9,15):
                tabela_aux.append(tabela[i][j])
        suspeito_X.append(tabela_aux)

    # 'Cria' ou 'faz' os treinos
    clf.fit(arma_X, arma_y)
    clf1.fit(lugar_X, lugar_y)
    clf2.fit(suspeito_X, suspeito_y)

    # Todas as possibilidades de acertos e erros
    acertos = 0
    acertos_arma = 0
    acertos_lugar = 0
    acertos_suspeito = 0
    erros_totais = 0
    acertos_arma_lugar = 0
    acertos_arma_suspeito = 0
    acertos_lugar_suspeito = 0

    for m in range(quant_palpites):
        crime, tabela = criar_cenario(chance1, chance_menos1)

        tabela_arma = []
        for i in range(4):
            for j in range(4):
                tabela_arma.append(tabela[i][j])

        tabela_lugar = []
        for i in range(4):
            for j in range(4,9):
                tabela_lugar.append(tabela[i][j])

        tabela_suspeito = []
        for i in range(4):
            for j in range(9,15):
                tabela_suspeito.append(tabela[i][j])

        palpite_arma = (clf.predict([tabela_arma]))
        palpite_lugar = (clf1.predict([tabela_lugar]))
        palpite_suspeito = (clf2.predict([tabela_suspeito]))

        if crime[0] == palpite_arma: # Arma
            if crime[1] == palpite_lugar: # Arma e Lugar
                if crime[2] == palpite_suspeito: # Arma, lugar e suspeito
                    acertos += 1
                else:
                    acertos_arma_lugar += 1
            elif crime[2] == palpite_suspeito: # Arma e suspeito
                acertos_arma_suspeito += 1
            else:
                acertos_arma += 1
        elif crime[1] == palpite_lugar: # Lugar
            if crime[2] == palpite_suspeito: # Lugar e suspeito
                acertos_lugar_suspeito += 1
            else:
                acertos_lugar += 1
        elif crime[2] == palpite_suspeito: # Suspeito
            acertos_suspeito += 1
        else:
            erros_totais += 1

    string = [
        f"\n\nPara um total de {quant_dados_jogos} jogos para treino\n",
        f"Para um total de {quant_palpites} palpites\n",
        f"Com chance de {chance1}% de Corromper o 1\n",
        f"Com chance de {chance_menos1}% de Corromer o -1\n",
        f"\nAconteceram\n",
        f"Acertou tudo: {acertos}\n",
        f"Acertou somente Arma e Lugar: {acertos_arma_lugar}\n",
        f"Acertou somente Arma e Suspeito: {acertos_arma_suspeito}\n",
        f"Acertou somente Lugar e Suspeito: {acertos_lugar_suspeito}\n",
        f"Acertou apenas de Arma: {acertos_arma}\n",
        f"Acertou apenas de Lugar: {acertos_lugar}\n",
        f"Acertou apenas de Suspeito: {acertos_suspeito}\n",
        f"Errou tudo: {erros_totais}\n"
    ]

    print("".join(string))
                

def main(): 
    treinar()
    # gerar_jogo_arquivo()


if __name__ == "__main__":
    main()