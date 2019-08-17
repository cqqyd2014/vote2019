
import json
from python_common.common import DateTimeEncoder
from . import Base,Column,String,Integer,Text,DateTime

class ProxyServer(Base):
    __tablename__ = "proxy_server"
    
    p_ip = Column(String(256), primary_key=True)
    p_port = Column(Integer, primary_key=True)
    p_type= Column(String(64))
    p_location= Column(String(256))
    p_speed=Column(Integer)
    p_from_page = Column(Text)
    p_add_time=Column(DateTime)
    p_lastcheck_time=Column(DateTime)
    p_from_website_name=Column(String(64))

    def to_json(self):
        json_string = {
            
            'p_ip': self.p_ip,
            'p_port': self.p_port,
            'p_type': self.p_type,
            'p_location': self.p_location,
            'p_speed': self.p_speed,
            'p_from_page': self.p_from_page,
            'p_from_website_name': self.p_from_website_name,
            'p_add_time': json.dumps(self.p_add_time, cls=DateTimeEncoder),
            'p_lastcheck_time': json.dumps(self.p_lastcheck_time, cls=DateTimeEncoder),

        }
        return json_string

    @staticmethod
    def delete_all(db_session):
        db_session.query(ProxyServer).delete()

    def saveOfUpdate(self, session):
        db_data = session.query(ProxyServer).filter(
            ProxyServer.p_ip == self.p_ip,ProxyServer.p_port == self.p_port).one_or_none()
        if db_data == None:
            session.add(self)
        else:
            db_data.p_type = self.p_type
            db_data.p_from_website_name = self.p_from_website_name
            db_data.p_from_page = self.p_from_page
            db_data.p_add_time = self.p_add_time
            db_data.p_lastcheck_time = self.p_lastcheck_time
            db_data.p_location = self.p_location
            db_data.p_speed = self.p_speed
