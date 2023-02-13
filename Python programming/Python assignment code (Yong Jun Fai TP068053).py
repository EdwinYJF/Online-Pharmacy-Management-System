#YONG JUN FAI
#TP068053


def menu():
  
    while True:
        print('\n====================Welcome to OCEAN SDN BHD!====================')
        print('\nWe are a Malaysian leading company to manage pharmacy functionalities.') 
        print("\nChoose '1 or 2 or 3' to select the user from the options below.")
        print()
        print('\t1. ADMIN\n \t2. NEW CUSTOMER\n \t3. REGISTERED CUSTOMER\n')
        choice=input('\nUser: ')
        try:
            choice=int(choice)
        except:
            print('\nInvalid input')
            menu()

        if choice < 1 or choice > 3:
            print("\nThis is an invalid input! Please choose '1 or 2 or 3' to select the user from the options above.")

        elif choice == 1:
            admin_login()
            admin_system()
            break
        
        elif choice == 2:
            new_customer_menu()
            break
        
        elif choice == 3:
            login_customer()
            break


def admin_login():
    
    print("\nType '1' to continue if you are an admin. Type '2' to exit if you are not an admin.")
    choice=input('\nChoice: ')
    try:
        choice=int(choice)
    except:
        print('\nInvalid input')
        admin_login()
        
    if choice == 1:
        admin_username = input('\nAdmin login username: ')
        while admin_username != 'Yong Jun Fai' and admin_username != 'Viknesh Ramamoorthy':
            print('\nWrong username! Please enter the correct username.')
            admin_username=input('\nRetype admin username: ')
        else:
            print('\nPlease continue')
        
        admin_password_login =input('\nPassword: ')
        while admin_password_login != 'Yong123' and admin_password_login != 'Viknesh123':
            print('\nWrong password! Please re-enter the password.')
            admin_password_login=input('\nRetype password: ')
        else:
            print('\nWelcome to the admin system,' + ' ' + admin_username + '!')
            
    elif choice == 2:
        menu()

    else:
        print('\nInvalid input!')
        admin_login()
        
def admin_system():
    while True:
        print('\nYou may select a type of function by entering the number from the options given below.')
        print()
        print("\t1. Upload medicine detail\n \t2. View all medicines\n \t3. Update medicine information\n \t4. Delete medicine information\n \t5. Search medicine detail\n \t6. View customers' orders\n \t7. Search customers' orders\n \t8. Exit") 
        print()
        choice=input('\nEnter your choice: ')
        try:
            choice=int(choice)
        except:
            print('\nInvalid input')
            admin_system()
        
        if choice < 1 or choice > 8:
            print('\nError! Please choose the functions from the options given above')
        elif choice == 1:
            upload_medicine_detail()
            break
        
        elif choice == 2:
            view_all_medicines()
            break
        
        elif choice == 3:
            update_medicine_information()
            upload_medicine_detail()
            break

        elif choice == 4:
            delete_medicine_information()
            break

        elif choice == 5:
            search_medicine_details()
            break

        elif choice == 6:
            view_customers_orders()
            break

        elif choice == 7:
            search_customers_orders()
            break

        elif choice == 8:
            menu()
            break

def new_customer_menu():
    
    while True:
        print('\n====================Welcome to OCEAN SDN BHD!====================')
        print('\nWe are a Malaysian leading company to manage pharmacy functionalities.')
        print("\nChoose '1 or 2 or 3' to select the functions from the options below.")
        print()
        print('\t1. View medicine detail\n \t2. Register an account\n \t3. Exit\n')
        choice=input('\nFunctions: ')
        try:
            choice=int(choice)
        except:
            print('\nInvalid input')
            new_customer_menu()

        if choice < 1 or choice > 3:
            print("\nThis is an invalid input! Please choose '1 or 2 or 3' to select the user from the options above.")
        
        elif choice == 1:
            customer_view_medicine()
            break
            
        elif choice == 2:
            new_customer()
            break
        
        elif choice == 3:
            menu()
            break
        
