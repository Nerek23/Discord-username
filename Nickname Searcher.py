from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import time
#from pydub import AudioSegment
#from pydub.playback import play

# put your email and password.
email = 'Your email'
password = 'Your password'

# the path
pathtxt = 'Nicknames'

delaynickanmes = 3

delaylogin = 1

sound = True

pydubsound = 'hola.mp3'

#audio = AudioSegment.from_file(pydubsound)

driver = webdriver.Chrome()

driver.get('https://discord.com')

wait = WebDriverWait(driver, 10)

cookie_button = wait.until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))

time.sleep(delaylogin)

cookie_button.click()

time.sleep(delaylogin)

enlace_login = driver.find_element(By.CSS_SELECTOR, "a[href='//discord.com/login']")

driver.execute_script("arguments[0].click();", enlace_login)

time.sleep(3)

email_container = driver.find_element(By.ID, "uid_5")

time.sleep(delaylogin)

email_container.send_keys(email)

password_container = driver.find_element(By.ID, "uid_7")

time.sleep(delaylogin)

password_container.send_keys(password)

time.sleep(delaylogin)

password_container.send_keys(Keys.ENTER)

time.sleep(delaylogin)

settings = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='User Settings']")))

time.sleep(delaylogin)

settings.click()

EditUsername = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Edit username']")))

time.sleep(delaylogin)

EditUsername.click()

time.sleep(delaylogin)

Username_input = driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Username"]')

time.sleep(delaylogin)

Username_input.send_keys(Keys.CONTROL + 'a')
Username_input.send_keys(Keys.BACKSPACE)
Username_input.send_keys()


with open(pathtxt, 'r') as file:
    nicknames = file.read().splitlines()

for nickname in nicknames:


    Username_input = driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Username"]')
    Username_input.clear()
    Username_input.send_keys(nickname)
  
    Username_input.send_keys(Keys.ENTER)

    time.sleep(delaynickanmes)

    try:
        error_message = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "span.errorMessage-vIHOnc"))
        )
        if not "Username is unavailable" in error_message.text:

            raise ValueError("Unavailable username")
        
    except (TimeoutException, ValueError):
        Password_input = driver.find_element(By.CSS_SELECTOR, "input.inputDefault-Ciwd-S[type='password']")
        Password_input.send_keys(password)
        #Password_input.send_keys(Keys.ENTER)
        input("OG nickname found")
        if sound:
            #play(audio)
            input("OG nickname found")
        else:
            input("OG nickname found")
       

driver.quit()

