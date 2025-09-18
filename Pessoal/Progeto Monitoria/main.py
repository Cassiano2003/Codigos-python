import os
from models import Aluno
import glob
import pandas as pd
from utils import (
    Numeros_Validos,
    Adiciona_notas,
    Calcula_Nota_Final,
    Coloca_Notas,
    Alunos_Repetidos,
    Menores_Notas,
    Busca_Aluno,
    Imprime_Alunos,
    Pega_informacoes_atividades,
    Pega_informacoes_chamada,
    gerar_arquivo_medias
)

def menu(alunos):
    os.system("clear")
    arquivos = glob.glob('*.xlsx')
    opcoes = ["[ 0 ] Criar a colona com as Notas Finais","[ 1 ] Criar um arquivo que vai ter a media das Notas Finais",
              "[ 2 ] Criar um lista de alunos, para a manipulação","[ 3 ] Imprimir a lista de dados"]
    print("------"*10)
    for op in opcoes:
        print(op)
    print("------"*10)
    escolha = int(input("Escolha qual sera a operação desejada: "))
    print("------"*10)
    print("Selecione os arquivos que queiras manipular.")
    print("------"*10)
    numros_escolhas = Numeros_Validos(arquivos)
    print("------"*10)
    match escolha:
        case 0:
            #Lendo o arquivo
            for num in numros_escolhas:
                os.system("clear")
                print("Arquivo selecionado ",arquivos[num])
                print("------"*10)
                alunos = []
                arquivo = pd.read_excel(arquivos[num])

                #Gera a coluna final

                if 'Nota Final'in arquivo.columns:
                    print("A coluna Nota final ja existe.")
                else:
                    numero_colunas = len(arquivo.iloc[0])
                    arquivo.insert(numero_colunas,'Nota Final',0)

                #Gero o vetor da Classe Alunos

                email,nome,sobre,nota_final,nota_atividade = Pega_informacoes_atividades(arquivo=arquivo)
                ques = int(input("Quantas questoes tem: "))
                for i in range(len(arquivo)):
                    aluno = Aluno(email[i],nome[i],sobre[i])
                    aluno.Adiciona_Nota_Atividades(nota_atividade[i])
                    Adiciona_notas(i,arquivo,8+ques,aluno)
                    alunos.append(aluno)

                #Vai gerar as notas de cada aluno

                nota_corte = float(input("Digite a nota de corte: "))
                for aluno in alunos:
                    Calcula_Nota_Final(aluno,nota_corte)

                alunos.pop(len(alunos)-1)
                #Coloca as notas de cada aluno na planilha
                
                arquivo = Coloca_Notas(alunos,arquivo)
                repetidos = Alunos_Repetidos(alunos)
                menores = Menores_Notas(repetidos,alunos)
                arquivo = arquivo.drop(menores)
                arquivo = arquivo.reset_index(drop=True)
                #Imprime_Alunos(alunos)
                arquivo.to_excel(arquivos[num], index=False) # index=False para não incluir o índice do DataFrame no arquivo
        case 1:
            for num in numros_escolhas:
                arquivo = pd.read_excel(arquivos[num])
                email,nome,sobre,nota_final,nota_atividade = Pega_informacoes_atividades(arquivo=arquivo)
                if len(alunos) == 0:
                    print("Primeiro crie a lista de dados com a os nomes, sobrenome e emails dos alunos.")
                    break
                elif len(alunos) > 0:
                    for i,em in enumerate(email):
                        lugar = Busca_Aluno(em,alunos)
                        nova_nota = float(str(nota_final[i]).replace(",", "."))
                        if lugar != -1:
                            alunos[lugar].Adiciona_Notas_Final(nova_nota)
            for aluno in alunos:
                aluno.Calcula_Media(len(numros_escolhas))
            alunos.pop(len(alunos)-1)
            nome_arquivo = input("Digite o nome do arquivo: ")
            nome_arquivo = nome_arquivo+".xlsx"
            gerar_arquivo_medias(alunos,nome_arquivo)
        case 2:
            for num in numros_escolhas:
                arquivo = pd.read_excel(arquivos[num])
                nome, sobre, email = Pega_informacoes_chamada(arquivo)
                if len(alunos) == 0:
                    em_tam, nm_tam, sb_tam = len(email),len(nome),len(sobre)
                    if(em_tam == nm_tam == sb_tam):
                        for i in range(em_tam):
                            aluno = Aluno(email[i],nome[i],sobre[i])
                            alunos.append(aluno)
                else:
                    print("A lista de dados já existe!!!")
        case 3:
            Imprime_Alunos(alunos)
        case _:
            print("Não tem essa operação\nPrograma finalizado!!!")
            return False,alunos
    print("------"*10)
    input("Precione entter para continuar")
    return True,alunos


continua = type
alunos = []
while continua:
    continua,alunos = menu(alunos)