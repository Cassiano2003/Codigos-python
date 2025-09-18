import os
import pandas as pd
from models import Aluno


def Menores_Notas(repetidos: list[str],lista_alunos : list[Aluno]):
    menores = []
    for emais in repetidos:
        maior = -1
        local_maior = -1
        locais = Busca_Posicoes(emais,lista_alunos)
        for local in locais:
            if lista_alunos[local].Nota_Atividade > maior:
                print(lista_alunos[local].Nota_Atividade)
                maior = lista_alunos[local].Nota_Atividade
                if local_maior != -1:
                    menores.append(local_maior)
                local_maior = local
            else:
                menores.append(local)
    return menores

def Busca_Posicoes(email: str,alunos: list[Aluno]):
    posicoes = []
    for i,aluno in enumerate(alunos):
        if aluno.Email == email:
            posicoes.append(i)
    return posicoes

def Alunos_Repetidos(alunos: list[Aluno]):
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

def Coloca_Notas(alunos: list[Aluno],arquivo: pd.DataFrame):
    for i,aluno in enumerate(alunos):
        arquivo.loc[i, 'Nota Final'] = round(aluno.Nota, 2)
    return arquivo

def Calcula_Nota_Final(aluno: Aluno,nota_corte: float):
    quantas_notas = 0
    for nota in aluno.Nota_Exercicios:
        if nota >= nota_corte:
            quantas_notas += 1
    if quantas_notas >= 3:
        aluno.Adiciona_Nota(10.0)
    else:
        aluno.Adiciona_Nota(quantas_notas*(3.333333))

def Adiciona_notas(i: int,arquivo: pd.DataFrame,ate: int,aluno: Aluno):
    primeira_linha = arquivo.iloc[i]
    for j in range(8,ate):
        aluno.Adiciona_Notas_Exercicios(float(str(primeira_linha[j]).replace(",", ".")))

def Pega_informacoes_atividades(arquivo: pd.DataFrame):
    nomes = arquivo['Nome']
    sobre = arquivo['Sobrenome']
    email = arquivo['Endereço de email']
    nota_final = arquivo['Nota Final']
    nota_atividade = [float((ati).replace(",", ".")) for ati in arquivo['Avaliar/10,0']]
    return email,nomes,sobre,nota_final,nota_atividade

def Pega_Informacoes_chamada(arquivo: pd.DataFrame):
    nomes = arquivo['Nome']
    sobre = arquivo['Sobrenome']
    email = arquivo['Endereço de email']
    return nomes, sobre, email

def Busca_Aluno(email: str,list_alunos: list[Aluno]):
    for i,aluno in enumerate(list_alunos):
        if aluno.Email == email:
            return i
    return -1

def Imprime_Alunos(alunos: list[Aluno]):
    for aluno in alunos:
        print(aluno)
    
def Numeros_Validos(arquivos: list[str]):
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


def gerar_arquivo_medias(alunos: list[Aluno], nome_arquivo: str):
    # Determina quantas colunas NF precisamos (máximo de notas)
    max_notas = max(len(a.notas_finais) for a in alunos) if alunos else 0
    
    dados = {
        "Nome Completo": [f"{a.primeiro_nome} {a.segundo_nome}" for a in alunos],
        "Endereço de email": [a.email for a in alunos],
        # Para cada posição de nota, cria uma coluna NF
        **{f"NF{i+1}": [a.notas_finais[i] if i < len(a.notas_finais) else "0" for a in alunos] 
           for i in range(max_notas)},
        "Média Final": [round(a.calcular_media(max_notas), 2) for a in alunos],
    }
    
    # Cria DataFrame e ordena por nome
    df = pd.DataFrame(dados)
    df = df.sort_values(by="Nome Completo")
    
    df.to_excel(nome_arquivo + ".xlsx", index=False)
    print(f"✅ Arquivo '{nome_arquivo}.xlsx' gerado com {max_notas} colunas de notas (ordenado por nome).")


def limpa_tela():
    os.system("clear")

