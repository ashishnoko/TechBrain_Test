from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
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
    
    
def get_course_list():
    driver = setup()
    wait = WebDriverWait(driver,10)
    
    homepage_lists = element = wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@class='flex mb-3']/span[@class])[1]")))
    homepage_lists.click()
    time.sleep(2)
    
    total_chapters  = driver.find_elements(By.XPATH,'//h3/a')
    for i in range(len(total_chapters)):
        chapters  = driver.find_elements(By.XPATH,'//h3/a')
        time.sleep(2)
        chapters[i].click()
        time.sleep(5)
        
        
        try:
            redirect = driver.find_element(By.XPATH,'//nav[@aria-label="Breadcrumb"]//a[contains(text(),"Introduction")]')
            redirect.click()
            time.sleep(5)
        except Exception as e:
            print(f'error:{e}')
            
            
  
    
    
    teardown(driver)
    
get_course_list()