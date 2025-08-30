import pandas as pd
import glob
import os

def Colocar_Nota_10_para_4(arquivo):
    valor = (arquivo['Avaliar/10,0'])
    arquivo['Nota Final'] = arquivo['Nota Final'].astype(str)
    for i,n in enumerate(valor):
        novos_valores = (n.replace(',','.'))
        if len(valor)-1 > i:
            if float(novos_valores) >= 4.3:
                arquivo.loc[i,'Nota Final'] = '10,0'
            else:
                arquivo.loc[i,'Nota Final'] = arquivo.loc[i,'Avaliar/10,0']
        else:
            arquivo.loc[i,'Nota Final'] = ''
    return arquivo

def Cria_nome_e_sobre(arquivo):
    nomes = arquivo['Nome']
    sobre_nome = arquivo['Sobrenome']
    nome_sobre = []
    for i, nome in enumerate(nomes):
        if len(sobre_nome)-1 > i:
            nome_sobre.append(nome+' '+sobre_nome[i])
    return nome_sobre

def Verifica_nomes_repetidos(nomes_completos):
    contagem = {}
    repetidos = []
    for nome in nomes_completos:
        if nome in contagem:
            contagem[nome] += 1
        else:
            contagem[nome] = 1
    for nome, cont in contagem.items():
        if cont > 1:
            repetidos.append(nome)
    return repetidos

def Acha_posicao_nome(repetidos,nome_completo):
    dicio = {}
    for nome_in in repetidos:
        lis = []
        for i,nome_sb in enumerate(nome_completo):
            if nome_in == nome_sb:
                lis.append(i)
        dicio[nome_in] = lis
    return dicio

def Valores_que_devem_ser_removidos(arquivo,repetidos,dicionario):
    menores_l = []
    for nome in repetidos:
        maior_l = -1
        maior = -1
        for n,i in enumerate(dicionario[nome]):
            print("Qual é: ",n)
            print(arquivo.iloc[i])
            num = float(arquivo.loc[i, 'Avaliar/10,0'].replace(',','.'))
            print("Meu numero é: ",num)
            if num > maior:
                print("Maior antes: ",maior)
                maior = num
                print("Maior depois: ",maior)
                if maior_l != -1:
                    menores_l.append(maior_l)    
                maior_l = i
            else:
                menores_l.append(i)
    return menores_l


def Retira_Mais_Um_Envio(arquivo):
    nome_sobre = Cria_nome_e_sobre(arquivo=arquivo)
    repetidos = Verifica_nomes_repetidos(nomes_completos=nome_sobre)
    dicio = Acha_posicao_nome(repetidos=repetidos,nome_completo=nome_sobre)
    remover = Valores_que_devem_ser_removidos(arquivo=arquivo,repetidos=repetidos,dicionario=dicio)
    arquivo = arquivo.drop(remover)
    arquivo = arquivo.reset_index(drop=True)

    return arquivo



def main():
    os.system("clear")
    arquivos = glob.glob('*.xlsx')
    for arquivo_nome in arquivos:
        arquivo = pd.read_excel(arquivo_nome)
        if 'Nota Final'in arquivo.columns:
            print("A coluna Nota final ja existe.")
        else:
            numero_colunas = len(arquivo.iloc[0])
            arquivo.insert(numero_colunas,'Nota Final',0)
        arquivo = Colocar_Nota_10_para_4(arquivo)
        arquivo = Retira_Mais_Um_Envio(arquivo)
        arquivo.to_excel(arquivo_nome, index=False) # index=False para não incluir o índice do DataFrame no arquivo


main()