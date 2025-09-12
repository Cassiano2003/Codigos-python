import os
from models import Aluno
from utils import (
    pedir_inteiro, pedir_float,
    listar_planilhas, escolher_arquivos,
    carregar_alunos_de_excel, calcular_nota_final,
    salvar_planilha_com_notas, adicionar_notas_finais_em_alunos,
    gerar_arquivo_medias
)

def opcao_criar_coluna():
    arquivos = listar_planilhas()
    if not arquivos:
        print("Nenhum arquivo .xlsx encontrado.")
        return

    indices = escolher_arquivos(arquivos)

    for idx in indices:
        caminho = arquivos[idx]

        print("\n" + "=" * 60)
        print(f"📂 Processando arquivo: {caminho}")
        print("=" * 60 + "\n")

        # Pergunta a quantidade de questões e nota de corte para cada arquivo
        questoes = pedir_inteiro("Quantas questões tem este arquivo: ", 1)
        nota_corte = pedir_float("Digite a nota de corte para este arquivo: ")

        # Carrega alunos e calcula nota final
        alunos, df = carregar_alunos_de_excel(caminho, questoes)
        for aluno in alunos:
            calcular_nota_final(aluno, nota_corte)

        # Salva a planilha atualizada, removendo duplicatas e mantendo a maior nota
        salvar_planilha_com_notas(df, alunos, caminho)

def opcao_gerar_medias(lista_alunos: list[Aluno]):
    if not lista_alunos:
        print("⚠️ Crie a lista de alunos primeiro (opção 2).")
        return

    # Adiciona notas finais de vários arquivos para cada aluno, mantendo apenas a maior nota
    adicionar_notas_finais_em_alunos(lista_alunos)

    nome = input("Digite o nome do arquivo de saída: ")
    gerar_arquivo_medias(lista_alunos, nome)

def opcao_criar_lista() -> list[Aluno]:
    arquivos = listar_planilhas()
    if not arquivos:
        print("Nenhum arquivo .xlsx encontrado.")
        return []

    idx = pedir_inteiro(f"Escolha o arquivo [0-{len(arquivos)-1}]: ", 0, len(arquivos)-1)

    print("\n" + "=" * 60)
    print(f"📂 Criando lista a partir do arquivo: {arquivos[idx]}")
    print("=" * 60 + "\n")

    questoes = pedir_inteiro("Quantas questões tem este arquivo (apenas para leitura inicial): ", 1)
    alunos, _ = carregar_alunos_de_excel(arquivos[idx], questoes)

    print(f"✅ Lista de alunos criada ({len(alunos)} registros) a partir de: {arquivos[idx]}")
    return alunos

def opcao_imprimir(lista_alunos: list[Aluno]):
    if not lista_alunos:
        print("⚠️ Lista de alunos vazia.")
    else:
        for a in lista_alunos:
            print(a)

def menu():
    alunos: list[Aluno] = []
    opcoes = {
        0: opcao_criar_coluna,
        1: lambda: opcao_gerar_medias(alunos),
        2: lambda: alunos.extend(opcao_criar_lista()),
        3: lambda: opcao_imprimir(alunos)
    }

    while True:
        print("\n" + "-" * 50)
        print("0 - Criar/Atualizar coluna de notas finais")
        print("1 - Gerar arquivo com médias finais")
        print("2 - Criar lista de alunos")
        print("3 - Imprimir lista de alunos")
        print("4 - Sair")

        escolha = pedir_inteiro("Escolha uma opção: ", 0, 4)
        if escolha == 4:
            print("Programa finalizado.")
            break

        os.system("clear" if os.name == "posix" else "cls")
        opcoes[escolha]()

if __name__ == "__main__":
    menu()
