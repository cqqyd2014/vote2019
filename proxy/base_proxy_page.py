from abc import ABCMeta,abstractmethod

class BaseProxyPage(metaclass=ABCMeta):

    def __init__(self, name,url, min_num, max_num):
        self.name = name  
        self.url = url 
        self.min_num = min_num
        self.max_num= max_num

    def getPages(self):
        for page_index in range(self.min_num,self.max_num+1):
            page_url=self.url.replace('%d',str(page_index))
            self.getProxyListFromPage(page_url)


    @abstractmethod
    def getProxyListFromPage(self,page_url):
        pass
        
