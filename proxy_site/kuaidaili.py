#https://www.kuaidaili.com

#base_url='https://www.kuaidaili.com/free/inha/%d/'
import datetime
from selenium.webdriver.common.by import By

from database.orm import ProxyWebsite,ProxyServer
from database import _create_db_table,create_session
from python_common.selenium_common import Sel,hand_find_element
from python_common.common import DataClear



class Kuaidaili(Sel):
    
   

    @Sel.handle_open_page
    def scrap_servers(self,url,db_session):
        dc=DataClear()
        element_table = hand_find_element(self.driver,By.XPATH,'//*[@id="list"]/table')
        
        if element_table!=None:
            table_rows = element_table.find_elements_by_xpath('./tbody/tr')
            
            
            rows_len=len(table_rows)

            flag=0
            while flag<rows_len:
                ip=table_rows[flag].find_element_by_xpath('./td[1]').text
                port=dc.text_to_int(table_rows[flag].find_element_by_xpath('./td[2]').text)
                _type=table_rows[flag].find_element_by_xpath('./td[4]').text
                location=table_rows[flag].find_element_by_xpath('./td[5]').text
                speed=dc.text_to_int(table_rows[flag].find_element_by_xpath('./td[6]').text)
                proxyServer=ProxyServer(p_lastcheck_status="未知",p_inuse=True,p_add_time=datetime.datetime.now(),p_ip=ip,p_port=port,p_type=_type,p_location=location,p_speed=speed,p_from_page=url,p_from_website_name="快代理")
                proxyServer.saveOfUpdate(db_session)
                flag+=1
        

