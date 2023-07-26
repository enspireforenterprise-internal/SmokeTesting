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
        element = WebDriverWait(self.driver, 10, 500).until(EC.visibility_of_element_located(by_locator))
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


                #driver.find_element(By.LINK_TEXT,"Contact Us").click()
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
            
            self.find_my_element((By.NAME,"FirstName")).send_keys("Test Lead")
         
          #  driver.find_element(By.NAME,"FirstName").send_keys("Test Lead")
         
            driver.find_element(By.NAME,"LastName").send_keys("CCA Please Ignore")
            driver.find_element(By.XPATH,"//*[text()='Call Me']")
            driver.find_element(By.XPATH,"//button[text()='Email Me']")
            driver.find_element(By.XPATH,"//input[@placeholder='Enter your phone number']").send_keys("9056428161")
            driver.find_element(By.NAME,"EmailAddress").send_keys("testleadfa07252023@ccapleaseignore.com")
            driver.find_element(By.NAME,"PostalCode").send_keys("99501")
           # driver.find_element(By.XPATH,"//label[text()='My Preferred Store']//following-sibling::div/input[@name='MyStore']")
            driver.find_element(By.NAME,"OpportunityNotes").send_keys("Test Lead")
            print("last stpe ")
            # scroll_distance = 800  # Adjust the value based on how much you want to scroll
            # driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
            send_button=driver.find_element(By.XPATH,"//button[text()='Send Message']")
            # driver.execute_script("arguments[0].scrollIntoView();", send_button)
            #wait = WebDriverWait(driver, 10)  # Maximum wait time of 10 seconds
           # element_to_scroll = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Send Message']")))
            script = f"arguments[0].scrollIntoView({{behavior: 'auto', block: 'center'}});" 
            driver.execute_script(script, send_button)
    # Step 4: Scroll to the element using JavaScript
            #driver.execute_script("arguments[0].scrollIntoView();", element_to_scroll)
            time.sleep(5)
            send_button.click()
            time.sleep(5)
            print("form submitted")
            # time.sleep(10)
        
        #     print(e)
        #     print("2.Program interrupted by user.")
        # try:
            #CSS selector
            message=driver.find_element(By.XPATH,"//section[@class='section-header   ']//h3/strong").text        
            print(message)
            time.sleep(10)
            assert "THANK YOU" in message
            # #driver.close()
            print("passed")
            time.sleep(5)
            driver.find_element(By.LINK_TEXT, "Book Appointment")
        # except Exception as e:
        #     print(e)
        #     print("3.Program interrupted by user.")
        # finally:
            #self.driver.quit()
            print("browser  close")

