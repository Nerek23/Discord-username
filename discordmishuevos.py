from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get('https://discord.com')


wait = WebDriverWait(driver, 10)

cookie_button = wait.until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))

time.sleep(1)

cookie_button.click()

time.sleep(1)

driver.get('https://discord.com/login')

time.sleep(60)

#wait = WebDriverWait(driver, 10)
#login_button = driver.find_element(By.CLASS_NAME, 'button-ZGMevK')

#login_button = wait.until(EC.element_to_be_clickable((By.TAG_NAME, ".button-1I7cbj")))

#login_button.click()

# input("s ") porno

driver.quit()

