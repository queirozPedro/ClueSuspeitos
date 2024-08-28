from sklearn.model_selection import GridSearchCV
from sklearn.neural_network import MLPClassifier
import numpy as np
from joblib import parallel_backend

from matplotlib_venn import venn3, venn3_circles
from matplotlib import pyplot as plt
from matplotlib_venn.layout.venn3 import DefaultLayoutAlgorithm

from Scene import *
from SaveToFile import *
from Table import *


def treinar(entradas, jogos_teste, chance1, chance_menos1):

    clf_arma = MLPClassifier(hidden_layer_sizes=(16, 8), activation='relu', solver='adam', alpha=0.0001, max_iter=1000000, random_state=1)
    clf_lugar = MLPClassifier(hidden_layer_sizes=(20, 10), activation='relu', solver='adam', alpha=0.0001, max_iter=1000000, random_state=1)
    clf_suspeito = MLPClassifier(hidden_layer_sizes=(24, 12), activation='relu', solver='adam', alpha=0.0001, max_iter=1000000, random_state=1)

    param_grid_arma = {
        'hidden_layer_sizes': (16, 8),  # [(50,50), (100,)]
        'activation': ['relu'],
        'solver': ['adam'],               #, 'sgd'],
    }
    param_grid_lugar = {
        'hidden_layer_sizes': (20, 10), # [(50,50), (100,)]
        'activation': ['relu'],           #,
        'solver': ['adam'],                   #['adam', 'sgd'],
    }
    param_grid_suspeito = {
        'hidden_layer_sizes': (24, 12), # [(50,50), (100,)]
        'activation': ['relu'],
        'solver': ['adam'],                   #['adam', 'sgd'],
    }
    
    grid_search_arma = GridSearchCV(estimator=clf_arma, param_grid=param_grid_arma, n_jobs=-1, cv=3)
    grid_search_lugar = GridSearchCV(estimator=clf_lugar, param_grid=param_grid_lugar, n_jobs=-1, cv=3)
    grid_search_suspeito = GridSearchCV(estimator=clf_suspeito, param_grid=param_grid_suspeito, n_jobs=-1, cv=3)

    # clf_arma = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(8, 4), random_state=1, max_iter=1000000)
    # clf_lugar = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(10, 5), random_state=1, max_iter=1000000)
    # clf_suspeito = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(12, 6), random_state=1, max_iter=1000000)

    # Os itens nomeados com X serão as tabelas com 0, 1 e -1 referentes aos jogadores.
    arma_X = []
    lugar_X = []
    suspeito_X = []
    # Os itens nomeados com y serão as respostas dos crimes.
    arma_y = []
    lugar_y = []
    suspeito_y = []

    # Base de dados
    for n in range(entradas):
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

    # # 'Cria' ou 'faz' os treinos
    # clf_arma.fit(arma_X, arma_y)
    # clf_lugar.fit(lugar_X, lugar_y)
    # clf_suspeito.fit(suspeito_X, suspeito_y)

    # 'Cria' ou 'faz' os treinos
    grid_search_arma.fit(arma_X, arma_y)
    grid_search_lugar.fit(lugar_X, lugar_y)
    grid_search_suspeito.fit(suspeito_X, suspeito_y)

    # Todas as possibilidades de acertos e erros
    acertos = 0
    acertos_arma = 0
    acertos_lugar = 0
    acertos_suspeito = 0
    erros_totais = 0
    acertos_arma_lugar = 0
    acertos_arma_suspeito = 0
    acertos_lugar_suspeito = 0

    for m in range(jogos_teste):
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

        palpite_arma = (grid_search_arma.predict([tabela_arma]))
        palpite_lugar = (grid_search_lugar.predict([tabela_lugar]))
        palpite_suspeito = (grid_search_suspeito.predict([tabela_suspeito]))

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

    # Vou deixar  aqui só para caso queira tirar a prova
    string = [
        f"\n\nCom um total de {entradas} entradas de jogos\n",
        f"Para um total de {jogos_teste} testes automáticos e aleatórios\n",
        f"Com chance de {chance1}% de Corromper o 1\n",
        f"Com chance de {chance_menos1}% de Corromer o -1\n",
        f"Resultado\n",
        f"Acertou tudo: {acertos} ou {(acertos/jogos_teste)*100:.2f}%\n",
        f"Acertou somente Arma e Lugar: {acertos_arma_lugar} ou {(acertos_arma_lugar/jogos_teste)*100:.2f}%\n",
        f"Acertou somente Arma e Suspeito: {acertos_arma_suspeito} ou {(acertos_arma_suspeito/jogos_teste)*100:.2f}%\n",
        f"Acertou somente Lugar e Suspeito: {acertos_lugar_suspeito} ou {(acertos_lugar_suspeito/jogos_teste)*100:.2f}%\n",
        f"Acertou apenas a Arma: {acertos_arma} ou {(acertos_arma/jogos_teste)*100:.2f}%\n",
        f"Acertou apenas o Lugar: {acertos_lugar} ou {(acertos_lugar/jogos_teste)*100:.2f}%\n",
        f"Acertou apenas o Suspeito: {acertos_suspeito} ou {(acertos_suspeito/jogos_teste)*100:.2f}%\n",
        f"Errou tudo: {erros_totais} ou {(erros_totais/jogos_teste)*100:.2f}%\n"
    ]
    print("".join(string))
    
    subsets = [
        round((acertos_arma/jogos_teste)*100, 2), 
            round((acertos_lugar/jogos_teste)*100, 2), 
            round((acertos_arma_lugar/jogos_teste)*100, 2), 
            round((acertos_suspeito/jogos_teste)*100, 2),
            round((acertos_arma_suspeito/jogos_teste)*100, 2), 
            round((acertos_lugar_suspeito/jogos_teste)*100, 2),
            round((acertos/jogos_teste)*100, 2)
    ]

    venn3(subsets=subsets, 
        set_labels=("Arma", "Lugar", "Suspeito"),
        set_colors=("orange", "blue", "red"),
        layout_algorithm=DefaultLayoutAlgorithm(fixed_subset_sizes=(1,1,1,1,1,1,1)))
    
    venn3_circles(subsets=(subsets), layout_algorithm=DefaultLayoutAlgorithm(fixed_subset_sizes=(1,1,1,1,1,1,1)))
    
    plt.title(f"Resultado do treino (em %)")
    string = [
        f"Total de entradas: {entradas}\n",
        f"Total de testes: {jogos_teste}\n",
        f"Corrupção de 1 e -1: {chance1}%, {chance_menos1}%",
    ]
    plt.text(-1, -0.8, "".join(string), fontsize=10)
    plt.text(0.5, -0.5, f"Erros: {round((erros_totais/jogos_teste)*100, 2)}", fontsize=12)
    plt.savefig(f'{entradas}_entradas_e_{jogos_teste}_testes_{chance1}%_para_1_e_{chance_menos1}%_para_-1')
    # plt.show()
    plt.clf()

def treino_unitario():
    print(f"\n\nCaracteristicas do Treino")
    entradas = int(input("Quantidade de Jogos para Treinamento: "))
    jogos_teste = int(input("Quantidade de Testes: "))
    print(f"Informações adicionais")
    chance1 = int(input("Chance de Corromper o 1: "))
    chance_menos1 = int(input("Chance de Corromper o -1: "))
    treinar(entradas, jogos_teste, chance1, chance_menos1)

def main(): 
    treino_unitario()


if __name__ == "__main__":
    main()