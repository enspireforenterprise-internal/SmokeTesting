import datetime
import time
from tkinter import BROWSE
from selenium.common.exceptions import WebDriverException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObject.commonPage import CommonPage


class FAContactPage:

    def __init__(self, driver):
        self.common_page = CommonPage(driver)

    def navigate_to_site(self, driver, url):

        try:
            driver.get(url)
            driver.maximize_window()
            print("Current URL:", driver.current_url)

            # Check if the current URL matches the provided URL
            if driver.current_url == url:
                print("URL is correct")
            else:
                print("URL is different from the provided URL")

            print("Site navigation successful")

        except WebDriverException as e:
            if "ERR_CONNECTION_TIMED_OUT" in str(e):
                print("Connection timed out. Please check your internet connection or the website URL.")
            else:
                print("An unexpected WebDriverException occurred:", str(e))

        except Exception as e:
            print("An unexpected error occurred:", str(e))

        finally:
            print("Navigation completed")

    # Example usage:
    # common_page = CommonPage()
    # common_page.navigate_to_site(driver, "https://www.perrysflooringamerica.com/")

    def submit_form(self, driver):
        # try:
        self.common_page.find_my_element((By.XPATH, "//button[@id='CookieConsent']")).click()
        self.common_page.find_my_element((By.LINK_TEXT,"Contact Us")).click()
        print("form page")
        #time.sleep(5)
        self.common_page.find_my_element((By.NAME, "FirstName")).send_keys("FA Test Lead")

        self.common_page.find_my_element((By.NAME, "LastName")).send_keys("CCA Please Ignore")

        self.common_page.find_my_element((By.XPATH, "//input[@placeholder='Enter your phone number']")).send_keys(
            "9056428161")
        formatted_date = self.common_page.get_current_date_monthday_year_format()
        # print(formatted_date)
        email_address = f"testleadfa{formatted_date}@ccapleaseignore.com"
        self.common_page.find_my_element((By.NAME, "EmailAddress")).send_keys(email_address)
        self.common_page.find_my_element((By.NAME, "PostalCode")).send_keys("99501")
        self.common_page.find_my_element((By.NAME, "OpportunityNotes")).send_keys("Test Lead")
        # print("last stpe ")
        send_button = self.common_page.find_my_element((By.XPATH, "//button[text()='Send Message']"))

        script = f"arguments[0].scrollIntoView({{behavior: 'auto', block: 'center'}});"
        driver.execute_script(script, send_button)
        time.sleep(1)
        send_button.click()
        print("form submitted")
        # time.sleep(10)
        # print("browser  close")
        try:
            WebDriverWait(driver, 10).until(
                EC.text_to_be_present_in_element((By.XPATH, "//h3/strong"), "THANK YOU")
            )
            print("Thank You message found")
        except Exception as e:
            print("Unable to find Thank You message:", e)
        return email_address

    def get_location_details(self, driver):
        time.sleep(5)
        self.common_page.find_my_element((By.XPATH, "(//*[contains(text(),'Manage Location')])[1]")).click()
        locationNumber = self.common_page.find_my_element(
            (By.XPATH, "//*[contains(text(),'Location Number')]/following-sibling::label")).text
        locationName = self.common_page.find_my_element(
            (By.XPATH, "//*[contains(text(),'Location Name')]/following-sibling::label")).text
        print(locationNumber)
        print(locationName)
        return locationNumber, locationName

    # Function to  validate the submitted form through email
    def validates_form_in_centermark(self, driver, LocNumber, LocName, returned_email_address):

        SearchBox = self.common_page.find_my_element((By.ID, "filterText"))
        SearchBox.send_keys(LocNumber)
        SearchBox.send_keys(Keys.ENTER)
        self.common_page.find_my_element((By.XPATH, f'//*[text()="{LocName}"]')).click()
        time.sleep(3)
        RecentEmails = driver.find_elements(By.XPATH, "//table[@id='contacts']/tbody/tr/td[3]/span")
        for RecentEmail in RecentEmails:
            email_text = RecentEmail.text
            print(email_text)
            # count=0
            # print(email_text)
            if returned_email_address in email_text:
                print("Email Found in Yodle", returned_email_address)
                # count+=1
                driver.get_screenshot_as_file("Leads.png")
                break




