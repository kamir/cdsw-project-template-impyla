
from impala.dbapi import connect

IMPALA_HOST='cdsw-demo-3.vpc.cloudera.com'
IMPALA_PORT=21050

conn = connect(host=IMPALA_HOST, 
               auth_mechanism='GSSAPI', 
               use_ssl=False, 
               database='default', 
               port=IMPALA_PORT)  

cur = conn.cursor()

cur.execute('SHOW TABLES')

cur.fetchall()

