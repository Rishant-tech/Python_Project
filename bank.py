##management system:
##bank management system
##1. account open
##2. cash deposit
##3. cash withdrawl
##4. account details
##5. delete account
##6. exit

try:
    import mysql.connector as c
    con=c.connect(host='localhost',
                  user='root',
                  password='12345',
                  database='rishant'
                  )
    cur=con.cursor()
    print("Successfull Connection to database")
except:
    print("You have a connection error")


class bank:
    def __init__(self):
        self.name=None
        self.accType=None
        self.DOB=None
        self.Address=None
        self.mobile=None
        query="create table if not exists bank (name char(255),acctype char(255), dob char(255),address char(255),mobile char(255), cash int(255));"
        try:
            cur.execute(query)
        except:
            print("Table error")
        finally:
            con.commit()
    def open(self):
        self.name=input("Enter customer name : ")
        self.accType=input("Enter the account type you want to open 'saving, current' : ")
        self.DOB=input("Enter the DOB : ")
        self.Address=input("Enter the address : ")
        self.mobile=int(input("Enter the mobile number :"))
        cash=0
        query="insert into bank values('{}','{}','{}','{}',{},{});".format(self.name,self.accType,self.DOB,self.Address,self.mobile,cash)
        try:
            cur.execute(query)
            print("Account opened successfully")
        except:
            print("Insertion Error")
        finally:
            con.commit()
    def deposit(self):
        self.name=input("Enter the name in account : ") 
        cash=int(input("Enter the amount to deposit : "))
        try:
            cur.execute("select * from bank;")
            data=cur.fetchall()
            for i in data:
                if self.name in i:
                    cash=cash+int(i[5])
                    query="update bank set cash={} where name='{}' ".format(cash,self.name)
                    cur.execute(query)
                    print("successfully deposited")
                    break
            else:
                print("Account does not exists ")
        except:
            print("Account does not exists ")
        finally:
            con.commit()
            
    def withdrawl(self):
        self.name=input("Enter the name in account : ") 
        cash=int(input("Enter the amount to withdraw : "))
        try:
            cur.execute("select * from bank;")
            data=cur.fetchall()
            for i in data:
                if self.name in i:
                    if int(i[5]<cash):
                        print("You have insuffecient balance to withdraw")
                        break
                    else:
                        cash=int(i[5])-cash
                        query="update bank set cash={} where name='{}' ".format(cash,self.name)
                        cur.execute(query)
                        print("Amount withdrawl successfully")
                        break
            else:
                print("Account does not exists ")    
        except:
            print("Account does not exists ")    
        finally:
            con.commit()
            
    def detail(self):
        self.name=input("Enter the name to get details of account : ")
        query="select * from bank"
        try:
            cur.execute(query)
            data=cur.fetchall()
            for i in data:
                if self.name in i:
                    print("Name = ",i[0])
                    print("accTYpe= ",i[1])
                    print("DOB = ",i[2])
                    print("Address= ",i[3])
                    print("Mobile= ",i[4])
                    print("Amount= ",i[5])
                    break
            else:
                print("Customer does not exists")
        except:
            print("Customer does not exists")
        finally:
            con.commit()
    def delete(self):
        self.name=input("Enter the custome name you want to delete : ")
        try:
            cur.execute("Select * from bank")
            data=cur.fetchall()
            for i in data:
                if self.name in i:
                    query="delete from bank where name='{}'".format(self.name)
                    cur.execute(query)
                    print("Deleted successfully" )
                    break
            else:
                print("Customer does not exists")
        except:
            print("Deletion error")
        finally:
            con.commit()
if __name__=='__main__':
    bk=bank()
    print("Hii!! Welcome to the Bank Management System")
    while True:
        choice=int(input("Enter your choice what do you want to do \n1:account open \n2:cash deposit \n3:cash withdrawl \n4:account details \n5:delete account \n6:exit : "))
        if choice==6:
            break
        elif choice==1:
            bk.open()
        elif choice ==2:
            bk.deposit()
        elif choice ==3:
            bk.withdrawl()
        elif choice ==4:
            bk.detail()
        elif choice==5:
            bk.delete()
        else:
            print("Invalid choice!!")
    con.close()
    

