# coding:utf-8
from spider_tool.DataOutput import DataOutput
from spider_tool.URLManager import UrlManager
from spider_tool.HtmlDownloader import HtmlDownloader
from spider_tool.HtmlParser import HtmlParser


class DoubanSpiderManager(object):
    def __init__(self):
        self.manager = UrlManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = DataOutput()

    def crawl(self, root_url):
        # 添加入口URL
        self.manager.add_new_url(root_url)
        # 判断url管理器中是否有新的url,同时判断抓取了多少个url
        while self.manager.has_new_url() and self.manager.old_url_size() < 100:
            try:
                # 从管理器中获取新的url
                print("------获取URL------")
                new_url = self.manager.get_new_url()
                #  HTML 下载器下载网页
                print("------下载数据------")
                html = self.downloader.download(new_url)
                # HTML解析器抽取网页数据
                print("------解析数据------")
                new_urls, data = self.parser.parser(new_url, html)
                # 将抽取的url添加到URL管理器中
                print("------抽取新的URL------")
                self.manager.add_new_urls(new_urls)
                # 将数据存储文件
                print("------存储数据------")
                self.output.store_data(data)
                print("已经抓取%s个链接" % self.manager.old_url_size())
            except Exception as e:
                print("crawl failed" + e)
        # 数据存储器将文件输出成制定格式
        self.output.output_html()


if __name__ == '__main__':
    print("-----爬虫开始-----")
    spider_man = DoubanSpiderManager()
    spider_man.crawl("https://movie.douban.com/top250?start=27")
