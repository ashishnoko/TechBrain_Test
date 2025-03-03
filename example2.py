from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def setup():
    driver = webdriver.Chrome()
    driver.get("https://techbrain.ai/")
    driver.maximize_window()  # Optional: Maximize the browser for better element visibility
    return driver

def teardown(driver):
    driver.quit()
    
    
def accessAllLessonFromCourseDescriptionPage():
    driver = setup()
    courseListLink = driver.find_element(By.XPATH,'(//span[contains(text(),"Lists")])[1]').click()
    time.sleep(2)
    numberOfLessons = len(driver.find_elements(By.XPATH,'//h3/a'))
    for i in range(numberOfLessons):
        lessons = driver.find_elements(By.XPATH,'//h3/a')
        time.sleep(1)
        lessons[i].click()
        time.sleep(1)
        driver.find_element(By.XPATH,'//a[contains(text(),"Introduction to Ruby and Object Oriented Programming")]').click()
        time.sleep(1)
    print("All lesson traversed")
    teardown(driver)
accessAllLessonFromCourseDescriptionPage()