def new_customer():

    choice=input("\nType '1' to continue. Type '2' to exit: ")
    try:
        choice=int(choice)
        if choice ==1:
            pass
                         
        elif choice ==2:
            new_customer_menu()
            
        else:
            print('\nInvalid input!')
            new_customer()
                  
    except:
        print('\nError! Invalid input!')
        new_customer()
        
    print("\n====================Welcome to OCEAN SDN BHD. Let's create your account!====================")
    try:
        New_customer=open('New customer.txt','a')
        customer_info=open('Customer detail.txt','a')
    except:
        print('\nError! File does not exist')
        new_customer()
    
    customer_login1st = input('\nFirst name: ')
    customer_login2nd = input('\nLast name: ')
    
    while customer_login1st == '' and customer_login2nd == '':
        print('\nInvalid input! Do not leave it blank!')
        customer_login1st = input('\nFirst name: ')
        customer_login2nd = input('\nLast name: ')
    else:
        pass
    
    customer_name = customer_login1st + ' ' + customer_login2nd
    New_customer.write('\n' + 'Customer name: ' + customer_name + ',' + ' ')
    print('\nHi', customer_name , 'welcome to OCEAN SDN BHD, please continue to register.')
    address = input('\nHouse address: ')

    while address == '':
        print('\nInvalid input! Do not leave it blank!')
        address = input('\nHouse address: ')
    else:
        pass
    
    New_customer.write('House address: ' + address + ',' + ' ')
    Email_ID = input('\nEmail address: ')
    New_customer.write('Email address: ' + Email_ID + ',' + ' ')
    contact_number = input('\nPhone number: ')

    while contact_number == '':
        print('\nInvalid input! Do not leave it blank!')
        contact_number = input('\nPhone number: ')
    else:
        pass
    
    New_customer.write('Phone number: ' + contact_number + ',' + ' ')
    gender=input('\nGender: ')
    New_customer.write('Gender: ' + gender + ',' + ' ')
    DOB=input('\nDate of birth (DD/MM/YY): ')
    New_customer.write('Date of birth (DD/MM/YY): ' + DOB + ',' + ' ')
    print('\nNow create your USER ID.')
    userID=input('\nUSER ID: ')
    
    while userID =='':
        print('\nInvalid input! Do not leave it blank!')
        userID=input('\nUSER ID: ')
    else:
        pass

    New_customer.write('USER ID: ' + userID + ',' + ' ')
    customer_info.write('\n' + userID + ',' + ' ')
    print('\nNow create your password.')
    ncpassword=input('\nPassword: ')
    confirm_password=input('\nConfirm password: ')

    while ncpassword =='' and confirm_password== '':
        print('\nInvalid input! Do not leave it blank!')
        ncpassword=input('\nPassword: ')
        confirm_password=input('\nConfirm password: ')
    else:
        pass
    
    while ncpassword != confirm_password:
        print('\nPassword mismatch! Please retype your password.')
        confirm_password=input('\nRetype password: ')
    else:
        New_customer.write('Password: ' + confirm_password)
        New_customer.close()
        customer_info.write(confirm_password)
        customer_info.close()
        print('\nYou have successfully registered!')

    try:
        leave=int(input("\nType '2' to exit the page: "))
        while leave != 2:
            leave=int(input("\nType '2' to exit the page: "))
        else:
            menu()
            
    except:
        print('\nInvalid input')
        menu()
        
  
def login_customer():
    
    print('\n===============Welcome back to OCEAN SDN BHD! Please enter your USER ID and password to login.===============')
    print("\nIf you do not have an account type '1' to register. Type '2' to continue.")

    choice=input('\nChoice: ')
    try:
        choice=int(choice)
    except:
        print('\nInvalid input')
        login_customer()
        
    if choice == 1:
        new_customer()
        
    elif choice == 2:
        try:
            customer_login=open('Customer detail.txt','r')
        except:
            print('\nError! This file does not exist.')
            login_customer()
        user_ID=input('\nUSER ID: ')
        customer_login_password=input('\nPassword: ')
        lines=customer_login.readlines()
        customer_list=[]
  
        for line in lines:
            customer_list.append(line.strip())
    
    
        for line in customer_list:
            if (user_ID + ', ' + customer_login_password) in customer_list:
                print('\nWelcome to OCEAN SDN BHD!' + ' ' + user_ID + '!')
                customer_menu()
            else:
                print('\nError! Wrong USER ID or password.')
                login_customer()
    else:
        print('\nInvalid input')
        login_customer()

    customer_login.close()
        
    
