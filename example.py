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

def lists():
    driver = setup()
    
    try:
        # Click the first course from the list
        course_list = driver.find_element(By.XPATH, '(//a[@class="flex mb-3"]/span[@class="text-blue-700"])[1]')
        course_list.click()
        time.sleep(5)

        # Find the chapters dynamically in each iteration
        total_chapters = driver.find_elements(By.XPATH, '//*/h3')

        for i in range(len(total_chapters)):
            # Re-locate the elements before each click to avoid stale references
            total_chapters = driver.find_elements(By.XPATH, '//*/h3')
            
            if i < len(total_chapters):  # Ensure the element still exists
                total_chapters[i].click()
                time.sleep(5)

                # Click on the redirect chapter
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
