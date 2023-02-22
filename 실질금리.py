import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


now = time
y = str(now.localtime().tm_year)
m = str(now.localtime().tm_mon)
d = str(now.localtime().tm_mday)
h = str(now.localtime().tm_hour)

nowtime=y+"년"+m+"월"+d+"일"+h+"시 기준"

options = ChromeOptions()
options.add_argument('headless')
options.add_argument("disable-gpu")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("window-size=1920x1080")
driver = webdriver.Chrome('chromedriver.exe', options=options)

#

driver.get('https://www.bok.or.kr/portal/main/main.do')
기준금리dd1 = driver.find_element("xpath",'//*[@id="content"]/div/div/div[1]/div[2]/div[2]/dl/dd[1]')
기준금리 = 기준금리dd1.text
명목금리=기준금리.replace('%','')

#

driver.get('https://search.naver.com/search.naver?ie=UTF-8&sm=whl_sug&query=%EB%AC%BC%EA%B0%80%EC%83%81%EC%8A%B9%EB%A5%A0')
물가상승률dd1 = driver.find_element("xpath",'/html/body/div[3]/div[2]/div/div[1]/section[1]/div/div[1]/div[1]/div[2]/div[2]/em')
물가상승률 = 물가상승률dd1.text
물가상승률퍼 = "+"+물가상승률
물가상승률 = 물가상승률.replace('%','')

#

driver.get('https://m.stock.naver.com/marketindex/domesticInterest/KFIA114000')
CD금리dd1 = driver.find_element("xpath",'/html/body/div[1]/div[2]/div/div[2]/strong')
CD금리 = CD금리dd1.text

driver.get('https://m.stock.naver.com/marketindex/domesticInterest/KFIA114000')
CD금리퍼dd1 = driver.find_element("xpath",'/html/body/div[1]/div[2]/div/div[2]/div/span[2]')
CD금리퍼 = CD금리퍼dd1.text


#


#
print("\n- - - - - - - - - - - - - - ")
time.sleep(0.5)
print("\n - - - - - - - - - - - - - \n\n\n\n")

print("     현재시간: ",nowtime)

print('\033[37m'+"------------")
print('\033[37m'+ "현재 시각:", '\033[93m'+nowtime)
print('\033[37m'+"\n기준금리(현재): ", '\033[93m'+기준금리)
print('\033[37m'+"\n물가상승률(전년동월대비): ", '\033[93m'+물가상승률퍼)
print()
print('\033[37m'+"CD금리: ", '\033[93m'+CD금리, '\033[33m'+"  /  ",'\033[93m'+CD금리퍼)
print('\033[37m'+"------------")

명목금리=float(명목금리)
물가상승률=float(물가상승률)

실질금리=명목금리-물가상승률

print('\033[34m'+ "실지금리 ≒ "+'\033[93m',round(실질금리,2))

if (실질금리 < 0):
    print("\n"+'\033[37m',nowtime,'\033[91m'+"\n은행의 이자율 보다 소비자 물가가 더 빠르게 증가하고 있어요.")
else:
    print(nowtime,'\033[93m'+"\n소비자 물가 보다 은행의 이자율 더 빠르게 증가하고 있어요.")




print('\033[0m'+"\n\n자료출처: 기준금리(한국은행 홈페이지), 물가상승률(네이버, 통계청 kosis 지표), CD금리(네이버 증권정보)")
print('\033[37m'+"--------------------\n\n"+'\033[0m')
os.system('pause')