
import json
from python_common.common import DateTimeEncoder
from . import Base,Column,String,Integer,Text,DateTime,Boolean,Date

class CheckProxyLog(Base):
    __tablename__ = "check_proxy_log"
    
    c_ip = Column(String(256), primary_key=True)
    c_port = Column(Integer,primary_key=True)
    c_datetime= Column(DateTime,primary_key=True)
    c_message= Column(Text)
    c_status=Column(String(256))

    
    

    def to_json(self):
        json_string = {
            
            'c_ip': self.c_ip,
            'c_port': self.c_port,
            'c_datetime': json.dumps(self.c_datetime, cls=DateTimeEncoder),
            'c_message': self.c_message,
            'c_status': self.c_status,
            
        }
        return json_string

    @staticmethod
    def delete_all(db_session):
        db_session.query(CheckProxyLog).delete()

    def saveOfUpdate(self, session):
        db_data = session.query(CheckProxyLog).filter(
            CheckProxyLog.c_ip == self.c_ip,CheckProxyLog.c_port == self.c_port,CheckProxyLog.c_datetime == self.c_datetime).one_or_none()
        if db_data == None:
            session.add(self)
        else:
            pass
            
