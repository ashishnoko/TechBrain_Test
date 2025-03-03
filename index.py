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
    aat = driver.find_element(By.XPATH,'(//a[@class="p-4 flex items-center break-all"])[1]')
    aat.click()
    time.sleep(5)
    #For going to another lesson 
    nok = driver.find_element(By.XPATH,'//button[@type="submit"]')
    nok.click()
    time.sleep(5)
    #For accessing lesson list
    ram = driver.find_element(By.XPATH,'(//a[@class]/span[@class="pr-1"])')
    ram.click()
    time.sleep(5)
    am = driver.find_element(By.XPATH,'//span[@class="text-gray-500"]')
    am.click()
    time.sleep(5)
    
    
    

    
    teardown(driver)
    
    
    
lists()