def customer_menu():

    while True:
        print('\nWe are a Malaysian leading company to manage pharmacy functionalities.')
        print('\nYou may select a type of function from the options below by entering the number.')
        print()
        print('\t1. View medicine detail\n \t2. Order medicines\n \t3. View order\n \t4. View personal information\n \t5. Exit\n')

        choice=input('\nFunctions: ')
        try:
            choice=int(choice)
        except:
            print('\nInvalid input')
            customer_menu()

        if choice < 1 or choice > 5:
            print("\nThis is an invalid input! Please choose '1 or 2 or 3' to select the user from the options above.")
        
        elif choice == 1:
            customer_view_medicine()
            break
            
        elif choice == 2:
            order_medicines()
            break
        
        elif choice == 3:
            view_order()
            break
            
        elif choice == 4:
            view_personal_info()
            break

        elif choice == 5:
            menu()
            break
            
def upload_medicine_detail():
    
    print('\nYou have chosen to upload medicine detail.')
    try:
        Medicine_list=open('Medicine list.txt','a')
        Medicine_price=open('Medicine price.txt','a')
    except:
        print('\nError')
        upload_medicine_detail()
        
    medicine_name=input('\nMedicine name: ')
    Medicine_list.write('\n' + 'Medicine name: ' + medicine_name + ',' + ' ')
    Medicine_price.write(medicine_name + '\n')
    
    specifications_of_medicine=input('\nSpecifications: ')
    Medicine_list.write('Specifications: ' + specifications_of_medicine + ',' + ' ')
    
    medicine_price=input('\nMedicine price: RM ')
    try:
        medicine_price=float(medicine_price)
        while medicine_price <= 0:
            print('\nInvalid input!')
            medicine_price=input('\nMedicine price: RM ')
        else:
            pass
        
    except:
        print('\nInvalid input')
        upload_medicine_detail()
    
    Medicine_list.write('Medicine price: RM ' + str(medicine_price) + ',' + ' ')
    Medicine_price.write(str(medicine_price) + '\n')  
    medicine_expiry_date=input('\nExpiry date (DD/MM/YY): ')
    Medicine_list.write('Expiry date (DD/MM/YY): ' + medicine_expiry_date + ' ')
    
    print('\nThe medicine details has been saved successfully.')
    Medicine_list.close()
    Medicine_price.close()

    choice=input("\nType '1' to continue uploading medicine. Type '2' to exit: ")
    try:
        choice=int(choice)
        while choice != 1 and choice != 2:
            print('\nError!')
            choice=int(input("\nType '1' to continue uploading medicine. Type '2' to exit: "))
        
        while choice == 1:
            upload_medicine_detail()
            
        if choice == 2:
            admin_system()
    except:
        print('\nInvalid input')
        upload_medicine_detail()
        

def view_all_medicines():
    
    print('\nYou have chosen to view medicine detail.')
    
    try:
        Medicine_list=open('Medicine list.txt','r')
        open_Medicine_list=Medicine_list.readlines()
    except:
        print('\nError! This file does not exist.')

    for i in open_Medicine_list:
        print('\n' + i)

    choice=int(input("\nType '2' to exit: "))
    try:
        choice=int(choice)
        while choice != 2:
            choice=int(input("\nType '2' to exit: "))
        else:
            admin_system()

    except:
        print('\nInvalid input')
        view_all_medicines()
    Medicine_list.close()
        

def update_medicine_information():

    print('\nYou have chosen to update medicine information.')
    print()
    try:
        medicine_list=open('Medicine list.txt','r')
        a=medicine_list.readlines()
    except:
        print('\nError! File does not exist')

    for i in a:
        print('\n' + i)
    
    print('\nSearch the medicine that you want to update')
    search_medicine=input('\nSearch: ').lower()
   
    if search_medicine =='':
        print('\nError! Do not leave it blank!')
        update_medicine_information()
    else:
        open_file=open('Medicine list.txt','w')

    for line in a:
        print(line)
        if not line.lower().startswith('medicine name: ' + search_medicine):
            open_file.write(line + '\n')
    medicine_list.close()
    open_file.close()
    
                    
