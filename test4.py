import time
from selenium.common import NoSuchElementException
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
variant_id = 7062330

koszula = driver.find_element(By.CSS_SELECTOR,'.product-tag-details[data-id="' + str(produkt_id) + '"] a')
koszula.click()

add_to_fav = driver.find_element(By.CSS_SELECTOR, '#product-variant-form .add-to-favorite')
add_to_fav.click()

time.sleep(1)

fav_link = driver.find_element(By.CSS_SELECTOR,'header .navbar .navbar-header .favorite-container button')
fav_link.click()

try:
    driver.find_element(By.CSS_SELECTOR,'.product-page-items .product-tag-details[data-id="' + str(produkt_id) + '"]')
except NoSuchElementException:
    print("Nie ma naszego produktu w ulubionych")
    raise

else:
    print("test wykonany poprawnie")

finally:
    driver.quit()


