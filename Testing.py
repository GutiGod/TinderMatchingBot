from selenium import webdriver
from time import sleep

from logindata import username, password

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://tinder.com/')        
        sleep(5)
        fblogin = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/div[2]/button')
        fblogin.click()
        basetinder = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])
        usernamebtn = self.driver.find_element_by_xpath('//*[@id="email"]')
        usernamebtn.send_keys(username)
        passbtn = self.driver.find_element_by_xpath('//*[@id="pass"]')
        passbtn.send_keys(password)
        logined = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        logined.click() 
        self.driver.switch_to_window(basetinder)
        sleep(4)
        allowlocation= self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        allowlocation.click()
        sleep(2)
        allownotifs = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        allownotifs.click()
        sleep(2)

    def like(self):
        while True:
            try:
                sleep (1)
                likebtn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]')
                likebtn.click()
            except:
                try:
                    popupbtn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
                    popupbtn.click()
                except:
                    try:    
                        matchbtn = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
                        matchbtn.click()
                    except:
                        break    

bot = TinderBot()
bot.login()
bot.like()

