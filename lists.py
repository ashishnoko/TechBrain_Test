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
    course_list= driver.find_element(By.XPATH,'(//a[@class="flex mb-3"]/span[@class="text-blue-700"])[1]')
    course_list.click()
    time.sleep(5)
    chapters = driver.find_elements(By.XPATH,'//*/h3')
    time.sleep(5)
    for i in range(len(chapters)):
        total_chapters = driver.find_elements(By.XPATH,'//*/h3')
        
        total_chapters[i].click()
        time.sleep(5)
        redirect_chapters= driver.find_element(By.XPATH,'//a[contains(text(),"Introduction to Ruby and Object Oriented Programmi")]')
        redirect_chapters.click()
        time.sleep(5)
        
        
        
        
        
        # try:
            # redirect_chapters = driver.find_element(By.XPATH, '//a[contains(text(),"Introduction to Ruby and Object Oriented Programmi")]')
                    # redirect_chapters.click()
                    # time.sleep(5)
                # except Exception as e:
                    # print(f"Redirect chapter not found: {e}")
        
        

        
        
    


        
    
    
        
        
        
        
        
        
    
    teardown(driver)
    
    
lists()
    

