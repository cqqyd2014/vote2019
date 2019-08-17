from python_common.selenium_common import Sel
from selenium import webdriver
import time
import datetime

from python_common.selenium_common import Sel,hand_browse_webpage_wait
from database import _create_db_table,create_session
from database.orm import ProxyServer,SystemPar

from .xiaoxiaotong import Xiaoxiaotong

if __name__ == "__main__":
    db_session=None
    
    try:

        db_session=create_session()
        #db_chrome_driver=db_session.query(SystemPar).filter(SystemPar.par_code=='chrome_driver').one()
        chrome_driver=SystemPar.get_value(db_session,'chrome_driver')
        
        #循环读取代理服务器发布页面
        servers=db_session.query(ProxyServer).filter(ProxyServer.p_inuse==True,ProxyServer.p_type=="HTTP",ProxyServer.p_lastcheck_time!=None).all()
        #print(len(servers))
        for server in servers:
            #测试是否可用
            xiaoxiaotong=Xiaoxiaotong('Chrome',db_session,SystemPar,server.p_ip+':'+str(server.p_port))
            
            url="http://2019cybc.xiaoxiaotong.org/scratch/detail?workId=32873825&func=shared&from=timeline&isappinstalled=0"

            xiaoxiaotong.web_click(url,db_session,server.p_ip,server.p_port)
            
            xiaoxiaotong.closeWindow()

        db_session.commit()
    except:
        db_session.rollback()
        raise
    finally:
        
        db_session.close()