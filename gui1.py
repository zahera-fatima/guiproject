import tkinter as tk
from tkinter import ttk
from csv import DictWriter
import os
win = tk.Tk()
win.title('GUI')
# create label
#widget for button radiobutton---- import ttk
name_label = ttk.Label(win, text='Enter your name: ')
name_label.grid(row=0, column=0, sticky=tk.W)
email_label = ttk.Label(win, text='Enter your email: ')
email_label.grid(row=1, column=0, sticky=tk.W)
age_label = ttk.Label(win, text='Enter your age: ')
age_label.grid(row=2, column=0, sticky=tk.W)
gender_label = ttk.Label(win, text='select your gender: ')
gender_label.grid(row=3, column=0, sticky=tk.W)

#create entry box

name_var = tk.StringVar() 
name_entrybox = ttk.Entry(win, width=16, textvariable = name_var)
name_entrybox.grid(row=0, column=1)
name_entrybox.focus()
email_var = tk.StringVar() 
email_entrybox = ttk.Entry(win, width=16, textvariable = email_var)
email_entrybox.grid(row=1, column=1)
age_var = tk.StringVar() 
age_entrybox = ttk.Entry(win, width=16, textvariable = age_var)
age_entrybox.grid(row=2, column=1)

# create combobox
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(win, width=14, textvariable=gender_var, state='readonly')
gender_combobox['values'] = ('Male', 'Female', 'Other')
gender_combobox.current(0)
gender_combobox.grid(row=3, column=1)

#radio button
usertype = tk.StringVar()
radiobtn1 = ttk.Radiobutton(win, text='Student', value='Student', variable=usertype)
radiobtn1.grid(row=4, column =0)
radiobtn2 = ttk.Radiobutton(win, text='Teacher', value='Teacher', variable=usertype)
radiobtn2.grid(row=4, column =1)

#check button
checkbtn_var = tk.IntVar()
checkbtn = ttk.Checkbutton(win, text='check if you want to subscribe to our newsletter', variable=checkbtn_var)
checkbtn.grid(row=5, columnspan=3)

# create button
#write to csv file
def action():
    user_name = name_var.get()
    user_age = age_var.get()
    user_email = email_var.get()
    user_gender = gender_var.get()
    user_type = usertype.get()
    if checkbtn_var.get() == 0:
         subscribed ='NO'
    else:
         subscribed = 'YES'
    with open('filee.csv','a', newline='') as f:
        dict_writer = DictWriter(f, fieldnames=['UserName','User Age','User Email Address',
        'User Gender','User Type','Subscribed'])
        if os.stat('filee.csv').st_size==0:
             dict_writer.writeheader()
        
        dict_writer.writerow({
            'UserName':user_name ,
            'User Age':user_age,
            'User Email Address':user_email,
            'User Gender':user_gender,
            'User Type':user_type,
            'Subscribed':subscribed
        })
    name_entrybox.delete(0, tk.END)
    age_entrybox.delete(0, tk.END)
    email_entrybox.delete(0, tk.END)
    
    
    # name_label.configure(foreground='#b388ff')

submit_button = tk.Button(win, text='Submit', command=action)
submit_button.grid(row=6, column=0)
submit_button.configure(background='Blue')
win.mainloop()