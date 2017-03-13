from selenium import webdriver
import re
import requests
# url = 'https://item.taobao.com/item.htm?spm=a230r.1.14.291.pHHyq4&id=546393032803&ns=1&abbucket=15'


def judge_is(type_want, size_want, platform):  # type_want:鞋类型名字,size_wang:鞋码,url为网址,platform为淘宝或者天猫
    driver = webdriver.Chrome('/Users/root_1/Downloads/chromedriver')  # 打开浏览器
    driver.get(url)  # 打开url
    content = requests.get(url).text
    # content = driver.page_source
    string_re = 'center no-repeat.*?<span>(.*?)</span>'
    # size_re = '<a href=\"javascript:void(0);\"> '+'\n'+'                                <span>(.*?)</span>'
    size_re = '<li data-value.*?<span>(.*?)</span>'
    type_thing = re.findall(string_re, content, re.S)
    all_thing = re.findall(size_re, content, re.S)
    size_thing = all_thing[0:(len(all_thing)-len(type_thing))]
    print(size_thing)
    print(type_thing)
    if type_want in type_thing:
        type_number = type_thing.index(type_want)+1
        # 点击鞋子
        driver.find_element_by_xpath("//ul[@data-property = '颜色分类']/li["+str(type_number)+"]/a").click()
        if size_want in size_thing:
            size_number = size_thing.index(size_want)+1
            driver.find_element_by_xpath("//ul[@data-property = '鞋码']/li["+str(size_number)+"]/a").click()
            if platform == '淘宝':
                driver.find_element_by_xpath("//div[@class='tb-btn-add']").click()
                a = driver.find_element_by_xpath('//*[@id="J_SureSKU"]/p[1]')
                # print(a.text)
                if a.text != '请勾选您要的商品信息！':
                    print('Yes!')
                else:
                    print("暂时无货,请耐心等待")
            elif platform == '天猫':
                driver.find_element_by_xpath("//div[@class='tb-btn-basket tb-btn-sku ']").click()
                a = driver.find_element_by_xpath("//p[@class='tb-note-title']")
                print(a.text)
                if a.text[0:10] != '请选择您要的商品信息':
                    print('Yes!')
                else:
                    print('暂时无货,请耐心等待')
        else:
            print('您输入的'+size_want+'信息有误,请断开重新输入')
    else:
        print('您输入的'+type_want+'类型信息有误,请断开重新输入')
url = 'https://detail.tmall.com/item.htm?spm=a230r.1.0.0.tjXVNg&id=521626955017&ns=1&skuId=3417967983715'
judge_is('1号黑色/亮白/1号黑色', '36.5', '天猫')

