from sklearn.model_selection import GridSearchCV
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, confusion_matrix

from matplotlib_venn import venn3, venn3_circles
from matplotlib import pyplot as plt
from matplotlib_venn.layout.venn3 import DefaultLayoutAlgorithm

from scene import *
from save_to_file import *
from table import *


def gerar_dados(dados, chance):
    '''
    Função responsável por gerar a base de dados usada no treino.
    Recebe a quantidade de dados que devem ser gerados, a chance do
    número 1 ser corrompido e a chance do número -1 ser corrompido.
    Retorna X seguido de y para cada tipo de carta.
    '''
    # Os itens nomeados com X serão as tabelas com 0, 1 e -1 referentes aos jogadores.
    arma_X = []
    lugar_X = []
    suspeito_X = []
    # Os itens nomeados com y serão as respostas dos crimes.
    arma_y = []
    lugar_y = []
    suspeito_y = []

    # Base de dados
    for _ in range(dados):
        # Vou criar o crime e a tabela
        crime, tabela = criar_cenario(chance)
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

    return (arma_X, arma_y, lugar_X, lugar_y, suspeito_X, suspeito_y)


def definir_param_grid():
    '''
    Função que retorna os param_grid de arma, lugar e suspeito
    '''

    """
    Os param_grid são dicionários de diferentes combinações que 
    deseja testar no modelo.
    """
    param_grid_arma = {
        'hidden_layer_sizes': [(8, 4), (8,), (4,), (16, 8)],
        'activation': ['identity', 'relu'],
        'solver': ['adam', 'lbfgs'],
        'learning_rate': ['constant', 'adaptive'],
    }
    param_grid_lugar = {
        'hidden_layer_sizes': [(10, 5), (10,), (5,), (20, 10)],
        'activation': ['identity', 'relu'],
        'solver': ['adam', 'lbfgs'],
        'learning_rate': ['constant', 'adaptive'],
    }
    param_grid_suspeito = {
        'hidden_layer_sizes': [(12, 6), (12,), (6,), (24, 12)],
        'activation': ['identity', 'relu'],
        'solver': ['adam', 'lbfgs'],
        'learning_rate': ['constant', 'adaptive'],
    }
    return (param_grid_arma, param_grid_lugar, param_grid_suspeito)


def exibir_info_treino(name, item_X, item_y, grid_search_item):
    print(f"\n{name} Classification Report:")
    print(classification_report(item_y, grid_search_item.predict(item_X)))
    print("Confusion Matrix:")
    print(f"{confusion_matrix(item_y, grid_search_item.predict(item_X))}\n")


def print_resultados(dados, testes, chance, resultados):
    # Vou deixar aqui só para caso queira tirar a prova
    string = [
        f"\n\nCom um total de {dados} dados de jogos\n",
        f"Para um total de {testes} testes automáticos e aleatórios\n",
        f"Com chance de {chance[0]}% de Corromper o 1\n",
        f"Com chance de {chance[1]}% de Corromer o -1\n",
        f"Resultado\n",
        f"Acertou tudo: {resultados[0]} ou {(resultados[0]/testes)*100:.2f}%\n",
        f"Acertou apenas a Arma: {resultados[1]} ou {(resultados[1]/testes)*100:.2f}%\n",
        f"Acertou apenas o Lugar: {resultados[2]} ou {(resultados[2]/testes)*100:.2f}%\n",
        f"Acertou apenas o Suspeito: {resultados[3]} ou {(resultados[3]/testes)*100:.2f}%\n",
        f"Acertou apenas a Arma e Lugar: {resultados[4]} ou {(resultados[4]/testes)*100:.2f}%\n",
        f"Acertou apenas o Lugar e o Suspeito: {resultados[5]} ou {(resultados[5]/testes)*100:.2f}%\n",
        f"Acertou apenas o Suspeito e a Arma: {resultados[6]} ou {(resultados[6]/testes)*100:.2f}%\n",
        f"Errou tudo: {resultados[7]} ou {(resultados[7]/testes)*100:.2f}%\n"
    ]
    print("".join(string))


def gerar_diagrama_venn(dados, testes, chance, resultados):
    
    subsets = [
            round((resultados[1]/testes)*100, 2), 
            round((resultados[2]/testes)*100, 2), 
            round((resultados[4]/testes)*100, 2), 
            round((resultados[3]/testes)*100, 2),
            round((resultados[6]/testes)*100, 2), 
            round((resultados[5]/testes)*100, 2),
            round((resultados[0]/testes)*100, 2)
    ]

    venn3(subsets=subsets, 
        set_labels=("Arma", "Lugar", "Suspeito"),
        set_colors=("orange", "blue", "red"),
        layout_algorithm=DefaultLayoutAlgorithm(fixed_subset_sizes=(1,1,1,1,1,1,1)))
    
    venn3_circles(subsets=(subsets), layout_algorithm=DefaultLayoutAlgorithm(fixed_subset_sizes=(1,1,1,1,1,1,1)))
    
    plt.title(f"Resultado do treino (em %)")
    string = [
        f"Total de dados: {dados}\n",
        f"Total de testes: {testes}\n",
        f"Corrupção de 1 e -1: {chance[0]}%, {chance[1]}%",
    ]
    plt.text(-1, -0.8, "".join(string), fontsize=10)
    plt.text(0.5, -0.5, f"Erros: {round((resultados[7]/testes)*100, 2)}", fontsize=12)
    plt.savefig(f'{dados}_dados_e_{testes}_testes_{chance[0]}%_para_1_e_{chance[1]}%_para_-1')
    # plt.show()
    plt.clf()


