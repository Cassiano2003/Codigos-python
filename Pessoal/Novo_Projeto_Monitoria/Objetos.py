

class Aluno:
    def __init__(self, email, primeiro_nome, segundo_nome):
        self.email = email #Minha key 
        self.primeiro_nome = primeiro_nome #Primeiro nome do aluno
        self.segundo_nome = segundo_nome #Segundo nome do aluno
        self.atividades_feitas = [] #Lista das atividades feitas pelo aluno
    
    def adicionar_atividade(self, atividade):
        self.atividades_feitas.append(atividade)

    def __str__(self):
        return f"{self.email} | {self.primeiro_nome} {self.segundo_nome}"