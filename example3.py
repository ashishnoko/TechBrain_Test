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

def course_popUp():
    driver = setup()
    wait = WebDriverWait(driver,5)
    listsLink = wait.until(EC.presence_of_element_located((By.XPATH,'(//a//span[contains(text(),"Lists")])[1]'))).click()
    numberOfLessons = len(wait.until(EC.presence_of_all_elements_located((By.XPATH,'//h3//a'))))
    firstLesson = wait.until(EC.presence_of_element_located((By.XPATH,'//a[contains(text(),"Goals of the Intro Course")]'))).click()

    for i in range(numberOfLessons):
        try:
            lessonPopUp = wait.until(EC.element_to_be_clickable((By.XPATH,'//a[@data-modal-toggle="lessonListModal"]')))
            lessonPopUp.click()
        except:
            lessonPopUp = wait.until(EC.element_to_be_clickable((By.XPATH,'//a[@data-modal-toggle="lessonListModal"]')))
            lessonPopUp.click()
            
        lessonsList = wait.until(EC.presence_of_all_elements_located((By.XPATH,'//h3//a')))
        lessonsList[i].click()
        time.sleep(5) 
         
    teardown(driver)    
course_popUp()