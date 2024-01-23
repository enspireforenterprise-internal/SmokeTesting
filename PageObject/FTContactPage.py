import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from PageObject.commonPage import CommonPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException



class FTContactPage:

    def __init__(self, driver):
        self.common_page = CommonPage(driver)

    def submit_Quote_form(self, driver):
        email_address = "testleadft01032023@ccapleaseignore.com"
        try:
            formatted_date = self.common_page.get_current_date_monthday_year_format()
            email_address = f"testleadft{formatted_date}@ccapleaseignore.com"
            expected_message = "Thank You"
            print("form page")
            self.common_page.find_my_element((By.XPATH,'//a[contains(text(),"Request a Quote")]')).click()
            time.sleep(5)
            current_Url=driver.current_url
            print(current_Url)
            if "/request-quote" in current_Url:
                # popup_box=self.common_page.find_my_element((By.XPATH,'//*[@id="mozmess-Popup"]'))
                # if self.common_page.find_my_element((By.XPATH,'//*[@id="mozmess-Popup"]')):
                # popup_Contact = self.common_page.find_my_element((By.XPATH, '//*[@id ="mozmess-launcher"]'))

                # popup_Contact=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id ="mozmess-launcher"]')))
                # if self.common_page.find_my_element((By.XPATH, '//*[@id ="mozmess-launcher"]')).is_displayed():
                # if popup_Contact.is_displayed():
                # popup_Contact = self.common_page.find_my_element((By.XPATH, '//*[@id ="mozmess-launcher"]'))
                self.common_page.find_my_clickable_element((By.NAME, "FirstName")).send_keys("Test Lead")
                self.common_page.find_my_element((By.NAME, "LastName")).send_keys("CCA Please Ignore")
                self.common_page.find_my_element((By.NAME, "CleanHomePhone")).send_keys("9056428161")
                # print(formatted_date)
                self.common_page.find_my_element((By.NAME, "EmailAddress")).send_keys(email_address)
                self.common_page.find_my_element((By.NAME, "PostalCode")).send_keys("99501")
                self.common_page.find_my_element((By.NAME, "OpportunityNotes")).send_keys("Test Lead")
                # dropdown_element = self.common_page.find_my_clickable_element((By.ID, "contactPreferredLocation"))
                # if dropdown_element:
                #     # dropdown_element = self.common_page.find_my_clickable_element((By.ID, "contactPreferredLocation"))
                #     dropdown = Select(dropdown_element)
                #     dropdown.select_by_index(1)
                #     self.common_page.find_my_element(
                #         (By.XPATH, "//*[@value='Request a Quote']")).click()  # //button[text()='Send Message']
                #     print("form submitted")
                # else:
                #     print("Dropdown element not found for this location. Skipping.")
                self.common_page.find_my_element((By.XPATH, "//*[@value='Request a Quote']")).click()  # //button[text()='Send Message']
                print("form submitted")
                time.sleep(3)
                try:
                    actual_message = driver.title
                    print(actual_message)
                    assert expected_message.lower() in actual_message.lower(), f"Expected '{expected_message}' not found in '{actual_message}'"
                    print("Assertion passed: Success message is displayed.")
                except AssertionError:
                    print("Assertion failed: Success message is not displayed.")

            else:
                iframe_locator = (By.ID, "moz-frame")
                print("Before switching to iframe")
                iframe_element = WebDriverWait(driver, 100).until(EC.visibility_of_element_located(iframe_locator))
                print("Switching to iframe")
                # driver.switch_to.frame(iframe_locator)

                driver.switch_to.frame(iframe_element)
                print("After switching to iframe")
                # time.sleep(5)
                print("enter to framess")
                self.common_page.find_my_element((By.XPATH, '//button[text()="Email Us"]')).click()
                # self.common_page.find_my_clickable_element((By.XPATH,'// *[ @ id = "mozmess-launcher"]')).click()
                self.common_page.find_my_clickable_element((By.XPATH,
                                                            '//*[@id="km-UYRasdduyp"]//label[text()="First Name"]/following-sibling::input')).send_keys(
                    "Test Lead")
                self.common_page.find_my_clickable_element((By.XPATH,
                                                            '//*[@id="km-UYRasdduyp"]//label[text()="Last Name"]/following-sibling::input')).send_keys(
                    "CCA Please Ignore")
                self.common_page.find_my_clickable_element(
                    (By.XPATH, '//*[@id="km-UYRasdduyp"]//label[text()="Email"]/following-sibling::input')).send_keys(
                    email_address)
                self.common_page.find_my_clickable_element(
                    (By.XPATH, '//*[@id="km-UYRasdduyp"]//label[text()="Message"]/following-sibling::input')).send_keys(
                    "Test Lead")
                self.common_page.find_my_element((By.XPATH, '//*[@id="km-UYRasdduyp"]/button')).click()
                # time.sleep(5)
                try:

                    popup_message = WebDriverWait(driver, 180).until(
                        EC.visibility_of_element_located((By.XPATH, "//*[@class='modal-content']/p")))
                    # actual_message=self.common_page.find_my_element((By.XPATH,"//*[@class='modal-content']/p")).text
                    actual_message = popup_message.text
                    print(actual_message)
                    assert expected_message.lower() in actual_message.lower(), f"Expected '{expected_message}' found '{actual_message}'"
                    print("Assertion passed: Success message is displayed.")
                    time.sleep(10)
                except AssertionError as e:
                    print(f"An error occurred: {e}")
                finally:
                    driver.switch_to.default_content()
        except WebDriverException as e:
                    error_message = str(e)
                    if 'ERR_HTTP2_PROTOCOL_ERROR' in error_message:
                        print(f"An HTTP/2 protocol error occurred: {error_message}")
                    else:
                        print(f"An exception occurred: {error_message}")

                    print("Closing the execution.")
        return email_address
