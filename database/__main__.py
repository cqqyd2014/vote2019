#encoding:utf-8
#数据库初始化
import datetime
from .orm_session import create_session,_create_db_table
from .orm import SystemPar,SystemCode,ProxyWebsite,ProxyCheck
import platform
from python_common.selenium_common import init_database_system_par
from python_common.database_common import base_system_code


def init_db(db_session):
    _create_db_table()
    db_session.commit()
    SystemPar.delete_all(db_session)
    SystemCode.delete_all(db_session)
    db_session.commit()
    system_type=''
    if platform.platform().find('Windows')>=0:
        system_type='Windows'
    elif platform.platform().find('Darwin')>=0:
        system_type='Mac'
    elif platform.platform().find('Linux')>=0:
        system_type='Linux'
    else:
        system_type=None
    base_system_code(db_session,SystemCode)
    init_database_system_par(system_type,db_session,SystemPar)
    # 基础数据
    systemPar = SystemPar(par_code='version',
                          par_desc='版本信息', par_value='1.0', par_type=2)
    db_session.add(systemPar)
    systemPar = SystemPar(par_code='polling_second',
                          par_desc='Queue轮询间隔秒数', par_value='5', par_type=1)
    db_session.add(systemPar)
    proxyWebsite=ProxyWebsite(p_name='快代理',p_url='https://www.kuaidaili.com/free/inha/%d/',p_min=1,p_max=40,p_lastcheck_time=datetime.datetime.now(),p_inuse=True)
    db_session.add(proxyWebsite)


    db_session.commit()
    print('init db ok！')


def main():
    db_session=create_session()
    init_db(db_session)
    db_session.close()
    

if __name__ == '__main__':
    main()