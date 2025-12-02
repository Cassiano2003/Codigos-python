import glob #Uma biblioteca que me ajuda a caregar todos os arquivos (*.xlsx)
import pandas as pd #Essa biblioteca me permite fazer a manipulaçao desses arquivos
import os

class Aluno:
    def __init__(self, email, primeiro_nome, segundo_nome):
        self.email = email #Minha key 
        self.primeiro_nome = primeiro_nome #Primeiro nome do aluno
        self.segundo_nome = segundo_nome #Segundo nome do aluno
        self.atividades_feitas = [] #Lista das atividades feitas pelo aluno
    
    def adicionar_atividade(self, atividade):
        self.atividades_feitas.append(atividade)

    def __str__(self):
        return f"{self.email} | {self.primeiro_nome} {self.segundo_nome} | {self.atividades_feitas}"
    

#Vai ficar limpando a tela
def limpa_tela():
    os.system("clear")

def Pega_Informacoes(arquivo: pd.DataFrame):
    nomes = arquivo['Nome']
    sobre = arquivo['Sobrenome']
    email = arquivo['Endereço de email']
    try:
        avaliacoes = arquivo['Avaliar/10,0']
        return nomes, sobre, email, avaliacoes
    except:
        return nomes, sobre, email, None

def Busca_Aluno(emai : str,nome: str,sobre : str,list_alunos: list[Aluno]):
    nome_sobre = f"{nome} {sobre}"
    for i,aluno in enumerate(list_alunos):
        nome_aluno = f"{aluno.primeiro_nome} {aluno.segundo_nome}"
        if (aluno.email == emai) or (nome_aluno == nome_sobre) or (aluno.primeiro_nome == nome and aluno.segundo_nome == sobre):
            return i
    return -1

#Vai apenas imprimir os objetos alunos
def Imprime_Alunos(alunos: list[Aluno]):
    for aluno in alunos:
        print(aluno)

def gerar_arquivo(alunos: list[Aluno]):
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


def menu():
    limpa_tela() #Vai chamar a funçao que vai ficar limpando a tela
    alunos = []
    arquivos = glob.glob('*.xlsx') #Vai me retornar uma lista com todos os arquivos .xlsx
    arquivos.sort()
    print("------"*10)
    print("Gerar arquivo dos alunos com atividades feitas")
    print("------"*10)
    print("A primeira exocolha tem que ser a lista de presenças.")
    print("Selecione os arquivos que queiras manipular.")
    print("------"*10)
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
    gerar_arquivo(alunos)
    print("------"*10)

if __name__ == "__main__":
    menu()
