import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PageObject.commonPage import CommonPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class FAContactPage:

    def __init__(self, driver):
        self.common_page = CommonPage(driver)

    def submit_form(self, driver, brand_name, cookieConsent=True):  # ,
        # try:

        # try:
        #     self.common_page.find_my_element((By.XPATH,'//a[contains(text(),"Contact Us")]')).click()
        # except Exception as e:
        #     print(str(e))
        if cookieConsent:
            self.common_page.find_my_element((By.XPATH, "//button[@id='CookieConsent']")).click()

        time.sleep(5)
        self.common_page.find_my_element((By.NAME, "FirstName")).send_keys("Test Lead")

        self.common_page.find_my_element((By.NAME, "LastName")).send_keys("CCA Please Ignore")

        self.common_page.find_my_element((By.NAME, "CleanHomePhone")).send_keys("9056428161")
        formatted_date = self.common_page.get_current_date_monthday_year_format()
        # print(formatted_date)
        email_address = f"testlead{brand_name}{formatted_date}@ccapleaseignore.com"
        self.common_page.find_my_element((By.NAME, "EmailAddress")).send_keys(email_address)
        self.common_page.find_my_element((By.NAME, "PostalCode")).send_keys("99501")
        self.common_page.find_my_element((By.NAME, "OpportunityNotes")).send_keys("Test Lead")
        # preferred_location=self.common_page.find_my_element((By.ID, "contactPreferredLocation"))
        # if preferred_location:
        #     select = Select(self.common_page.find_my_element((By.ID, "contactPreferredLocation")))
        #     select.select_by_index(1)
        # else:
        #     print("No Preferred Location field exists")
        send_button = self.common_page.find_my_element((By.XPATH, '//button[text()="Send Message"]'))
        script = f"arguments[0].scrollIntoView({{behavior: 'auto', block: 'center'}});"
        driver.execute_script(script, send_button)
        time.sleep(1)
        send_button.click()
        print("form submitted")
        time.sleep(3)
        try:
            expcected_title = "Thank You"
            actual_title = driver.title
            print("Page Tile:",actual_title)
            assert expcected_title in actual_title, f"Expected '{expcected_title}' in title, but found '{actual_title}'"
            print("Assertion passed: Success message is displayed.")
        except AssertionError:
            print("Assertion failed: Success message is not displayed.")

        # time.sleep(10)
        # print("browser  close")
        # try:
        #     WebDriverWait(driver, 10).until(
        #         EC.text_to_be_present_in_element((By.XPATH,"//*[contains(text(), 'Thank you')]"), "THANK YOU")      #"//h3/strong"
        #     )
        #     print("Thank You message found")
        # except Exception as e:
        #     print("Unable to find Thank You message:", e)
        return email_address

    def get_location_details(self, driver, location_locator):
        time.sleep(2)
        self.common_page.find_my_element((By.XPATH, location_locator)).click()
        locationNumber = self.common_page.find_my_element(
            (By.XPATH, "//*[contains(text(),'Location Number')]/following-sibling::label")).text
        locationName = self.common_page.find_my_element(
            (By.XPATH, "//*[contains(text(),'Name')]/following-sibling::label")).text
        partial_locName = locationName.split()[-1]

        print("Location Number:", locationNumber)
        print("Location Name:", locationName)
        driver.back()
        return locationNumber, partial_locName
