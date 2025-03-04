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
    
def sign_up():
    
    try:
        driver = setup()
        sign_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//a[@href='/users/sign_in']/span)[1]")))
        sign_in.click()
    
        sign_up = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/users/sign_up']")))
        
    
        sign_up.click()
        time.sleep(5)
    
        user_email = driver.find_element(By.XPATH,'//input[@id="user_email"]')
        user_email.send_keys("janehir273@calmpros.com")
    
        password = driver.find_element(By.XPATH,'//input[@id="user_password"]')
        password.send_keys('ashish')
    
        confirmation_password = driver.find_element(By.XPATH,'//input[@id="user_password_confirmation"]')  
        confirmation_password.send_keys('ashish')
    
        button = driver.find_element(By.XPATH,'//input[@value="Sign up"]')
        button.click()
        time.sleep(5)
        
        driver.get("https://temp-mail.org/en/view/67c58c73aa538e002bfc801c")
        reset_link = driver.find_element(By.XPATH,'//a[contains(text(),"http")]')
        reset_link.click()
        
        #signin 
        
        email = driver.find_element(By.XPATH,'//input[@id="user_email"]')
        email.send_keys('janehir273@calmpros.com')
        
        email = driver.find_element(By.XPATH,'//input[@id="user_password"]')
        password.send_key('ashish')
        
        submit_btn =driver.find_element(By.XPATH,'//input[@type="submit"]')
        submit_btn.click()
        
        
        
        
        
        
    except Exception as e:
        print(f'Error as {e}')
    
    
    teardown(driver)
    
sign_up()
    

    
    
