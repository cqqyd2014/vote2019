from python_common.selenium_common import Sel
from selenium import webdriver
import time
import datetime

from python_common.selenium_common import Sel
from database import _create_db_table,create_session
from database.orm import ProxyServer,SystemPar,CheckProxyLog

if __name__ == "__main__":
    print("对代理服务器的测试有三种方式，1、测试所有代理服务器；2、测试，未知，状态的代理服务器；3、测试，可用，的代理服务器；4、测试，不可用，的代理服务器")
    print("请输入您的选择")
    inputLine = input()
    
    db_session=None
    
    try:

        db_session=create_session()
        #db_chrome_driver=db_session.query(SystemPar).filter(SystemPar.par_code=='chrome_driver').one()
        chrome_driver=SystemPar.get_value(db_session,'chrome_driver')
        servers=None
        #循环读取代理服务器发布页面
        if inputLine=='1':
            servers=db_session.query(ProxyServer).filter(ProxyServer.p_inuse==True,ProxyServer.p_type=="HTTP").all()
        elif inputLine=='2':
            servers=db_session.query(ProxyServer).filter(ProxyServer.p_lastcheck_status=="未知",ProxyServer.p_inuse==True,ProxyServer.p_type=="HTTP").all()
        elif inputLine=='3':
            servers=db_session.query(ProxyServer).filter(ProxyServer.p_lastcheck_status=="可用",ProxyServer.p_inuse==True,ProxyServer.p_type=="HTTP").all()
        elif inputLine=='4':
            servers=db_session.query(ProxyServer).filter(ProxyServer.p_lastcheck_status=="不可用",ProxyServer.p_inuse==True,ProxyServer.p_type=="HTTP").all()
        else:
            servers=db_session.query(ProxyServer).filter(ProxyServer.p_inuse==True,ProxyServer.p_type=="HTTP").all()
        flag=1
        print('需要测试的代理服务器有'+str(len(servers))+'个')
        for server in servers:
            #测试是否可用
            db_check_session=create_session()
            try:

                print('当前测试代理服务器'+str(flag)+':'+server.p_ip)
                sel=Sel('Chrome',db_check_session,SystemPar,server.p_ip+':'+str(server.p_port))
                net_test_dist=SystemPar.get_value(db_check_session,'net_test_dist')
                net_test_dist_exists_text=SystemPar.get_value(db_check_session,'net_test_dist_exists_text')
                server_check=db_check_session.query(ProxyServer).filter(ProxyServer.p_port==server.p_port,ProxyServer.p_ip==server.p_ip,ProxyServer.p_inuse==True,ProxyServer.p_type=="HTTP").all()
                server_check.p_lastcheck_time=datetime.datetime.now()
                if (net_test_dist_exists_text in sel.getHtmlSource(net_test_dist)):
                    server_check.p_lastcheck_status="可用"
                else:
                    server_check.p_lastcheck_status="不可用"
                sel.closeWindow()
                db_check_session.commit()
            except:
                db_session.rollback()
                raise
            finally:
                db_check_session.close()

        db_session.commit()
    except:
        db_session.rollback()
        raise
    finally:
        
        db_session.close()