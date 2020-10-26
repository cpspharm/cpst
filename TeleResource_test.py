from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time

#from DbConnector import DbConnector_test

class TeleResource_test():
    def test(self):
        global driver
        #global categoryName
        #categoryName = "test852020"
        # To Launch Telemanage Application
    driver = webdriver.Chrome('P://IT Transformation -Automation//WPR//WPR//ChromeDriver2//chromedriver.exe')
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://qa-telemanage.cpstelepharmacy.com/")
    time.sleep(20)
    print(driver.title)
    print('Home Page Displays')


    # Tele resource
    def addcategory(self):
        global driver
        global element
    time.sleep(20)
    #driver.find_element_by_xpath("//img[@src='../../../assets/images/logo.png']").is_displayed()
    #print("Displays")
    #driver.find_element_by_xpath("(//span[contains(@class,'mat-button-wrapper')])[11]").click()
    #driver.find_element_by_xpath("//button[contains(.,'TeleResource')]").click()
    #driver.find_element_by_xpath("//button[contains(@id,'btnManageResource')]").click()
    driver.find_element_by_xpath("//span[@class='mat-button-wrapper'][contains(.,'TeleResource')]").click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("///span[contains(.,'Manage Resources')]").click()




