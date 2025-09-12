class Aluno:
    def __init__(self, email, primeiro_nome, segundo_nome):
        self.email = email
        self.primeiro_nome = primeiro_nome
        self.segundo_nome = segundo_nome
        self.nota_atividade = 0.0
        self.nota_final = 0.0
        self.notas_exercicios = []
        self.notas_finais = []  # ✅ Para guardar as notas finais de cada arquivo

    def adicionar_nota_exercicio(self, nota: float):
        self.notas_exercicios.append(nota)

    def adicionar_nota_final(self, nota: float):
        self.notas_finais.append(nota)  # ✅ Nova função para armazenar

    def calcular_media(self) -> float:
        if not self.notas_finais:
            return 0.0
        return sum(self.notas_finais) / len(self.notas_finais)
