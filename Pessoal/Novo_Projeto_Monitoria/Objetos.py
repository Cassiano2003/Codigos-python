

class Aluno:
    def __init__(self, email, primeiro_nome, segundo_nome):
        self.email = email #Minha key 
        self.primeiro_nome = primeiro_nome #Primeiro nome do aluno
        self.segundo_nome = segundo_nome #Segundo nome do aluno
        self.atividades_feitas = [] #Lista das atividades feitas pelo aluno
        self.nota_atividades = [] #Nota da atividade
        self.notas_para_media_final = []  # Para guardar as notas finais de cada arquivo
        self.quantos_exes_feitos = 0
        self.nota_final_atividade = 0.0 #Nota final do aluno
        self.nota_media = 0.0 #Nota media do aluno
    
    def adicionar_atividade(self, atividade : str):
        self.atividades_feitas.append(atividade)
    
    def set_nota_atividades(self, nota: float):
        self.nota_atividades.append(nota)

    def set_notas_para_media_final(self, nota: float):  
        self.notas_para_media_final.append(nota)  # Nova função para armazenar
    
    def set_nota_final_atividade(self, nota : float):
        self.nota_final_atividade = nota
    
    def set_quantos_exes_feitos(self, qnt : int):
        self.quantos_exes_feitos = qnt

    def set_nota_media(self, div : float):
        if not self.notas_para_media_final:
            self.nota_media = 0.0
        else:
            self.nota_media = sum(self.notas_para_media_final) / div

    def __str__(self):
        return f"{self.email} | {self.primeiro_nome} {self.segundo_nome} | {self.atividades_feitas} | {self.quantos_exes_feitos} | {self.nota_final_atividade} | {self.nota_media}"