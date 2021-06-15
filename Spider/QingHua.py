from lxml import etree
import requests


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

def Search(key,content):
    for k in key:
        if k in content:
            print("YES")
            return True
    print('NO')
    return  False

def QingHua():
    info_lists = []
    for j in range(1, 2):
        print('正在爬取第%d页' % j)
        url = 'https://iiis.tsinghua.edu.cn/list-265-' + str(j) + '.html'
        page_text = test(url)
        tree = etree.HTML(page_text)
        page_total = len(tree.xpath('//tbody/tr'))
        for n in range(1, page_total + 1):
            info_dic = {'title': '',
                        'reporter': '',
                        'notice_time': '',
                        'report_time': '',
                        'address': '',
                        'link': '',
                        'university': '清华大学'
                        }
            lists = tree.xpath('//tbody/tr[' + str(n) + ']/td')
            print('讲座题目:', tree.xpath('//tbody/tr[' + str(n) + ']/td/a/text()')[0])
            info_dic['title'] = tree.xpath('//tbody/tr[' + str(n) + ']/td/a/text()')[0]
            reporter_infos=lists[1].xpath('//tbody/tr[' + str(n) + ']/td[2]//text()')
            reporter=''
            for rep in reporter_infos:
                reporter=reporter+rep.strip()+' '
            reporter=reporter.lstrip()
            print('主讲人:', reporter)
            info_dic['reporter'] = reporter

            print('报告时间:', lists[2].text.lstrip())
            info_dic['report_time'] = lists[2].text.lstrip()
            info_dic['notice_time'] = info_dic['report_time'][:10]
            print('通知时间', info_dic['notice_time'])
            print('地址:', lists[3].text)
            info_dic['address'] = lists[3].text
            print('链接:', 'https://iiis.tsinghua.edu.cn/' + tree.xpath('//tbody/tr[' + str(n) + ']/td/a/@href')[0])
            info_dic['link'] = 'https://iiis.tsinghua.edu.cn/' + tree.xpath('//tbody/tr[' + str(n) + ']/td/a/@href')[0]

            detail_text = test(info_dic['link'])
            d_tree = etree.HTML(detail_text)
            content_tag = d_tree.xpath('//div[@class="contentss"]//text()')
            content = ''
            for c in content_tag:
                content=content+c.strip()
            # print(content)
            key=['cryptography','information security','密码学','信息安全','密码','cryptology']
            if Search(key,content):
                info_lists.append(info_dic)
            print('\n\n')
    return info_lists