from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def setup():
    driver = webdriver.Chrome()
    driver.get("https://techbrain.ai/")
    driver.maximize_window()  
    return driver

def teardown(driver):
    driver.quit()

def lists():
    
    driver = setup()
    wait = WebDriverWait(driver,10)
    
    
        
        
    course_list = wait.until(EC.element_to_be_clickable((By.XPATH,'(//a/span[contains(text(),"Lists")])[1]'))) 
    course_list.click()
    time.sleep(5)

    number_of_chapters = len(driver.find_elements(By.XPATH, '//*/h3/a'))
    for i in range(number_of_chapters):
        # redirect_chapters = wait.until(EC.element_to_be_clickable((By.XPATH,'//nav[@aria-label="Breadcrumb"]//a[contains(text(),"Introduction")]')))     
        try: 
            total_chapters = driver.find_elements(By.XPATH, '//*/h3/a')
            total_chapters[i].click()
            time.sleep(2)
            redirect_chapters = wait.until(EC.element_to_be_clickable((By.XPATH,'//a[contains(text(),"Introduction")]')))
            redirect_chapters.click()
                                 
        except Exception as e:
            print(f'error{e}')    
        
    teardown(driver)

lists()
