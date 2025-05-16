from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class LoginPage:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.url = "http://exemplo.com/login"

    def open(self):
        self.driver.get(self.url)

    def fill_login(self, username, password):
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)

    def submit(self):
        self.driver.find_element(By.ID, "login").click()

    def is_logged_in(self):
        return "Página Inicial" in self.driver.page_source

    def close(self):
        self.driver.quit()

