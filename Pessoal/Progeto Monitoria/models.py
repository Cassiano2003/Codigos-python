#Estado	Iniciado em	Completo	Tempo utilizado
#Uma classe para cada aluno, na onde vai ter as informações de cada aluno
#Com isso posso criar uma lista de alunos e manipular as informações de cada aluno e gerar uma nova planilha com as informações de cada aluno

class Aluno:
    def __init__(self, email, primeiro_nome, segundo_nome):
        self.email = email #Minha key 
        self.primeiro_nome = primeiro_nome #Primeiro nome do aluno
        self.segundo_nome = segundo_nome #Segundo nome do aluno
        self.estado = "" #Estado do aluno
        self.iniciado_em = "" #Data e hora de inicio
        self.completo = "" #Data e hora de completo
        self.tempo_utilizado = "" #Tempo utilizado
        self.fez_lista = False #Se o aluno fez a lista
        self.nota_atividade = 0.0 #Nota da atividade
        self.nota_final_atividade = 0.0 #Nota final
        self.notas_exercicios = [] #Lista das notas dos exercicios
        self.notas_para_media_final = []  # Para guardar as notas finais de cada arquivo

    def adicionar_nota_exercicio(self, nota: float):
        self.notas_exercicios.append(nota)

    def adicionar_nota_final(self, nota: float):
        self.notas_para_media_final.append(nota)  # ✅ Nova função para armazenar

    def calcular_media(self,div) -> float:
        if not self.notas_para_media_final:
            return 0.0
        return sum(self.notas_para_media_final) / div
    def __str__(self):
        return f"{self.email} | {self.primeiro_nome} {self.segundo_nome} | {self.notas_para_media_final} | {self.nota_final}"