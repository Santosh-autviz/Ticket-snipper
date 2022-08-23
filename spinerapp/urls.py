from selenium.webdriver.chrome.options import Options
from selenium import webdriver

url = 'https://github.com/'

options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")

driver = webdriver.Chrome(options=options)

driver.get(url)

