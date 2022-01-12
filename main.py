# ATM GUI application

# Import dependancies
import os
from tkinter import *
from tkinter import font
from PIL import ImageTk, Image
from tkinter import messagebox
import datetime
from datetime import date
import re

# Initial window
root = Tk()
root.title("Shimbank app")

# Image import
img = Image.open('Resources/undraw_Savings_re_eq4w.png')
img = img.resize((250,180))
img = ImageTk.PhotoImage(img)

# Function to withdraw the amount of money
def sub_withd():
    withd_amount = t_withd_amount.get()
    current_balance = lines[5].strip()

    save_path = './clients/'
    file_name = log_email+'.txt'
    completeName = os.path.join(save_path, file_name)
    
    if withd_amount.isalpha():
        notif.config(fg='red',text='Input must be numbers')
    elif withd_amount == '':
        notif.config(fg='red',text='Plase input the amount of money \nyou would like to withdraw')
    
    else:
        new_balance = int(current_balance) - int(withd_amount)

        with open(completeName,'r') as file:
            data = file.readlines()

        data[5] = str(new_balance)+'\n'

        with open(completeName, 'w') as file:
            file.writelines(data)

        notif.config(fg='green',text='Withdrawing $ '+ withd_amount)

# withdrawal page
def withdrawal():
    global t_withd_amount
    global notif
    t_withd_amount = StringVar()
    current_balance = lines[5].strip()

    withdrawal_screen = Toplevel(root)
    withdrawal_screen.title("withdrawal")

    if current_balance == '0':
        messagebox.showwarning('Balance 0','Your current balance is 0. \n Please deposit money first')

    Label(withdrawal_screen, text="How much would you like to withdraw?", font=('Calibri',16)).grid(row=0, pady=10, padx=30,sticky=N)
    Entry(withdrawal_screen, textvariable=t_withd_amount, font=('Calibri',14)).grid(row=1, padx=5)
    Button(withdrawal_screen, text="withdraw",font=('Calibri',14),command=sub_withd).grid(row=2, padx=5,pady=10)
    notif = Label(withdrawal_screen, font=('Calibri',12))
    notif.grid(row=6, padx=5, pady=10)

# Function to deposit input money
def add_deposit():
    depo_amount = t_depo_amount.get()
    current_balance = lines[5].strip()

    save_path = './clients/'
    file_name = log_email+'.txt'
    completeName = os.path.join(save_path, file_name)
    
    if depo_amount.isalpha():
        notif.config(fg='red',text='Input must be numbers')
    elif depo_amount == '':
        notif.config(fg='red',text='Plase input the amount of money \nyou would like to deposit')
    else:
        new_balance = int(current_balance) + int(depo_amount)

        with open(completeName,'r') as file:
            data = file.readlines()

        data[5] = str(new_balance)+'\n'

        with open(completeName, 'w') as file:
            file.writelines(data)

        notif.config(fg='green',text='Successfully deposited $ '+ depo_amount)

# Deposit page
def deposit():
    global t_depo_amount
    global notif
    t_depo_amount = StringVar()

    deposit_screen = Toplevel(root)
    deposit_screen.title("Deposit")

    Label(deposit_screen, text="How much would you like to deposit?", font=('Calibri',16)).grid(row=0, pady=10, padx=30,sticky=N)
    Entry(deposit_screen, textvariable=t_depo_amount, font=('Calibri',14)).grid(row=1, padx=5)
    Button(deposit_screen, text="Deposit",font=('Calibri',14),command=add_deposit).grid(row=2, padx=5,pady=10)
    notif = Label(deposit_screen, font=('Calibri',12))
    notif.grid(row=6, padx=5, pady=10)


# Balance page
def balance():
    balance_screen = Toplevel(root)
    balance_screen.title("Balance")
    Label(balance_screen, text="Your Current Balance", font=('Calibri',16)).grid(row=0, pady=10, padx=30,sticky=N)
    Label(balance_screen, text="CAD$ "+(lines[5]).strip(), font=('Calibri',14)).grid(row=1,pady=10, padx=30)

