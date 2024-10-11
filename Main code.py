
#importing libraries

import mysql.connector as sql , random 
from datetime import date as d
from datetime import datetime as d1
import matplotlib.pyplot as plt


#making connection with mysql

conn=sql.connect(host='localhost',user='root',passwd='',database='ebs')
if conn.is_connected():
    print("successfully connected")
    
c='YES' or "yes" or 'Yes'or 'y'
v='YES' or "yes" or 'Yes' or 'y'
c1=conn.cursor() 
 

while c=='YES' or c=="yes" or c=='Yes' or c=='y':
    print('-+-+-+-+-+-+-+-WELCOME TO ELECTRICITY BILLING SYSTEM-+-+-+-+-+-+-+-')
    now=d1.now()
    print(now.strftime("%d/%m/%Y %H:%M:%S"))
    print('1.NEW USER')
    print('2.EXISTING USER')
    print('3.EXIT')
    choice1=int(input('ENTER YOUR CHOICE:'))
    if choice1==1:
        username=input("Enter your username:")
        password=input("Enter your password:")
        confirmpasswd=input("Confirm  your password:")
        if password==confirmpasswd:
            info1="insert into newuser(username,password,confirmpasswd) values('{}','{}','{}')".format(username,password,confirmpasswd)
            c1.execute(info1)
            conn.commit()
            c=input("do you want to continue?(yes or no)")
        else:
            print('your confirm password is incorrect')
            print('Try again')
            c=input("do you want to continue?(yes or no)")
    elif choice1==2:
        username=input('Enter your username:')
        password=input('Enter your password:')
        info2="select * from newuser where username='{}' and password='{}'".format(username,password)
        c1.execute(info2)
        data=c1.fetchall()
        while v=='YES' or v=="yes" or v=='Yes'or v=='y':
            if any(data):
                print('-+-+-+-+-+-+-+-WELCOME TO ELECTRICITY BILLING SYSTEM-+-+-+-+-+-+-+-+-')
                print("1.ACCOUNT SETTINGS")
                print("2.TRANSACTION")
                print("3.VIEW CUSTOMER DETAILS")
                print("4.GRAPHICAL REPRESENTATION")
                print('5.EXIT')
                choice2=int(input('ENTER YOUR CHOICE'))
                if choice2==1:
                    print('1.NEW CUSTOMER ACCOUNT')
                    print('2.DELETE EXISTING ACCOUNT')
                    print('3 EXIT')
                    choice12=int(input('ENTER YOUR CHOICE:'))
                    if choice12==1:
                        accountno=random.randrange(1000000,9999999,1)
                        print("your accountno is",accountno)
                        boxid=input("enter your meter box ID:")
                        bankname=input('Enter your BANK NAME  :')
                        bankbranch=input('Enter your BANK BRANCH  :')
                        name=input('Enter your name  :')
                        address=input('Enter your address  :')
                        pincode=int(input('Enter your area PIN CODE  :'))
                        phoneno=int(input('Enter your PHONE NUMBER  :'))
                        if len(str(phoneno))!=10:
                            print('please check your phone number')
                            continue
                        email=input('Enter your email  :')
                        data123="select max(uid) from newuser"
                        c1.execute(data123)
                        e=c1.fetchone()[0]
                        info2="insert into AddNewCustomer values({},{},'{}','{}','{}','{}',{},{},'{}','{}')".format(accountno,e,bankname,bankbranch,name,address,pincode,phoneno,email,boxid)
                        c1.execute(info2)
                        conn.commit()
                        print("THANK YOU FOR USING OUR SOFTWARE,YOUR ACCOUNT IS SUCCESFULLY CREATED")
                        v=input("do you want to continue?(yes or no)")
                        if v=='YES' or v=="yes" or v=='Yes'or v=='y':
                            continue
                        else:
                            break
                    elif choice12==2:
                        acc=input("ENTER YOUR ACCOUNT NUMBER:")
                        use=input("ENTER YOUR USERNAME:")
                        info6=c1.execute("delete from billing where accountno='{}'".format(acc))
                        info101=c1.execute("delete from transaction where accountno='{}'".format(acc))
                        info7=c1.execute("delete from AddNewCustomer where accountno='{}'".format(acc))
                        info8=c1.execute("delete from newuser where username='{}'".format(use))
                        c1.execute(info6)
                        c1.execute(info101)
                        c1.execute(info7)
                        c1.execute(info8)
                        conn.commit()
                        print("THANK YOU FOR USING OUR SOFTWARE,YOUR ACCOUNT IS SUCCESFULLY DELETED")
                        v=input("do you want to continue?(yes or no)")
                        if v=='YES' or v=="yes" or v=='Yes'or v=='y':
                            continue
                        else:
                            break
                    
                elif choice2==2:
                    accountno=int(input('Enter your account number  :'))
                    billdate=str(d.today().replace(day=1))
                    
                    info12="select count(*) from Transaction where status='paid' and bill_date = last_day(now()- interval 1 month)+ interval 1 day and accountno="+str(accountno) 
                    c1.execute(info12)

                    dt=c1.fetchone()[0]
                    #print(dt)
                    if dt!=0:
                        print('you have already paid the bill')
                        break    
                    else:
                        unit=random.randint(0,101)
                        print('Dear customer, you have used ',unit,'units of electricity.')
                        print('One unit of curent is 150 ruppees')
                        amount=150*unit
                        bill_date=d.today().replace(day=1)
                        due_date=d.today().replace(day=15)
                        transaction_date=d.today()
                        if due_date<transaction_date:
                            fine=(transaction_date-due_date).days
                            fine=fine*30
                            totamt=amount+fine
                            print('you have dealyed for ',(transaction_date-due_date).days,'days.The fine per day is 30 rupees.')
                            GST=(15/100)*totamt
                            total_amount=totamt+GST
                            print('Pleae payup ',total_amount,'rupees inclding GST')
                            p=input("Please Enter YES to transact or NO to cancel")
                            if p=="YES"or p=='Yes'or p=='yes' or p=='y':
                                status='paid'
                                print("Transaction successful")
                                print("You have paid the bill")
                                print('amount paid=',total_amount)
                                print('transaction date=',transaction_date)
                                info3="insert into Transaction(accountno,bill_date,due_date,transaction_date,total_amount,status) values({},'{}','{}','{}',{},'{}')".format(accountno,bill_date,due_date,transaction_date,total_amount,status)
                                info102="insert into billing(accountno,t_date,unit,amount,gst,net_amount) values({},'{}',{},{},{},{})".format(accountno,transaction_date,unit,totamt,GST,total_amount)

                                c1.execute(info3)
                                c1.execute(info102)
                                conn.commit()
                            elif p=='no' or 'NO' or 'No':
                                print('plz pay the bill sooner')
                        else:
                            totamt=amount
                            GST=(15/100)*amount
                            total_amount=amount+GST
                            print('Pleae payup ',total_amount,'rupees inclding GST')
                            p=input("Please Enter YES to transact or NO to cancel")
                            if p=="YES"or p=='Yes'or p=='yes' or p=='y':
                                status='paid'
                                print("Transaction successful")
                                print("You have paid the bill")
                                info3="insert into Transaction(accountno,bill_date,due_date,transaction_date,total_amount,status) values({},'{}','{}','{}',{},'{}')".format(accountno,bill_date,due_date,transaction_date,total_amount,status)
                                c1.execute(info3)
                                data105="select max(tid) from transaction"
                                c1.execute(data105)  
                                b=c1.fetchone()[0]
                                info102="insert into billing(tid,accountno,t_date,unit,amount,gst,net_amount) values({},{},'{}',{},{},{},{})".format(b,accountno,transaction_date,unit,totamt,GST,total_amount)
                                c1.execute(info102)
                                conn.commit()
                                
                            elif p=='no' or p=='NO' or p=='No' or p=='n':
                                print('plz pay the bill sooner')
                                info3="insert into Transaction(accountno,bill_date,due_date,transaction_date,total_amount) values({},'{}','{}','{}',{})".format(accountno,bill_date,due_date,transaction_date,total_amount)
                                c1.execute(info3)
                                data105="select max(tid) from transaction"
                                c1.execute(data105)  
                                b=c1.fetchone()[0]
                                info102="insert into billing(accountno,tid,t_date,unit,amount,gst,net_amount) values({},{},'{}',{},{},{},{})".format(accountno,b,transaction_date,unit,totamt,GST,total_amount)
                                c1.execute(info102)
                                conn.commit()
                                 
                        v=input("do you want to continue?(yes or no)")
                        if v=='YES' or v=="yes" or v=='Yes' or v=='y':
                            continue
                        else:
                            break                    
                elif choice2==3:
                    accountno=int(input('Enter your account number  :'))
                    info4="select * from AddNewCustomer where accountno=" + str(accountno)
                    c1.execute(info4)
                    data1=c1.fetchall()
                    for row in data1:
                        print(" Account Number: ", row[0])
                        print("bankname:",row[2])
                        print("bankbranch:",row[3])
                        print("Person name:",row[4])
                        print("Your meter device ID=",row[9])
                        print("Residential address:",row[5])
                        print("pin code:",row[6])
                        print("phone number:",row[7])
                        print("email:",row[8])
                        info5="select * from billing where accountno=" + str(accountno)
                        c1.execute(info5)
                        data2=c1.fetchall()
                        for row in data2:
                
                         print(" Unit : ",row[4])
                         print(" last used on:",row[3])
                         print("amount to be paid without GST:",row[5])
                         print("GST=",row[6])
                         print("amount to be paid including GST:",row[7])

                    v=input("do you want to continue?(yes or no)")
                    if v=='YES' or v=="yes" or v=='Yes' or v=='y':
                        continue
                    else:
                        break
                elif choice2==4:
                    info9="select total_amount from transaction where status= 'paid'"
                    c1.execute(info9)
                    L1=[]
                    for i in c1.fetchall():
                        L1.append(i[0])
                        
                    plt.plot(L1,marker='*')
                    
                    plt.title("GRAPH")
                    plt.xlabel('transactions')
                    plt.ylabel('total amount')
                    plt.show()
                    v=input("do you want to continue?(yes or no)")
                    if v=='YES' or v=="yes" or v=='Yes' or v=='y':
                        continue
                    else:
                        break
                elif choice2==5:
                    print(                                  "THANK  YOU!!!!  VISIT AGAIN!!!!"                           )
                    break
                    c='no'

          
            else:
                print('username / password is incorrect')
                break
                c=input("do you want to try again?(yes or no)")
            
                    
        else:
            print(                                  "THANK  YOU!!!!  VISIT AGAIN!!!!"                                  )
            v='no'
            
    

    elif choice1==3:
        print(                                  "THANK  YOU!!!!  VISIT AGAIN!!!!"                                  )

        break        
    else:
        print("invalid choice")
        c=input("do you want to try again?(yes or no)")
else:
    print(                                  "THANK  YOU!!!!  VISIT AGAIN!!!!"                                  )
    
    c='yes'
    
          
          

