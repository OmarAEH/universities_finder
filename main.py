# Importing Necessary Libraries
import time
from selenium import webdriver

# Setting up Web Driver
driver = webdriver.Chrome("chromedriver.exe")  # Address of the Driver Executable


# Searches for Nearest University
def find_land():
    driver.get("https://www.google.com/maps")
    time.sleep(2)
    land = driver.find_element_by_class_name("tactile-searchbox-input")
    land.send_keys("university near me")
    find_button = driver.find_element_by_xpath('//*[@id="searchbox-searchbutton"]')
    find_button.click()


find_land()


# Gets a Route for the Nearest University
def nearest_route():
    time.sleep(7)

    routes = driver.find_element_by_xpath('//*[contains(@src,"ic_directions_gm_blue_24px.png")]')
    # '//*[@src="//maps.gstatic.com/consumer/images/icons/1x/ic_directions_gm_blue_24px.png"]'
    routes.click()


nearest_route()
