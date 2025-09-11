import pandas as pd
import glob
import os

class Aluno:
    def __init__(self,Email,Primeiro_nome,Segundo_Nome):
        self.Email = Email #Minha key
        self.Primeiro_nome = Primeiro_nome
        self.Segundo_nome = Segundo_Nome
        self.Nota_Final = []
        self.Media_Final = 0
    
    def Calcula_Media(self,div):
        soma = 0
        for nota in self.Nota_Final:
            soma += nota
        self.Media_Final = soma/div


    def Adiciona_Notas(self,nota):
        self.Nota_Final.append(nota)
    
    def __str__(self):
        return f"{self.Primeiro_nome} {self.Segundo_nome} e suas notas é {self.Nota_Final} e a media desse aluno é {self.Media_Final}"

def Colocar_Nota_10_para_4(arquivo):
    valor = (arquivo['Avaliar/10,0'])
    arquivo['Nota Final'] = arquivo['Nota Final'].astype(str)
    for i,n in enumerate(valor):
        novos_valores = (n.replace(',','.'))
        if len(valor)-1 > i:
            if float(novos_valores) >= 4:
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
    return nome,sobre_nome,nome_sobre

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
    nome,sobre_nome,nome_sobre = Cria_nome_e_sobre(arquivo=arquivo)
    repetidos = Verifica_nomes_repetidos(nomes_completos=nome_sobre)
    dicio = Acha_posicao_nome(repetidos=repetidos,nome_completo=nome_sobre)
    remover = Valores_que_devem_ser_removidos(arquivo=arquivo,repetidos=repetidos,dicionario=dicio)
    arquivo = arquivo.drop(remover)
    arquivo = arquivo.reset_index(drop=True)

    return arquivo

def Pega_informacoes(arquivo):
    nomes = arquivo['Nome']
    sobre = arquivo['Sobrenome']
    email = arquivo['Endereço de email']
    nota_final = arquivo['Nota Final']
    return email,nomes,sobre,nota_final

def Busca_Aluno(email,list_alunos):
    for i,aluno in enumerate(list_alunos):
        if aluno.Email == email:
            return i
    return -1

def Imprime_Alunos(alunos):
    for aluno in alunos:
        print(aluno)


def Gera_dados(alunos):
    dados = {"Sobrenome": None,	"Nome":None,"Media Final":None}
    

def menu():
    os.system("clear")
    opcoes = ["[ 0 ] Criar a colona com as Notas Finais","[ 1 ] Criar um arquivo que vai ter a media das Notas Finais"]
    arquivos = glob.glob('*.xlsx')
    print("------"*10)
    print("Selecione os arquivos que queiras manipular.")
    print("------"*10)
    for i,ar in enumerate(arquivos):
        print("[",i,"]",ar)
    print("------"*10)
    minhas_escolhas = input("Digite os numeros desejados separados por espaço: ")
    numros_escolhas = [int(es) for es in minhas_escolhas.split()]
    div = len(numros_escolhas)
    print("------"*10)
    for op in opcoes:
        print(op)
    print("------"*10)
    escolha = int(input("Escolha qual sera a operação desejada: "))
    alunos = []
    match escolha:
        case 0:
            for num in numros_escolhas:
                arquivo = pd.read_excel(arquivos[num])
                if 'Nota Final'in arquivo.columns:
                    print("A coluna Nota final ja existe.")
                else:
                    numero_colunas = len(arquivo.iloc[0])
                    arquivo.insert(numero_colunas,'Nota Final',0)
                    arquivo = Colocar_Nota_10_para_4(arquivo)
                    arquivo = Retira_Mais_Um_Envio(arquivo)
                    arquivo.to_excel(arquivos[num], index=False) # index=False para não incluir o índice do DataFrame no arquivo
        case 1:
            for num in numros_escolhas:
                arquivo = pd.read_excel(arquivos[num])
                email,nome,sobre,nota_final = Pega_informacoes(arquivo=arquivo)
                if len(alunos) == 0:
                    em_tam, nm_tam, sb_tam, nf_tam = len(email),len(nome),len(sobre),len(nota_final)
                    if(em_tam == nm_tam == sb_tam == nf_tam):
                        for i in range(em_tam):
                            nova_nota = float(str(nota_final[i]).replace(",", "."))
                            aluno = Aluno(email[i],nome[i],sobre[i])
                            aluno.Adiciona_Notas(nova_nota)
                            alunos.append(aluno)
                elif len(alunos) > 0:
                    for i,em in enumerate(email):
                        lugar = Busca_Aluno(em,alunos)
                        nova_nota = float(str(nota_final[i]).replace(",", "."))
                        if lugar != -1:
                            alunos[lugar].Adiciona_Notas(nova_nota)
            for aluno in alunos:
                aluno.Calcula_Media(len(numros_escolhas))
            alunos.pop(len(alunos)-1)
            Imprime_Alunos(alunos)
        case _:
            print("Não tem essa operação\nPrograma finalizado!!!")
            return
    

menu()