# Importando o SELENIUM / para o navegador
from selenium import webdriver
# Referenciar os elementos por meio dos id's
from selenium.webdriver.common.by import By
# Utilizado para digitar direto no navegador
from selenium.webdriver.common.keys import Keys

#Imports panda / leitor de arquivos #
import pandas as pd
import time  # OBS: use o time caso o navegador seja rapido d+


# Abrir / ler aquivo Excel
class manipularArquivos:

    def __init__(self, arquivos):  # método construtor da class
        self.arquivo = arquivos

        self.url = "https://www.rpachallenge.com/."
        self.googleChrome = webdriver.Chrome(
            executable_path='pacotesUteis\chromedriver.exe')

    def abrir_site(self):
        # time.sleep(1)
        self.googleChrome.get(self.url)
        # time.sleep(1)

    def ler_arquivo(self):
        dados = pd.read_excel(self.arquivo)
        return dados

    def percorrer_planilha(self):
        d = self.ler_arquivo()

        # iniciar site
        self.abrir_site()
        # time.sleep(1)

        # btn START
        self.googleChrome.find_element(
            By.XPATH, "/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button").click()

        for index, row in d.iterrows():

            self.googleChrome.find_element(
                By.XPATH, "//label[text() = 'First Name']/following-sibling::input").send_keys(row["First Name"])
            self.googleChrome.find_element(
                By.XPATH, "//label[text() = 'Last Name']/following-sibling::input").send_keys(row["Last Name "])
            self.googleChrome.find_element(
                By.XPATH, "//label[text() = 'Company Name']/following-sibling::input").send_keys(row["Company Name"])
            self.googleChrome.find_element(
                By.XPATH, "//label[text() = 'Role in Company']/following-sibling::input").send_keys(row["Role in Company"])
            self.googleChrome.find_element(
                By.XPATH, "//label[text() = 'Address']/following-sibling::input").send_keys(row["Address"])
            self.googleChrome.find_element(
                By.XPATH, "//label[text() = 'Email']/following-sibling::input").send_keys(row["Email"])
            self.googleChrome.find_element(
                By.XPATH, "//label[text() = 'Phone Number']/following-sibling::input").send_keys(row["Phone Number"])

            # time.sleep(3)

            # Salvando output
            with open("arquivos\output_processo.dat", "a") as arq:
                print(f"{row['First Name'],row['Last Name '],row['Company Name'],row['Role in Company'],row['Address'],row['Email'],row['Phone Number'] }", file=arq)

            # btn SUBMIT
            self.googleChrome.find_element(
                By.XPATH, "/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input").click()

        self.googleChrome.quit
