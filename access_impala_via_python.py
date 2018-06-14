
IMPALA_HOST = 'cdsw-demo-3.vpc.cloudera.com'

conn = connect(host=IMPALA_HOST, 
               auth_mechanism='GSSAPI', 
               use_ssl=False, 
               database='default', 
               port=21050)  

cur = conn.cursor()

cur.execute('SHOW TABLES')

cur.fetchall()


