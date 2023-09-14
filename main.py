# Projeto desenvolvido na disciplina de Tópicos em Projeto e Análise de Algoritmos orientada pelo professor Luiz Fernando Carvalho
# Desenvolvido por  Camila Beatriz da Silva             2103214
#                   Hevellyn Paz                        1593676
#                   Yuri Constantino Geteruck Podmowski 2103303


from dataclasses import dataclass
import pandas as pd
import numpy as np
import random
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

file = open('coordenadas.txt', 'r')

coordenadas_txt = file.readlines()

# Criação do vetor onde as coordenadas serão armazenadas
coordenadas = np.arange(400, dtype=float).reshape(100, 4)

for i in range(100):  # criando o ID de cada estrela, e zerando suas coordenadas
    coordenadas[i][0] = i
    coordenadas[i][1] = 0
    coordenadas[i][2] = 0
    coordenadas[i][3] = 0

contador_linhas = 0

for line in coordenadas_txt:  # For responsavel por correr todas as linhas do documento txt com as coordenadas

    aux = (['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'])
    contador = 0
    cont = 0
    for i in range(len(line)):  # For responsavel por percorrer todos os caracteres de cada linhas

        # Condição responsavel para  ir para a proxima coordenada ou proxima linha
        if line[i] != (" "):
            aux[i-cont] = line[i]
        else:
            cont = i+1
            contador += 1
        if contador == 1:
            x_temp = float(''.join(aux))
            coordenadas[contador_linhas][1] = x_temp
            aux = (['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'])
            contador += 1
        if contador == 3:
            y_temp = float(''.join(aux))
            coordenadas[contador_linhas][2] = y_temp
            aux = (['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'])
            contador += 1

        if contador == 5:
            z_temp = float(''.join(aux))
            coordenadas[contador_linhas][3] = z_temp
            aux = (['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'])
            contador += 1
    contador_linhas += 1


def randompath():  # Função que a partir do sol escolhe uma estrela aleatória para ir, e a partir da nova estrela repete o processo até as estrelas se esgotarem, e entao retorna ao sol.

    proximo = 0
    distancia = 0

    atual_coord = np.array([0, 0, 0], dtype=float)
    proximo_coord = np.array([0, 0, 0], dtype=float)

    posicao = np.arange(100)  # cria um vetor com os IDs das estrelas
    posicao = np.delete(posicao, 0)

    caminho = np.zeros(101, dtype=float)
    i = 0

    controle = True

    while controle:

        random.shuffle(posicao)  # embaralha o vetor com os IDs das estrelas
        proximo = posicao[0]  # escolhe a posicao 0 como a próxima estrela
        caminho[i+1] = proximo
        posicao = np.delete(posicao, 0)  # retira a estrela escolhida do vetor

        proximo_coord[0] = coordenadas[proximo][1]
        proximo_coord[1] = coordenadas[proximo][2]
        proximo_coord[2] = coordenadas[proximo][3]

        # calcula a distancia entre a estrela atual e a proxima
        distancia_temp = np.linalg.norm(atual_coord - proximo_coord)

        distancia += distancia_temp

        atual_coord[0] = proximo_coord[0]
        atual_coord[1] = proximo_coord[1]
        atual_coord[2] = proximo_coord[2]

        if len(posicao.tolist()) == 0:
            controle = False

        i += 1

    caminho = caminho.astype(int)
    print('Distancia Percorrida RandomPath = '+str(distancia))

    return caminho


def randompath_comportamento():  # Função que a partir do sol escolhe uma estrela aleatória para ir, e a partir da nova estrela repete o processo até as estrelas se esgotarem, e entao retorna ao sol.

    proximo = 0
    distancia = 0

    atual_coord = np.array([0, 0, 0], dtype=float)
    proximo_coord = np.array([0, 0, 0], dtype=float)

    posicao = np.arange(100)  # cria um vetor com os IDs das estrelas
    posicao = np.delete(posicao, 0)

    caminho = np.zeros(101, dtype=float)
    i = 0

    controle = True

    while controle:

        random.shuffle(posicao)  # embaralha o vetor com os IDs das estrelas
        proximo = posicao[0]  # escolhe a posicao 0 como a próxima estrela
        caminho[i+1] = proximo
        posicao = np.delete(posicao, 0)  # retira a estrela escolhida do vetor

        proximo_coord[0] = coordenadas[proximo][1]
        proximo_coord[1] = coordenadas[proximo][2]
        proximo_coord[2] = coordenadas[proximo][3]

        # calcula a distancia entre a estrela atual e a proxima
        distancia_temp = np.linalg.norm(atual_coord - proximo_coord)

        distancia += distancia_temp

        atual_coord[0] = proximo_coord[0]
        atual_coord[1] = proximo_coord[1]
        atual_coord[2] = proximo_coord[2]

        if len(posicao.tolist()) == 0:
            controle = False

        i += 1

    caminho = caminho.astype(int)

    return distancia


