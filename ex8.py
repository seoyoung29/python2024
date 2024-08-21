from selenium import webdriver #pip install selenium
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("http://www.naver.com")
driver.implicitly_wait(0.5)
driver.implicitly_wait(0.5)
query_text="부산 날씨"
while True:
    message=driver.find_element(by=By.ID,value="time_are")
    print(message.text)
    if  message.text=="2024년 04월 02일 13시 47분 44초":
        break
print("시간 됐어요")

time.sleep(10)
