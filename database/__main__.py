#encoding:utf-8

from .orm_session import create_session,_create_db_table
from .orm import SystemPar,SystemCode,ProxyWebsite
import platform


def init_db(db_session):
    _create_db_table()
    db_session.commit()
    SystemPar.delete_all(db_session)
    db_session.commit()
    system_type=''
    if platform.platform().find('Windows')>=0:
        system_type='Windows'
    else:
        system_type='UNIX'
    # 基础数据
    systemPar = SystemPar(par_code='version',
                          par_desc='版本信息', par_value='1.0', par_type=2)
    db_session.add(systemPar)
    if system_type=='UNIX':
        systemPar = SystemPar(par_code='chrome_driver', par_desc='Chrome驱动',
                          par_value='/u01/software/chromedriver.exe', par_type=2)
        db_session.add(systemPar)
        systemPar = SystemPar(par_code='chrome_user-data-dir', par_desc='Chrome用户目录',
                          par_value='/u01/chrome_user_data_dir/', par_type=2)
        db_session.add(systemPar)

    else:
        systemPar = SystemPar(par_code='chrome_driver', par_desc='Chrome驱动',
                          par_value=r'D:\software\chromedriver.exe', par_type=2)
        db_session.add(systemPar)
        systemPar = SystemPar(par_code='chrome_user-data-dir', par_desc='Chrome用户目录',
                          par_value=r'D:\chrome_user_data_dir', par_type=2)
        db_session.add(systemPar)
    

    
    systemPar = SystemPar(par_code='polling_second',
                          par_desc='Queue轮询间隔秒数', par_value='5', par_type=1)
    db_session.add(systemPar)
    SystemCode.delete_all(db_session)
    systemCode = SystemCode(code_main='currency', code_desc='货币',
                            code_code='CNY', code_value='人民币元', code_type=2)
    db_session.add(systemCode)
    systemCode = SystemCode(code_main='currency', code_desc='货币',
                            code_code='HKD', code_value='港元', code_type=2)
    db_session.add(systemCode)
    systemCode = SystemCode(code_main='currency', code_desc='货币',
                            code_code='JPY', code_value='日圆', code_type=2)
    db_session.add(systemCode)
    systemCode = SystemCode(code_main='currency', code_desc='货币',
                            code_code='SUR', code_value='卢布', code_type=2)
    db_session.add(systemCode)
    systemCode = SystemCode(code_main='currency', code_desc='货币',
                            code_code='CAD', code_value='加元', code_type=2)
    db_session.add(systemCode)
    systemCode = SystemCode(code_main='currency', code_desc='货币',
                            code_code='USD', code_value='美元', code_type=2)
    db_session.add(systemCode)
    systemCode = SystemCode(code_main='currency', code_desc='货币',
                            code_code='AUD', code_value='澳大利亚元', code_type=2)
    db_session.add(systemCode)
    systemCode = SystemCode(code_main='currency', code_desc='货币',
                            code_code='NZD', code_value='新西兰元', code_type=2)
    db_session.add(systemCode)
    systemCode = SystemCode(code_main='currency', code_desc='货币',
                            code_code='SGD', code_value='新加坡元', code_type=2)
    db_session.add(systemCode)
    
    proxyWebsite=ProxyWebsite(p_name='爱快网',p_url='https://www.kuaidaili.com/free/inha/%d/',p_min=1,p_max=4)
    db_session.add(proxyWebsite)


    db_session.commit()
    print('init db ok')


def main():
    db_session=create_session()
    init_db(db_session)
    db_session.close()
    

if __name__ == '__main__':
    main()