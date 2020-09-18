import sqlite3
from swiggy import *
conn=sqlite3.connect("users.db")


# create_user_table = "create table userlist(name char,number int,address varchar,password varchar,date date,order_amount)"
# conn.execute(create_user_table)
# print("user table Created")
# create_restaurants_table = "create table retro_list(restro_name text,address varchar,ph_number int)"
# conn.execute(create_restaurants_table)
# print("restaurant table Created")
# create_restaurants_menu = "create table menu(item text, rate int)"
# conn.execute(create_restaurants_menu)
# create_order_history = "create table order_history(date date, ph_number int, order_sum)"
# conn.execute(create_order_history)
# print("success")


class Users:
    def user_check(self,username,password):
        u_c="Select number , password from userlist"
        res=conn.execute(u_c)
        checker=False
        for i in res:
            if username == i[0] and password==i[1]:
                checker=True
                return checker
        return checker
    def user_p(self,number):
        check=conn.execute("SELECT * FROM userlist WHERE number = ?",(number,))
        print("**********************************************************************************".center(80))
        print("Name".center(20),"Number".center(20),"Address".center(20),"Password".center(20))
        print("**********************************************************************************".center(80))
        for i in check:
            print(str(i[0]).center(20),str(i[1]).center(20),str(i[2]).center(20),str(i[3]).center(20))

    def check_userID(self,number):
        check_point = False
        check=conn.execute('Select number from userlist')
        for i in check:
            if number == i[0]:
                check_point = True
                return check_point
        return check_point

    def add_user(self,name,number,address,password):
        cursor=conn.cursor()
        cursor.execute('INSERT INTO userlist VALUES(?,?,?,?)',(name,number,address,password))
        conn.commit()
        print("---------------------------------------")
        print(str(name),"has been registered")
        print("---------------------------------------")
        Others.main_home(self)

    def place_order(self,sum,restro_id,time,id,count,checker,number):
        check=conn.execute('SELECT item,rate,restro_id,prepare_time,item_id From menu WHERE item_id={}'.format(id))
        cursor=conn.cursor()
        #print("Item ID".center(20),"Item".center(20),"Rate".center(20),"Preparing Time(Min)".center(20))
        #print("      ---------------------------------------------------------------------------".center(60))
        for i in check:
            """print(str(i[4]).center(20),str(i[0]).center(20),str(i[1]).center(20),str(i[3]).center(20))"""

            cursor.execute("INSERT INTO order_history (time,ph_number,order_sum,restro_id,items) VALUES(?,?,?,?,?)",(date,number,i[1],i[2],i[0]))
            conn.commit()
            sum+=i[1]
            count+=1        
            if count<3:
                print("Press 1 for more items offered by the same Restaurants ")
                print("Press 2 to Exit Cart")
                choice = int(input("Enter the Choice - ")) 
                if choice == 1:
                    Menu.show_menu_by_restro(self,i[2],number,sum,count)
                    #id=int(input("Enter the Item ID - "))
                    #Users.place_order(self,sum,i[2],time,id,count,checker,number)  
                elif choice == 2: 
                    Users.today_order(self,number,date,restro_id,sum)
                    User.user_dashboard(self,number)
            else:
                Users.today_order(self,number,date,restro_id,sum)
                User.user_dashboard(self,number)
        
    def today_order(self,number,date,restro_id,sum):
        mycursor = conn.cursor()
        mycursor.execute("SELECT * FROM order_history WHERE (ph_number,time,restro_id) = (?,?,?)",(number,date,restro_id,))
        myresult = mycursor.fetchall() 
        print("**********************************************************************************".center(80))
        print("Date".center(20),"Item".center(20),"Rate".center(20),"Restro_id)".center(20))
        print("**********************************************************************************".center(80))

        for i in myresult: 
            print(str(i[0]).center(20),str(i[4]).center(20),str(i[2]).center(20),str(i[3]).center(20))
            print("----------------------------------------------------------------------------------".center(80))
            
            res_id=i[3]
            date=i[0]

        print("            Total Billing is".center(50),sum)
        print("**********************************************************************************".center(80))
        restro_name=Restaurant.show_name_by_id(self,res_id)
        restro_number=Restaurant.show_restro_by_name1(self,restro_name)
        address=Users.find_user_details(self,number)

    def orders_history(self,number):
        mycursor = conn.cursor()
        myresult=mycursor.execute('SELECT * FROM order_history WHERE ph_number=(?)',(number,))
        #myresult = mycursor.fetchall() 
        print("**********************************************************************************".center(80))
        print("Date".center(20),"Item".center(20),"Rate".center(20),"Restro_id)".center(20))
        print("**********************************************************************************".center(80))
        for i in myresult:
            print(str(i[0]).center(20),str(i[4]).center(20),str(i[2]).center(20),str(i[3]).center(20))
            print("----------------------------------------------------------------------------------".center(80))

        print("**********************************************************************************".center(80))
    
    def delete_user(self,id):
        mycursor = conn.cursor()
        mycursor.execute("DELETE FROM userlist WHERE number = ?",(id,))
        mycursor.execute("DELETE FROM order_history WHERE ph_number = ?",(id,))
        conn.commit()
        Others.main_home(self)

    def find_user_details(self,number):
        mycursor = conn.cursor()
        mycursor.execute("SELECT * FROM userlist WHERE (number) = (?)",(number,))
        myresult = mycursor.fetchall() 
        for i in myresult:
            c=i[2]
        return c
    
