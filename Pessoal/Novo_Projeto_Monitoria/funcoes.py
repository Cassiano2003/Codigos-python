import pandas as pd
import os
from Objetos import Aluno

def Opcaes_Menu():
    #Eu cria listas de para facilitar a adiçao e modificaçao do meu menu
    opcoes = ["[ 0 ] Criar a colona com as Notas Finais","[ 1 ] Criar um arquivo que vai ter a media das Notas Finais",
                "[ 2 ] Gerar arquivo com presenças EAD"]
    print("------"*10)
    for op in opcoes:
        print(op)
    print("------"*10)
    return len(opcoes)

def Escolha_Arquivo(arquivos: list[str]):
    print("Selecione os arquivos que queiras manipular.")
    print("------"*10)
    for i,ar in enumerate(arquivos):
        print("[",i,"]",ar)
    print("------"*10)
    minhas_escolhas = input("Digite os numeros desejados separados por espaço: ")
    numros_escolhas = [int(es) for es in minhas_escolhas.split()]
    print("------"*10)
    for num in numros_escolhas:
        if num > len(arquivos)-1:
            print("Numeros invalidos!!!")
            return None
    print("Numeros validos!!!")
    return numros_escolhas

#Vai ficar limpando a tela
def limpa_tela():
    os.system("clear")

def Pega_Informacoes(arquivo: pd.DataFrame,lista_tiotulos: list[str]):
    dis = {}
    for titulo in lista_tiotulos:
        dis[titulo] = arquivo[titulo]
    return dis

def Busca_Aluno(emai : str,nome: str,sobre : str,list_alunos: list[Aluno]):
    nome_sobre = f"{nome} {sobre}"
    for i,aluno in enumerate(list_alunos):
        nome_aluno = f"{aluno.primeiro_nome} {aluno.segundo_nome}"
        if (aluno.email == emai) or (nome_aluno == nome_sobre) or (aluno.primeiro_nome == nome and aluno.segundo_nome == sobre):
            return i
    return -1

def Gera_lista_sem_duplicados(alunos: list[Aluno]) -> list[Aluno]:
    # Remove duplicatas mantendo o primeiro (maior nota)
    alunos_sem_duplicatas = []
    emails_vistos = set()

    for aluno in alunos:
        if aluno.email not in emails_vistos:
            emails_vistos.add(aluno.email)
            alunos_sem_duplicatas.append(aluno)
            
    return alunos_sem_duplicatas

#Vai apenas imprimir os objetos alunos
def Imprime_Alunos(alunos: list[Aluno]):
    for aluno in alunos:
        print(aluno)

def Pega_informacoes_atividades(arquivo: pd.DataFrame):
    nomes = arquivo['Nome']
    sobre = arquivo['Sobrenome']
    email = arquivo['Endereço de email']
    nota_atividade = [float((ati).replace(",", ".")) for ati in arquivo['Avaliar/10,0']]
    return email,nomes,sobre,nota_atividade

#Vai colocar as notas finais ja calculadas no arquivo e me retornar o arquivo ja modificado
def Coloca_Notas(alunos: list[Aluno],arquivo: pd.DataFrame):
    # Converter a coluna 'Nota Final' para float antes de atribuir valores
    arquivo['Nota Final'] = arquivo['Nota Final'].astype(float)
    
    for i,aluno in enumerate(alunos):
        arquivo.loc[i, 'Nota Final'] = round(aluno.nota_final_atividade, 2)
    return arquivo

def gerar_arquivo_EAD(alunos: list[Aluno]):
    nome_arquivo = input("Digite o nome do arquivo a ser gerado (sem extensão): ")
    # Determina o número máximo de atividades entre todos os alunos
    max_atividades = max(len(aluno.atividades_feitas) for aluno in alunos)
    
    # Prepara os dados para o DataFrame
    dados = {
        "Nome Completo": [],
        "Endereço de email": [],
        **{f"EAD{i+1}": [] for i in range(max_atividades)}
    }
    
    # Preenche os dados de cada aluno
    for aluno in alunos:
        dados["Nome Completo"].append(f"{aluno.primeiro_nome} {aluno.segundo_nome}")
        dados["Endereço de email"].append(aluno.email)
        
        # Preenche as atividades do aluno
        for i in range(max_atividades):
            if i < len(aluno.atividades_feitas):
                dados[f"EAD{i+1}"].append(aluno.atividades_feitas[i])
            else:
                dados[f"EAD{i+1}"].append("")  # String vazia em vez de espaço
    
    # Cria DataFrame e ordena por nome
    df = pd.DataFrame(dados)
    df = df.sort_values(by="Nome Completo")

    # Exportar para Excel
    df.to_excel(nome_arquivo + ".xlsx", index=False)
    print(f"✅ Arquivo '{nome_arquivo}.xlsx' gerado com {max_atividades} colunas de notas (linhas coloridas por média).")
