# Create a WebDriver instance (assuming you have installed the appropriate webdriver)
import sys
import os
# from DriverManager import DriverManager
# from FAContactUsPage import FAContactPage
# from Login import Login
from PageObject.DriverManager import DriverManager
from PageObject.FAContactPage import FAContactPage
from PageObject.Login import Login
from PageObject.commonPage import CommonPage

current_directory = os.path.dirname(os.path.abspath(__file__))
pageobject_path = os.path.join(current_directory, "..", "PageObject")
sys.path.append(pageobject_path)

def Run_Test_Case():
    driver_manager = DriverManager()
    driver_manager.start_driver()
    driver = driver_manager.get_driver()

    try:
        contact_page = FAContactPage(driver)
        common_page = CommonPage(driver)
        login_page = Login(driver)
        manageLocation_locator="(//*[contains(text(),'Manage Location')])[1]"
        common_page.navigate_to_site(driver,"https://www.brystonflooringcanada.ca/contact-us")
        returned_email = contact_page.submit_form(driver,"fc")
        login_page.user_Login_to_siteadmin(driver, )
        locationNumber, locationName = contact_page.get_location_details(driver,manageLocation_locator)
        login_page.user_Login_to_yodle(driver)
        login_page.validates_form_in_centermark(driver,locationNumber, locationName,returned_email,"FC")

    except Exception as e:
        print(str(e))

    finally:
        print("Lead Submittion and Verification Completed")
        driver_manager.quit_driver()

# Run the test case
Run_Test_Case()
