class Restaurant:
    
    def restro_check(self,username,password):
        u_c="Select restro_id , password from retro_list"
        res=conn.execute(u_c)
        checker=False
        for i in res:
            if username == i[0] and password==i[1]:
                checker=True
                return checker
        return checker
    
    def add_restro(self,restro_name,address,ph_number,restro_id,password):
        cursor=conn.cursor()
        cursor.execute('INSERT INTO retro_list(restro_name,address,ph_number,restro_id,password) VALUES(?,?,?,?,?)',(restro_name,address,ph_number,restro_id,password,))
        conn.commit()
    
    def show_restaurants(self):
        check=conn.execute('Select restro_name,address,ph_number,id from retro_list')
        print("ID".center(20),"Name".center(20),"Address".center(20),"Phone No".center(20))
        print("      ---------------------------------------------------------------------------".center(60))
        for i in check:
            print(str(i[3]).center(20),str(i[0]).center(20),str(i[1]).center(20),str(i[2]).center(20))
    
    def select_restaurant(self,number):
        id = int(input("Select the Restaurant from above by entering ID - "))
        check=conn.execute('Select restro_name,address,ph_number,id from retro_list where id={}'.format(id))
        print("ID".center(20),"Name".center(20),"Address".center(20),"Phone No".center(20))
        print("      ---------------------------------------------------------------------------".center(60))
        for i in check:
            print(str(i[3]).center(20),str(i[0]).center(20),str(i[1]).center(20),str(i[2]).center(20))
        c=i[3]
        Menu.show_menu_by_restro(self,i[3],number)

    def show_restro_by_name(self,restro_name):
        check=conn.execute('SELECT restro_name,address,ph_number,restro_id FROM retro_list WHERE restro_name LIKE ?',(restro_name,))
        print("ID".center(20),"Name".center(20),"Address".center(20),"Phone No".center(20))
        print("      ---------------------------------------------------------------------------".center(60))
        for i in check:
            print(str(i[3]).center(20),str(i[0]).center(20),str(i[1]).center(20),str(i[2]).center(20))
            
    def show_restro_by_id(self,id):
        check=conn.execute('SELECT restro_name,address,ph_number,restro_id FROM retro_list WHERE restro_id=?',(id,))
        print("ID".center(20),"Name".center(20),"Address".center(20),"Phone No".center(20))
        print("      ---------------------------------------------------------------------------".center(60))
        for i in check:
            print(str(i[3]).center(20),str(i[0]).center(20),str(i[1]).center(20),str(i[2]).center(20))
            
    def show_name_by_id(self,id):
        check=conn.execute('SELECT restro_name,address,ph_number,restro_id FROM retro_list WHERE restro_id=?',(id,))
        for i in check:
            c=i[0]
        return c
    
    def show_restro_by_name1(self,restro_name):
        check=conn.execute('SELECT restro_name,address,ph_number,restro_id FROM retro_list WHERE restro_name LIKE ?',(restro_name,))

        for i in check:

            return i[2]
    
    def show_name_by_id(self,id):
        check=conn.execute('SELECT restro_name,address,ph_number,restro_id FROM retro_list WHERE restro_id=?',(id,))
        for i in check:
            c=i[0]
            
        return str(c)
        
            
    def orders(self,id):
        mycursor = conn.cursor()
        myresult=mycursor.execute('SELECT * FROM order_history WHERE restro_id=(?)',(id,))
        #myresult = mycursor.fetchall() 
        print("**********************************************************************************".center(80))
        print("Date".center(20),"Item".center(20),"Rate".center(20),"Restro_id)".center(20))
        print("**********************************************************************************".center(80))
        for i in myresult:
            print(str(i[0]).center(20),str(i[4]).center(20),str(i[2]).center(20),str(i[3]).center(20))
            print("----------------------------------------------------------------------------------".center(80))
        
        print("**********************************************************************************".center(80))

    def delete_restro(self,id):
        mycursor = conn.cursor()
        mycursor.execute("DELETE FROM retro_list WHERE restro_id = ?",(id,))
        mycursor.execute("DELETE FROM menu WHERE restro_id = ?",(id,))
        conn.commit()
        print("needfull done")
        Others.main_home(self)
        
