from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as CondicaoEsperada 
from selenium.common.exceptions import * 
from selenium.webdriver import ActionChains 
from selenium.webdriver.common.keys import Keys 
import time 
import random 




class AutoSafeone: 
    def __init__(self):
        
        
        options = webdriver.ChromeOptions()
        options.add_argument("lang=pt-BR") 
        self.driver = webdriver.Chrome() 
        self.wait = WebDriverWait( 
            self.driver,
            10, 
            poll_frequency=1,
            ignored_exceptions=[
                NoSuchElementException,
                ElementNotVisibleException,
                ElementNotSelectableException,
            ]
        )
        self.empresa = "safeone"
        self.email = "--"
        self.senha = "--"
        self.link_safeone = "https://www.mysafeone.com/v2/client/login"
    
    def Start(self):
        self.driver.get(self.link_safeone) #
        self.LoginSafeone()
        self.SolicitarLinkFirstMaq()
        self.GerarRelatorios()

    def LoginSafeone(self):
        print("Preenchendo os dados e fazendo login")
        campo_empresa = self.wait.until(CondicaoEsperada.element_to_be_clickable((By.XPATH,'//input[@placeholder = "minhaempresa"]')))    
        campo_email = self.wait.until(CondicaoEsperada.element_to_be_clickable((By.XPATH,'//input[@name="email"]')))
        campo_senha = self.wait.until(CondicaoEsperada.element_to_be_clickable((By.XPATH,'//input[@name="password"]')))   
    
        campo_empresa.clear()
        campo_empresa.send_keys(self.empresa)
        time.sleep(1/30)
        campo_email.clear()
        campo_email.send_keys(self.email)
        time.sleep(1/30)
        campo_senha.clear()
        campo_senha.send_keys(self.senha)
        time.sleep(1/30)

        #como o botao de login só fica clicavel apos a entrada dos dados acima, a verificação usando o xpath do botao deve seguir abaixo

        botao_login = self.wait.until(CondicaoEsperada.element_to_be_clickable(
            (By.XPATH,'//button[@type="submit"]')))
        botao_login.click()    

    def SolicitarLinkFirstMaq(self):
        print("INSTRUÇÃO: COPIE O LINK DA PRIMEIRA MÁQUINA DA LISTA DE MÁQUINAS QUE DESEJA BAIXAR\n") 
       
        self.link_first_maq = input("Cole o Link abaixo:\n")

        self.driver.get(self.link_first_maq) 

    def GerarRelatorios(self):
        
        
            #aguarda entrar na tela da primeira máquina e em seguida clica no botão relatório apreciação de risco
            botao_apreciacao = self.wait.until(CondicaoEsperada.element_to_be_clickable((By.XPATH,'//span[text()="Relatório Apreciação de Risco"]')))
            botao_apreciacao.click()

            #aguarda o botão de confirmar o tipo de relatorio estar ativo e em seguida clica no mesmo
            botao_confirmar = self.wait.until(CondicaoEsperada.element_to_be_clickable((By.XPATH,'//span[text()="Confirmar"]')))
            botao_confirmar.click()

            time.sleep(1/5)
            
            #necessario subir uma pagina para clicar no botao next
            referencia_pageup = self.wait.until(CondicaoEsperada.visibility_of_element_located((By.XPATH,'//div[@class="d-flex col-sm-12"]/div[1]/a')))
            referencia_pageup.send_keys(Keys.PAGE_UP) 
            
            #aguarda o botao next estar ativo apos gerar o relatorio e vai para a prox maquina
            time.sleep(1)

            botao_next = self.wait.until(CondicaoEsperada.element_to_be_clickable((By.XPATH,'//button[@id="machine-nav-next"]')))
            botao_next.click() 

            #caso n ocorra nenhuma excessao nesse bloco do codigo, o processo reinicia ate baixar todas as maquinas 
            if botao_next is not None:
                print("Indo para a proxima pagina")
                self.GerarRelatorios()

bot = AutoSafeone()
bot.Start()