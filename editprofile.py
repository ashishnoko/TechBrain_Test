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
    
    
def signin():
    
    
    try:
        
        driver = setup()
    
    
        sign_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//a[@href='/users/sign_in']/span)[1]")))
        sign_in.click()
    
    
        email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='user_email']")))
        email.send_keys('nokoaashish@gmail.com')
    
        password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='user_password']")))
        password.send_keys('ashish')
    
        btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='submit']")))
        btn.click()
    

        profile = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'(//span[contains(text(),"Profile")])[1]')))
    
        profile.click()
        
        
        
        edit_profile = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//a[@href="/profile/edit"]')))
        edit_profile.click()

        
        
    
    
        #editprofile
        first_name= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//input[@id="user_first_name"]')))
        first_name.clear()
        first_name.send_keys('Marcus')
        
        last_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//input[@id="user_last_name"]')))
        last_name.clear()
        last_name.send_keys('Rashford')
    
        phone = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//input[@id="user_phone"]')))
        phone.clear()
        phone.send_keys('9841001400')
    
        street_address = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//input[@id="user_street_address"]')))
        street_address.clear()
        street_address.send_keys('Manchester')
    
        
        postal_code = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//input[@id="user_postalcode"]')))
        postal_code.clear()
        postal_code.send_keys('N78DB')
        
        city = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//input[@id="user_city"]')))
        city.clear()
        city.send_keys("Old trafford")
        
        

        select_country = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//select[@id="user_country"]')))
        select = Select(select_country)
        select.select_by_visible_text('France')
    
    
        #uploadimage
        upload_image = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//input[@id="user_avatar"]')))
        image_path = r"C:\Users\A C E R\Pictures\Screenshots\Screenshot (1).png"
        upload_image.send_keys(image_path)
    
    
        #updateprofile
        
        update_profile = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//input[@type="submit"]')))
        update_profile.click()
        
        
        #signout 
        
        signout = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'(//span[contains(text(),"Sign out")])[1]')))
        
        
        signout.click()
        
    
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(2)
       

    except Exception as e:
        print(f"Error:{e}")
        
    teardown(driver)
    
signin()
    
    
    
    
    
    
    
    


