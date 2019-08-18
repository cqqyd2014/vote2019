from python_common.selenium_common import Sel
from selenium import webdriver
import time
import datetime

from python_common.selenium_common import Sel
from database import _create_db_table,create_session
from database.orm import ProxyServer,SystemPar,CheckProxyLog

if __name__ == "__main__":
    db_session=None
    
    try:

        db_session=create_session()
        #db_chrome_driver=db_session.query(SystemPar).filter(SystemPar.par_code=='chrome_driver').one()
        chrome_driver=SystemPar.get_value(db_session,'chrome_driver')
        
        #循环读取代理服务器发布页面
        servers=db_session.query(ProxyServer).filter(ProxyServer.p_inuse==True,ProxyServer.p_type=="HTTP").all()
        for server in servers:
            #测试是否可用
            sel=Sel('Chrome',db_session,SystemPar,server.p_ip+':'+str(server.p_port))
            net_test_dist=SystemPar.get_value(db_session,'net_test_dist')
            net_test_dist_exists_text=SystemPar.get_value(db_session,'net_test_dist_exists_text')
            server.p_lastcheck_time=datetime.datetime.now()
            if (net_test_dist_exists_text in sel.getHtmlSource(net_test_dist)):
                server.p_lastcheck_status="可用"
            else:
                server.p_lastcheck_status="不可用"
            sel.closeWindow()

        db_session.commit()
    except:
        db_session.rollback()
        raise
    finally:
        
        db_session.close()