def inorderpath():  # gera um caminho com a ordem em que as coordenadas aparecem no txt

    proximo = 0
    distancia = 0
    caminho = np.zeros(101, dtype=int)

    atual_coord = np.array([0, 0, 0], dtype=float)
    proximo_coord = np.array([0, 0, 0], dtype=float)

    posicao = np.arange(100)
    posicao = np.delete(posicao, 0)

    controle = True

    distancias = np.arange(100, dtype=float)
    linha = 0

    while controle:

        proximo = posicao[0]
        caminho[linha+1] = posicao[0]
        posicao = np.delete(posicao, 0)

        proximo_coord[0] = coordenadas[proximo][1]
        proximo_coord[1] = coordenadas[proximo][2]
        proximo_coord[2] = coordenadas[proximo][3]

        distancia_temp = np.linalg.norm(atual_coord - proximo_coord)

        distancias[linha] = distancia_temp

        distancia += distancia_temp

        atual_coord[0] = proximo_coord[0]
        atual_coord[1] = proximo_coord[1]
        atual_coord[2] = proximo_coord[2]

        if len(posicao.tolist()) == 0:
            controle = False
            distancia_temp = np.linalg.norm(atual_coord - [0, 0, 0])
            distancias[linha+1] = distancia_temp
            distancia += distancia_temp
        linha += 1

    print('Distancia percorrida InOrder= ' + str(distancia))

    return caminho


def closestpath():  # algoritimo guloso, calcula todas as distancias a partir do sol, escolhe a estrela que possui a menor distancia da atual(sol no primeiro caso), vai para ela e entao repete o prcesso a partir dela

    coordenadas_aux = np.delete(coordenadas, 0, 0)  # coordenadas sem o sol

    atual_coord = np.array([0, 0, 0], dtype=float)
    proximo_coord = np.array([0, 0, 0], dtype=float)

    caminho = np.zeros(101, dtype=int)
    caminho_aux = 1

    distancia_percorrida = 0

    controle = True

    range_for = 99

    while controle:

        distancias = np.ones(100)
        distancias = distancias*1000000

        for i in range(range_for):  # gera as distancias a partir do ponto atual

            proximo_coord[0] = coordenadas_aux[i][1]
            proximo_coord[1] = coordenadas_aux[i][2]
            proximo_coord[2] = coordenadas_aux[i][3]

            distancias[i] = np.linalg.norm(atual_coord - proximo_coord)

        # print(distancias)
        # print('------------------------------------------------------------------------------- ' +
        #       str(np.where(distancias == np.min(distancias))[0][0]))

        distancia_percorrida += np.min(distancias)

        posisao_no_vetor = (np.where(distancias == np.min(distancias))[0][0])

        caminho[caminho_aux] = coordenadas_aux[posisao_no_vetor][0]
        caminho_aux += 1

        atual_coord[0] = coordenadas_aux[posisao_no_vetor][1]
        atual_coord[1] = coordenadas_aux[posisao_no_vetor][2]
        atual_coord[2] = coordenadas_aux[posisao_no_vetor][3]

        coordenadas_aux = np.delete(coordenadas_aux, posisao_no_vetor, 0)

        # print(atual_coord)
        # print(distancia_percorrida)
        # print(coordenadas[posisao_no_vetor][0])

        range_for = range_for-1

        # if (range_for == 95):
        #     controle = False

        if (coordenadas_aux.shape[0] == 0):
            controle = False

    distancia_percorrida += np.linalg.norm(atual_coord - [0, 0, 0])

    print('Distancia Percorrida ClosestPath = '+str(distancia_percorrida))

    print(caminho)

    return caminho


