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


def Run_Test_Case():
    driver_manager = DriverManager()
    driver_manager.start_driver()
    driver = driver_manager.get_driver()

    try:
        common_page = CommonPage(driver)
        contact_page = FAContactPage(driver)
        login_page = Login(driver)
        manageLocation_locator="(//*[contains(text(),'Manage Location')])[1]"
        common_page.navigate_to_site(driver,"https://www.perrysflooringamerica.com/contact-us")
        returned_email = contact_page.submit_form(driver,"fa1")
        login_page.user_Login_to_siteadmin(driver, "https://www.perrysflooringamerica.com/")
        locationNumber, locationName = contact_page.get_location_details(driver,manageLocation_locator)
        login_page.user_Login_to_yodle(driver)
        login_page.validates_form_in_centermark(driver,locationNumber, locationName,returned_email)
    except Exception as e:
        print(str(e))

    finally:
        print("done")
        driver_manager.quit_driver()

# Run the test case
Run_Test_Case()
















