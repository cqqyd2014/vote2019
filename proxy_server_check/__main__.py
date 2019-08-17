from python_common.selenium_common import Sel
from selenium import webdriver
import time
import datetime


from database import _create_db_table,create_session
from database.orm import ProxyServer,SystemPar

if __name__ == "__main__":
    db_session=None
    
    try:

        db_session=create_session()
        db_chrome_driver=db_session.query(SystemPar).filter(SystemPar.par_code=='chrome_driver').one()
        chrome_driver=db_chrome_driver.par_value
        
        #循环读取代理服务器发布页面
        servers=db_session.query(ProxyServer).filter(ProxyServer.p_inuse==True,ProxyServer.p_type=="HTTP").all()
        for server in servers:
            #测试是否可用
            chromeOptions = webdriver.ChromeOptions()
            chromeOptions.add_argument('--proxy-server=http://'+server.p_ip+':'+str(server.p_port))  
            browser = webdriver.Chrome(executable_path=chrome_driver,options=chromeOptions)
            browser.get("http://httpbin.org/ip")
            if (r'"origin":' in browser.page_source):
                server.p_lastcheck_time=datetime.datetime.now()
            else:
                server.p_lastcheck_time=None
            browser.quit()

        db_session.commit()
    except:
        db_session.rollback()
        raise
    finally:
        
        db_session.close()