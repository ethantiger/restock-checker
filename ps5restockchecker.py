from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from win10toast_click import ToastNotifier
import webbrowser

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver2 = webdriver.Chrome(PATH)

ps5Url = 'https://www.bestbuy.ca/en-ca/product/playstation-5-console/14962185'
xboxUrl = 'https://www.bestbuy.ca/en-ca/product/xbox-series-x-1tb-console/14964951'
addToCart = '//*[@id="test"]/button'

driver.get(ps5Url)
driver2.get(xboxUrl)

button = driver.find_element(By.XPATH, addToCart)
button2 = driver2.find_element(By.XPATH, addToCart)

buyButton = button.is_enabled()
buyButton2 = button2.is_enabled()
toast = ToastNotifier()

while not buyButton and not buyButton2:
    button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, addToCart)))
    button2 = WebDriverWait(driver2, 5).until(EC.presence_of_element_located((By.XPATH, addToCart)))
    print("Button isn't ready yet")
    buyButton = button.is_enabled()
    buyButton2 = button2.is_enabled()
    driver.refresh()
    driver2.refresh()

driver.close()
driver2.close()

def open_url(page_url):
    try:
        webbrowser.open_new(page_url)
    except:
        print("Failed to open URL")

if buyButton:
    toast.show_toast("PS5 Restock", "PS5's are in stock at best buy", duration=10, icon_path=None,threaded=False, callback_on_click=open_url(ps5Url))
else:
    toast.show_toast("XBOX Restock", "XBOX Series X's are in stock at best buy", duration=10, icon_path=None, threaded=False, callback_on_click=open_url(xboxUrl))




