# from pprint import pprint
import time
import pytz
import datetime as dt
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller
from pyvirtualdisplay import Display
import os

display = Display(visible=0, size=(800, 800))  
display.start()

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path


chrome_options = webdriver.ChromeOptions()
# Add your options as needed    
options = [
  # Define window size here
   "--window-size=1200,1200",
    "--ignore-certificate-errors"
 
    #"--headless",
    #"--disable-gpu",
    #"--window-size=1920,1200",
    #"--ignore-certificate-errors",
    #"--disable-extensions",
    #"--no-sandbox",
    #"--disable-dev-shm-usage",
    #'--remote-debugging-port=9222'
]

for option in options:
    chrome_options.add_argument(option)

driver = webdriver.Chrome(options = chrome_options)
driver.maximize_window()
driver.get("https://cryptocurrency.market/")


time.sleep(20)

driver.find_element(
    By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div[1]/div[2]/div/div/button[2]'
).click()

time.sleep(20)

driver.find_element(By.XPATH, '//*[@id="mui-13"]').send_keys("FTMO")

time.sleep(20)

htdd_port_name = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div[1]/div[3]/table/tbody/tr[1]/td[1]/td[4]/div/span').text
htdd_port_last = driver.find_element(
        By.XPATH,
        '//*[@id="app"]/div[1]/div/div[1]/div[1]/div[3]/table/tbody/tr[1]/td[2]/p',
    ).text
htdd_24h_change = driver.find_element(
    By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div[1]/div[3]/table/tbody/tr[1]/td[3]/p'
).text

terry_port_name = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div[1]/div[3]/table/tbody/tr[2]/td[1]/td[4]/div/span').text
terry_port_last = driver.find_element(
        By.XPATH,
        '//*[@id="app"]/div[1]/div/div[1]/div[1]/div[3]/table/tbody/tr[2]/td[2]/p',
    ).text
terry_24h_change = driver.find_element(
    By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div[1]/div[3]/table/tbody/tr[2]/td[3]/p'
).text

brian_port_name = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div[1]/div[3]/table/tbody/tr[3]/td[1]/td[4]/div/span').text
brian_port_last = driver.find_element(
        By.XPATH,
        '//*[@id="app"]/div[1]/div/div[1]/div[1]/div[3]/table/tbody/tr[3]/td[2]/p',
    ).text
brian_24h_change = driver.find_element(
    By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div[1]/div[3]/table/tbody/tr[3]/td[3]/p'
).text

# print(htdd_port_last)
# print(terry_port_last)
# print(brian_port_last)

# print(htdd_24h_change)
# print(terry_24h_change)
# print(brian_24h_change)



message = f"> **Daily Portfolio Performance Report** - {dt.datetime.now(pytz.timezone('Asia/Ho_Chi_Minh')).strftime("%A, %B %d")}\n\n\
- **{htdd_port_name}**\t|\t**Last Price**: {htdd_port_last}\t|\t**24-hour Change**: {htdd_24h_change}\n\
- **{terry_port_name}**\t|\t**Last Price**: {terry_port_last}\t|\t**24-hour Change**: {terry_24h_change}\n\
- **{brian_port_name}**\t|\t**Last Price**: {brian_port_last}\t|\t**24-hour Change**: {brian_24h_change}"

print(message)


payload = {"content": message + "\n\n-----------------------------------\n"}

print(message)

discord_channel_url = "https://discord.com/api/v9/channels/1262761214514040873/messages"
headers = {
    "Authorization": os.environ.get("DISCORD_AUTH_KEY")
}  # auth key needed to send messages through discord

requests.post(discord_channel_url, payload, headers=headers)
