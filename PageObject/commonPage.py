import datetime
import os
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException




class CommonPage:

    def __init__(self, driver):
        self.driver = driver

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

            #print("Site navigation successful")

        except WebDriverException as e:
            if "ERR_CONNECTION_TIMED_OUT" in str(e):
                print("Connection timed out. Please check your internet connection or the website URL.")
            else:
                print("An unexpected WebDriverException occurred:", str(e))

        except Exception as e:
            print("An unexpected error occurred:", str(e))

        finally:
            print("Navigation completed")

    def find_my_element(self, by_locator, offset=0):
        element = WebDriverWait(self.driver, 10, 500).until(EC.presence_of_element_located(by_locator))

        # Scroll into view with an offset
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", element)

        # If there's a need for an additional vertical offset
        self.driver.execute_script(f"window.scrollBy(0, {offset});")

        return element

    def find_my_elements(self, by_locator):
        elements = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(by_locator))
        for element in elements:
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return elements



    def find_my_clickable_element(self, by_locator):
        element = WebDriverWait(self.driver, 10, 500).until(EC.element_to_be_clickable(by_locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    def get_current_date_monthday_year_format(self):
        current_date = datetime.datetime.now().strftime("%m%d%Y")
        return current_date

    def read_credentials_from_file(self, file_name):
        credentials = {}
        # Construct the path using a relative path, including the provided file_name
        # current_directory = os.path.dirname(os.path.abspath(__file__))
        # file_path = os.path.join(current_directory, file_name)
        # Navigate up one level from the script's directory
        current_directory = os.path.dirname(os.path.abspath(__file__))
        project_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
        file_path = os.path.join(project_directory, file_name)
        #print("File path:", file_path)
        with open(file_path, "r") as file:
            for line in file:
                key, value = line.strip().split(": ")
                credentials[key] = value
        #print("Credentials:", credentials)  # Add this line for debugging
        return credentials

    def switch_to_tab_by_index(self, driver, index):
        new_tab = driver.window_handles[index]
        driver.switch_to.window(new_tab)

    def open_new_tab_and_focus(self, url):
        self.driver.execute_script("window.open('{}', '_blank');".format(url))  # Open URL in a new tab
        time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[-1])  # Switch to the newly opened tab

    def click_my_element(self,by_locator):
        self.find_my_element(by_locator).click()

    def execute_script_and_click(self, locator, script):
        # Use JavaScript to execute the specified script
        self.driver.execute_script(script)

        # Wait for a moment to ensure the script execution is complete (adjust sleep duration if needed)
        time.sleep(1)

        # Click the element after executing the script
        self.click_my_element(locator)

