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
    driver = setup()
    wait = WebDriverWait(driver,10)
    
    sign_in =driver.find_element(By.XPATH, "(//a[@href='/users/sign_in']/span)[1]")
    sign_in.click()
    time.sleep(3)
    
    
    sign_up = driver.find_element(By.XPATH, "//a[@href='/users/sign_up']")
    sign_up.click()
    time.sleep(3)
    
    
    
    user_email = wait.until(EC.presence_of_element_located((By.XPATH,'//input[@id="user_email"]')))
    user_email.send_keys("sunil@endtest-mail.io")
    
    password = wait.until(EC.presence_of_element_located((By.XPATH,'//input[@id="user_password"]')))
    password.send_keys('ashish')
    
    confirmation_password = wait.until(EC.presence_of_element_located((By.XPATH,'//input[@id="user_password_confirmation"]')))
    confirmation_password.send_keys('ashish')
    
    button = wait.until(EC.presence_of_element_located((By.XPATH,'//input[@value="Sign up"]')))
    button.click()
    time.sleep(3)
    
    
       
    driver.get("https://app.endtest.io/mailbox?email=sunil@endtest-mail.io")
    
    
    mail = wait.until(EC.presence_of_element_located((By.XPATH,'//div[@class="email_list"]')))
    mail.click()
    time.sleep(2)
    

    reset_link = driver.find_element(By.XPATH,'(//a[@href])[1]')
    reset_link.click()
    time.sleep(4)
    
    
    
    
    driver.get("https://techbrain.ai/")
    sign_inagain= driver.find_element(By.XPATH,'(//span[contains(text(),"Sign in")])[1]')
    sign_inagain.click()
        
    #Again_signin 
    
    email = wait.until(EC.presence_of_element_located((By.XPATH,'//input[@id="user_email"]')))
    email.send_keys('sunil@endtest-mail.io')
    
        
    password = wait.unitl(EC.presence_of_element_located((By.XPATH,'//input[@id="user_password"]')))
    password.send_key('ashish')
    
        
    submit_btn =wait.until(EC.element_to_be_clickable((By.XPATH,'//input[@type="submit"]')))
    submit_btn.click()
        
        
    teardown(driver)
    
sign_up()
    

    
    
