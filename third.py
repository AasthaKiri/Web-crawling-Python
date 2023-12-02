# from bs4 import BeautifulSoup
from PIL import Image
import pytesseract
from io import BytesIO
from selenium import webdriver
from selenium.webdriver.common.by import By

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

driver = webdriver.Chrome()
driver.get("https://directory6.org/submit?c=2&LINK_TYPE=1")
captcha_element = driver.find_element(By.CSS_SELECTOR, "img.captcha")
# get the screenshot of the captcha
captcha_screenshot = captcha_element.screenshot_as_png
# convert screenshot to image object
captcha_image = Image.open(BytesIO(captcha_screenshot))
# use pytesseract to extract text from captcha image
text = pytesseract.image_to_string(captcha_image)
captcha_value = ''.join(filter(str.isalnum, text))
print(captcha_value)

if len(captcha_value) == 5:
    driver.find_element("name", "TITLE").send_keys("Data17")
    driver.find_element("name", "URL").send_keys("https://data17.com/")
    driver.find_element("name", "CAPTCHA").send_keys(captcha_value)
    driver.find_element("name","AGREERULES").click()
    driver.find_element("name","continue").click()
    driver.quit()

else:
    print('Try Again')