def delete_medicine_information():

    print('\nYou have chosen to delete medicine.')
    try:
        medicine_list=open('Medicine list.txt','r')
        b=medicine_list.readlines()
    except:
        print('\nError! File does not exist')

    for i in b:
        print('\n' + i)
       
    print('\nSearch the medicine that you want to delete')
    search_medicine=input('\nSearch: ').lower()
    
    if search_medicine =='':
        print('\nError! Do not leave it blank!')
        delete_medicine_information()
    else:
        open_file=open('Medicine list.txt','w')

    for line in b:
        if not line.lower().startswith('medicine name: ' + search_medicine):
            open_file.write(line + '\n')
    medicine_list.close()
    open_file.close()
    print('\nThe medicine has been deleted successfully.')
    admin_system()


def search_medicine_details():
    
    print('\nYou have chosen to search medicine information.')
    print()
    try:
        file = open('Medicine list.txt','r')
        c=file.readlines()
    except:
        print ('Error! File cannot be opened:')
        search_medicine_details()
        
    for i in c:
        print('\n' + i)
        
    search = input('\nSearch medicine: ').lower()
    print()
    
    for line in c:
        if line.lower().startswith('medicine name: ' + search):
            print()
            print(line)
    file.close()

    choice=input("\nType '1' to continue searching medicine information. Type '2' to exit: ")
    try:
        choice=int(choice)
        while choice != 1 and choice != 2:
            choice=int(input("\nType '1' to continue searching medicine information. Type '2' to exit: "))    
        
        while choice ==1:
            search_medicine_details()
        
        if choice ==2:
            admin_system()
    except:
        print('\nInvalid input')
        search_medicine_details()


def view_customers_orders():
    
    print("\nYou have chosen to view customers' orders.")
    print()
    try:
        customer_order=open('Customers orders.txt','r')
    except:
        print('\nError! File does not exist.')
        
    open_customer_order=customer_order.read()
    print(open_customer_order)

    choice=input("\nType '2' to exit: ")
    try:
        choice=int(choice)
        while choice != 2:
            choice=int(input("\nType '2' to exit: "))
        else:  
            admin_system()
    except:
        print('\nInvalid input')
        view_customers_orders()
    customer_order.close()

        
def search_customers_orders():
    
    while True:
        print("\nYou have chosen to search customers' orders.")
        print('\nIf you want to exit then press enter.')
        try:
            order = open('Customers orders.txt','r')
            Customer = order.readlines()
        except:
            print ('\nError! File cannot be opened:')
            
        for i in Customer:
            print('\n' + i)
                  
        search = input("\nSearch customers' USER ID: ")        
    
        for line in Customer:
            if line.startswith('USER ID: ' +search):
                print()
                print(line)
        if search =='':
            admin_system()
        else:
            continue
            
    order.close()

    
def customer_view_medicine():

    print('\nYou have chosen to view medicine detail.')
    print()
    try:
        Medicine_list=open('Medicine list.txt','r')
        open_Medicine_list=Medicine_list.readlines()
    except:
        print('\nError! The file does not exist.')

    for i in open_Medicine_list:
        print('\n' + i)
        
    choice=input("\nType '2' to exit: ")
    try:
        choice=int(choice)
        while choice != 2:
            choice=int(input("\nType '2' to exit: "))
        else:  
            customer_menu()
    except:
        print('\nInvalid input')
        customer_view_medicine()

    Medicine_list.close()


