from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
import time
def get_text_captcha(url_captcha:str)->str:
    
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  
    # chrome_options.add_argument("--disable-gpu") 
    # chrome_options.add_argument("--no-sandbox")  
    

    web_captcha = webdriver.Chrome(options=chrome_options)
    # web_captcha= webdriver.Chrome()

    web_captcha.get('https://www.google.com/')

    captcha_url=url_captcha

    time.sleep(1)

    
    
    lens_butt=web_captcha.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[3]/div[3]')
    lens_butt.click()
    time.sleep(1)
    \

    lens_text_fill=web_captcha.find_element(By.XPATH,'//input[@placeholder="Paste image link"]')
    lens_text_fill.send_keys(captcha_url)
    lens_text_fill.send_keys(Keys.ENTER)
    time.sleep(1)


    get_imagge_text_button=web_captcha.find_element(By.XPATH,'//*[@id="ucj-2"]')
    get_imagge_text_button.click()
    time.sleep(2)

    click_buttonn=web_captcha.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/c-wiz/div/div[2]/c-wiz/div/div/div/div[2]/div[1]/div/div/div/div[2]/div/div/button')
    click_buttonn.click()
    time.sleep(2)
   
    result=web_captcha.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/c-wiz/div/div[2]/c-wiz/div/div/span/div/h1').text
    web_captcha.close()

    return result

