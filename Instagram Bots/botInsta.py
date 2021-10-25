
from selenium import webdriver
import time
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import os
from os import path
from pathlib import Path

home = Path.home()

main_folder = path.join(path.expanduser("~"), r"AppData\Local\Mozilla Firefox\firefox.exe")

options = Options()

#r"C:\Users\gabri\AppData\Local\Mozilla Firefox\firefox.exe"
options.binary_location = main_folder



##=============================================================================================================



class instaBot():
    def __init__(self, user, password):
        self.driver = webdriver.Firefox(options=options,executable_path=r"geckodriver.exe")
        self.user = user
        self.password = password


    def login (self):
        driver = self.driver
        self.driver.get('https://www.instagram.com')
        time.sleep(2)
        #placeholder da tela de login
        # //input[@name='username']
        #//input[@name='password']
        pH_userElementUsername = driver.find_element_by_xpath("//input[@name='username']")
        pH_userElementUsername.clear()
        pH_userElementUsername.send_keys(self.user)
        ph_userElementPassword = driver.find_element_by_xpath("//input[@name='password']")
        ph_userElementPassword.clear()
        ph_userElementPassword.send_keys(self.password)
        ph_userElementPassword.send_keys(Keys.RETURN)
        time.sleep(5)


    def startByUser(self,userAsk):
        self.getPageByUser(userAsk)


    def startByTag (self,tagg):
        self.getPageByTag(tagg)
        

    def acces(self,link):
        self.driver.get(link)
        time.sleep(3)


    def getPageByUser (self, userAsk):
        driver = self.driver
        
        driver.get('https://www.instagram.com/'+userAsk+'/')
        time.sleep(5)
        self.getLinksPub()
        time.sleep(3)


    def getPageByTag (self,hashtag):
        driver= self.driver
        
        driver.get('https://www.instagram.com/explore/tags/'+hashtag+'/')
        time.sleep(5)
        self.getLinksPub()
        time.sleep(3)


    def getLinksPub(self):
        driver= self.driver
        self.scrollPage(3)
        time.sleep(3)
        tagAs = driver.find_elements_by_tag_name('a')
        allLinks = []
        for tagA in tagAs:
            href = tagA.get_attribute("href")  
            if (href.startswith("https://www.instagram.com/p/")):
                allLinks.append(href)
        if len(allLinks)<=39 :
            for i in range(0,5):
                self.scrollPage(3)
                time.sleep(3)
                tagAs = driver.find_elements_by_tag_name('a')
            for tagA in tagAs:
                href = tagA.get_attribute("href")  
            if (href.startswith("https://www.instagram.com/p/")):
                allLinks.append(href)

        os.system('cls')
        print(f'elementos encontrados: {len(allLinks)}')
        return allLinks


    def like(self):
        driver = self.driver
        blike = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button')
        blike.click()
        

    def scrollPage(self, roll):
        driver = self.driver
        for i in range(1, int(roll)):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
        


    def comment(self, coment):
        driver = self.driver
        textArea = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/textarea')
        textArea.click()
        time.sleep(1)
        textArea = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/textarea')
        textArea.clear()
        time.sleep(1)
        textArea.send_keys(coment)
        time.sleep(1)
        send_buttom = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/button[2]')
        send_buttom.click()


    def actions (self, comentarioP, like= True, comment= True):
        links = self.getLinksPub()
        counter = 0
        for link in links:
            self.acces(link)
            if like:
                self.like()
            time.sleep(1)
            if comment:
                self.comment(comentarioP)
            counter = counter+1
            os.system('cls')
            print("\n\n\n\n")
            print(f'Publicações curtidas e comentadas: {counter} de {len(links)} publicações encontradas.')
            print("\n\n")
            print("Bot em Execução....\n")
            print("[ ! ] Use 'ctrl + c' no terminal para parar o bot.\n")
            print("Problemas no bot? contate o desenvolvedor: (85)9 9256-6393\n")
            print("Versão: Free Beta 1.1.0")

            if counter == len(links):
                print(f"O bot já curtiu e comentou todas as {len(links)} publicações encontradas. ")
                print("Bot encerrado!. Reinicie")
                print("\n\n\n\n")
                print("[ ! ] Use 'ctrl + c' no terminal para parar o bot.\n")
                print("Problemas no bot? contate o desenvolvedor: (85)9 9256-6393\n")
                print("Versão: Free Beta 1.1.0")

            time.sleep(15)
       

#========================================================================================================================


def main():
    print("\n\n\n\n")
    print("Iniciando o bot!.... Por favor aguarde...")
    time.sleep(2)
    os.system('cls')
    print("\n\n\n\n")
    print("INSTABOT")
    print('By Gabriel R. Michaliszën')
    time.sleep(3)
    os.system('cls')
    print("\n\n\n\n")
    login_usernmae = str(input("Digite o seu usuário: "))
    login_password = str(input("Digite a sua senha: "))
    os.system('cls')


    def hidenPass(password):
        tamanho = int(len(password))
        hidenPassword = ""
        for i in range (0, tamanho):
            hidenPassword = hidenPassword+"*"
        return hidenPassword
         

    print("\n\n\n\n")
    print(f"Usuário: {login_usernmae}")
    print(f"Senha: {hidenPass(login_password)}")
    time.sleep(2)
    print("Carregando...")
    time.sleep(2)
    os.system('cls')
    print("\n\n\n\n")

    userORtag = str(input("Você deseja buscar por [usuario] ou [hashtag]: "))
    
    print('Carregando....')
    time.sleep(2)

    if userORtag == ('hashtag'):
        tag = str(input("Digite a #(hashtag) que você deseja: "))
        
    if userORtag == ('usuario'):
        user = str(input("Digite o usuário desejado: "))
        
    comentario = str(input("Digite o comentário padrão para os posts: "))

    
    
    print("Iniciando....")
    time.sleep(3)
    os.system('cls')

    print("\n\n\n\n")
    print("Bot em Execução....\n")
    print("[ ! ] Use 'ctrl + c' no terminal para parar o bot.\n")
    print("Problemas no bot? contate o desenvolvedor: (85)9 9256-6393\n")
    print("Versão: Free Beta 1.1.0")



    bot = instaBot(login_usernmae,login_password)
    bot.login()

    if userORtag == 'hashtag':
        bot.startByTag(tag)
    if userORtag == 'usuario':
        bot.startByUser(user)

    bot.actions(comentario)
    

if __name__ == "__main__":
    main()
