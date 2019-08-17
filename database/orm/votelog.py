
import json
from python_common.common import DateTimeEncoder
from . import Base,Column,String,Integer,Text,DateTime,Boolean,Date

class VoteLog(Base):
    __tablename__ = "vote_log"
    
    v_ip = Column(String(256), primary_key=True)
    v_port = Column(Integer,primary_key=True)
    v_datetime= Column(DateTime,primary_key=True)

    
    

    def to_json(self):
        json_string = {
            
            'v_ip': self.v_ip,
            'v_port': self.v_port,
            'v_datetime': json.dumps(self.v_datetime, cls=DateTimeEncoder),

            
        }
        return json_string

    @staticmethod
    def delete_all(db_session):
        db_session.query(ProxyWebsite).delete()

    def saveOfUpdate(self, session):
        db_data = session.query(VoteLog).filter(
            VoteLog.v_ip == self.v_ip,VoteLog.v_port == self.v_port,VoteLog.v_port == self.v_datetime).one_or_none()
        if db_data == None:
            session.add(self)
        else:
            pass
            
