from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
 
def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)

names = ["쿠팡", "애플", "테슬라", "로블록스", "현대자동차"]
urls = ["https://search.naver.com/search.naver?where=nexearch&sm=top_sug.pre&fbm=1&acr=8&acq=%EC%BF%A0%ED%8C%A1+&qdt=0&ie=utf8&query=%EC%BF%A0%ED%8C%A1+%EC%A3%BC%EA%B0%80", "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%95%A0%ED%94%8C+%EC%A3%BC%EA%B0%80&oquery=dovmf+%EC%A3%BC%EA%B0%80&tqi=h5M32lp0J14ssSrKRIwssssssmh-088125", "https://search.naver.com/search.naver?sm=tab_sug.top&where=nexearch&query=%ED%85%8C%EC%8A%AC%EB%9D%BC+%EC%A3%BC%EA%B0%80&oquery=%EC%95%A0%ED%94%8C+%EC%A3%BC%EA%B0%80&tqi=h5M3Isp0J1sssTEsX5wssssstql-321923&acq=%ED%85%8C%EC%8A%AC%EB%9D%BC+%EC%A3%BC%EA%B0%80&acr=1&qdt=0", "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%A1%9C%EB%B8%94%EB%A1%9D%EC%8A%A4+%EC%A3%BC%EA%B0%80&oquery=%EB%A1%9C%EB%B8%94%EB%A1%9D%EA%B7%B8+%EC%A3%BC%EA%B0%80&tqi=h5MJbsprvTVssC54nuNssssssVN-340615", "https://search.naver.com/search.naver?sm=tab_sug.mbk&where=nexearch&query=%ED%98%84%EB%8C%80%EC%B0%A8+%EC%A3%BC%EA%B0%80&oquery=%EB%A1%9C%EB%B8%94%EB%A1%9D%EC%8A%A4+%EC%A3%BC%EA%B0%80&tqi=h5MJbwprvxZss6FIk0hssssstp4-160932&acq=%EB%A0%A8%EB%8C%80+%EC%A3%BC%EA%B0%80&acr=1&qdt=0"]
i=len(names)
driver = webdriver.Chrome('/Users/apple/dev/py/stock/chromedriver')
while True:
    driver.get(urls[i%len(urls)])
    time.sleep(0.2)
    elem = driver.find_element_by_css_selector(".spt_con").find_element_by_css_selector("strong").text
    msg = time.strftime('%Y %m %d %p %I %M %S', time.localtime(time.time())) + "  " + names[i%len(names)] + " : " + elem + "달러"
    myToken = str(open("slackToken.txt", "r", encoding="UTF-8").readline())
    post_message(myToken,"#stock",msg)
    i+=1
    time.sleep(0.1)