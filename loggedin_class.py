from tkinter import *

class loggedin_class:
    def __init__(self):



        top=Tk()
        top.title("Online Job Portal")
        L1=Label(top,text="Enter Your Details")
        L1.grid(column=5,row=0)
        #labels
        L2=Label(top,text="Name:")
        L3=Label(top,text="DOB:")
        L4=Label(top,text="Degree")
        L5=Label(top,text="Skillset 1")
        L5=Label(top,text="Skillset2")
        L6=Label(top,text="Skillset3")
        L1.place(relx=0.3, rely=0.2, anchor=CENTER)
        L2.place(relx=0.3, rely=0.3, anchor=CENTER)
        L3.place(relx=0.3, rely=0.4, anchor=CENTER)
        L4.place(relx=0.3, rely=0.5, anchor=CENTER)
        L5.place(relx=0.3, rely=0.6, anchor=CENTER)
        L6.place(relx=0.3, rely=0.7, anchor=CENTER)
        #entries
        name=Entry(top,width=20)
        dob=Entry(top,width=20)
        degree=Entry(top,width=20)
        sk1=Entry(top,width=20)
        sk2=Entry(top,width=20)
        sk3=Entry(top,width=20)
        name.place(relx=0.45, rely=0.2, anchor=CENTER)
        dob.place(relx=0.45, rely=0.3, anchor=CENTER)
        degree.place(relx=0.45, rely=0.4, anchor=CENTER)
        sk1.place(relx=0.45, rely=0.5, anchor=CENTER)
        sk2.place(relx=0.45, rely=0.6, anchor=CENTER)
        sk3.place(relx=0.45, rely=0.7, anchor=CENTER)
        submit=Button(top,text="Submit",command=send)
        loginbtn.place(relx=0.45, rely=0.6, anchor=CENTER)
                
        top.geometry('350x200')
        top.mainloop()


obj=loggedin_class()
