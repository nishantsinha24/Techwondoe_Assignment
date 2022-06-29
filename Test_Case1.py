import password as password
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
class access_github:
    def __init__(self,user,password):
        self.user = user
        self.password = password

    def login(self):
        driver.get("https://github.com/login")
        username = driver.find_element(By.NAME, "login")
        password = driver.find_element(By.NAME, "password")
        signin = driver.find_element(By.NAME, "commit")
        username.send_keys("nishantsinha1024@gmail.com")
        password.send_keys("Nishant@2410")
        signin.click()
        driver.implicitly_wait(3)
        time.sleep(5)
    def click_menu(self):
        menu = driver.find_element(By.XPATH, "//summary[@aria-label='View profile and more']")
        menu.click()
        time.sleep(5)
    def view_profile(self):
        profile = driver.find_element(By.LINK_TEXT, "Your profile")
        profile.click()
        time.sleep(5)
    def logout(self):
        logout = driver.find_element(By.XPATH, "//button[@class=’dropdown-item dropdown-signout’]")
        logout.click()

usr= "nishnatsinha1024@gmail.com"
pwd= "Nishant@2410"
start = access_github(usr,pwd)

start.login()
start.click_menu()
start.view_profile()
start.click_menu()
start.logout()
