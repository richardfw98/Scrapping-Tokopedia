from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd

data = {}
produk = []
harga = []
rating = []
kota = []

driver = webdriver.Chrome()

for page in range(1, 2):
    driver.get(f"https://www.tokopedia.com/search?navsource=home&page={page}&q=kayu%20manis&source=universe&srp_component_id=02.02.01.02&st=product")
    jumlah_scroll = 18

    for _ in range(jumlah_scroll):
        driver.execute_script("window.scrollBy(0, 300);")  # Menggulir 300 piksel ke bawah
        time.sleep(5)

    cinnamon = driver.find_elements(By.XPATH, "//span[@class='OWkG6oHwAppMn1hIBsC3pQ==']")
    harga_produk = driver.find_elements(By.XPATH, "//div[@class='_8cR53N0JqdRc+mQCckhS0g== Phc0SDQ0Yjt43vf3XuwYOg==']")
    rating_produk = driver.find_elements(By.XPATH, "//span[@class='nBBbPk9MrELbIUbobepKbQ==']")
    kota_seller = driver.find_elements(By.XPATH, "//span[@class ='-9tiTbQgmU1vCjykywQqvA== flip']")


    for kayu_manis in cinnamon:
        if kayu_manis:
            produk.append(kayu_manis.text)
        else:
            produk.append("Unknown")

    for harga_cinnamon in harga_produk:
        if harga_cinnamon:
            harga.append(harga_cinnamon.text)
        else:
            harga.append("Unknown")

    for rating_cinnamon in rating_produk:
        if rating_cinnamon:
            rating.append(rating_cinnamon.text)
        else:
            rating.append("Unknown")

    for seller_kota in kota_seller:
        if seller_kota:
            kota.append(kota.text)
        else:
            rating.append("Unkown")
    
# Check for mismatched lengths and adjust
max_length = max(len(produk), len(harga), len(rating), len(kota))

# Ensure all lists are the same length
while len(produk) < max_length:
    produk.append("Unknown")
while len(harga) < max_length:
    harga.append("Unknown")
while len(rating) < max_length:
    rating.append("Unknown")
while len(kota) < max_length:
    kota.append("Unknown")

data['cinnamon'] = produk
data['harga'] = harga
data['rating'] = rating
data['kota'] = kota

df = pd.DataFrame(data)
df.to_csv('kayumanis_tokopedia.csv', index=False)

driver.quit()