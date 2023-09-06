import datetime
import time
from tkinter import BROWSE
from selenium.common.exceptions import WebDriverException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class FAContactPage:
    def __init__(self,driver) :
        self.driver=driver
    
    def find_my_element(self, by_locator):
        element = WebDriverWait(self.driver, 10, 500).until(EC.presence_of_element_located(by_locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element
    
    def find_my_clickable_element(self, by_locator):
        element = WebDriverWait(self.driver, 10, 500).until(EC.element_to_be_clickable(by_locator))
        
        return element

    # Function to submit the form on the contact us page
    def Navigate_to_Site(self,driver,url):
            try:
                driver.get(url)
                driver.maximize_window()
                print(driver.title)
                Current_Url=driver.current_url
                print(Current_Url)
                if Current_Url==url:
                    print("URL is correct")
                else:
                    print("URL is redirecting")


                #self.find_my_element(By.LINK_TEXT,"Contact Us").click()
                print("url opened")
            except WebDriverException as e:
                if "ERR_CONNECTION_TIMED_OUT" in str(e):
                    print("Connection timed out. Please check your internet connection or the website URL.")
                else:
                    print("An unexpected WebDriverException occurred:", str(e))
            finally:
                print("2.url opened")
    

    def submit_form(self, driver):
        #try:
            print("form page")
            
            self.find_my_element((By.NAME,"FirstName")).send_keys("FA Test Lead")
                 
            self.find_my_element((By.NAME,"LastName")).send_keys("CCA Please Ignore")
    
            self.find_my_element((By.XPATH,"//input[@placeholder='Enter your phone number']")).send_keys("9056428161")
            formatted_date = self.get_current_date_monthday_year_format()
            #print(formatted_date)
            email_address= f"testleadfa{formatted_date}@ccapleaseignore.com"
            self.find_my_element((By.NAME,"EmailAddress")).send_keys(email_address)
            self.find_my_element((By.NAME,"PostalCode")).send_keys("99501")
            self.find_my_element((By.NAME,"OpportunityNotes")).send_keys("Test Lead")
           # print("last stpe ")
            send_button=self.find_my_element((By.XPATH,"//button[text()='Send Message']"))
          
            script = f"arguments[0].scrollIntoView({{behavior: 'auto', block: 'center'}});" 
            driver.execute_script(script, send_button)  
            time.sleep(1)
            send_button.click()
            print("form submitted")
            #time.sleep(10)        
            #print("browser  close")
            try:
                WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.XPATH, "//h3/strong"), "THANK YOU")
        )
                print("Thank You message found")
            except Exception as e:
                print("Unable to find Thank You message:", e)
            return email_address

    
    def get_current_date_monthday_year_format(self):
        current_date = datetime.datetime.now().strftime("%m%d%Y")
        return current_date
    
    def read_credentials_from_file(self,file_name):
        credentials = {}
        with open(file_name, "r") as file:
            for line in file:
                key, value = line.strip().split(": ")
                credentials[key] = value
        print("Credentials:", credentials)  # Add this line for debugging
        return credentials

    def switch_to_tab_by_index(self,driver, index):
        new_tab=driver.window_handles[index]
        driver.switch_to.window(new_tab)

    def get_location_details(self,driver):
        time.sleep(5)
        self.find_my_element((By.XPATH,"(//*[contains(text(),'Manage Location')])[1]")).click()
        locationNumber=self.find_my_element((By.XPATH,"//*[contains(text(),'Location Number')]/following-sibling::label")).text
        locationName=self.find_my_element((By.XPATH,"//*[contains(text(),'Location Name')]/following-sibling::label")).text
        print (locationNumber)
        print(locationName)
        return locationNumber , locationName
    
    
    # Function to  validate the submitted form through email
    def validates_form_in_centermark(self, driver,LocNumber,LocName, returned_email_address):
        
        SearchBox=self.find_my_element((By.ID,"filterText"))
        SearchBox.send_keys(LocNumber)
        SearchBox.send_keys(Keys.ENTER)
        self.find_my_element((By.XPATH,f"//*[text()='{LocName}']")).click()
        time.sleep(3)
        RecentEmails=driver.find_elements(By.XPATH,"//table[@id='contacts']/tbody/tr/td[3]/span")
        for RecentEmail in RecentEmails:
            email_text=RecentEmail.text
            print(email_text)
           # count=0
            #print(email_text)
            if returned_email_address in email_text:
                print("Email Found in Yodle", returned_email_address)
                #count+=1
                print(count)
                break

    def open_new_tab_and_focus(self, url):
        self.driver.execute_script("window.open('{}', '_blank');".format(url))  # Open URL in a new tab
        time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[-1])  # Switch to the newly opened tab

        
