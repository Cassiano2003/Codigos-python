import os
import pandas as pd
from models import Aluno

#Vai buscar as menores notas no meu vetor de alunos
def Menores_Notas(repetidos: list[str],lista_alunos : list[Aluno]):
    menores = []
    for emais in repetidos:
        maior = -1
        local_maior = -1
        locais = Busca_Posicoes(emais,lista_alunos)
        for local in locais:
            if lista_alunos[local].nota_atividade > maior:
                maior = lista_alunos[local].nota_atividade
                if local_maior != -1:
                    menores.append(local_maior)
                local_maior = local
            else:
                menores.append(local)
    return menores

#Vai me retornar as posicoes em que os alunos se repetem no vetor da quele arquivo
def Busca_Posicoes(email: str,alunos: list[Aluno]):
    posicoes = []
    for i,aluno in enumerate(alunos):
        if aluno.email == email:
            posicoes.append(i)
    return posicoes

#Vai me dar a contagen de quantas vezes aquele email ja se repetio no meu vetor
#Apenas uma contagen de de quantas veses um aluno enviou as respostas
def Alunos_Repetidos(alunos: list[Aluno]):
    contagem = {}
    repetidos = []
    for aluno in alunos:
        if aluno.email in contagem:
            contagem[aluno.email] += 1
        else:
            contagem[aluno.email] = 1
    
    for email, cont in contagem.items():
        if cont > 1:
            repetidos.append(email)
    return repetidos

#Vai colocar as notas finais ja calculadas no arquivo e me retornar o arquivo ja modificado
def Coloca_Notas(alunos: list[Aluno],arquivo: pd.DataFrame):
    for i,aluno in enumerate(alunos):
        arquivo.loc[i, 'Nota Final'] = round(aluno.nota_final_atividade, 2)
    return arquivo

#Vai calcular a nota final de cada aluno e adicionar essa nota no aluno
def Calcula_Nota_Final(aluno: Aluno,nota_corte: float,qnt_execicios: int):
    quantas_notas = 0
    for nota in aluno.notas_exercicios:
        if nota >= nota_corte:
            quantas_notas += 1
    if quantas_notas >= qnt_execicios:
        aluno.set_nota_final_exercicios(10.0)
    else:
        aluno.set_nota_final_exercicios(aluno.nota_atividade)

#Vai adicionar as notas de cada exercicio q o aluno fez
def Adiciona_notas(i: int,arquivo: pd.DataFrame,ate: int,aluno: Aluno):
    primeira_linha = arquivo.iloc[i]
    for j in range(8,ate):
        if str(primeira_linha[j]) == "-":
            aluno.set_notas_exercicios(float(str(primeira_linha[j]).replace("-", "0")))
        else:
            aluno.set_notas_exercicios(float(str(primeira_linha[j]).replace(",", ".")))

#Vai pegar as informaçoes da tabela de alunos, mais pegando 
def Pega_informacoes_atividades(arquivo: pd.DataFrame):
    nomes = arquivo['Nome']
    sobre = arquivo['Sobrenome']
    email = arquivo['Endereço de email']
    nota_final = arquivo['Nota Final']
    nota_atividade = [float((ati).replace(",", ".")) for ati in arquivo['Avaliar/10,0']]
    return email,nomes,sobre,nota_final,nota_atividade

#Vai criar uma lista de alunos baseado na lista presença
def Pega_Informacoes_chamada(arquivo: pd.DataFrame):
    nomes = arquivo['Nome']
    sobre = arquivo['Sobrenome']
    email = arquivo['Endereço de email']
    return nomes, sobre, email

#Vai apenas buscas o aluno na lista de alunos criada apartir da lista de presenças
def Busca_Aluno(email: str,list_alunos: list[Aluno]):
    for i,aluno in enumerate(list_alunos):
        if aluno.email == email:
            return i
    return -1

#Vai apenas imprimir os objetos alunos
def Imprime_Alunos(alunos: list[Aluno]):
    for aluno in alunos:
        print(aluno)


#Apenas para verificar se um numero é valido ou nao como escolha
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


#Uma funçao que vai gerar o arquivo contendo a media das notas finais de cada atividade
def gerar_arquivo_medias(alunos: list[Aluno], nome_arquivo: str):
    # Determina quantas colunas NF precisamos (máximo de notas)
    max_notas = max(len(a.notas_para_media_final) for a in alunos) if alunos else 0
    
    dados = {
        "Nome Completo": [f"{a.primeiro_nome} {a.segundo_nome}" for a in alunos],
        "Endereço de email": [a.email for a in alunos],
        # Para cada posição de nota, cria uma coluna NF
        **{f"NF{i+1}": [a.notas_para_media_final[i] if i < len(a.notas_para_media_final) else "0" for a in alunos] 
           for i in range(max_notas)},
        "Média Final": [round(a.calcular_media(max_notas), 2) for a in alunos],
    }
    
    # Cria DataFrame e ordena por nome
    df = pd.DataFrame(dados)
    df = df.sort_values(by="Nome Completo")
    
    df.to_excel(nome_arquivo + ".xlsx", index=False)
    print(f"✅ Arquivo '{nome_arquivo}.xlsx' gerado com {max_notas} colunas de notas (ordenado por nome).")

#Vai ficar limpando a tela
def limpa_tela():
    os.system("clear")

