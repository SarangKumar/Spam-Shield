#!/usr/bin/env python
# coding: utf-8

# In[352]:


import mysql.connector
from mysql.connector import Error
import pandas as pd


# In[353]:


def create_server_connection(user_name="root", user_password="16020byaadav",host_name="localhost"):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password)
        print("MySQL Database connection successful!")
    except Error as err:
        print(f"Error: '{err}'")
    return connection

#put our MySQL Terminal password

#pw = "16020byaadav"

#Database name
db = 'hackattack'
connection = create_server_connection()


# In[354]:


#create mysql_python

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        #cursor = connection.cursor()
        cursor.execute(query)
        print("Database created successfully!")
        
    except Error as err:
        print(f"Error: '{err}'")
        
create_database_query = "Create database hackattack"
create_database(connection,create_database_query)
        


# In[355]:


def create_db_connection(db_name,host_name="localhost", user_name="root", user_password="16020byaadav"):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password,
            database = db_name)
        print("MySQL Database connection successful!")
    
    except Error as err:
        print(f"Error: '{err}'")
        
    return connection
    


# In[356]:


#Execute SQL Queries
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query was successful!")
        
    except Error as err:
        print(f"Error: '{err}'")
        


# In[357]:


create_table = """
create table spam_list_new(
spams int not null,
email_id_phone_num varchar(30) not null
)
"""

#connect to the database
connection = create_db_connection(db)
execute_query(connection,create_table)


# In[358]:

#db1 = mysql.connector.connect(host_name="localhost",user_name='root',user_password='16020byaadav',db_name='hackattack')

cur = connection.cursor()

s = 'INSERT INTO spam_list_new values(%s,%s)'

t = (0,"bbb@gmail.com")
cur.execute(s,t)
connection.commit()




'''
    con = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "16020byaadav",
        database = "hackattack"
    )

    cur = con.cursor()
    no = 0
    id = "abc@gmail.com"
    query = "Insert into spam_list_new({},'{}')".format(no,id)
    print("before execute")
    cur.execute(query)
    print("after execute")
    con.commit()
    print("after commit")
    '''





'''
    mysql_var = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "16020byaadav",
        database = "hackattack"
    )
    cursor = mysql_var.cursor()
    cursor.execute("""INSERT INTO hackattack (int,str)
        VALUES (%s, '%s')""" % (int,str))
    mysql_var.commit()
'''

'''
    mycursor = mysql_var.cursor()
    sql = """insert into spam_list_new(No. of spams, Email_id_Phone_num) values(%s,'%s')"""
    val = [
        (0,"hello"),
        (0,"hi")
    ]

    mycursor.executemany(sql,val)
    mysql_var.commit()
'''
'''
    data_orders = """
    insert into spam_list_new values
    (0,id)
    """
    

    connection = create_db_connection(db)
    execute_query(connection, data_orders)
'''

#my_insert(id)
'''
id = "abc.gmail.com"
#insert data
data_orders = """
insert into spam_list values
(0,id,6293730802),
(2,'xyz@gmail.com',2794562286)
"""
'''




# In[359]:


def read_query(connection,query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    
    except Error as err:
        print(f"Error: '{err}'")

    
    


# In[360]:


#Using the select statement

q1 = """
select * from spam_list_new;
"""

connection = create_db_connection(db)
results = read_query(connection,q1)
for result in results:
    print(result)


# In[361]:


'''
q2 = """
select customer_name, phone_number from orders;
"""

connection = create_db_connection("localhost","root",pw,db)
results = read_query(connection,q2)
for result in results:
    print(result)
'''


# In[362]:


'''
q3 = """
select year(date_ordered) from orders;
"""

connection = create_db_connection("localhost","root",pw,db)
results = read_query(connection,q3)
for result in results:
    print(result)
'''


# In[363]:


'''
q4 = """
select distinct year(date_ordered) from orders;
"""

connection = create_db_connection("localhost","root",pw,db)
results = read_query(connection,q4)
for result in results:
    print(result)
'''


# In[364]:


'''q5 = """
select * from orders where date_ordered<'2018-12-31'
"""

connection = create_db_connection("localhost","root",pw,db)
results = read_query(connection,q5)
for result in results:
    print(result)
'''


# In[373]:


from_db = []
for result in results:
    result = list(result)
    from_db.append(result)
    
columns = ["No. of spams","Email_id_Phone_num"]

df = pd.DataFrame(from_db,columns = columns)
print(df)


# In[366]:


#update command
'''
update = """
update orders
set unit_price = 45
where order_id = 103
"""
connection = create_db_connection("localhost","root",pw,db)
execute_query(connection,update)
'''



# In[367]:


'''
q8 = """
select * from orders where order_id = 103;
"""

connection = create_db_connection("localhost","root",pw,db)
results = read_query(connection,q8)
for result in results:
    print(result)
'''


# In[368]:


#delete command
'''
delete_order = """
delete from orders
where order_id = 105
"""

connection = create_db_connection("localhost","root",pw,db)
execute_query(connection,delete_order)
'''


# In[369]:


'''
q9 = """
select * from orders;
"""

connection = create_db_connection("localhost","root",pw,db)
results = read_query(connection,q9)
for result in results:
    print(result)
'''


# In[ ]:




