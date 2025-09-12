import pandas as pd
import glob
import os

class Aluno:
    def __init__(self,Email,Primeiro_nome,Segundo_Nome,Nota_Atividade):
        self.Email = Email #Minha key
        self.Primeiro_nome = Primeiro_nome
        self.Segundo_nome = Segundo_Nome
        self.Nota_Final = [] #Vai ser usada para poder gerar a media
        self.Nota = 0
        self.Nota_Atividade = Nota_Atividade
        self.Nota_Exercicios = [] #Lista das notas da quele .xlsx
        self.Media_Final = 0
    
    def Calcula_Media(self,div):
        soma = 0
        for nota in self.Nota_Final:
            soma += nota
        self.Media_Final = soma/div


    def Adiciona_Nota(self,nota):
        self.Nota = nota

    def Adiciona_Notas_Exercicios(self,nota):
        self.Nota_Exercicios.append(nota)

    def Adiciona_Notas_Final(self,nota):
        self.Nota_Final.append(nota)
    
    def __str__(self):
        return f"{self.Primeiro_nome} {self.Segundo_nome} e suas notas é {self.Nota_Exercicios},notas de atividades {self.Nota_Atividade} e sua nota final é {self.Nota}\nAs notas finais{self.Nota_Final} e a media desse aluno é {self.Media_Final}"

def Menores_Notas(repetidos,alunos,arquivo):
    menores = []
    for emais in repetidos:
        maior = -1
        local_maior = -1
        locais = Busca_Posicoes(emais,alunos)
        for local in locais:
            if alunos[local].Nota_Atividade > maior:
                print(alunos[local].Nota_Atividade)
                maior = alunos[local].Nota_Atividade
                if local_maior != -1:
                    menores.append(local_maior)
                local_maior = local
            else:
                menores.append(local)
    return menores

def Busca_Posicoes(email,alunos):
    posicoes = []
    for i,aluno in enumerate(alunos):
        if aluno.Email == email:
            posicoes.append(i)
    return posicoes

def Alunos_Repetidos(alunos):
    contagem = {}
    repetidos = []
    for aluno in alunos:
        if aluno.Email in contagem:
            contagem[aluno.Email] += 1
        else:
            contagem[aluno.Email] = 1
    
    for email, cont in contagem.items():
        if cont > 1:
            repetidos.append(email)
    return repetidos

def Coloca_Notas(alunos,arquivo):
    for i,aluno in enumerate(alunos):
        arquivo.loc[i, 'Nota Final'] = round(aluno.Nota, 2)
    return arquivo

def Calcula_Nota_Final(aluno,nota_corte):
    quantas_notas = 0
    for nota in aluno.Nota_Exercicios:
        if nota >= nota_corte:
            quantas_notas += 1
    if quantas_notas >= 3:
        aluno.Adiciona_Nota(10.0)
    else:
        aluno.Adiciona_Nota(quantas_notas*(3.333333))

def Adiciona_notas(i,arquivo,ate,aluno):
    primeira_linha = arquivo.iloc[i]
    for j in range(8,ate):
        aluno.Adiciona_Notas_Exercicios(float(str(primeira_linha[j]).replace(",", ".")))

def Pega_informacoes(arquivo):
    nomes = arquivo['Nome']
    sobre = arquivo['Sobrenome']
    email = arquivo['Endereço de email']
    nota_final = arquivo['Nota Final']
    nota_atividade = [float((ati).replace(",", ".")) for ati in arquivo['Avaliar/10,0']]
    return email,nomes,sobre,nota_final,nota_atividade

def Busca_Aluno(email,list_alunos):
    for i,aluno in enumerate(list_alunos):
        if aluno.Email == email:
            return i
    return -1

def Imprime_Alunos(alunos):
    for aluno in alunos:
        print(aluno)

def Gera_dados(alunos):
    dados = {"Sobrenome": [],	"Nome":[],"Endereço de email": [],"Media Final":[]}
    for aluno in alunos:
        dados["Nome"].append(aluno.Primeiro_nome)
        dados["Sobrenome"].append(aluno.Segundo_nome)
        dados["Endereço de email"].append(aluno.Email)
        dados["Media Final"].append(round(aluno.Media_Final, 2))
    df = pd.DataFrame(dados)
    print(df)
    nome_arquivo = input("Digite o nome do arquivo: ")
    nome_arquivo = nome_arquivo+".xlsx"
    df.to_excel(nome_arquivo,index=False)
    
