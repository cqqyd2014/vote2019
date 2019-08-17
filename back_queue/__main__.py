
import os


import datetime
import uuid
import time


import sys

from database.orm_session import create_session
from database.orm import SystemPar,SystemCode



ps=0
try:
    db_session=create_session()
    #读取执行的间隔
    polling_second=db_session.query(SystemPar).filter(SystemPar.par_code=='polling_second').one()
    ps=int(polling_second.par_value)
    db_session.commit()
    
except:
    db_session.rollback()
    raise
finally:
    db_session.close()
print("连接数据库成功，轮询间隔"+str(ps))
if ps>0:
    while True:
        
        #
        
        time.sleep(ps)