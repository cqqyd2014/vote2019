#https://www.kuaidaili.com

#base_url='https://www.kuaidaili.com/free/inha/%d/'

from database.orm import ProxyWebsite
from database import _create_db_table,create_session
from .base_proxy_site import  BaseProxySite


class Kuaidaili(BaseProxySite):
    

    def getProxyListFromPage(self,sel):
        proxy_pages=self.getPagesUrls()
        for page in proxy_pages:
            print(page)
            sel.handle_open_page(page,self.scrap_servers(sel))
    
    def scrap_servers(self,sel):
        pass
