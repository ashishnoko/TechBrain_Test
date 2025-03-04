from selenium import webdriver
from selenium.webdriver.common.by import By
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
    
    try:
        
        course_list = driver.find_element(By.XPATH, '(//a[@class="flex mb-3"]/span[@class="text-blue-700"])[1]')
        course_list.click()
        time.sleep(5)

        
        total_chapters = driver.find_elements(By.XPATH, '//*/h3')

        for i in range(len(total_chapters)):
        
            total_chapters = driver.find_elements(By.XPATH, '//*/h3')
            
            if i < len(total_chapters):  
                total_chapters[i].click()
                time.sleep(5)

                
                try:
                    redirect_chapters = driver.find_element(By.XPATH, '//a[contains(text(),"Introduction to Ruby and Object Oriented Programmi")]')
                    redirect_chapters.click()
                    time.sleep(5)
                except Exception as e:
                    print(f"Redirect chapter not found: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        teardown(driver)

lists()
