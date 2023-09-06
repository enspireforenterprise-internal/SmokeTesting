import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from DriverManager import DriverManager
from FAContactUsPage import FAContactPage

class Login():

    def __init__(self, driver):
         self.contact_page=FAContactPage(driver)

    def user_Login_to_siteadmin(self,driver):
            try:
                
                self.contact_page.find_my_element((By.XPATH,"//button[@id='CookieConsent']")).click()
                copyright_element = self.contact_page.find_my_element((By.XPATH, "//footer//*[contains(text(),'©')]"))
                time.sleep(1)
                copyright_element.click()
                self.contact_page.switch_to_tab_by_index(driver,1)
                credentials = self.contact_page.read_credentials_from_file("credentials.txt")
                email = credentials.get("email")
                password = credentials.get("password")
                print(email)
                print(password)
                email_field=self.contact_page.find_my_element((By.ID, "Email"))
                email_field.send_keys(email)
                # Press Tab to move to the next field
                email_field.send_keys(Keys.TAB)
                password_field=self.contact_page.find_my_element((By.ID,"Password"))
                password_field.send_keys(password)
                self.contact_page.find_my_element((By.XPATH,"//button[@type='submit']")).click()
            except KeyboardInterrupt:
                # Clean up or perform any necessary actions before exiting
                print("Program interrupted by keyboard.")
            finally:
                 print("logged in to siteadmin Successfully")
                 #driver.close()
    
    # Function to login to Centermark and validate the submitted form through email
    def user_Login_to_yodle(self, driver):
        try:
            self.contact_page.open_new_tab_and_focus("http://live.yodle.com/")
            print("Welcome to Yodle")

            # Rest of your code for logging in to Yodle
            credentials = self.contact_page.read_credentials_from_file("credentials.txt")
            email = credentials.get("email")
            password = credentials.get("password")
            print(email)
            print(password)
            email_field = self.contact_page.find_my_element((By.ID, "usernameForm"))
            email_field.send_keys(email)
            # Press Tab to move to the next field
            email_field.send_keys(Keys.TAB)
            password_field = self.contact_page.find_my_element((By.ID, "password"))
            password_field.send_keys(password)
            self.contact_page.find_my_element((By.NAME, "submit")).click()

        except Exception as e:
            if "ERR_CONNECTION_TIMED_OUT" in str(e):
                print("Connection timed out. Please check your internet connection or the website URL.")
            else:
                print("An unexpected exception occurred:", str(e))

            