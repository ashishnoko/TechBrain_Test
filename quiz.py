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
    
    quiz_options= driver.find_elements(By.XPATH,'//li[@class="mb-8 last:mb-0 flex"]')
    length = len(quiz_options)
    
    for i in range(length):
        
        quiz_options= driver.find_elements(By.XPATH,'//li[@class="mb-8 last:mb-0 flex"]')
        checkbox_clk = driver.find_element(By.XPATH,'//label[@class="checkbox"]').click()
        for y in quiz_options:
            print(y)
        time.sleep(5)
        
        

        
        
            
        
        
    
    
    
    #for i in range(len(quiz_options)):
        
        
   

        # quiz_options= driver.find_elements(By.XPATH,'//li')
        # quiz_options[i] = driver.find_element(By.XPATH,'//label[@class="checkbox"]').click()
        
        # time.sleep(5)
        
        
        
        #submitbutton
        #submit_btn = driver.find_element(By.XPATH,'//button[@type="submit"]')
        #submit_btn.click()
        
        
        
    
    teardown(driver)



lists()


    
