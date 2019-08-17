

class ProxySite():

    def __init__(self, name,url, min_num, max_num):
        self.name = name  
        self.url = url 
        self.min_num = min_num
        self.max_num= max_num

    def getPagesUrls(self):
        urls=[]
        for page_index in range(self.min_num,self.max_num+1):
            page_url=self.url.replace('%d',str(page_index))
            
            urls.append(page_url)
        return urls


        
