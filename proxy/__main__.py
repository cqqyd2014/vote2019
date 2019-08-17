

from database import _create_db_table,create_session
from database.orm import ProxyWebsite,SystemPar
from .kuaidaili import Kuaidaili
from python_common.selenium_common import Sel



if __name__ == "__main__":
    db_session=None
    sel=None
    try:

        db_session=create_session()
        sel=Sel('Chrome',db_session,SystemPar)
        #循环读取代理服务器发布页面
        sites=db_session.query(ProxyWebsite).filter(ProxyWebsite.p_inuse==True).all()
        for site in sites:
            site_name=site.p_name
            site_url=site.p_url
            site_min=site.p_min
            site_max=site.p_max
            if site_name=='爱快网':
                kuaidaili=Kuaidaili(site_name,site_url,site_min,site_max)
                kuaidaili.getProxyListFromPage(sel)
            elif site_name=='新浪网':
                pass
            else:
                pass

    
    except:
        db_session.rollback()
        raise
    finally:
        db_session.close()
        sel.closeWindow()