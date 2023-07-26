# Create a WebDriver instance (assuming you have installed the appropriate webdriver)
import sys
import os
from DriverManager import DriverManager
from FAContactUsPage import FAContactPage

current_directory = os.path.dirname(os.path.abspath(__file__))
pageobject_path = os.path.join(current_directory, "..", "PageObject")
sys.path.append(pageobject_path)

def run_test_case():
    driver_manager = DriverManager()
    driver_manager.start_driver()
    driver = driver_manager.get_driver()

    try:
        contact_page = FAContactPage(driver)
        contact_page.Navigate_to_Site(driver,"https://www.caseycarpetoflascruces.com/contact-us")
        contact_page.submit_form(driver) 
    except Exception as e:
        print(str(e)) 

    finally:
        print("done")
        #driver_manager.quit_driver()

# Run the test case
run_test_case()















