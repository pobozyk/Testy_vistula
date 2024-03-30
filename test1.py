import time
import pytest
from selenium import webdriver


driver = webdriver.Chrome()
driver.get('https://vistula.pl/login')
button1_cookies = driver.find_element('id','acceptAllCookiesBottom')
button1_cookies.click()

time.sleep(2)

main_content = driver.find_element('class name','main-content')

e_mail = main_content.find_element('id','login-email')
e_mail.send_keys('tester@tester.pl')

haslo = main_content.find_element('id','login-password')
haslo.send_keys('1qaz2wsx')

submit = main_content.find_element('css selector','form button[type="submit"]')
submit.click()

message = driver.find_element('css selector','.main-content form .invalid-information i').get_attribute('title')

try:
    assert message == "Niepoprawne dane do logowania."
except AssertionError:
    print("nie znaleziono odpowiedniego komunikatu")
    raise

else:
    print("test wykonany poprawnie")

finally:
    driver.quit()
