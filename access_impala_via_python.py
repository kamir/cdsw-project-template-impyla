conn = connect(host='cdsw-demo-3.vpc.cloudera.com', 
               auth_mechanism='GSSAPI', 
               use_ssl=False, 
               database='default', 
               port=21050)  

cur = conn.cursor()
cur.execute('SHOW TABLES')

# now we are ready to get all tablenames ...
cur.fetchall()