# Change password
def update_passward():
    c_pass = c_t_pass.get()
    o_pass = o_t_pass.get()

    save_path = './clients/'
    file_name = log_email+'.txt'
    completeName = os.path.join(save_path, file_name)

    if o_pass.strip() == (lines[4].strip()) and len(c_pass) >= 6:
        with open(completeName,'r') as file:
            data = file.readlines()
            data[4] = c_pass+'\n'

        with open(completeName, 'w') as file:
            file.writelines(data)
        notif.config(fg='green',text='Updated your password')

    else:
        notif.config(fg='red',text='Old password is wrong or \n Password must be more than 6 letters')

# Ask for new password
def change_password():
    global c_t_pass
    global o_t_pass
    global notif
    c_t_pass = StringVar()
    o_t_pass = StringVar()

    change_passward_screen = Toplevel(root)
    change_passward_screen.title("Change Password")
    change_passward_screen.geometry('500x250')

    Label(change_passward_screen, text="Old Passward: ", font=('Calibri',14)).grid(row=0, pady=10, padx=30,sticky=N)
    Label(change_passward_screen, text="New Password: ", font=('Calibri',14)).grid(row=1, pady=10,padx=30,sticky=N)

    Entry(change_passward_screen, textvariable=o_t_pass, font=('Calibri',14),show='*').grid(row=0, column=1,pady=10)
    Entry(change_passward_screen,textvariable=c_t_pass, font=('Calibri',14),show='*').grid(row=1,column=1,pady=10)

    Button(change_passward_screen, text="Change Passward", font=('Calibri',14), command=update_passward).grid(row=2,column=1,pady=15,sticky=W)
    notif = Label(change_passward_screen, font=('Calibri',12))
    notif.grid(row=3, padx=10, pady=10,column=1)

# Change email
def update_email():
    c_email = c_t_email.get()

    save_path = './clients/'
    file_name = log_email+'.txt'
    completeName = os.path.join(save_path, file_name)

    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    if c_email != "" and (re.fullmatch(regex, c_email)):
        with open(completeName,'r') as file:
            data = file.readlines()
        data[3] = c_email+'\n'

        with open(completeName, 'w') as file:
            file.writelines(data)

        #change file name
        user_list = os.listdir("./clients")
        if (log_email+'.txt') in user_list:
            os.rename(('./clients/'+log_email+'.txt'),('./clients/'+c_email+'.txt'))
        
        notif.config(fg='green',text='Updated your email address')
    else:
        notif.config(fg='red',text='Email is not valid')

# Ask for new email
def change_email():
    global c_t_email 
    global notif
    c_t_email = StringVar()

    change_email_screen = Toplevel(root)
    change_email_screen.title("Change Email")
    change_email_screen.geometry('500x250')

    Label(change_email_screen, text="Old Email: ", font=('Calibri',14)).grid(row=0, pady=10, padx=30,sticky=N)
    Label(change_email_screen, text="New Email: ", font=('Calibri',14)).grid(row=1, pady=10,padx=30,sticky=N)

    Label(change_email_screen, text=lines[3].strip(), font=('Calibri',14)).grid(row=0, column=1,pady=10)
    Entry(change_email_screen,textvariable=c_t_email, font=('Calibri',14)).grid(row=1,column=1,pady=10)

    Button(change_email_screen, text="Change Email", font=('Calibri',14), command=update_email).grid(row=2,column=1,pady=15,sticky=W)
    notif = Label(change_email_screen, font=('Calibri',12))
    notif.grid(row=3, padx=10, pady=10,column=1)

