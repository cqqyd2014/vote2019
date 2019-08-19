#https://www.kuaidaili.com

#base_url='https://www.kuaidaili.com/free/inha/%d/'
import datetime
from selenium.webdriver.common.by import By

from database.orm import ProxyWebsite,ProxyServer,VoteLog,CheckProxyLog
from database import _create_db_table,create_session
from python_common.selenium_common import Sel,hand_find_element,hand_click,hand_browse_webpage_wait
from python_common.common import DataClear



class Xiaoxiaotong(Sel):

    @Sel.handle_open_page
    def web_check(self,url,db_session,ip,port):
        dc=DataClear()
        like_span = hand_find_element(self.driver,By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div/span[1]/i')
        #print(like_span)
        if like_span!=None:
            
            hand_browse_webpage_wait()
            hand_click(like_span)
            checkProxyLog=CheckProxyLog(c_ip=ip,c_port=port,c_datetime=datetime.datetime.now(),c_status='可用')
            db_session.add(checkProxyLog)
            hand_browse_webpage_wait()
            
        else:
            checkProxyLog=CheckProxyLog(c_ip=ip,c_port=port,c_datetime=datetime.datetime.now(),c_status='不可用')
            db_session.add(checkProxyLog)
            hand_browse_webpage_wait()
            
    
   

    @Sel.handle_open_page
    def web_click(self,url,db_session,ip,port):
        dc=DataClear()
        like_span = hand_find_element(self.driver,By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div/span[1]/i')
        #print(like_span)
        if like_span!=None:
            
            hand_browse_webpage_wait()
            hand_click(like_span)
            voteLog=VoteLog(v_ip=ip,v_port=port,v_datetime=datetime.datetime.now(),v_status="成功")
            db_session.add(voteLog)
            hand_browse_webpage_wait()
        else:
            voteLog=VoteLog(v_ip=ip,v_port=port,v_datetime=datetime.datetime.now(),v_status="失败")
            db_session.add(voteLog)
            hand_browse_webpage_wait()

            
            
        

