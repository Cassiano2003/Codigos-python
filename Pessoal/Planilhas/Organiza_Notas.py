import pandas as pd
import glob

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

def Retira_Mais_Um_Envio(arquivo):
    nomes = arquivo['Nome']
    sobre_nome = arquivo['Sobrenome']
    nome_sobre = []
    for i, nome in enumerate(nomes):
        if len(sobre_nome)-1 > i:
            nome_sobre.append(nome+' '+sobre_nome[i])
    
    valores = []
    repetidos = []
    for i,nome in enumerate(nome_sobre):
        if nome not in valores:
            valores.append(nome)
        else:
            repetidos.append(nome)
    
    print(repetidos)
    #return
    dicio = {nome : '' for nome in repetidos}

    for nome_in in repetidos:
        lis = []
        for i,nome_sb in enumerate(nome_sobre):
            if nome_in == nome_sb:
                lis.append(i)
        dicio[nome_in] = lis
    
    for nome in repetidos:
        menores = []
        maior = -1
        for i in dicio[nome]:
            print(arquivo.iloc[i])
            num = float(arquivo.loc[i, 'Avaliar/10,0'].replace(',','.'))
            print("Teste: ",num)
            if num >= maior:
                maior = num
            else:
                menores.append(i)

        print(menores)
        for remover in menores:
            arquivo = arquivo.drop(remover)
            arquivo = arquivo.reset_index(drop=True)
        

    '''arquivo = arquivo.drop(2)
    arquivo = arquivo.reset_index(drop=True)'''
    return arquivo



def main():
    arquivos = glob.glob('*.xlsx')
    for arquivo_nome in arquivos:
        arquivo = pd.read_excel(arquivo_nome)
        if 'Nota Final'in arquivo.columns:
            print("A coluna Nota final ja existe.")
        else:
            numero_colunas = len(arquivo.iloc[0])
            arquivo.insert(numero_colunas,'Nota Final',0)
        arquivo = Colocar_Nota_10_para_4(arquivo)
        for i in range(10):
            arquivo = Retira_Mais_Um_Envio(arquivo)
            arquivo.to_excel(arquivo_nome, index=False) # index=False para não incluir o índice do DataFrame no arquivo


main()