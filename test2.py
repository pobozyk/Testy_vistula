import time
from selenium.webdriver.common.by import By
from selenium import webdriver


driver = webdriver.Chrome()
driver.get('https://vistula.pl/')
driver.maximize_window()
button1_cookies = driver.find_element('id','acceptAllCookiesBottom')
button1_cookies.click()

time.sleep(2)

bottom_koszule = driver.find_element(By.XPATH, '//*[@id="nav-left"]/ul/li[1]/div/div/ul[1]/li[3]/a')

#ukryty element => display: none
driver.execute_script("arguments[0].click();", bottom_koszule)

produkt_id = 47746

koszula = driver.find_element(By.CSS_SELECTOR,'.product-tag-details[data-id="' + str(produkt_id) + '"] a')
koszula.click()


add_to_cart = driver.find_element(By.CSS_SELECTOR, '#product-variant-form #addToCart')
add_to_cart.click()

time.sleep(2)

message = driver.find_element('css selector','.notifications .notification-message')


try:
    assert message.text == "WYBIERZ DOSTĘPNY WARIANT PRODUKTU"
except AssertionError:
    print("Błąd. Można dodać produkt do koszyka bez wyboru rozmiaru")
    raise

else:
    print("test wykonany poprawnie")

finally:
    driver.quit()


