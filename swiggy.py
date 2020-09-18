from sqldata import *

class User:  
    
    def user_login(self):
        
        username = int(input("Please Enter the UserName - "))
        password = input ("Please Enter the Password - ")
        if Users.user_check(self,username,password):
            User.user_dashboard(self,username)
        else:
            print("Incorrect UserID or Password")
            self.user_login()
    def new_user(self):
        name= input("Enter the Name - ")
        number = int (input("Enter the Contact Number - "))
        address = input("Enter the City Name - ")
        password= input("Enter the Password - ")
        
        if not Users.check_userID(self,number):
            Users.add_user(self,name,number,address,password)
        else:
            print("User is Already Registered with",number)
            print()
            Others.main_home(self)
            """choice = input("Press 1 for Home and 2 for Sign up and E for Exit- ")
            if choice == '1':
                self.home()
            elif choice == '2':
                self.new_user()
            elif choice == 'E':
                quit()"""
    def del_user (self,id):
        Users.delete_user(self,id)
    def orders(self,number):
        Users.orders_history(self,number)
        
    def search_resto(self,number):
        restro_name=input("Enter the Restaurant Name - ")
        Restaurant.show_restro_by_name(self,restro_name)
        print("Press 1 to continue and place order.")
        print("Press 2 for Home")
        print("Press 3 to Exit.")
        choice = int(input("Enter your Choice - "))
        if choice == 1:
            id=input("Please Enter the Restro ID listed above- ")
            Menu.show_menu_by_restro(self,id,number,0,0)
        elif choice == 2:
            User.user_dashboard(self,number)
        elif choice == 3:
            quit()
             
    def search_item(self,number):
        item_name= input("Enter the Item Name - ")
        Menu.show_menu_by_item(self,item_name,number)

    def user_dashboard(self,name):
        print()
        print("----------------------------------********---------------------------------".center(40))
        #print("    Welcome Back ",name)
        print(name)
        print()
        print("----------------------------------********---------------------------------".center(40))
        print("Please Choose from below Options")
        print()
        print("1 for search food Item")
        print("2 for search Restaurant")
        print("3 to check Order History")
        print("4 to user Profile")
        print("0 to Sign out")
        choice = int(input("Enter your Choice from Above - "))
        if choice == 1:
            User.search_item(self,name)
        elif choice == 2:
            User.search_resto(self,name)
        elif choice == 3:
            User.orders(self,name)
        elif choice == 4:
            Users.user_p(self,name)
            choice=int(input("Please Enter 1 to delete the profile or 2 for Dashboard - "))
            if choice ==1:
                User.del_user(self,name)
            elif choice == 2:
                User.user_dashboard(self,name)
        elif choice == 0:
            quit()

class Restro :
    def restro_login(self):
        username = input("Please Enter the UserName (Restaurant ID)- ")
        password = input ("Please Enter the Password - ")
        if Restaurant.restro_check(self,username,password):
            Restro.restro_dashboard(self,username)    
        else:
            print("Incorrect ID and Password")
            Restro.restro_login(self)   
                    
    def new_registration(self):
        restro_name = input("Enter the Name - ")
        city = input("Enter the city - ")
        ph_number = input("Enter the Contact Number - ")
        restro_id = restro_name[0:3]+ph_number[3:6]+city[0:3]
        password= input("Enter the Password - ")
        Restaurant.add_restro(self,restro_name,city,ph_number,restro_id,password)
        print("Registration Done, Your Restro ID is",restro_id)
        Menu.add_menu(self)
    
    def restro_dashboard(self,restro_id):
        print()
        print("----------------------------------********---------------------------------".center(40))
        #print("    Welcome Back ",name);
        print(restro_id)
        print()
        print("----------------------------------********---------------------------------".center(40))
        
        print()
        
        print()
        print("Please Choose from below Options")
        print()
        print("1 Update Menu")
        print("2 Check Orders")
        print("3 Delete User")
        print("0 to Sign out")
        choice = int(input("Enter your Choice from Above - "))
        if choice == 1:
            Restro.alter_menu(self,restro_id)
        elif choice == 2:
            Restro.manage_orders(self,restro_id)
        elif choice == 3:
            Restaurant.delete_restro(self,restro_id)
        elif  choice == 0:
            quit()   
             
    def manage_orders(self,restro_id):
        Restaurant.orders(self,restro_id)

    
    def alter_menu(self,restro_id):
        Menu.show_menu_by_restro_name(self,restro_id)
        Menu.change_menu(self,restro_id)
   
    def restro_home(self):
        print("Welcome to Swiggy (Partner's Login)")
        print("")
        print("Please choose the options from below")
        print("")
        print("Enter 1 for Restro Owner's sign in")
        print("Enter 2 for new Registration")
        print("Enter E Exit")
        ch=input("Enter Your Choice - ")
        if ch == '1':
            Restro.restro_login(self)
        elif ch == '2':
            Restro.new_registration(self)
        elif ch == 'E' or 'e':
            quit()
        else:
            restro_home()
    
class Others:  
    def main_home(self):
        print("")
        print("Please choose the options from below")
        print("")
        print("Enter 1 for user sign in")
        print("Enter 2 for user sign up")
        print("Are you a Restaurant Owner ?? Press 3")
        print("Enter E Exit")
        ch=input("Enter Your Choice - ")
        if ch == '1':
            User.user_login(self)
        elif ch == '2':
            User.new_user(self)
        elif ch == '3':
            Restro.restro_home(self)
        elif ch == 'E' or 'e':
            quit()
        else:
            self.main_home()

if __name__ == '__main__':
    start=Others()
    start.main_home()
    
    #=Others()
    #obj_Others.main_home()
    
    

    
    
    