# Account detail page
def details():
    user_details_screen = Toplevel(root)
    user_details_screen.title("User Details")
    user_details_screen.geometry('400x400')

    Label(user_details_screen, text="Here is your account information", font=('Calibri',16)).grid(row=0, pady=10, padx=30,sticky=N)

    Label(user_details_screen, text="Name:", font=('Calibri',14)).grid(row=1,pady=10,padx=30 ,sticky=W)
    Label(user_details_screen, text="Birht Date:", font=('Calibri',14)).grid(row=2, pady=10, padx=30,sticky=W)
    Label(user_details_screen, text="Age:", font=('Calibri',14)).grid(row=3, pady=10, padx=30,sticky=W)
    Label(user_details_screen, text="Email:", font=('Calibri',14)).grid(row=4, pady=10, padx=30,sticky=W)

    Label(user_details_screen, text=(lines[0]).strip(), font=('Calibri',14)).grid(row=1,pady=10, padx=30,sticky=E)
    Label(user_details_screen, text=(lines[1]).strip() , font=('Calibri',14)).grid(row=2, pady=10,padx=30,sticky=E)
    Label(user_details_screen, text=(lines[2]).strip(), font=('Calibri',14)).grid(row=3, pady=10,padx=30,sticky=E)
    Label(user_details_screen, text=(lines[3]).strip(), font=('Calibri',14)).grid(row=4, pady=10,padx=30,sticky=E)

    Button(user_details_screen, text='Change email', font=('Calibri',14), width=15,command=change_email).grid(row=5,pady=10,padx=30)
    Button(user_details_screen, text='Change password', font=('Calibri',14), width=15,command=change_password).grid(row=6,pady=10,padx=30)


# User's account home page
def user_page():
    # Date for the day
    now = datetime.datetime.now()
    month = now.strftime('%B')
    day = now.strftime('%d')
    year = now.strftime('%Y')
    
    user_page = Toplevel(root)
    user_page.title("Account Home")
    Label(user_page,text="Hi " + (lines[0]).upper() +"\nWhat would you like to do today?", font=('Calibri',16)).grid(row=0,sticky=N, pady=5,padx=50)
    Label(user_page,text=f'Today is {month} {day},{year}',font=('Calibri',14)).grid(row=1, pady=5,padx=50)
    
    Button(user_page, text="Withdrawal",font=('Calibri',14), height=2, width=15, command=withdrawal).grid(row=2, padx=5, pady=10)
    Button(user_page, text="Deposit",font=('Calibri',14), height=2, width=15, command=deposit).grid(row=3, padx=5, pady=10)
    Button(user_page, text="Check Balance",font=('Calibri',14),height=2, width=15, command=balance).grid(row=4, padx=5, pady=10)
    Button(user_page, text="Account details",font=('Calibri',14),height=2, width=15, command=details).grid(row=5, padx=5, pady=10)

# Functions to check log in information
def check_log_in():
    global lines
    global log_email
    log_email = log_t_email.get()
    log_password = log_t_pass.get()
    log_accounts = os.listdir('clients')

    save_path = './clients/'
    file_name = log_email+'.txt'
    completeName = os.path.join(save_path, file_name)

    user_list = []
    for account in log_accounts:
        account_name = account.split('.txt')[0]
        user_list.append(account_name)

    if log_email in user_list:
        with open(completeName,'r') as file:
            lines = file.readlines()
            if log_email ==(lines[3]).strip() and log_password == (lines[4]).strip():
                notif.config(fg='green',text="Successfully logined")
                user_page()
            else:
                notif.config(fg='red',text="Wrong password \n please try again")
    else:
        notif.config(fg='red',text="Account does not exist. \n Please sign up your account first")

# Function to write details for sign up
def write_info():
    global age
    name = t_name.get()
    age = t_age.get()
    email = t_email.get()
    password = t_pass.get()
    accounts = os.listdir('clients')

    if name == "" or age == "" or email == "" or password == "":
        notif.config(fg='red',text="All fields are required")
        return
    elif len(password) < 6:
        notif.config(fg='red',text="Password has to be more than 6 characters")
        return
    
    def calculate_age(born):
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    year = int(age.split('-')[0])
    month = int(age.split('-')[1])
    day = int(age.split('-')[2])

    cal_age = str(calculate_age(date(year, month, day)))

    save_path = './clients/'
    file_name = email+'.txt'
    completeName = os.path.join(save_path, file_name)

    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    for account in accounts:
        account_name = account.split('.txt')[0]
        
        if email == account_name:
            notif.config(fg='red',text="Account already exists")
            return
        elif (re.fullmatch(regex, email)):
            with open(completeName,'w') as new_account:
                new_account.write(name+'\n')
                new_account.write(age+'\n')
                new_account.write(cal_age+'\n')
                new_account.write(email+'\n')
                new_account.write(password+'\n')
                new_account.write('0')
                notif.config(fg='green', text='Thank you for creating your account today!')
        else:
            notif.config(fg='red', text='Email is not valid')

