from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time

PATH = "C:\Program Files (x86)\\chromedriver.exe"

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver= webdriver.Chrome(options=options)
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()

 #firstname
first_name=driver.find_element(By.ID,"firstName")
first_name.send_keys("user_first_name")
#Lastname
last_name=driver.find_element(By.ID,"lastName")
last_name.send_keys("user_last_name")
#email typing
email=driver.find_element(By.ID,"userEmail")
email.send_keys("user.email@gmail.com")
#gender
gender=driver.find_element(
    By.XPATH,"//label[@for='gender-radio-1']").click()
selected_gender=driver.find_element(
    By.XPATH,"//label[@for='gender-radio-1']").is_selected()


#phone number 
phone_number=driver.find_element(By.ID,"userNumber")
phone_number.send_keys("0712345678")

#date of birth
date_of_birth=driver.find_element(By.ID,"dateOfBirthInput").click()
month_of_birth=driver.find_element(By.XPATH,'//*[@id="dateOfBirth"]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/select/option[1]').click()
year_of_birth=driver.find_element(By.XPATH,'//*[@id="dateOfBirth"]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/select/option[101]').click()
day_of_birth=driver.find_element(By.XPATH,'//*[@id="dateOfBirth"]/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div[7]').click()

#subjects

subject=driver.find_element(By.XPATH,'//*[@id="subjectsInput"]')
subject.send_keys("Computer science")
subject.send_keys(Keys.RETURN)


#scroll down the page and wait
driver.execute_script("window.scrollTo(0, 500)") 
driver.implicitly_wait(5)

time.sleep(5)
class FromTest(unittest.TestCase):
    def setUp(self):
        self.browser=webdriver.Chrome()
        self.addCleanup(self.browser.quit)
#check if the title of the page is DEMOQA  
    def test_page_title(self):
        self.browser.get("https://demoqa.com/automation-practice-form")
        self.assertIn("DEMOQA",self.browser.title)
        
    
    #check if the first name field is present
    def test_presence_of_first_name_field(self):
        fn_field=self.browser.find_element(By.XPATH,'//*[@id="firstName"]')
        if len(fn_field !=0):
            print("element present")
        else:
            print("element no present")
        
    def test_if_the_gender_checkbox_is_present(self):
        check_box=self.browser.find_element(By.XPATH,"//label[@for='gender-radio-1']")
        if len(check_box!=0):
            pass
    
if __name__=="__main__":
    unittest.main()
        
