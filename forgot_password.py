from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://techbrain.ai/")
    return driver

def teardown(driver):
  
    driver.quit()
    
def sign_in():
    driver = setup()
    wait = WebDriverWait(driver,5)
    
    
    
   
    
    sign_in = driver.find_element(By.XPATH, "(//a[@href='/users/sign_in']/span)[1]")
    sign_in.click()
     
    forgot_pwd = wait.until(EC.element_to_be_clickable((By.XPATH,'(//a[@class="text-gray-500 text-sm"])[1]'))).click()
     
     
    time.sleep(3)
    
    
    enter_email =  wait.until(EC.presence_of_element_located((By.XPATH,'//input[@id="user_email"]')))
    enter_email.send_keys('a@endtest-mail.io')
    
    sub_btn = wait.until(EC.element_to_be_clickable((By.XPATH,'//input[@type="submit"]')))
    sub_btn.click()
    time.sleep(5)
    driver.get("https://app.endtest.io/mailbox?email=a@endtest-mail.io")
    time.sleep(5)
    reset_password = wait.until(EC.presence_of_element_located((By.XPATH,'(//div[@class="email_subject"])[1]'))).click()
    

    
    
 

    
 
    
         
    teardown(driver)
    
sign_in()
    