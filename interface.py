from tkinter import *

win_LOGIN = Tk()

win_LOGIN.title("LOGIN")


#--------text for new account
text_for_login = Label(win_LOGIN, text="             If u don't have an account please create one by press in (New Account).           ")
text_for_login.grid(row=0, column=0, columnspan=3)

#-------- CIN
CIN_text = Label(win_LOGIN, text="CIN :")
CIN_text.grid(row=1, column=0)

CIN_input = Entry(win_LOGIN, width=30, borderwidth=3)
CIN_input.insert(0, "Enter your CIN :")
CIN_input.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

#-------- Password
CIN_text = Label(win_LOGIN, text="PASSWORD :")
CIN_text.grid(row=2, column=0)

PSW_input = Entry(win_LOGIN, width=30, borderwidth=3)
PSW_input.insert(0, "Enter your PSW :")
PSW_input.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

#------login
def LOGIN():
    cin = CIN_input.get()
    CIN_input.delete(0, END)
    PSW_input.delete(0, END)
    return cin,

#--------register
def New_Account():

    win_new_account = Toplevel()
    win_new_account.title("Create New Account")

    #-----first name
    first_name_text = Label(win_new_account, text="First Name :")
    first_name_text.grid(row=0, column=0)

    first_name_input = Entry(win_new_account, width=30, borderwidth=3)
    first_name_input.insert(0, "Enter your First name :")
    first_name_input.grid(row=0, column=1, padx=5, pady=5)

    #-----last name
    last_name_text = Label(win_new_account, text="last Name :")
    last_name_text.grid(row=1, column=0)

    last_name_input = Entry(win_new_account, width=30, borderwidth=3)
    last_name_input.insert(0, "Enter your last name :")
    last_name_input.grid(row=1, column=1, padx=5, pady=5)

    #-------CIN
    cin_text = Label(win_new_account, text="CIN :")
    cin_text.grid(row=2, column=0)

    cin_input = Entry(win_new_account, width=30, borderwidth=3)
    cin_input.insert(0, "Enter your CIN :")
    cin_input.grid(row=2, column=1, padx=5, pady=5)

    #-----password
    psw_text = Label(win_new_account, text="Password :")
    psw_text.grid(row=3, column=0)

    psw_input = Entry(win_new_account, width=30, borderwidth=3)
    psw_input.insert(0, "Enter your Password :")
    psw_input.grid(row=3, column=1, padx=5, pady=5)



    # --------Button for register
    register_button = Button(win_new_account, text="REGISTER", width=30, borderwidth=4)
    register_button.grid(row=5, column=0)

    # --------Button for Cancel
    cancel_button = Button(win_new_account, text="Back to login", width=10, borderwidth=4, command=win_new_account.destroy)
    cancel_button.grid(row=5, column=1)





#--------Button for login
login_button = Button(win_LOGIN, text="LOGIN", width=30, borderwidth=4, command=LOGIN)
login_button.grid(row=3, column=0, columnspan=2)

#--------Button for new account
NEW_ACCOUNT_button = Button(win_LOGIN, text="New Account", width=10, borderwidth=4, command=New_Account)
NEW_ACCOUNT_button.grid(row=3, column=2, columnspan=1)




win_LOGIN.mainloop()

