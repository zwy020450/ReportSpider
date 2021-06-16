import re

import requests
from lxml import etree

# 参数为网址，返回html文本
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
    # with open('./test.html', 'w', encoding='utf-8') as fp:
    #     fp.write(response.text)
    return response.text

# 参数为某个讲座所有内容，提取其中的报告时间返回
def findTime(content, year=''):
    time = []
    time.append(re.findall('(....年.?.?月.?.?日)', content))
    time.append(re.findall('时间：(.*?)地点', content))
    time.append(re.findall('时间：(.*?)中关', content))
    time.append(re.findall('时间：(.*日)（', content))
    time.append(re.findall('定于(.*?日)', content))
    time.append(re.findall('时间：(.*?日)\d', content))
    time.append(re.findall('SeminarTime:(.*?).\d', content))
    time.append(re.findall('Time:(.*?)Location', content))
    time.append(re.findall('日期:(.*?日)', content))
    time.append(re.findall('Time:(.*?日)Abstract', content))
    time.append(re.findall('讲座时间： (.*?）)', content))
    for i in time:
        for j in i:
            if j != '' and len(j) < 30:
                j = j.replace('年', '-')
                j = j.replace('月', '-')
                j = j.replace('日', '')
                if j[0].isdigit() and j[:2] != '20':
                    j = year + '-' + j
                if j=='Monday':
                    j='2014-10-13'
                return j

# 参数为某个讲座所有内容，提取其中的报告人返回
def findReporter(content):
    # print(content)
    reporter = []
    reporter.append(re.findall('报告人简介：(.*?博士)', content))
    reporter.append(re.findall('主讲人介绍：(.*?)，', content))
    reporter.append(re.findall('报告人：(.*?教授)', content))
    reporter.append(re.findall('（(.{2,10})，.*?大学）', content))
    reporter.append(re.findall('报告人：(.*?)\\(', content))
    reporter.append(re.findall('主讲人：(.*?)女士', content))
    reporter.append(re.findall('报告人：(.*?)报告摘要', content))
    reporter.append(re.findall('报告人：(.*?)报告人简介', content))
    reporter.append(re.findall('报告人：(.*?),', content))
    reporter.append(re.findall('主讲人：(.*?)Senior ', content))
    reporter.append(re.findall('孟鸿', content))
    reporter.append(re.findall('联系人：(.*?)教授 ', content))
    reporter.append(re.findall('主讲人：(.*?)Senior', content))
    reporter.append(re.findall('图灵奖获得者(.*?)博士', content))
    reporter.append(re.findall('KaiLi', content))
    reporter.append(re.findall('GuriSohi', content))
    reporter.append(re.findall('嘉宾：(.*?)研究员', content))
    reporter.append(re.findall('演讲人简介：(.*?)，', content))
    reporter.append(re.findall('主讲人：(.*?)，', content))
    reporter.append(re.findall('嘉宾：(.*?)博士', content))
    reporter.append(re.findall('XinFang', content))
    reporter.append(re.findall('主讲人：(.*?)中国科学院', content))
    reporter.append(re.findall('信息科学技术学院(...)', content))
    # print(reporter)
    for i in reporter:
        for j in i:
            if (len(j) < 25):
                # print(j)
                return j

# 检查讲座网页中有没有图片
def check_img(url, title):
    page_text = test(url)
    select1 = re.findall('vsbcontent_img', page_text)
    select2 = re.findall('img_vsb_content', page_text)
    if len(select1) > 0 or len(select2) > 0:
        tree = etree.HTML(page_text)
        try:
            img_url = 'http://eecs.pku.edu.cn/' + tree.xpath('//img[@class="img_vsb_content"]/@src')[0]
            # print('图片链接：', img_url)
            # return True
            return img_url
        except:
            print('not find')
        try:
            img_url = tree.xpath('//p[@class="vsbcontent_img"]/img/@src')[0]
            if 'http' not in img_url:
                img_url = 'http://eecs.pku.edu.cn/' + img_url
            # print('图片链接：', img_url)
            # return True
            return img_url
        except:
            print('not find')
    else:
        # return False
        return ""

# 从讲座网页提取所有内容文本
def find_content(url):
    page_text = test(url)
    tree = etree.HTML(page_text)
    content = tree.xpath('//div[@class="v_news_content"]//p//text()')
    if len(content) > 0:
        return content
    return ''

# 检测内容文本中有没有关键词（信息安全。。。） 返回bool
def Search(key,content):
    for k in key:
        if k in content:
            print("YES")
            return True
    print('NO')
    return False

# 在主程序调用，返回所有讲座信息的字典列表
def BeiDa():
    url = 'http://eecs.pku.edu.cn/xygk1/jzxx1.htm'
    num = 0
    info_lists = []

    pic_lists = []
    while 1:
        num = num + 1
        print('第%d页' % num)
        page_text = test(url)
        tree = etree.HTML(page_text)
        lists = tree.xpath('//ul[@class="ggtzM"]/li')
        for item in lists:
            info_dic = {'title': '',
                        'reporter': '',
                        'notice_time': '',
                        'report_time': '',
                        'address': '',
                        'link': '',
                        'university': '北京大学'
                        }
            title = item.xpath('./a[@class="hvr-shutter-out-vertical"]/@title')[0]
            link = item.xpath('./a[@class="hvr-shutter-out-vertical"]/@href')[0]
            notice_time = item.xpath('./a/em/text()')[0]
            if num == 1:
                link = link.replace('..', 'http://eecs.pku.edu.cn/')
            else:
                link = link.replace('../..', 'http://eecs.pku.edu.cn/')
            print('标题', title)
            print('通知时间', notice_time)
            print('链接', link)
            info_dic['title'] = title
            info_dic['notice_time'] = notice_time
            info_dic['link'] = link
            # 如果有文字
            detail = find_content(link)
            content = ''
            if len(detail) > 0:
                for i in detail:
                    content = content + i
                content = ' '.join(content.split())
                # print(content)
                # info_dic['reporter']=findReporter(content)
                # print(info_dic['reporter'])
                info_dic['report_time'] = findTime(content, notice_time[:4])
                # print(info_dic['report_time'])
                # print(content,'\n')
                print('\n')
                key = ['cryptography', 'information security', '密码学', '信息安全', '密码', 'cryptology']
                if Search(key, content):
                    info_lists.append(info_dic)
                continue

            # 如果只有图片
            pic_url = check_img(link, title)
            if (pic_url != ''):
                print(pic_url)
                # try:
                #     DownloadPic(pic_url, title)
                # except:
                #     print("下载失败")
            print('\n')
        try:
            next = tree.xpath('//span[@class="p_next p_fun"]/a/@href')[0]
        except:
            break
        if len(next) <= 5:
            url = 'http://eecs.pku.edu.cn/xygk1/jzxx1/' + next
        else:
            url = 'http://eecs.pku.edu.cn/xygk1/' + next
    return info_lists