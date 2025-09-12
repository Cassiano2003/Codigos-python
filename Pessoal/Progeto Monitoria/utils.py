import os
import glob
import pandas as pd
from models import Aluno

# ===================== Entrada Segura =====================
def pedir_inteiro(msg: str, minimo=0, maximo=None) -> int:
    while True:
        try:
            valor = int(input(msg))
            if maximo is not None and not (minimo <= valor <= maximo):
                raise ValueError
            return valor
        except ValueError:
            print("⚠️ Entrada inválida, tente novamente.")

def pedir_float(msg: str) -> float:
    while True:
        try:
            return float(input(msg).replace(",", "."))
        except ValueError:
            print("⚠️ Digite um número válido.")

# ===================== Manipulação de Arquivos =====================
def listar_planilhas() -> list[str]:
    arquivos = glob.glob("*.xlsx")
    for i, arq in enumerate(arquivos):
        print(f"[{i}] {arq}")
    return arquivos

def escolher_arquivos(arquivos: list[str]) -> list[int]:
    while True:
        try:
            escolhas = [int(x) for x in input("Digite os números desejados separados por espaço: ").split()]
            if all(0 <= e < len(arquivos) for e in escolhas):
                return escolhas
        except ValueError:
            pass
        print("⚠️ Números inválidos, tente novamente.")

# ===================== Leitura e Criação de Alunos =====================
def carregar_alunos_de_excel(caminho: str, questoes: int) -> list[Aluno]:
    df = pd.read_excel(caminho)
    emails = df["Endereço de email"]
    nomes = df["Nome"]
    sobrenomes = df["Sobrenome"]

    if questoes != 0:
        atividades = pd.to_numeric(
            df["Avaliar/10,0"].astype(str).str.replace(",", "."),
            errors="coerce"
        )

    alunos = []
    for i in range(len(df)):
        aluno = Aluno(emails[i], nomes[i], sobrenomes[i])
        if questoes != 0:
            aluno.nota_atividade = atividades[i]
        for j in range(8, 8 + questoes):
            nota = pd.to_numeric(str(df.iloc[i, j]).replace(",", "."), errors="coerce")
            if pd.notna(nota):
                aluno.adicionar_nota_exercicio(float(nota))
        alunos.append(aluno)
    return alunos, df

def calcular_nota_final(aluno: Aluno, nota_corte: float):
    acertos = sum(1 for n in aluno.notas_exercicios if n >= nota_corte)
    aluno.nota_final = 10.0 if acertos >= 3 else acertos * 3.3333

def salvar_planilha_com_notas(df: pd.DataFrame, alunos: list[Aluno], caminho: str):
    # Se não existir a coluna "Nota Final", cria
    if "Nota Final" not in df.columns:
        df.insert(len(df.columns), "Nota Final", 0.0)

    # Atualiza/insere a nota final de cada aluno
    for i, aluno in enumerate(alunos):
        df.loc[i, "Nota Final"] = round(aluno.nota_final, 2)

    # 🔑 Mantém apenas a maior nota por aluno
    # Ordena pela maior Nota Final primeiro
    df = df.sort_values("Avaliar/10,0", ascending=False)

    # Remove duplicatas com base em Emails (pode trocar por "Endereço de email" se for mais seguro)
    df = df.drop_duplicates(subset=["Endereço de email"], keep="first")

    # Salva a planilha já atualizada e sem duplicatas
    df.to_excel(caminho, index=False)
    print(f"✅ Planilha '{caminho}' atualizada (duplicatas removidas e maior nota mantida).")


def adicionar_notas_finais_em_alunos(alunos: list[Aluno]):
    arquivos = listar_planilhas()
    if not arquivos:
        print("Nenhum arquivo .xlsx encontrado.")
        return

    indices = escolher_arquivos(arquivos)

    for idx in indices:
        caminho = arquivos[idx]
        print("\n" + "=" * 60)
        print(f"📂 Lendo notas finais do arquivo: {caminho}")
        print("=" * 60 + "\n")

        df = pd.read_excel(caminho)
        if "Nota Final" not in df.columns:
            print(f"⚠️ O arquivo {caminho} não contém a coluna 'Nota Final'. Pulando.")
            continue

        # 🔑 Mantém apenas a maior nota por aluno
        df = df.sort_values("Nota Final", ascending=False)
        df = df.drop_duplicates(subset=["Endereço de email"], keep="first")

        emails = df["Endereço de email"]
        notas_finais = pd.to_numeric(df["Nota Final"], errors="coerce")

        for email, nota in zip(emails, notas_finais):
            if pd.isna(nota):
                continue
            for aluno in alunos:
                if aluno.email == email:
                    aluno.adicionar_nota_final(float(nota))
                    break


def gerar_arquivo_medias(alunos: list[Aluno], nome_arquivo: str):
    # Calcula a média considerando todas as notas finais já filtradas (maior nota por arquivo)
    dados = {
        "Sobrenome": [a.segundo_nome for a in alunos],
        "Nome": [a.primeiro_nome for a in alunos],
        "Endereço de email": [a.email for a in alunos],
        "Média Final": [round(a.calcular_media(), 2) for a in alunos],
    }
    pd.DataFrame(dados).to_excel(nome_arquivo + ".xlsx", index=False)
    print(f"✅ Arquivo '{nome_arquivo}.xlsx' gerado com as médias finais.")
