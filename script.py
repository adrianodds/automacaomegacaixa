from selenium import webdriver
from time import sleep
import openpyxl

mega = openpyxl.load_workbook('mega.xlsx')
planilha = mega['Plan1']

cont = 2

class ChromeAuto:
    def __init__(self):
        self.driver_path = 'chromedriver'
        self.options = webdriver.ChromeOptions()
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )

    def acessa(self, site):
        self.chrome.get(site)

    def sair(self):
        self.chrome.quit()

    def clica_idade(self):
        try:
            btn_idade = self.chrome.find_element_by_id('botaosim')
            btn_idade.click()
        except:
            pass
    def clica_megasena(self):
        try:
            btn_mega = self.chrome.find_element_by_xpath('/html/body/div[3]/div/ul[2]/li/div/a[2]')
            btn_mega .click()
        except:
            pass
    def clica_numero(self, numero):
        try:
            for i in numero:
                i = int(i) * 1
                if i < 10:
                    btn_numero = self.chrome.find_element_by_id('n0' + str(i))
                    btn_numero.click()
                    sleep(0.5)
                else:
                    btn_numero = self.chrome.find_element_by_id('n' + str(i))
                    btn_numero.click()
                    sleep(0.5)

        except:
            pass
    def carrinho(self):
        try:
            btn_carrinho = self.chrome.find_element_by_id('colocarnocarrinho')
            btn_carrinho.click()
            sleep(2)
            confirmar = self.chrome.find_element_by_id('confirmarModalConfirmacao')
            confirmar.click()
        except:
            pass

    def jogar(self, jogos):
        try:
            for a in jogos:
                numero = planilha[a].value
                b = numero.split(",")
                chrome.clica_numero(list(b))
                sleep(1.5)
                chrome.carrinho()

        except:
            pass

if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acessa('https://www.loteriasonline.caixa.gov.br/silce-web/?utm_source=site_caixa&utm_medium=home&utm_campaign=loteriasonline&utm_term=quina#/mega-sena')
    sleep(3)
    chrome.clica_idade()
    sleep(3)
    chrome.clica_megasena()
    sleep(3)

    while cont != 5:
        teste = ('C' + str(cont), 'D' + str(cont))
        chrome.jogar(list(teste))
        cont = cont + 1
