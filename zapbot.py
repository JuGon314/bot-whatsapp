from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class WhatsAppBot:
    def __init__(self):
        # A mensagem que será enviada
        self.mensagem = "This is a test"

        # Nome dos grupos/contatos que você quer enviar a mensagem
        self.contatos = ["Contato1", "Grupo1"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe', chrome_options=options)

    def EnviarMensagens(self):
        # <span dir="auto" title="Me" aria-label="" class="ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr _11JPr">Me</span>
        # <div tabindex="-1" class="_3Uu1_">
        # <span data-testid="send" data-icon="send" class="">
        self.driver.get('https://web.whatsapp.com')
        time.sleep(30)

        for contato in self.contatos:
            campo_grupo = self.driver.find_element(By.XPATH, f"//span[@title='{contato}']")
            time.sleep(3)
            campo_grupo.click()
            chat_box = self.driver.find_element(By.CLASS_NAME, '_3Uu1_')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element(By.XPATH, "//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(3)

bot = WhatsAppBot()
bot.EnviarMensagens()