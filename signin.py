from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://techbrain.ai/")
    return driver

def teardown(driver):
    
    driver.quit()
    
    
def signin():
    driver = setup()
    sign_in = driver.find_element(By.XPATH, "(//a[@href='/users/sign_in']/span)[1]")
    sign_in.click()
    
    email = driver.find_element(By.XPATH,"//input[@id='user_email']")
    email.send_keys('nokoaashish@gmail.com')

    password = driver.find_element(By.XPATH,'//input[@id="user_password"]')
    password.send_keys('ashish')
    btn = driver.find_element(By.XPATH,'//input[@type="submit"]')
    btn.click()
    
    
    lists = driver.find_element(By.XPATH,'(//a[@class="flex mb-3"]/span[@class="text-blue-700"])[1]')
    lists.click()
    time.sleep(5)
    
    chapters = driver.find_elements(By.XPATH,'//*/h3')
    time.sleep(5)
    
    for i in range(len(chapters)):
        total_chapters = driver.find_elements(By.XPATH,'//*/h3')
        
        total_chapters[i].click()
        time.sleep(5)
        try:
             redirect_chapters= driver.find_element(By.XPATH,'//a[contains(text(),"Introduction to Ruby and Object Oriented Programmi")]')
             redirect_chapters.click()
        except Exception as e:
            
            print(f"Redirect chapter not found:{e}")
        time.sleep(5)
        
    teardown(driver)
        
        
        
signin()
    