def order_medicines():

    print('\nYou have chosen to order medicine.')
    print('\nThe list below shows the medicines we sell.')
    
    try:
        medicine_list=open('Medicine list.txt','r')
        open_medicine_list=medicine_list.readlines()
    except:
        print('\nError! This file does not exist.')

    for i in open_medicine_list:
        print('\n' + i)
    
    print('\nType in the search bar to search the medicine information that you want to buy.')
    search= input("\nSearch medicine: ").lower()
    
    for line in open_medicine_list:
        if line.lower().startswith('medicine name: ' + search): 
            print()
            print(line)
    medicine_list.close()
        
    try:
        medicine_file=open('Customers orders.txt','a')
    except:
        print('\nError! This file does not exist.')

    print('\nDo you want to order this medicine?')

    choice=input("\nType '1' to continue. Type '2' to search again: ")
    try:
        choice=int(choice)
        if choice ==1:
            pass
                         
        elif choice ==2:
            order_medicines()
            
    except:
        print('\nError!')
        order_medicines()
        
    name=input('\nEnter your USER ID: ')
    place_order=input('\nEnter medicine name to order: ')
    try:
        quantity=int(input('\nEnter quantity: '))
    except:
        print('\nInvalid input!')
        order_medicines()
        
    medicine_file.write('\n' + 'USER ID: ' + name + ',' + ' ' + 'Order:  ' + place_order.lower() + ',' + ' '+ 'Quantity: ' + str(quantity) + '\n')
    medicine_file.close()

    choice=input("\nType '1' to make payment: ")

    while choice != '1':
        choice=input("\nType '1' to make payment: ")
            
    if choice == '1':
        pay(place_order,quantity)
        
    else:
        print('\nInvalid input!')
        order_medicines()    
            
   
def view_order():

    print('\nYou have chosen to view your order.')
    
    try:
        customers_orders = open('Customers orders.txt','r')
    except:
        print('\nError! This file does not exist.')
        
    print('\nSearch your order by entering your USER ID')
    
    try:
        search = input("\nSearch USER ID: ")
        if search =='':
            print('\nError! Please enter your USER ID.')
            view_order()
        else:
            pass
        
    except:
        print('\nInvalid input')
        view_order()
        
    for line in customers_orders:
        if line.startswith('USER ID: ' + search):
            print()
            print(line)
    customers_orders.close()
    customer_menu()

    
def view_personal_info():

    print('\nYou have chosen to view your personal information.')

    try:
        personal_info = open('New customer.txt','r')
    except:
        print('\nError! This file does not exist.')

    print('\nType your USER ID to view your personal information')
    search = input("\nSearch your USER ID: ")
    
    for line in personal_info:
        line = line.rstrip()
        if not search in line: 
            continue
        print()
        print(line)
    personal_info.close()
    customer_menu()
        

def pay(place_order,quantity):

    print('\nYou have chosen to pay for your order.')

    try:
        order=open('Customers orders.txt','r')
        medicine=open('Medicine price.txt','r')
    except:
        print('\nError! This file does not exist.')
        pay(place_order,quantity)

    customer_order=order.readlines()
    customer_list=[]
    for line in customer_order:
        customer_list.append(line.strip())

    print('\nEnter your USER ID to confirm your order: ')
    search=input('\nSearch USER ID: ')

    for line in customer_list:
        if line.startswith('USER ID: ' + search): 
            print()
            print(line)
            break
        
    print('\nPlease confirm your order.')

    medicine_price=[]
    for line in medicine:
        medicine_price.append(line.strip())

    for a in range(0,len(medicine_price),2):
        if place_order == medicine_price[a]:
            total=(quantity * float(medicine_price[a+1]))
            print('\nTotal= RM ' + str(total))

    choice=input("\nType '1' to confirm and pay: ")
    try:
        choice=int(choice)
        while choice != 1:
            choice=int(input("\nType '1' to confirm and pay: "))
            
        else:
            print('\nPayment done!')
            print('\nThank you for choosing OCEAN SDN BHD')
            
    except:
        print('\nInvalid input!')
        pay(place_order,quantity)

    choice=input("\nType '1' to continue buying. Type '2' to exit: ")
    try:
        choice=int(choice)
        while choice != 1 and choice != 2:
            choice=int(input("\nType '1' to continue buying. Type '2' to exit: "))
            
        if choice ==1:
            order_medicines()
            
        elif choice ==2:
            print('\nThank you for choosing OCEAN SDN BHD')
            menu()
            
    except:
        print('\nInvalid input!')
        menu()
        
menu()


    














































































































































































































































    



