from tkinter import *

class startingpage:
    islogin=0
    isregister=0

 

    def __init__(self):
        top =Tk()
        top.title("Online Job Portal")   
        #loginbtn.grid(column=0,row=)
        def login():
            self.islogin=1
            top.destroy()

        def register():
            self.isregister=1
            top.destroy()



        loginbtn= Button(top,text="LOGIN",command=login)
        loginbtn.place(relx=0.5, rely=0.4, anchor=CENTER)

        loginbtn= Button(top,text="REGISTER",command=register)
        loginbtn.place(relx=0.5, rely=0.55, anchor=CENTER)
        top.geometry('350x200')
        top.mainloop()

        

