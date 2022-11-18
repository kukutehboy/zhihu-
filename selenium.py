from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


from lxml import etree


def spider_huya():
  # 创建一个驱动
  service = Service('./chromedriver.exe')
  # 创建一个浏览器
  driver = Chrome(service=service)
  # 设置隐式等待
  driver.implicitly_wait(5)
  # 访问网址
  driver.get('https://www.huya.com/g/lol')
  count = 1
  while True:
    # print('获取了第%d页' % count)
    # count += 1
    # 提取数据
    e = etree.HTML(driver.page_source)
    names = e.xpath('//i[@class="nick"]/@title')
    person_nums = e.xpath('//i[@class="js-num"]/text()')
    # 打印数据
    # for n,p in zip(names,person_nums):
    #   print(f'主播名:{n}  人气:{p}')
    
    # 找到下一页的按钮


    # try:
    #   next_btn = driver.find_element(By.XPATH,'//a[@class="laypage_next"]')
    #   next_btn.click()
    # except Exception as e:
    #   break
    if driver.page_source.find('laypage_next') == -1:
      break
    next_btn = driver.find_element(By.XPATH,'//a[@class="laypage_next"]')
    next_btn.click()
    
  # 关闭浏览器
  driver.quit()




if __name__ == '__main__':
  spider_huya()
