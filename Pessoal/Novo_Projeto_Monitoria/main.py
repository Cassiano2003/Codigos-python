import glob #Uma biblioteca que me ajuda a caregar todos os arquivos (*.xlsx)
import pandas as pd #Essa biblioteca me permite fazer a manipulaçao desses arquivos
from funcoes import (
    Pega_Informacoes, Busca_Aluno, Imprime_Alunos, gerar_arquivo_EAD, limpa_tela,
    Opcaes_Menu, Escolha_Arquivo,Coloca_Notas,Gera_lista_sem_duplicados)
from Objetos import Aluno

def Caso_0 (escolha_arquivos : list[int], arquivos : pd.DataFrame):#Criaçao da nova tabela de notas finais no arquivo
    if escolha_arquivos is not None:
        for num in escolha_arquivos:
            limpa_tela()
            print("Arquivo selecionado ",arquivos[num])
            print("------"*10)
            alunos = []
            arquivo = pd.read_excel(arquivos[num])

            #Gera a coluna final
            lista_temp = arquivo.columns.tolist()
            numero_colunas = len(lista_temp)
            if 'Nota Final' in arquivo.columns:
                print("A coluna Nota final ja existe.")
                numero_colunas = numero_colunas - 1
            else:
                arquivo.insert(numero_colunas,'Nota Final',0)

            #Gero o vetor da Classe Alunos
            informacoes_dis = Pega_Informacoes(arquivo)
            #ques = int(input("Quantas questoes tem: "))
            ques = numero_colunas - 8

            str_nota_modificada = lista_temp[8].replace("Q. 1 /","")
            nota_corte = float(str_nota_modificada.replace(",","."))
            print(nota_corte)
            qnt_para_10 = int(input("Quantas notas cheias para ir com 10: "))
            nota_total = True if qnt_para_10 == ques else False

            for chave, lista in informacoes_dis.items():
                aluno = Aluno(email[i],nome[i],sobre[i])
                aluno.set_quantos_exes_feitos(int(nota_atividade[i]/nota_corte))
                if not nota_total:
                    if aluno.quantos_exes_feitos >= qnt_para_10:
                        aluno.set_nota_final_atividade(10.0)
                    else:
                        aluno.set_nota_final_atividade((10/qnt_para_10)*aluno.quantos_exes_feitos)
                alunos.append(aluno)
            #Imprime_Alunos(alunos)
            ultimo = alunos.pop()
            alunos.sort(key=lambda x: (x.email, -x.nota_final_atividade))
            alunos_unicos = Gera_lista_sem_duplicados(alunos)
            alunos_unicos.append(ultimo)
            print("------"*10)
            Imprime_Alunos(alunos_unicos)


def Caso_1 (): #Criaçao do arquivo com a media das notas finais
    print("Funcionalidade em desenvolvimento...")   

def Caso_2 (alunos : list[Aluno],arquivos : pd.DataFrame): #Gerar arquivo com presenças EAD
    for i,arq in enumerate(arquivos):
        print(f"[ {i} ] - {arq}")
        nomes, sobre, email, avaliacoes = Pega_Informacoes(pd.read_excel(arq))
        if i == 0:
            for j in range(len(email)):
                alunos.append(Aluno(email[j], nomes[j], sobre[j]))
        else:
            for j in range(len(email)):
                idx = Busca_Aluno(email[j], nomes[j], sobre[j], alunos)
                if idx != -1:
                    alunos[idx].adicionar_atividade("X")
                else:
                    print(f"⚠️ Aluno não encontrado: {nomes[j]} {sobre[j]} ({email[j]}) no arquivo {arq}")
    print("------"*10)
    Imprime_Alunos(alunos)
    print("quantidade de alunos: ",len(alunos))
    gerar_arquivo_EAD(alunos)
    print("------"*10)

def menu():
    while True:
        limpa_tela() #Vai chamar a funçao que vai ficar limpando a tela
        alunos = []
        arquivos = glob.glob('*.xlsx') #Vai me retornar uma lista com todos os arquivos .xlsx
        arquivos.sort()
        qnt = Opcaes_Menu()
        escolha = int(input("Escolha qual sera a operação desejada: "))
        if escolha < 0 or escolha >= qnt:
            print("Opção inválida! Tente novamente.")
            break
        escolha_arquivos = Escolha_Arquivo(arquivos)
        match escolha:
            case 0:#Criaçao da nova tabela de notas finais no arquivo
                Caso_0(escolha_arquivos, arquivos)
            case 1:#Criaçao do arquivo com a media das notas finais
                print("Funcionalidade em desenvolvimento...")
            case 2:#Gerar arquivo com presenças EAD
                Caso_2(alunos, arquivos)
            case _:
                print("Opção inválida! Tente novamente.")
        input("Pressione Enter para continuar...")

if __name__ == "__main__":
    menu()
