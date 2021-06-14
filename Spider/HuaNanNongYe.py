import re

import requests
from lxml import etree


def test(url, code='utf-8'):
    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'

    }
    data = {
    }
    proxies = {'http': '72.252.4.129'}
    response = requests.get(url, headers=head)
    response.encoding = code
    # print(response.text)
    with open('./test.html', 'w', encoding='utf-8') as fp:
        fp.write(response.text)
    return response.text

def findReporter(content):
    reporter = []
    reporter.append(re.findall('报告人：(.*?教授)', content))
    reporter.append(re.findall('报告人：(.*?)（', content))
    reporter.append(re.findall('报告人：(.*?院士)', content))
    reporter.append(re.findall('报告人：(.*?研究员)', content))
    reporter.append(re.findall('报告人:(.*?)北', content))
    reporter.append(re.findall('报告人：(.*?)报告时间', content))
    reporter.append(re.findall('(报 告 人：.*?教授)', content))
    reporter.append(re.findall('报告人: (.* ?)（', content))
    reporter.append(re.findall('报告人:(.*?)（', content))

    for i in reporter:
        for j in i:
            if len(j) < 20:
                return j


def findTime(content,year=''):
    time = []
    time.append(re.findall('(....年.?.?月.?.?日)', content))
    time.append(re.findall('时间：(.*?)地点：', content))
    time.append(re.findall('报告时间：(.*?)报告地点:', content))
    time.append(re.findall('日期：(.*?)时间：', content))
    time.append(re.findall('(....年\d*?月.*?日)', content))
    for i in time:
        for j in i:
            if j != '':
                j = j.replace('年', '-')
                j = j.replace('月', '-')
                j = j.replace('日', '')
                j = j.replace('/', '-')
                j = j.replace('.', '-')
                if j[:2]!='20':
                    j=year+'-'+j
                return j


def findAddress(content):
    address = []
    address.append(re.findall('地点：(.*?)报告厅联系人', content))
    address.append(re.findall('(腾讯会议ID：.*?)\D', content))
    address.append(re.findall('(腾讯会议ID:.*?)\D', content))
    address.append(re.findall('地点:(.*?)报告摘要', content))
    address.append(re.findall('地点：(.*?)报告人：', content))
    address.append(re.findall('地点:(.*?)摘要', content))
    address.append(re.findall('地点：(.*?)联系人', content))
    address.append(re.findall('地点：(.*?)主办单位', content))
    address.append(re.findall('地点：(.*?)摘要：', content))
    address.append(re.findall('地点：(.*?)报告人简介', content))
    address.append(re.findall('报告地点：(.*?)联系人', content))

    for i in address:
        for j in i:
            if j!='' and len(j)<20:
                return j

def Search(key,content):
    for k in key:
        if k in content:
            print("YES")
            return
    print('NO')

def HuaNanNongYe():
    info_list = []
    for j in range(1, 3):
        url = 'https://info.scau.edu.cn/xsdt/list' + str(j) + '.htm'
        page_text = test(url)
        tree = etree.HTML(page_text)
        titles = tree.xpath('//div[@class="list-with-thumbnail"]//div[@class="title"][1]/text()')
        urls = tree.xpath('//div[@class="desc"]/a/@href')
        notice_times = tree.xpath('//div[@class="date text-secondary"]/small/text()')
        infos = []
        for i in range(0, len(urls)):
            urls[i] = 'https://info.scau.edu.cn/' + urls[i]
        for i in range(0, len(titles)):
            info_dic = {'title': '',
                        'reporter': '',
                        'notice_time': '',
                        'report_time': '',
                        'address': '',
                        'link': '',
                        'university': '华南农业大学'
                        }
            info = []
            print(titles[i])
            print(notice_times[i])
            print(urls[i])
            info_dic['title'] = titles[i]
            info_dic['notice_time'] = notice_times[i]
            info_dic['link'] = urls[i]
            detail = test(urls[i])
            detail_tree = etree.HTML(detail)
            detail_text = detail_tree.xpath('//div[@class="wp_articlecontent"]/p//text()')
            content = ''
            for j in detail_text:
                content = content + j
            content = ''.join(content.split())
            # print(content,'\n\n')

            info_dic['reporter']=findReporter(content)
            print(info_dic['reporter'])

            info_dic['report_time'] = findTime(content,year=re.findall('info.scau.edu.cn//(.*?)/',urls[i])[0])
            print(info_dic['report_time'])

            info_dic['address']=findAddress(content)
            print(info_dic['address'])

            key=['cryptography','security','密码学','信息安全','密码']
            Search(key,content)
            info_list.append(info_dic)


    return info_list
