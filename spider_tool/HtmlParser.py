# coding:utf-8
import re
from urllib.parse import urlparse
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from lxml import etree


class HtmlParser(object):
    def parser(self, page_url, html_cont):
        '''
        用于解析网页内容，抽取URL和数据
        :param page_url:
        :param html_cont:
        :return:
        '''
        if page_url is None or html_cont is None:
            return
        # soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        soup = BeautifulSoup(html_cont, 'lxml')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        '''
        抽取新的URL集合
        :param page_url:
        :param soup:
        :return:
        '''
        new_urls = set()
        # 抽取符合要求的a标签
        # data_title = data.xpath('div/div[2]/div[@class="hd"]/a/span[1]/text()')
        # links = soup.find_all('a', href=re.compile(r'/view/\d+\.htm'))
        links = soup.find('div', class_='hd').find('a', href=re.compile(r'/movie/\d'))
        print(links)
        for link in links:
            # 提取href属性
            new_url = link['href']
            # 拼接成完整网址
            new_full_url = urljoin(page_url, new_url)
            new_urls.add(new_full_url)
            print(new_url)

        return new_urls

    def _get_new_data(self, page_url, soup):
        '''
        抽取所有数据
        :param page_url:
        :param soup:
        :return:
        '''
        data = {}
        data['url'] = page_url
        # data_title = data.xpath('div/div[2]/div[@class="hd"]/a/span[1]/text()')
        # data_info = data.xpath('div/div[2]/div[@class="bd"]/p[1]/text()')
        # data_quote = data.xpath('div/div[2]/div[@class="bd"]/p[2]/span/text()')
        # data_score = data.xpath('div/div[2]/div[@class="bd"]/div/span[@class="rating_num"]/text()')
        # data_num = data.xpath('div/div[2]/div[@class="bd"]/div/span[4]/text()')
        # data_picurl = data.xpath('div/div[1]/a/img/@src')
        title = soup.find('div', class_='hd').find('span').get_text()
        print(title)
        data['title'] = title.get_text()
        summary = soup.find('div', class_='lemma-summary')
        # 获取tag中包含的所有文本内容，包含子孙tag中的内容，
        data['summary'] = summary.get_text()
        return data