from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time

#from DbConnector import DbConnector_test


class ClinicalInterventionCategory():
    def test(self):
        global driver
        global categoryName
        categoryName = "test852020"
        # To Launch Telemanage Application
    driver = webdriver.Chrome('P://IT Transformation -Automation//WPR//WPR//ChromeDriver2//chromedriver.exe')
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://qa-telemanage.cpstelepharmacy.com/")
    time.sleep(20)
    print(driver.title)
    print('Home Page Displays')

    #To add Category
    def addcategory(self):
        global driver
        global element
    time.sleep(20)
    driver.find_element_by_xpath("//img[@src='../../../assets/images/logo.png']").is_displayed()
    print("Displays")
    driver.find_element_by_xpath("(//span[contains(@class,'mat-button-wrapper')])[6]").click()
	
    driver.find_element_by_xpath("//button[contains(.,'Add New Category')]").click()
    time.sleep(5)
    driver.find_element_by_xpath("//input[contains(@id,'txtname')]").send_keys(categoryName)
    time.sleep(5)
    driver.find_element_by_xpath("//span[contains(@class,'mat-select-placeholder ng-tns-c16-11 ng-star-inserted')]").click()
    clinicaltype_element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//span[@class='mat-option-text'][contains(.,'Clinical Interventions')]")))
    time.sleep(5)
    driver.execute_script("arguments[0].click();", clinicaltype_element)
    time.sleep(5)
    driver.find_element_by_xpath("//span[@class='mat-button-wrapper'][contains(.,'OK')]").click()

    # To update Category
    def updatecategory(self):
        global driver

    driver.find_element_by_xpath("//mat-cell[contains(.,'Name: test852020')]").click()
    time.sleep(10)
    driver.find_element_by_xpath("//div[contains(@class,'mat-checkbox-inner-container')]").click()
    driver.find_element_by_xpath("//span[@class='mat-button-wrapper'][contains(.,'OK')]").click()
    print("Record updated Successfully")

    # # Verify created data in Database
    # def verifyCategoryInDatabase(self):
    #     print("c1"+c1)
    #     return DbConnector_test.verifyCategory(self,CategoryName)

    #To verify adding duplicate category
    def Verify_Dupulicate_values(self):
        global driver
        time.sleep(2)
        driver.find_element_by_xpath("//img[@src='../../../assets/images/logo.png']").is_displayed()
        print("Displays")
        driver.find_element_by_xpath("(//span[contains(@class,'mat-button-wrapper')])[6]").click()
        driver.find_element_by_xpath("//button[contains(.,'Add New Category')]").click()
        time.sleep(5)
        driver.find_element_by_xpath("//input[contains(@id,'txtname')]").send_keys("CategoryName")
        time.sleep(5)
        driver.find_element_by_xpath("//span[contains(@class,'mat-select-placeholder ng-tns-c16-11 ng-star-inserted')]").click()
        clinicaltype_element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//span[@class='mat-option-text'][contains(.,'Clinical Interventions')]")))
        driver.execute_script("arguments[0].click();", clinicaltype_element)
        time.sleep(5)
        driver.find_element_by_xpath("//span[@class='mat-button-wrapper'][contains(.,'OK')]").click()
        #warning_message=driver.find_element_by_xpath("//div[@class = 'cdk-overlay-pane']//span").text
       # print(warning_message)
        #return warning_message

        # To delete added Category
        def deletecategory(self):
            global driver
        driver.find_element_by_xpath("(//a[@mattooltip='Delete Clinical Intervention Category'])[40]").click()
        time.sleep(10)
        driver.find_element_by_xpath("//button[contains(.,'OK')]").click()
        print("Record deleted Successfully")