# Input screen for sign up
def sign_up():
    global t_name
    global t_age
    global t_email
    global t_pass
    global notif

    t_name = StringVar()
    t_age = StringVar()
    t_email = StringVar()
    t_pass = StringVar()

    sign_up_screen = Toplevel(root)
    sign_up_screen.geometry('600x350')
    sign_up_screen.title("Sign up")
    Label(sign_up_screen,text="Create your account", font=('Poppins',16)).grid(row=0,sticky=N, pady=20,padx=50)

    Label(sign_up_screen, text='Name',font=('Calibri',14)).grid(row=1,padx=30, sticky=W)
    Label(sign_up_screen, text='Birth Date (yyyy-mm-dd)',font=('Calibri',14)).grid(row=2,padx=30,sticky=W)
    Label(sign_up_screen, text='Email',font=('Calibri',14)).grid(row=3,padx=30,sticky=W)
    Label(sign_up_screen, text='Password (More than 6 characters)',font=('Calibri',14)).grid(row=4,padx=30,sticky=W)
    
    Entry(sign_up_screen, textvariable=t_name, font=('Calibri',14)).grid(row=1,column=1,sticky=E)
    Entry(sign_up_screen, textvariable=t_age, font=('Calibri',14)).grid(row=2,column=1, sticky=E)
    Entry(sign_up_screen, textvariable=t_email, font=('Calibri',14)).grid(row=3, column=1, sticky=E)
    Entry(sign_up_screen, textvariable=t_pass, font=('Calibri',14), show='*').grid(row=4, column=1,sticky=E)

    Button(sign_up_screen, text="Submit",font=('Calibri',14),width=15, command=write_info).grid(row=5, padx=100, pady=20)

    notif = Label(sign_up_screen, font=('Calibri',12))
    notif.grid(row=6, padx=5, pady=5)

# Input screen for log in
def log_in():
    global log_t_email
    global log_t_pass
    global notif
    global log_in_screen

    log_t_email = StringVar()
    log_t_pass = StringVar()

    log_in_screen = Toplevel(root)
    log_in_screen.geometry('400x300')
    log_in_screen.title("Log in")

    Label(log_in_screen,text="Log in your account", font=('Poppins',16)).grid(row=0,sticky=N, pady=20,column=1)
    
    Label(log_in_screen, text='Email',font=('Calibri',14)).grid(row=1, padx=10)
    Label(log_in_screen, text='Password',font=('Calibri',14)).grid(row=2, padx=10)
    Entry(log_in_screen, font=('Calibri',14), textvariable=log_t_email).grid(row=1, column=1)
    Entry(log_in_screen, font=('Calibri',14), textvariable=log_t_pass, show='*').grid(row=2, column=1,pady=10)
    Button(log_in_screen, text='Log in',font=('Calibri',14), width=15,command=check_log_in).grid(row=3, column=1,pady=20)
    notif = Label(log_in_screen, font=('Calibri',12))
    notif.grid(row=4, column=1,padx=5, pady=10)

# Initial Screen
Label(root,text="Welcome to Shimbank!",font=('Poppins',18,'bold')).grid(row=0,sticky=N, pady=10,padx=50)
Label(root, image=img).grid(row=1,pady=10)
Button(root,text="Login",font=('Poppins',12),height=2, width=15,bg='white',command=log_in).grid(row=2, column=0, pady=10)
Button(root,text="Sign up",font=('Poppins',12),height=2, width=15, bg='white',command=sign_up).grid(row=3,column=0,pady=10, padx=50)


root.mainloop()