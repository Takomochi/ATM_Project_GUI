# ATM Project GUI

## Overview of the project
In this project, I have created ATM system by using tkinter. Main functions are sign up, log in, deposit & withdraw money, check balance, and account detail. All the accounts created are stored in clients folder as text files.

## Resouces
- Software : Python 3.7.10, Visual Studio Code
- Libraries: tkinter, os, Image, datetime, re

## Functions
### 1. Main page
The image below is the initial page. <br>
There are log in an sigh up buttons to choose.

<img width="250" alt="home_page" src="https://user-images.githubusercontent.com/85041697/149207996-8dddf65c-6611-416f-8b35-4a6cbad16e89.png">

### 2. Sign up 

There are some validations for sign up.
1. Email must be in an appropriate format.
    ```
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    ```
2. Password must be more than 6 characters.
    ```
    elif len(password) < 6:
        notif.config(fg='red',text="Password has to be more than 6 characters")
    ```
3. Check if the account already exist by checking clients folder
    ```
    accounts = os.listdir('clients')
    for account in accounts:
        account_name = account.split('.txt')[0]
        if email == account_name:
            notif.config(fg='red',text="Account already exists")
    ```

4. All fields are required to be filled


    <img width="350" alt="sign_up" src="https://user-images.githubusercontent.com/85041697/149211882-d0dfa9d2-af6c-43ec-a5ee-136745acc16b.png"> <img width="370" alt="account" src="https://user-images.githubusercontent.com/85041697/149211892-444e2e20-2101-404a-b463-d860a4a945f1.png">

    When you click submit button, new account text file is going to be created and write input information inside the text file. In the image on right side, we can see name, date of birth, age, email, password, and balance. Age is calculated from date of birth. Balance is automatically set as '0'.

### 3. Log in
Once you log in, the account home page will pop up.
There are four options you can choose.

<img width="301" alt="log_in" src="https://user-images.githubusercontent.com/85041697/149217512-4e411329-0839-457e-88c2-cbd031d662eb.png"> <img width="200" alt="account_home" src="https://user-images.githubusercontent.com/85041697/149217520-f07f7d6f-98f9-4648-90fd-0a1b6cf0bf3b.png">

### 4. Deposit
In deposit page, you can type the amount of money you want to deposit. If the input is empty or the input is alphabet, it will give you error message. Click "Deposit" button, system will automatically read the account text file and add current balance and input amount (0 + 500 = 500). In account balance, we can see the balance $500 is in the account.

<img width="291" alt="deposit" src="https://user-images.githubusercontent.com/85041697/149219187-90d24f95-50a7-4582-9a27-759deaee56bf.png">
<img width="300" alt="balance" src="https://user-images.githubusercontent.com/85041697/149221104-1be72763-fa44-4465-93ac-c8f2edae3f4f.png">

### 5. Withdrawal
Withdrawal page works similar way to deposit page. Check balance again, we can see that $100 withdrawal is successfully done.

<img width="304" alt="withdraw" src="https://user-images.githubusercontent.com/85041697/149221391-294df9bb-7327-412e-a7c0-0a1a37b21f7c.png"> <img width="300" alt="balance_withdraw" src="https://user-images.githubusercontent.com/85041697/149222870-5777493e-6e9b-4cfe-aee0-317b638f46fd.png">

### 6. Account Detail
The image below is the account detail page.
There are options to change email and password.

<img width="250" alt="user_details" src="https://user-images.githubusercontent.com/85041697/149224166-1b20ad9e-4dda-4c9d-be32-a22b363961e8.png">


**Change email**<br>
There is a validation to check if the new email is in proper format. If it is not valid, it will give error message.
Click "Change Email" button, system will cheange the account text file name and email inside the file.

<img width="374" alt="change_email" src="https://user-images.githubusercontent.com/85041697/149225309-995d5e31-ccc3-4ee2-85d0-89548f201703.png"> <img width="370" alt="change_email_text" src="https://user-images.githubusercontent.com/85041697/149225313-240cb3c8-c2bd-4d95-8fae-32d410531730.png">

**Change Password**<br>
There is the sanme validation with sign up for password. Also it will check if the old password is correct. Click "Change Password" button, system will change the password information inside the account text file.

<img width="372" alt="change_password" src="https://user-images.githubusercontent.com/85041697/149230218-06d248d0-fc55-4221-a14f-62fce1be716e.png"> <img width="370" alt="change_password_txt" src="https://user-images.githubusercontent.com/85041697/149226339-91c99ef2-dc1e-4278-8887-b8a65b10a1bf.png">
