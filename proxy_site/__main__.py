

from database import _create_db_table,create_session
from database.orm import ProxyWebsite,SystemPar
from .kuaidaili import Kuaidaili
from python_common.selenium_common import Sel
from .proxy_site import ProxySite



if __name__ == "__main__":
    db_session=None
    
    try:

        db_session=create_session()
        #sel=Sel('Chrome',db_session,SystemPar)
        #循环读取代理服务器发布页面
        sites=db_session.query(ProxyWebsite).filter(ProxyWebsite.p_inuse==True).all()
        for site in sites:
            site_name=site.p_name
            site_url=site.p_url
            site_min=site.p_min
            site_max=site.p_max
            proxySite=ProxySite(site_name,site_url,site_min,site_max)
            if site_name=="快代理":
                kuaidaili=Kuaidaili('Chrome',db_session,SystemPar)
                for url in proxySite.getPagesUrls():
                    kuaidaili.scrap_servers(url,db_session)
                kuaidaili.closeWindow()
            elif site_name=="新浪网":
                pass
            else:
                pass

        db_session.commit()
    except:
        db_session.rollback()
        raise
    finally:
        
        db_session.close()
        #sel.closeWindow()