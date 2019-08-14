#https://www.kuaidaili.com

#base_url='https://www.kuaidaili.com/free/inha/%d/'

from .base_proxy_page import  BaseProxyPage


class Kuaidaili(BaseProxyPage):
    def __init__(self):
        super().__init__('快代理','https://www.kuaidaili.com/free/inha/%d/',1,4)       

    def getProxyListFromPage(self,page_url):
        print(page_url)
