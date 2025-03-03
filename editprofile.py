from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import time

def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://techbrain.ai/")
    return driver

def teardown(driver):
    
    driver.quit()
    
    
def signin():
    driver = setup()
    sign_in = driver.find_element(By.XPATH, "(//a[@href='/users/sign_in']/span)[1]")
    sign_in.click()
    time.sleep(5)
    email = driver.find_element(By.XPATH,"//input[@id='user_email']")
    email.send_keys('nokoaashish@gmail.com')
    time.sleep(5)
    password = driver.find_element(By.XPATH,'//input[@id="user_password"]')
    password.send_keys('ashish')
    btn = driver.find_element(By.XPATH,'//input[@type="submit"]')
    btn.click()
    time.sleep(5)
    
    profile = driver.find_element(By.XPATH,'(//span[contains(text(),"Profile")])[1]')
    profile.click()
    time.sleep(5)
    edit_profile_btn = driver.find_element(By.XPATH,'//a[@href="/profile/edit"]')
    edit_profile_btn.click()
    time.sleep(5)
    
    #editprofile
    first_name = driver.find_element(By.XPATH,'//input[@id="user_first_name"]')
    first_name.clear()
    first_name.send_keys('Marcus')
    time.sleep(5)
    last_name = driver.find_element(By.XPATH,'//input[@id="user_last_name"]')
    last_name.clear()
    last_name.send_keys('Rashford')
    time.sleep(5)
    phone = driver.find_element(By.XPATH,'//input[@id="user_phone"]')
    phone.clear()
    phone.send_keys('9841001400')
    time.sleep(5)
    steet_address = driver.find_element(By.XPATH,'//input[@id="user_street_address"]')
    steet_address.clear()
    steet_address.send_keys('Manchester')
    time.sleep(5)
    postal_code = driver.find_element(By.XPATH,'//input[@id="user_postalcode"]')
    postal_code.clear()
    postal_code.send_keys('N78DB')
    time.sleep(5)
    city = driver.find_element(By.XPATH,'//input[@id="user_city"]')
    city.clear()
    city.send_keys("Old trafford")
    time.sleep(5)
    
    select_country = driver.find_element(By.XPATH,'//select[@id="user_country"]')
    select = Select(select_country)
    select.select_by_visible_text('India')
    time.sleep(5)
    
    #uploadimage
    upload_image = driver.find_element(By.XPATH,'//input[@id="user_avatar"]')
    image_path = r"C:\Users\A C E R\Desktop\Noko\noko.jpg"
    upload_image.send_keys(image_path)
    time.sleep(5)
    
    #updateprofile
    update_profile = driver.find_element(By.XPATH,'//input[@type="submit"]')
    update_profile.click()
    time.sleep(5)
    
    teardown(driver)    
signin()