def Numeros_Validos(arquivos):
    for i,ar in enumerate(arquivos):
        print("[",i,"]",ar)
    print("------"*10)
    minhas_escolhas = input("Digite os numeros desejados separados por espaço: ")
    numros_escolhas = [int(es) for es in minhas_escolhas.split()]
    print("------"*10)
    for num in numros_escolhas:
        if num > len(arquivos)-1:
            print("Numeros invalidos!!!")
            return Numeros_Validos(arquivos)
    print("Numeros validos!!!")
    return numros_escolhas     

def menu():
    os.system("clear")
    opcoes = ["[ 0 ] Criar a colona com as Notas Finais","[ 1 ] Criar um arquivo que vai ter a media das Notas Finais"]
    arquivos = glob.glob('*.xlsx')
    print("------"*10)
    print("Selecione os arquivos que queiras manipular.")
    print("------"*10)
    numros_escolhas = Numeros_Validos(arquivos)
    print("------"*10)
    for op in opcoes:
        print(op)
    print("------"*10)
    escolha = int(input("Escolha qual sera a operação desejada: "))
    match escolha:
        case 0:
            #Lendo o arquivo
            for num in numros_escolhas:
                print("------"*10)
                os.system("clear")
                print("Arquivo selecionado ",arquivos[num])
                print("------"*10)
                alunos = []
                arquivo = pd.read_excel(arquivos[num])
                if 'Nota Final'in arquivo.columns:
                    print("A coluna Nota final ja existe.")
                else:
                    numero_colunas = len(arquivo.iloc[0])
                    arquivo.insert(numero_colunas,'Nota Final',0)
                #Gero o vetor da Classe Alunos
                email,nome,sobre,nota_final,nota_atividade = Pega_informacoes(arquivo=arquivo)
                ques = int(input("Quantas questoes tem: "))
                for i in range(len(arquivo)):
                    aluno = Aluno(email[i],nome[i],sobre[i],nota_atividade[i])
                    Adiciona_notas(i,arquivo,8+ques,aluno)
                    alunos.append(aluno)
                #Vai gerar as notas de cada aluno
                nota_corte = float(input("Digite a nota de corte: "))
                for aluno in alunos:
                    Calcula_Nota_Final(aluno,nota_corte)
                #Coloca as notas de cada aluno na planilha
                alunos.pop(len(alunos)-1)
                arquivo = Coloca_Notas(alunos,arquivo)
                repetidos = Alunos_Repetidos(alunos)
                menores = Menores_Notas(repetidos,alunos,arquivo)
                print(menores)
                arquivo = arquivo.drop(menores)
                arquivo = arquivo.reset_index(drop=True)
                #Imprime_Alunos(alunos)
                arquivo.to_excel(arquivos[num], index=False) # index=False para não incluir o índice do DataFrame no arquivo
                input("Precione entter para continuar")
        case 1:
            alunos = []
            for num in numros_escolhas:
                arquivo = pd.read_excel(arquivos[num])
                email,nome,sobre,nota_final,nota_atividade = Pega_informacoes(arquivo=arquivo)
                if len(alunos) == 0:
                    em_tam, nm_tam, sb_tam, nf_tam = len(email),len(nome),len(sobre),len(nota_final)
                    if(em_tam == nm_tam == sb_tam == nf_tam):
                        for i in range(em_tam):
                            nova_nota = float(str(nota_final[i]).replace(",", "."))
                            aluno = Aluno(email[i],nome[i],sobre[i],nota_atividade[i])
                            aluno.Adiciona_Notas_Final(nova_nota)
                            alunos.append(aluno)
                elif len(alunos) > 0:
                    for i,em in enumerate(email):
                        lugar = Busca_Aluno(em,alunos)
                        nova_nota = float(str(nota_final[i]).replace(",", "."))
                        if lugar != -1:
                            alunos[lugar].Adiciona_Notas_Final(nova_nota)
            for aluno in alunos:
                aluno.Calcula_Media(len(numros_escolhas))
            alunos.pop(len(alunos)-1)
            #Imprime_Alunos(alunos)
            Gera_dados(alunos)
        case _:
            print("Não tem essa operação\nPrograma finalizado!!!")
            return
    print("------"*10)

menu()