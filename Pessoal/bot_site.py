from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyttsx3
import speech_recognition as sr
from time import sleep
import os

os.system("clear")

# Inicializa leitor de voz
voz = pyttsx3.init()
vozes = voz.getProperty('voices')
'''
for i, v in enumerate(vozes):
    print(f"{i}: {v.name} ({v.languages}) - {v.id}")'''
    
voz.setProperty('voice', vozes[95].id)  # exemplo: usa a voz 1 da lista

# Inicializa o navegador
driver = webdriver.Firefox()
driver.get("http://anotacao.ddns.net:8501/")  # <-- coloque o site certo aqui
input("Precione entere para começar!!!!!")

def falar(texto):
    voz.say(texto)
    voz.runAndWait()

def ouvir_resposta():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            print("Fale 'sim' ou 'não'...")
            audio = rec.listen(source)
            try:
                resposta = rec.recognize_google(audio, language="pt-BR").lower()
                print(f"Você disse: {resposta}")
                return resposta
            except sr.UnknownValueError:
                print("Não entendi o que você disse. Tente novamente...")
            except sr.RequestError:
                print("Erro na conexão com o serviço de reconhecimento.")
                return None
            

# Função para clicar de forma segura
def clicar_elemento(elem):
    try:
        elem.click()
    except:
        driver.execute_script("arguments[0].click();", elem)

# Lista para guardar o histórico de respostas
historico = []

wait = WebDriverWait(driver, 10)

'''# Fala opções
opcoes = ["Sim.","Não.","Fase.","Voltar.","Confirmar.","Sair.","Repetir."]
falar("Qual opção?")
for o in opcoes:
    falar(o)'''

def Vai_tudo_sim(botao_priximo):
    clicar_elemento(botao_priximo)
    falar("Indo para a proxima frase.")
    sleep(10)


while True:
    try:
        # Espera os botões estarem presentes
        botao_anterior = wait.until(EC.presence_of_element_located((By.XPATH, "//button//p[contains(text(), 'Anterior')]")))
        botao_priximo = wait.until(EC.presence_of_element_located((By.XPATH,"//button//p[contains(text(), 'Próxima')]")))
        botao_salvar = wait.until(EC.presence_of_element_located((By.XPATH,"//button//p[contains(text(), 'Salvar agora')]")))

        # Lê a pergunta da página
        pergunta_elem = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-testid='stMarkdown'] p")))
        pergunta = pergunta_elem.text
        print(f"Pergunta: {pergunta}")
        falar(pergunta)

        '''# Espera a resposta do usuário
        resposta = ouvir_resposta()
        while resposta is None:
            falar("Não entendi, pode repetir?")
            resposta = ouvir_resposta()

        resposta = resposta.lower().strip()'''
        radio = driver.find_element(By.CSS_SELECTOR, 'input[type="radio"][value="0"]')
        Vai_tudo_sim(botao_priximo)
        
        '''''# Processa a resposta
        if resposta.startswith("si"):  # Sim
            clicar_elemento(radio)
            clicar_elemento(botao_priximo)
            falar("Marcado sim e indo para a proxima.")
            historico.append({'pergunta': pergunta, 'resposta': 'Sim'})
            
        elif resposta.startswith("n"):  # Não
            radio = driver.find_element(By.CSS_SELECTOR, 'input[type="radio"][value="1"]')
            clicar_elemento(radio)
            clicar_elemento(botao_priximo)
            falar("Marcado não e indo para a proxima.")
            historico.append({'pergunta': pergunta, 'resposta': 'Não'})
            
        elif resposta.startswith("v"):  # Voltar
            clicar_elemento(botao_anterior)
            falar("Voltou.")
            
        elif resposta.startswith("c"):  # Confirmar/Avançar
            clicar_elemento(botao_priximo)
            falar("Avançou.")
            
        elif resposta.startswith("f"):  # Repetir pergunta
            falar(pergunta)
            
        elif resposta.startswith("re"):  # Repetir opções
            for o in opcoes:
                falar(o)
            
        elif resposta.startswith("sair"):  # Sair
            clicar_elemento(botao_salvar)
            falar("Seu programa foi encerrado!")
            break
            
        else:
            falar("Não entendi sua resposta.")

        sleep(5)  # Pequena pausa antes da próxima iteração'''

    except TimeoutException:
        falar("Tempo esgotado para carregar elementos, tentando novamente...")
        sleep(1)
    except StaleElementReferenceException:
        # Caso a página recarregue enquanto interagimos
        falar("A página recarregou, aguardando elementos...")
        sleep(1)

# O9y1h5xQ