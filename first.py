# import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service



chrome_driver_path = "D:\my\study software\chromeDriver\chromedriver-win64\chromedriver.exe";

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
# driver = webdriver.Chrome(executable_path=chrome_driver_path)
# driver = webdriver.Chrome()

# Navigate to the form page
driver.get("https://freeadsonline.biz/index.php?view=post&postevent=&cityid=389&lang=en&catid=1&subcatid=1")

# Find the form fields and fill in the data
driver.find_element("name", "adtitle").send_keys("Data Reference")
driver.find_element("name", "addesc").send_keys("Static Data")
driver.find_element("name", "email").send_keys("admin@gmail.com")
driver.find_element("name", "agree").click()
driver.find_element(By.CSS_SELECTOR, 'form button').click()
driver.quit()

# title = driver.find_element("name","adtitle")
# title.send_keys("Data Reference") 
# post = driver.find_element("name","addesc")
# post.send_keys("Static Data")

# email = driver.find_element("name","email")
# email.send_keys("admin@gmail.com")

# checkbox = driver.find_element("name","agree")
# checkbox.click()

# Find the submit button and click it
# submit_button = driver.find_element(By.CSS_SELECTOR, 'form button')
# submit_button.click()
# Close the browser window