import datetime
import os
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CommonPage:

    def __init__(self, driver):
        self.driver = driver

    def find_my_element(self, by_locator):
        element = WebDriverWait(self.driver, 10, 500).until(EC.presence_of_element_located(by_locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    def find_my_clickable_element(self, by_locator):
        element = WebDriverWait(self.driver, 10, 500).until(EC.element_to_be_clickable(by_locator))
        return element

    def get_current_date_monthday_year_format(self):
        current_date = datetime.datetime.now().strftime("%m%d%Y")
        return current_date

    def read_credentials_from_file(self, file_name):
        credentials = {}
        # Construct the path using a relative path, including the provided file_name
        current_directory = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_directory, '..', '..', 'SmokeTesting', file_name)
        with open(file_path, "r") as file:
            for line in file:
                key, value = line.strip().split(": ")
                credentials[key] = value
        print("Credentials:", credentials)  # Add this line for debugging
        return credentials

    def switch_to_tab_by_index(self, driver, index):
        new_tab = driver.window_handles[index]
        driver.switch_to.window(new_tab)

    def open_new_tab_and_focus(self, url):
        self.driver.execute_script("window.open('{}', '_blank');".format(url))  # Open URL in a new tab
        time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[-1])  # Switch to the newly opened tab