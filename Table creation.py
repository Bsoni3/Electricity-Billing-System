import mysql.connector as sql

#making connection with mysql

conn=sql.connect(host='localhost',user='root',passwd='')
if conn.is_connected():
    print("successfully connected")
    

c1=conn.cursor() 
#creation of tables and database
c1.execute('create database if not exists ebs')
c1.execute("use ebs")
c1.execute('create table newuser(uid int unsigned primary key not null auto_increment,username VARCHAR(100),password VARCHAR(100),confirmpasswd VARCHAR(100))')
c1.execute('create table AddNewCustomer(accountno int primary key,uid int unsigned not null,bankname VARCHAR(25),bankbranch VARCHAR(25),name VARCHAR(25),address VARCHAR(100),areacode INT(6),phoneno bigint,email VARCHAR(25),boxid VARCHAR(25),foreign key(uid) references newuser(uid))')
c1.execute('create table Transaction(tid int primary key not null auto_increment,accountno INT ,bill_date varchar(25),due_date VARCHAR(25),transaction_date varchar(25),total_amount INT,status VARCHAR(25) default "unpaid", foreign key(accountno) references AddNewCustomer(accountno))')          
c1.execute('create table billing(bid int primary key not null auto_increment,tid int,accountno int,t_date varchar(25),unit int, amount decimal(10,2),gst decimal(10,2),net_amount decimal(10,2),foreign key(tid) references transaction(tid),foreign key(accountno) references addnewcustomer(accountno))')
print("database and table created")  