def farestpath():  # funcao em desenvolvimento que faz o contrario da closestpath, ao ives da mais proxima, escolhe a mais distante

    coordenadas_aux = np.delete(coordenadas, 0, 0)  # coordenadas sem o sol

    atual_coord = np.array([0, 0, 0], dtype=float)
    proximo_coord = np.array([0, 0, 0], dtype=float)

    caminho = np.zeros(101, dtype=int)
    caminho_aux = 1

    distancia_percorrida = 0

    controle = True

    range_for = 99

    while controle:

        distancias = np.ones(100)
        distancias = distancias*1000000

        for i in range(range_for):  # gera as distancias a partir do ponto atual

            proximo_coord[0] = coordenadas_aux[i][1]
            proximo_coord[1] = coordenadas_aux[i][2]
            proximo_coord[2] = coordenadas_aux[i][3]

            distancias[i] = np.linalg.norm(atual_coord - proximo_coord)

        distancia_percorrida += np.max(distancias)

        posisao_no_vetor = (np.where(distancias == np.max(distancias))[0][0])

        caminho[caminho_aux] = coordenadas_aux[posisao_no_vetor][0]
        caminho_aux += 1

        atual_coord[0] = coordenadas_aux[posisao_no_vetor][1]
        atual_coord[1] = coordenadas_aux[posisao_no_vetor][2]
        atual_coord[2] = coordenadas_aux[posisao_no_vetor][3]

        coordenadas_aux = np.delete(coordenadas_aux, posisao_no_vetor, 0)

        range_for = range_for-1

        if (coordenadas_aux.shape[0] == 0):
            controle = False

    distancia_percorrida += np.linalg.norm(atual_coord - [0, 0, 0])

    print('Distancia Percorrida FarestPath = '+str(distancia_percorrida))

    print(caminho)

    return caminho


# analisa o coomportamento da funcao randompath
def random_comportamento(tamanho):
    vetor = np.zeros(tamanho, dtype=float)
    for i in range(tamanho):
        vetor[i] = randompath_comportamento()

    plt.figure()
    plt.hist(vetor)
    plt.show()
    plt.figure()
    plt.plot(np.sort(vetor))
    plt.show()


# fucao que recebe um vetor com os IDs da ordem do caminho gerado e plota esse caminho em 3D
def plota_caminho(caminho):
    ax = plt.figure().add_subplot(projection='3d')


    coordenadas_plot = np.arange(300, dtype=float)
    coordenadas_plot = coordenadas_plot.reshape(100, 3)

    coordenadas_x = np.arange(101, dtype=float)
    coordenadas_y = np.arange(101, dtype=float)
    coordenadas_z = np.arange(101, dtype=float)

    for i in range(101):
        coordenadas_x[i] = coordenadas[caminho[i]][1]
        coordenadas_y[i] = coordenadas[caminho[i]][2]
        coordenadas_z[i] = coordenadas[caminho[i]][3]

    ax.scatter(coordenadas_x[1:100], coordenadas_y[1:100],
               coordenadas_z[1:100], c='blue', s=15)

    ax.plot(coordenadas_x, coordenadas_y, coordenadas_z, color='k')

    ax.scatter(0, 0, 0, c='orange', s=80)

    plt.show()


controle = True

while controle:

    print("----------Projeto Star Tour----------\n\n")
    print("O que voce deseja fazer?\n")
    print("1 - Gerar uma rota aleatória\n2 - Verificar o comportamento do caminho alatório com N caminhos\n3 - Gerar um caminho na ordem em que os dados aparecem no txt\n4 - Gerar o melhor caminho usando algoritimos gulosos\n5 - Sair")

    escolha = int(input())

    if ((escolha < 6) and (escolha > 0)):

        if escolha == 1:
            plota_caminho(randompath())

        elif escolha == 2:

            interacoes = int(input('Defina o numero de interações:'))
            random_comportamento(interacoes)
            print("Aguarde o processamento...")

        elif escolha == 3:
            plota_caminho(inorderpath())
        elif escolha == 4:
            plota_caminho(closestpath())
        elif escolha == 5:
            controle = False

    else:
        print("opção invalida")

