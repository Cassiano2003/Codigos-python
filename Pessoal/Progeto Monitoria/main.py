from models import Aluno #Meu models.py q vai conter a classe Aluno
import glob #Uma biblioteca que me ajuda a caregar todos os arquivos (*.xlsx)
import pandas as pd #Essa biblioteca me permite fazer a manipulaçao desses arquivos 
#Como pegar os argumentos e criar novas tabelas
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
    Pega_Informacoes_chamada,
    gerar_arquivo_medias,
    limpa_tela
)#Aqui vai chamar as funçoes do meu ultis.py que vao me permetir fazer as manipulaçoes do arquivo


#Vai ter o objetivi de mostras as opçoes e oq podemos fazer com os arquivos
def menu(alunos:list[Aluno]):
    limpa_tela() #Vai chamar a funçao que vai ficar limpando a tela
    arquivos = glob.glob('*.xlsx') #Vai me retornar uma lista com todos os arquivos .xlsx
    #Eu cria listas de para facilitar a adiçao e modificaçao do meu menu
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
    #Um swit case para fazer as escolhas 
    match escolha:
        case 0:#Criaçao da nova tabela de notas finais no arquivo 
            #Lendo o arquivo
            for num in numros_escolhas:
                limpa_tela()
                print("Arquivo selecionado ",arquivos[num])
                print("------"*10)
                alunos = []
                arquivo = pd.read_excel(arquivos[num])

                #Gera a coluna final
                numero_colunas = len(arquivo.iloc[0])

                if 'Nota Final'in arquivo.columns:
                    print("A coluna Nota final ja existe.")
                    numero_colunas = numero_colunas - 1
                else:
                    arquivo.insert(numero_colunas,'Nota Final',0)

                #Gero o vetor da Classe Alunos
                email,nome,sobre,nota_final,nota_atividade = Pega_informacoes_atividades(arquivo=arquivo)
                #ques = int(input("Quantas questoes tem: "))
                ques = numero_colunas - 8
                print(ques)
                for i in range(len(arquivo)):
                    aluno = Aluno(email[i],nome[i],sobre[i])
                    aluno.set_nota_atividade(nota_atividade[i])
                    Adiciona_notas(i,arquivo,8+ques,aluno)
                    alunos.append(aluno)

                #Vai gerar as notas de cada aluno
                #nota_corte = float(input("Digite a nota de corte: "))
                str_nota = arquivo.iloc[0,8]
                str_nota_modificada = str_nota.replace("Q. 1 /","")
                nota_corte = float(str_nota_modificada.replace(",","."))
                print(nota_corte)
                qnt_para_10 = int(input("Quantas notas cheias para ir com 10: "))
                nota_baixa = True if qnt_para_10 == ques else False
                for aluno in alunos:
                    Calcula_Nota_Final(aluno,nota_corte,qnt_para_10,nota_baixa)

                alunos.pop(len(alunos)-1)
                #Coloca as notas de cada aluno na planilha
                arquivo = Coloca_Notas(alunos,arquivo)
                #Vai retornar os alunos que fizeram mais de um envio da atividade
                repetidos = Alunos_Repetidos(alunos)
                #Vai retornar uma lista com os alunos que tem as menores notas
                menores = Menores_Notas(repetidos,alunos)
                #Vai retirar os alunos com as menores notas 
                arquivo = arquivo.drop(menores)
                #Quando retiramos os alunos pode aver laculas esse comando vai arrumar isso
                arquivo = arquivo.reset_index(drop=True)
                #O arquivo vai ser salvo e assim teremos o arquivo ja modificado
                arquivo.to_excel(arquivos[num], index=False) # index=False para não incluir o índice do DataFrame no arquivo
        case 1:#Aqui vai fazer a geraçao do arquivo contendo a media final dos arquivos selecionados
            #OBS: Esse arquivo ja tem que ter passado pelo 0 pois ja tem que ter a coluna da Nota Final
            for num in numros_escolhas:
                #Vai em cada arquivo pegando as informaçoes
                arquivo = pd.read_excel(arquivos[num])
                email,nome,sobre,nota_final,nota_atividade = Pega_informacoes_atividades(arquivo=arquivo)
                #Se a lista esta vazia entao devemos criar ela com base na chamada, para nao termos alunos faltando
                if len(alunos) == 0:
                    print("Primeiro crie a lista de dados com a os nomes, sobrenome e emails dos alunos.")
                    break
                elif len(alunos) > 0:
                    for i,em in enumerate(email):#Vai andar em cada email
                        lugar = Busca_Aluno(em,alunos) #Pegar a posiçao do aluno no vetor apartir do email
                        nova_nota = float(str(nota_final[i]).replace(",", ".")) #Pega a Nota Final
                        if lugar != -1: #O aluno tem que existir
                            alunos[lugar].set_notas_para_media_final(nova_nota)#Adiciona a nota, no vetor de notas para a media final, para asssim poder calcular a media final
                        else:
                            print(f"Esse aluno nao existe: {em}")
            #Vai calcular a media final para todos os alunos 
            div = len(numros_escolhas)#Quantas notas sao no total
            for aluno in alunos:
                aluno.calcular_media(div)
            #Vai retirar o ultimo pois o ultimo é arquele media do arquivo e eu nao quero ele
            alunos.pop(len(alunos)-1)
            #Vai perguntar qual sera o nome do arquivo que vai conter as medias finais
            nome_arquivo = input("Digite o nome do arquivo: ")
            nome_arquivo = nome_arquivo+".xlsx"
            #E por fim chama a funçao para gerar o arquivo de medias finais de todos os alunos
            gerar_arquivo_medias(alunos,nome_arquivo)
        case 2:# É para fazer a criaçao da lista de alunos apartir da chamada
            aluno = []
            for num in numros_escolhas:
                #Percore todos os arquivos pegando as informaçoes 
                arquivo = pd.read_excel(arquivos[num])
                nome, sobre, email = Pega_Informacoes_chamada(arquivo)
                #Com as informaçoes apenas crio a lista de alunos
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


#Um loop para continuar chamando o menu e assim podendo fazer mais manipulaçoes nos arquivos
continua = type
alunos = []
while continua:
    continua,alunos = menu(alunos)