class Menu:
    
    def add_menu(self):
        restro_id= input("Enter the Restaurant ID - ")
        n=int(input("Enter the Number of Items - "))
        cursor=conn.cursor()
        for i in range(0,n):
            item=input("Enter the Item Name - ")
            rate=int(input("Enter the Item Rate - "))
            prepare_time=int(input("Enter the Item Preparing Time(in Min) - "))
            conn.execute("INSERT INTO menu (item,rate,restro_id,prepare_time) VALUES('{}',{},'{}',{})".format(item,rate,restro_id,prepare_time))
            conn.commit()

    def show_menu_by_item(self,item_name,number):
        check=conn.execute("SELECT item,rate,prepare_time,item_id FROM menu WHERE item LIKE ?",(item_name,))
        print("Item ID".center(20),"Item".center(20),"Rate".center(20),"Preparing Time(Min)".center(20))
        print("      ---------------------------------------------------------------------------".center(60))
        for i in check:
            print(str(i[3]).center(20),str(i[0]).center(20),str(i[1]).center(20),str(i[2]).center(20))
        choice=int(input("Press 1 for order or 2 for Home  -  "))
        if choice == 1:
            id=int(input("Please Enter the Item ID - "))
            Users.place_order(self,0,i[2],0,id,0,True,number)
        elif choice == 2:
            User.user_dashboard(self,number)

    def show_menu_by_restro(self,id,number,sum,count):
        check=conn.execute("SELECT item,rate,prepare_time,item_id,restro_id FROM menu WHERE restro_id=?",(id,))
        print("Item ID".center(20),"Item".center(20),"Rate".center(20),"Preparing Time(Min)".center(20))
        print("      ---------------------------------------------------------------------------".center(60))
        for i in check:
            print(str(i[3]).center(20),str(i[0]).center(20),str(i[1]).center(20),str(i[2]).center(20))
        print("")

        choice=int(input("Press 1 for order and 2 for Home - "))
        if choice ==1: 
            id2 = int(input("Enter the Item ID - "))
            Users.place_order(self,sum,id,0,id2,count,True,number)
        elif choice ==2:
            User.user_dashboard(self,number)

    def show_menu_by_restro_name(self,id):
        check=conn.execute("SELECT item,rate,prepare_time,item_id,restro_id FROM menu WHERE restro_id=?",(id,))
        print("Item ID".center(20),"Item".center(20),"Rate".center(20),"Preparing Time(Min)".center(20))
        print("      ---------------------------------------------------------------------------".center(60))
        for i in check:
            print(str(i[3]).center(20),str(i[0]).center(20),str(i[1]).center(20),str(i[2]).center(20))
        print("")

    
    def change_menu(self,name):
        mycursor = conn.cursor()
        id = int(input("Enter the Item ID for Action - "))
        print("Please choose from below options :- ")
        print( "1 - To Update Price")
        print( "2 - To Update Name")
        print( "3 - To Delete Item")
        print( "4 - To Dashboard")
        print( "5 - To Exit")
        choice = int(input("Please Enter the Choice - "))
        if choice == 1:
            new_price = int(input("Enter the new price - "))
            mycursor.execute("UPDATE menu SET rate = {} WHERE item_id = {}".format(new_price,id))
            conn.commit()
            print("Changes has been updated")
        if choice == 2:
            new_name = input("Enter the new Name - ")
            mycursor.execute("UPDATE menu SET item = ? WHERE item_id = ?",(new_name,id))
            conn.commit()
            print("Changes has been updated")
        if choice == 3 :
            mycursor.execute("DELETE FROM menu WHERE item_id = {}".format(id))
            conn.commit()
            print("Changes has been updated")
        if choice == 4:
            Restro.restro_dashboard(self,name)
        if choice == 5:
            quit()