def realizar_testes(testes, chance, grid_search_arma, grid_search_lugar, grid_search_suspeito):
    
    resultados = [0, 0, 0, 0, 0, 0, 0, 0]
    """
    resultados[0] os que acertaram tudo (acertos)
    resultados[1] os que acertaram apenas arma (acertos_arma)
    resultados[2] os que acertaram apenas lugar (acertos_lugar)
    resultados[3] os que acertaram apenas suspeito (acertos_suspeito)
    resultados[4] os que acertaram apenas arma e lugar (acertos_arma_lugar)
    resultados[5] os que acertaram apenas lugar e suspeito (acertos_lugar_suspeito)
    resultados[6] os que acertaram apenas suspeito e arma (acertos_suspeito_arma)
    resultados[7] os que erraram tudo (erros)
    """
    
    # Realiza os testes
    for _ in range(testes):
        crime, tabela = criar_cenario(chance)

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
                    resultados[0] += 1
                else:
                    resultados[4] += 1
            elif crime[2] == palpite_suspeito: # Arma e suspeito
                resultados[6] += 1
            else:
                resultados[1] += 1
        elif crime[1] == palpite_lugar: # Lugar
            if crime[2] == palpite_suspeito: # Lugar e suspeito
                resultados[5] += 1
            else:
                resultados[2] += 1
        elif crime[2] == palpite_suspeito: # Suspeito
            resultados[3] += 1
        else:
            resultados[7] += 1

    return (resultados)


def treinar(dados, testes, chance):

    # Definir os modelos
    clf_arma = MLPClassifier(max_iter=10000000)
    clf_lugar = MLPClassifier(max_iter=10000000)
    clf_suspeito = MLPClassifier(max_iter=10000000)

    # Definir os param_grid
    param_grid_arma, param_grid_lugar, param_grid_suspeito = definir_param_grid()
    
    # Configurar o grid_search
    grid_search_arma = GridSearchCV(estimator=clf_arma, param_grid=param_grid_arma, n_jobs=-1, cv=3)
    grid_search_lugar = GridSearchCV(estimator=clf_lugar, param_grid=param_grid_lugar, n_jobs=-1, cv=3)
    grid_search_suspeito = GridSearchCV(estimator=clf_suspeito, param_grid=param_grid_suspeito, n_jobs=-1, cv=3)

    # Gerar os Dados do treino
    arma_X, arma_y, lugar_X, lugar_y, suspeito_X, suspeito_y = gerar_dados(dados, chance)

    # Executar os Treinos
    grid_search_arma.fit(arma_X, arma_y)
    print("\nAjustou a Arma")
    grid_search_lugar.fit(lugar_X, lugar_y)
    print("Ajustou o Lugar")
    grid_search_suspeito.fit(suspeito_X, suspeito_y) 
    print("Ajustou o Suspeito\n")

    # Melhor combinação de hiperparâmetros
    print("Melhor combinação de parâmetros para Arma:", grid_search_arma.best_params_)
    print("Melhor combinação de parâmetros para Lugar:", grid_search_lugar.best_params_)
    print("Melhor combinação de parâmetros para Suspeito:", grid_search_suspeito.best_params_)

    # Exibir informações e matriz de confusão de cada treino
    # exibir_info_treino("Arma", arma_X, arma_y, grid_search_arma)
    # exibir_info_treino("Lugar", lugar_X, lugar_y, grid_search_lugar)
    # exibir_info_treino("Suspeito", suspeito_X, suspeito_y, grid_search_suspeito)

    # Faz os testes
    resultados = realizar_testes(testes, chance, grid_search_arma, grid_search_lugar, grid_search_suspeito)
    
    # Exibe o resultado no terminal
    print_resultados(dados, testes, chance, resultados)
    
    # Gera diagrama de Venn com base no resultado
    gerar_diagrama_venn(dados, testes, chance, resultados)


def treino_unitario():
    print(f"\n\nCaracteristicas do Treino")
    dados = int(input("Quantidade de Dados do Treinamento: "))
    testes = int(input("Quantidade de Testes: "))
    print(f"Informações adicionais")
    chance = [0, 0]
    chance[0] = int(input("Chance de Corromper o 1: "))
    chance[1] = int(input("Chance de Corromper o -1: "))
    treinar(dados, testes, chance)


def main(): 
    treino_unitario()

if __name__ == "__main__":
    main()