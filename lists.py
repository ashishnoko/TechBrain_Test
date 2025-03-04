from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        wait = WebDriverWait(driver,10)
        
        
        list_link= wait.until(EC.element_to_be_clickable((By.XPATH,'(//a[@class="flex mb-3"]/span[@class="text-blue-700"])[1]')))
        list_link.click()
        total_chapters = len(wait.until(EC.presence_of_all_elements_located((By.XPATH,'//*/h3'))))
        time.sleep(5)
        
        
        for i in range(total_chapters):
            try:
            
                total_chapters[i] = wait.until(EC.presence_of_all_elements_located((By.XPATH,'//*/h3')))
                
                
                
            
            except Exception as e:
                print(f'Error:{e}')
            
  
            
                   
                       
            
              
        
        teardown(driver)
    
    
lists()
    

