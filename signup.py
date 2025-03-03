from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def setup():
    driver = webdriver.Chrome()
    driver.get("https://techbrain.ai/")
    return driver

def teardown(driver):
    driver.quit()
    
def sign_up():
    driver = setup()
    
    sign_in= driver.find_element(By.XPATH,'(//a[@href="/users/sign_in"]/span)[1]')
    sign_in.click()
    time.sleep(5)
    
    sign_up = driver.find_element(By.XPATH,'//a[@href="/users/sign_up"]')
    
    sign_up.click()
    time.sleep(5)
    
    user_email = driver.find_element(By.XPATH,'//input[@id="user_email"]')
    user_email.send_keys("demo001@mailinator.com")
    password = driver.find_element(By.XPATH,'//input[@id="user_password"]')
    password.send_keys('ashish')
    confirmation_password = driver.find_element(By.XPATH,'//input[@id="user_password_confirmation"]')  
    confirmation_password.send_keys('ashish') 
    button = driver.find_element(By.XPATH,'//input[@value="Sign up"]')
    button.click()
    time.sleep(5)
    
    
    teardown(driver)
    
sign_up()
    

    
    
