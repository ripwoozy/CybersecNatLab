from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import io
import pytesseract
from PIL import Image
import requests
# -----------------------------------------------------------------
url = "http://captcha.challs.olicyber.it/"
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# -----------------------------------------------------------------

driver = webdriver.Chrome('bin/chromedriver.exe')
driver.get(url)

while True:
    Form = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.NAME,"risposta"))) # GET RISPOSTA FORM
    ImageObj = driver.find_element_by_tag_name('img')
    Btn = driver.find_element_by_id('next')
    ImageLink = ImageObj.get_attribute('src')
    r = requests.get(str(ImageLink))
    img = Image.open(io.BytesIO(r.content))
    text = pytesseract.image_to_string(img)
    Form.send_keys(text)


