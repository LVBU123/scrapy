import time
from selenium import webdriver
from fake_useragent import UserAgent
from scrapy.http import HtmlResponse

class LRTKDownloaderMiddleware(object):
    def __init__(self):
        self.ug = UserAgent()
    def process_request(self,request,spider):
        request.headers.setdefault("User-Agent",self.ug.random)
        driver = webdriver.PhantomJS()
        driver.get(request.url)
        time.sleep(1)
        driver.save_screenshot('1.png')
        #请求下一页
        print('请求下一页')
        next_url_list = driver.find_element_by_xpath('//*[@id="l"]/div[5]/ul/li[13]/a')
        #next_url = next_url_list[-2].find_element_by_xpath('./a')
        #next_url_list = driver.find
        next_url_list.click()
        time.sleep(2)
        html = driver.page_source
        # html = html.replace('<html><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">', '')
        # html = html.replace('</pre></body></html>', '')


        return HtmlResponse(url=request.url,encoding='utf-8',body=html,request=request)