from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome('P://IT Transformation -Automation//WPR//WPR//ChromeDriver//chromedriver.exe')
driver.implicitly_wait(3)
driver.maximize_window()
driver.get("https://qa-telemanage.cpstelepharmacy.com/")
time.sleep(10)
print(driver.title)
time.sleep(15)
driver.find_element_by_xpath("//img[@src='../../../assets/images/logo.png']").is_displayed()
# wait = WebDriverWait(driver, 15)
# menu_menu = wait.until(EC.presence_of_element_located(By.XPATH, "//img[@src='../../../assets/images/logo.png']"))
print("Displays")
print("Displays")

