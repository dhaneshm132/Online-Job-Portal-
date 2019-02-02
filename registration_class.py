from tkinter import *
from tkinter import messagebox
import cx_Oracle

class registration:

    isclosed=0
    def __init__(self):
        top=Tk()
        top.title("Online Job Portal")
        L1=Label(top,text="Enter Your Details")
        L1.grid(column=5,row=0)
        #labels
        L2=Label(top,text="Name:")
        L3=Label(top,text="Phone Number:")
        L4=Label(top,text="Password")
        L5=Label(top,text="Re-Enter Password")
        L6=Label(top,text="")

        #displaying grid
        L2.grid(column=0,row=1)
        L3.grid(column=0,row=2)
        L4.grid(column=0,row=3)
        L5.grid(column=0,row=4)
        L6.grid(column=0,row=6)

        #text fields
        uname=Entry(top,width=20)
        uname.grid(column=1,row=1)
        uname.focus();
        phonenumber=Entry(top,width=20)
        phonenumber.grid(column=1,row=2)
        password=Entry(top,show="*",width=20)
        password.grid(column=1,row=3)
        repassword=Entry(top,show="*",width=20)
        repassword.grid(column=1,row=4)
 
        #validating credentials
        def validate_pass(password):
            if (len(password)<8): 
                flag=0  
            elif not re.search("[a-z]", password): 
                flag=0   
            elif not re.search("[A-Z]", password): 
                flag=0    
            elif not re.search("[0-9]", password): 
                flag=0   
            elif not re.search("[_@$#%^&*!]", password): 
                flag=0   
            else:
                flag=1

            return flag

        def validate_phone(phone):
            if(len(phone)==10):
                if(phone.isdigit()):
                    return 1
                else:
                    return 0

        #end of validation  

        def get_values():
            name=uname.get()
            phno=phonenumber.get()
            passw=password.get()
            repassw=repassword.get()

        #button action
        def submit():
            
            #getting values
            get_values()

            #checking credentials
            passflag=0
            phoneflag=0
            passflag=validate_pass(password.get())
            phoneflag=validate_phone(phonenumber.get())
            if(passflag==0 or phoneflag==0):
              messagebox.showwarning("warning","INVALID password/phonenumber")
              L1.configure(text="RE-Enter values")
            else:
              con=cx_Oracle.connect('CODECHUCKS/123')
              cur=con.cursor()
              #cur.execute("create sequence app_sequence start with 1 increment by 1")
              cur.execute("insert into applicant values('%s','%s','%s','%s')"%('1',str(uname.get()),str(phonenumber.get()),str(password.get())))
              L1.configure(text="Registration Successful")
        def close():
            self.isclosed=1;
            top.destroy()
            
        #submit button
        btn=Button(top,text="Submit",command=submit)
        btn.grid(column=0,row=5)
        #back button
        back=Button(top,text="Back",command=close)
        back.grid(column=0,row=6)
  
        #window size
        top.geometry('350x200')
        top.mainloop()

    
