from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options



class DriverManager:
    def __init__(self):
        self.driver = None

    def start_driver(self):
        if not self.driver:
            ser = Service("C:\drivers\chromedriver.exe")
            self.driver = webdriver.Chrome(service=ser)
            chrome_options = Options()
            chrome_options.add_argument("--disable-http2")
            driver = webdriver.Chrome(options=chrome_options)

    def get_driver(self):
        return self.driver

    def quit_driver(self):
        if self.driver:
            self.driver.quit()
            self.driver = None