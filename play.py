from selenium import webdriver
import re
# url = 'https://item.taobao.com/item.htm?spm=a230r.1.14.291.pHHyq4&id=546393032803&ns=1&abbucket=15'


def judge_is(type_want, size_want, url):  # type_want:鞋类型名字,size_wang:鞋码,url为网址
    driver = webdriver.Chrome('/Users/root_1/Downloads/chromedriver')  # 打开浏览器
    driver.get(url)  # 打开url
    content = driver.page_source
    string_re = 'center no-repeat;\">'+'\n'+'                                <span>(.*?)</span>'
    # size_re = '<a href=\"javascript:void(0);\"> '+'\n'+'                                <span>(.*?)</span>'
    size_re = '<li data-value.*?<span>(.*?)</span>'
    type_thing = re.findall(string_re, content, re.S)
    all_thing = re.findall(size_re, content, re.S)
    size_thing = all_thing[0:(len(all_thing)-len(type_thing))]
    # print(size_thing)
    # print(type_thing)
    if type_want in type_thing:
        type_number = type_thing.index(type_want)+1
        driver.find_element_by_xpath('//*[@id="J_isku"]/div/dl[2]/dd/ul/li[' + str(type_number) + ']/a').click()
        if size_want in size_thing:
            size_number = size_thing.index(size_want)+1
            driver.find_element_by_xpath('//*[@id="J_isku"]/div/dl[1]/dd/ul/li['+str(size_number)+']/a/span').click()
            driver.find_element_by_xpath('//*[@id="J_juValid"]/div[2]/a').click()
            a = driver.find_element_by_xpath('//*[@id="J_SureSKU"]/p[1]')
            if a.text != '请勾选您要的商品信息':
                print('Yes!')
        else:
            print('您输入的'+size_want+'信息有误,请断开重新输入')
    else:
        print('您输入的'+type_want+'类型信息有误,请断开重新输入')

judge_is('S75967', '43')

