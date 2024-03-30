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
e_mail.send_keys('pobozyk.tester@o2.pl')

haslo = main_content.find_element('id','login-password')
haslo.send_keys('Pobozyktester1')

submit = main_content.find_element('css selector','form button[type="submit"]')
submit.click()

time.sleep(2)


try:
    assert driver.current_url == "https://vistula.pl/client"
except AssertionError:
    print("nie mozna sie zalogowac")
    raise

else:
    print("test wykonany poprawnie")

finally:
    driver.quit()
