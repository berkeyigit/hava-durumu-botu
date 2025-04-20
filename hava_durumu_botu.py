from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

def yavas_yaz(element, metin):
    for harf in metin:
        element.send_keys(harf)
        time.sleep(random.uniform(0.1, 0.3))

sehir = input("📍 Hava durumunu öğrenmek istediğiniz şehir: ").strip().lower()
arama_metni = f"{sehir} hava durumu"

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com")

wait = WebDriverWait(driver, 10)

try:
    #Capcthayı geçmek için
    search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
    yavas_yaz(search_box, arama_metni)
    time.sleep(random.uniform(0.5, 1.5))
    search_box.send_keys(Keys.RETURN)

    # DOM'u bekliyoruz
    sehir_bilgisi = wait.until(EC.presence_of_element_located((By.ID, "wob_loc"))).text
    sicaklik = driver.find_element(By.ID, "wob_tm").text
    durum = driver.find_element(By.ID, "wob_dc").text

    print(f"\n📍 {sehir_bilgisi}")
    print(f"🌡️ Sicaklik: {sicaklik}°C")
    print(f"⛅ Durum: {durum}")

except Exception as e:
    print("\n Veri çekilemedi. Muhtemelen hava durumu kutusu yüklenmedi ya da chromedriver güncel degil.")
    print("Hata:", e)

input("\nÇikmak için Enter'a bas...")
driver.quit()