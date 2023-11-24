from datetime import datetime, timedelta
import csv
import os
import random

nome_arquivo = 'dados.csv'
hoje = datetime.now()
inicio = hoje.strftime('%d/%m/%Y')

def criar_csv():
    if os.path.exists(nome_arquivo):
        pass
    else:
        with open('dados.csv', 'w', newline='') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(['Vicio ', ' Dificuldade', ' Inicio', ' Final'])

def ler_csv(arquivo):
    with open(arquivo, 'r') as file:
        reader = csv.reader(file)
        linhas = list(reader)
    return linhas

def traco():
    print('-'*30)

def erro():
    traco()
    print('Opção não encontrada!')
    traco()

def adicionar_meta(vicio, dificuldade, inicio, final):
    with open(nome_arquivo, 'a', newline='') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow([vicio, dificuldade, inicio, final])

def vizualizar_metas():
    linhas = ler_csv(nome_arquivo)
     
    if len(linhas) == 1:
        print('Não há dados no arquivo.')
    else:
        for linha in linhas:
            print(linha)

def dicas(resposta):
    respostas_prontas = {
        1: ["Tire um cochilo!", "Escute uma musica!", "Coma algo que goste muito!"],
        2: ["Faça carinho a um animal!", "Saia para caminhar no parque!", "Pratique algum esporte!"]
    }
   
    if resposta in respostas_prontas:
        return random.choice(respostas_prontas[resposta])
    else:
        return "Opção invalida, tente novamente."

criar_csv()

while True:
    try:
        menu = int(input(''' Menu -
    [1] adicionar meta
    [2] visualizar metas
    [3] consultar dicas para vício
    [4] finalizar programa\nSelecione a opção desejada: '''))
        print('')
        match menu:

            case 1:
                descricao = input("Insira o vicio que deseja combater: ").capitalize()
                while True:
                    try:
                        dias = int(input("Insira o período de tempo (em dias) que quer ficar sem esse vício: "))
                        break
                    except ValueError:
                        erro()
                dificuldade = input("Indique o quão dificil é essa meta (fácil, médio, difícil): ").capitalize()
                print('')
                final = hoje + timedelta(days=dias)
                final = final.strftime('%d/%m/%Y')
                adicionar_meta(descricao, dificuldade, inicio, final)
                print("Meta adicionada com sucesso.")

            case 2:
                vizualizar_metas()
            
            case 3:
                while True:
                    try:
                        print('Bem vindo ao menu de dicas: ')
                        print('')
                        menu_dicas = int(input('''Qual tipo de dica você quer? 
    [1] Dicas mais tranquilas
    [2] Dicas para me movimentar
    [3] Voltar para o menu principal\nSelecione a opção desejada: '''))
                        
                        if menu_dicas == 3:
                            print('Voltando para o menu principal.')
                            break

                        resposta = dicas(menu_dicas)
                        print("Dica:", resposta)
                        print('')

                    except ValueError:
                        erro()
            
            case 4:
                print('')
                print('Finalizando Programa...')
                break
            
            case _:
                traco()

    except ValueError:
        erro()