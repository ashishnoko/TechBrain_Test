from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def setup():
    driver = webdriver.Chrome()
    driver.get("https://techbrain.ai/")
    return driver

def teardown(driver):
    
    driver.quit()

def lists():
    driver = setup()
    vars = driver.find_element(By.XPATH,'(//a[@class="flex mb-3"]/span[@class="text-blue-700"])[1]')
    vars.click()
    time.sleep(5)
    
    quiz = driver.find_element(By.XPATH,'//h3[@class][7]')
    quiz.click()
    time.sleep(5)
    
    go_to_quiz = driver.find_element(By.XPATH,'(//span[@class="pr-1"])[2]')
    go_to_quiz.click()
    time.sleep(5)
    
    a = 0
    while(a<5):
        
        check_box = driver.find_element(By.XPATH,'//label[@class="checkbox"]')
        check_box.click()
        time.sleep(5)
        a = a + 1
        
    
        
        


    
    
    
    
    
    
    
    
    
    
    
    
    teardown(driver)



lists()


    
