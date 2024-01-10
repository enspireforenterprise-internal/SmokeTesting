import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from PageObject.commonPage import CommonPage
from datetime import datetime


class Login():

    def __init__(self, driver):
        self.common_page = CommonPage(driver)

    def get_current_date(self):
        return datetime.now().strftime("%m/%d/%Y")

    def user_Login_to_siteadmin(self, driver, url):
        try:

            # self.common_page.find_my_element((By.XPATH, "//button[@id='CookieConsent']")).click()
            # copyright_element = self.common_page.find_my_element((By.XPATH, "//footer//*[contains(text(),'©')]"))
            # time.sleep(1)
            # copyright_element.click()
            # current_url = driver.current_url
            new_url = url + '/siteadmin'
            print("navigating to siteadmin")
            driver.get(new_url)
            print("have to read cred")
            # self.common_page.switch_to_tab_by_index(driver, 1)
            credentials = self.common_page.read_credentials_from_file("credentials.txt")
            email = credentials.get("email")
            pw = credentials.get("password")
            print(email)
            print(pw)
            email_field = self.common_page.find_my_element((By.ID, "Email"))
            email_field.send_keys(email)
            # Press Tab to move to the next field
            email_field.send_keys(Keys.TAB)
            password_field = self.common_page.find_my_element((By.ID, "Password"))
            password_field.send_keys(pw)
            print(pw)
            self.common_page.find_my_element((By.XPATH, "//*[@type='submit']")).click()
        except KeyboardInterrupt:
            # Clean up or perform any necessary actions before exiting
            print("Program interrupted by keyboard.")
        finally:
            print("logged in to siteadmin Successfully")
            # driver.close()

    # Function to login to Centermark and validate the submitted form through email
    def user_Login_to_yodle(self, driver):
        try:
            self.common_page.open_new_tab_and_focus("http://live.yodle.com/")
            print("Welcome to Yodle")

            # Rest of your code for logging in to Yodle
            credentials = self.common_page.read_credentials_from_file("YLcredentials.txt")
            email = credentials.get("email")
            password = credentials.get("password")
            print(email)
            print(password)
            email_field = self.common_page.find_my_element((By.ID, "usernameForm"))
            email_field.send_keys(email)
            # Press Tab to move to the next field
            email_field.send_keys(Keys.TAB)
            password_field = self.common_page.find_my_element((By.ID, "password"))
            password_field.send_keys(password)
            self.common_page.find_my_element((By.NAME, "submit")).click()

        except Exception as e:
            if "ERR_CONNECTION_TIMED_OUT" in str(e):
                print("Connection timed out. Please check your internet connection or the website URL.")
            else:
                print("An unexpected exception occurred:", str(e))

        # Function to  validate the submitted form through email

    def validates_form_in_centermark(self, driver, LocNumber, LocName, returned_email_address):

        SearchBox = self.common_page.find_my_element((By.ID, "filterText"))
        SearchBox.send_keys(LocNumber)
        SearchBox.send_keys(Keys.ENTER)
        search_result_element = self.common_page.find_my_element(
            (By.XPATH, '//table[@class="dataGrid"]/tbody/tr/td[2]/a'))
        # self.common_page.find_my_element((By.XPATH, f'//*[text()="{LocName}"]')).click()
        # time.sleep(3)
        if LocName in search_result_element.text:
            # search_result_text=search_result_element.text
            search_result_element.click()
            time.sleep(3)
            RecentEmails = driver.find_elements(By.XPATH, "//table[@id='contacts']/tbody/tr/td[3]/span")
            for RecentEmail in RecentEmails:
                email_text = RecentEmail.text
                print(email_text)
                if returned_email_address in email_text:
                    print("Email Found in Yodle", returned_email_address)
                    driver.get_screenshot_as_file("YL_Leads.png")
                    break

    def validates_form_in_site_admin(self, driver, email_address):
        # No CASH option https: // www.floortraderbaltimore.com / siteadmin / home
        # self.common_page.click_my_element((By.XPATH,"//text()[contains(., 'Customer Management')]/following-sibling::a[contains(., 'Edit Now')]"))
        global current_date
        self.common_page.click_my_element(
            (By.XPATH, "//text()[contains(., 'CASH')]/following-sibling::a[contains(., 'Edit Now')]"))

        self.common_page.find_my_clickable_element((By.XPATH, '//*[@id="users"]'))
        options = self.common_page.find_my_elements((By.XPATH, '//*[@id="users"]/option'))

        if len(options) > 1:
            select = Select(self.common_page.find_my_element((By.ID, "users")))
            select.select_by_index(1)
            selected_option = select.first_selected_option
            selected_option.click()
            self.common_page.find_my_element((By.ID, "cashGo")).click()
            time.sleep(5)
            self.common_page.find_my_element((By.XPATH, '//*[@data-title="Customer"]'),0).click()

            self.common_page.find_my_element((By.XPATH, '//*[contains(text(),"All Projects / Opportunities")]'),0).click()
            current_date = self.get_current_date()
            print("Current Date:", current_date)
            # rows = driver.find_elements(By.XPATH, "//*[@id='json_data']/tr/td[1]")
            # for row in rows:
            #     row_content = row.text
            #     if email_address in row_content:
            #         print("Element found in CASH", row_content)
            #         driver.get_screenshot_as_file("CASH_Leads.png")
            #         break

            rows = driver.find_elements(By.XPATH, "//*[@id='json_data']/tr")

            for row in rows:
                date_content = row.find_element(By.XPATH, "./td[1]").text
                test_lead_content = row.find_element(By.XPATH, "./td[5]").text

                if current_date in date_content and "Test Lead" in test_lead_content:
                    print("Element found in CASH", date_content, test_lead_content)
                    driver.get_screenshot_as_file("CASH_Leads.png")
                    break

        else:
            print("No CASH user exists in the dropdown.")
