#!/usr/bin/env python3
import pymysql as py
db = py.connect(host = 'database-1.cfy5b4oaqkti.us-east-2.rds.amazonaws.com' , port = 3306 ,user= 'admin' , password = 'adminffao')


cursor = db.cursor()
sql = '''
create table user(
id int not null auto_increment,
name text,
password text,
primary key (id)
)
'''
cursor.execute(sql)



