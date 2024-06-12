
from itoolkit import *
from itoolkit.transport import DatabaseTransport
import ibm_db_dbi
conn = ibm_db_dbi.connect()
itransport = DatabaseTransport(conn)
itool = iToolKit()

itool.add(iCmd5250('wrkactjob', 'WRKACTJOB'))
itool.call(itransport)
wrkactjob = itool.dict_out('wrkactjob')
print(wrkactjob)