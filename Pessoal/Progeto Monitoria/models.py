#Estado	Iniciado em	Completo	Tempo utilizado
#Uma classe para cada aluno, na onde vai ter as informações de cada aluno
#Com isso posso criar uma lista de alunos e manipular as informações de cada aluno e gerar uma nova planilha com as informações de cada aluno

class Aluno:
    def __init__(self, email, primeiro_nome, segundo_nome):
        self.email = email #Minha key 
        self.primeiro_nome = primeiro_nome #Primeiro nome do aluno
        self.segundo_nome = segundo_nome #Segundo nome do aluno
        self.nota_atividade = 0.0 #Nota da atividade
        self.nota_final_atividade = 0.0 #Nota final
        self.notas_exercicios = [] #Lista das notas dos exercicios
        self.notas_para_media_final = []  # Para guardar as notas finais de cada arquivo
        self.nota_media = 0

    def set_notas_exercicios(self, nota: float):
        self.notas_exercicios.append(nota)

    def set_notas_para_media_final(self, nota: float):
        self.notas_para_media_final.append(nota)  # Nova função para armazenar
    
    def set_nota_media(self,nota):
        self.nota_media = nota

    def set_nota_atividade(self,nota):
        self.nota_atividade = nota
    
    def set_nota_final_exercicios(self,nota):
        self.nota_final_atividade = nota

    def calcular_media(self,div) -> float:
        if not self.notas_para_media_final:
            return 0.0
        return sum(self.notas_para_media_final) / div

    def __str__(self):
        return f"{self.email} | {self.primeiro_nome} {self.segundo_nome} | {self.notas_para_media_final} | {self.nota_final_atividade} | {self.nota_media}"