import requests
from lxml import etree

urls =['https://www.qishulou.com/dushi/zhang/{}.html'.format(i) for i in range(5294878,5295019)]

path = r'zhangzhongzhiwu/'

def get_txt(url):
    r = requests.get(url)
    r.encoding = 'utf-8'
    selector = etree.HTML(r.text)
    title = selector.xpath('//*[@id="nr_title"]/text()')
    text = selector.xpath('//*[@id="nr1"]/text()')
    with open(path + title[0],'w',encoding='utf-8') as f:
    # with open(path + 'content.txt','w',encoding='utf-8') as f:
        for i in text:
            f.write(i)



if __name__ == '__main__':
    for url in urls:
        get_txt(url)