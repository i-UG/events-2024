'''
 FormaServe IBM i Training

 For full disclaimer see https://www.formaserve.co.uk/examples.php

 © - FormaServe Systems Ltd.  1990 - 2024

 www.FormaServe.co.uk
 powerwire.eu

*** NOT FOR PUBLIC VIEWING ***

'''

from itoolkit import *
from itoolkit.transport import DatabaseTransport
import ibm_db_dbi

conn = ibm_db_dbi.connect()
itransport = DatabaseTransport(conn)
itool = iToolKit()

itool.add(iCmd5250('wrkjobscde', 'wrkjobscde'))
itool.call(itransport)
wrkjobscde = itool.dict_out('wrkjobscde')

print(wrkjobscde)

print("________________________________________________________________")

itool = iToolKit()

itool.add(iCmd5250('wrksbs', 'wrksbs'))
itool.call(itransport)
wrksbs = itool.dict_out('wrksbs')

print(wrksbs)

print("________________________________________________________________")

itool = iToolKit()

itool.add(iCmd5250('dsplibl', 'dsplibl'))
itool.call(itransport)
dsplibl = itool.dict_out('dsplibl')

print(dsplibl)

print("________________________________________________________________")
