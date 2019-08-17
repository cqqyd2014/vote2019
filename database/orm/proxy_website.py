
import json
from python_common.common import DateTimeEncoder
from . import Base,Column,String,Integer,Text,DateTime,Boolean

class ProxyWebsite(Base):
    __tablename__ = "proxy_website"
    
    p_name = Column(String(256), primary_key=True)
    p_url = Column(Text)
    p_min= Column(Integer)
    p_max = Column(Integer)
    p_lastcheck_time=Column(DateTime)
    p_inuse=Column(Boolean)
    

    def to_json(self):
        json_string = {
            
            'p_name': self.p_name,
            'p_url': self.p_url,
            'p_min': self.p_min,
            'p_max': self.p_max,
            'p_lastcheck_time': json.dumps(self.p_lastcheck_time, cls=DateTimeEncoder),
            'p_inuse': self.p_inuse,
            
        }
        return json_string

    @staticmethod
    def delete_all(db_session):
        db_session.query(ProxyWebsite).delete()

    def saveOfUpdate(self, session):
        db_data = session.query(ProxyWebsite).filter(
            ProxyWebsite.p_name == self.p_name).one_or_none()
        if db_data == None:
            session.add(self)
        else:
            db_data.p_url = self.p_url
            db_data.p_min = self.p_min
            db_data.p_max = self.p_max
            db_data.p_lastcheck_time=self.p_lastcheck_time
            db_data.p_inuse=self.p_inuse
            
