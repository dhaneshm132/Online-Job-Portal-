from tkinter import *
import cx_Oracle
class loginpage:
    
    valid=0
     

    def __init__(self):
        top =Tk()
        top.title("Online Job Portal")
       
        def admin():
            a=list()
            
            toppp=Tk()
            con=cx_Oracle.connect('CODECHUCKS/123')
            cur=con.cursor()
            L1=Label(toppp,text="Enter Criteria")
            L1.place(relx=0.3, rely=0.1, anchor=CENTER)
            criteria=Entry(toppp,width=20)
            criteria.place(relx=0.45, rely=0.1, anchor=CENTER)
           
            cri=str(criteria.get())
            def disp():
                cur.execute("select * from job order by sk1 asc")
                for i in cur:
                    print(i)
            submt=Button(toppp,text="submit",command=disp)
            submt.place(relx=0.60, rely=0.1, anchor=CENTER)
            
            
            
            
        def loggedin():
            
            def close():
                self.valid=1
                topp.destroy()
            def send():  
                con=cx_Oracle.connect('CODECHUCKS/123@xe')
                cur=con.cursor()
                a=name.get()
                b=dob.get()
                c=degree.get()
                d=sk1.get()
                e=sk2.get()
                f=sk3.get()
                cur.execute("""insert into job values('%s','%s','%s','%s','%s','%s')"""%(a,b,c,d,e,f))
                con.commit()
        
            topp=Tk()
            topp.title("Online Job Portal")
            
            
            #labels
            L1=Label(topp,text="Enter Your Details")
            L2=Label(topp,text="Name:")
            L3=Label(topp,text="DOB:")
            L4=Label(topp,text="Degree")
            L5=Label(topp,text="Skillset1")
            L6=Label(topp,text="Skillset2")
            L7=Label(topp,text="Skillset3")
            
            L1.place(relx=0.3, rely=0.1, anchor=CENTER)
            L2.place(relx=0.3, rely=0.3, anchor=CENTER)
            L3.place(relx=0.3, rely=0.4, anchor=CENTER)
            L4.place(relx=0.3, rely=0.5, anchor=CENTER)
            L5.place(relx=0.3, rely=0.6, anchor=CENTER)
            L6.place(relx=0.3, rely=0.7, anchor=CENTER)
            L7.place(relx=0.3, rely=0.8, anchor=CENTER)
            #entries
            name=Entry(topp,width=20)
            dob=Entry(topp,width=20)
            degree=Entry(topp,width=20)
            sk1=Entry(topp,width=20)
            sk2=Entry(topp,width=20)
            sk3=Entry(topp,width=20)
            name.place(relx=0.45, rely=0.3, anchor=CENTER)
            dob.place(relx=0.45, rely=0.4, anchor=CENTER)
            degree.place(relx=0.45, rely=0.5, anchor=CENTER)
            sk1.place(relx=0.45, rely=0.6, anchor=CENTER)
            sk2.place(relx=0.45, rely=0.7, anchor=CENTER)
            sk3.place(relx=0.45, rely=0.8, anchor=CENTER)
            submit=Button(topp,text="Submit",command=send)
            submit.place(relx=0.45, rely=0.9, anchor=CENTER)
            back=Button(topp,text="Back",command=close)
            back.place(relx=0.45, rely=1, anchor=CENTER)        
            topp.geometry('350x200')
            topp.mainloop()


        
        def validate():
            
            con=cx_Oracle.connect('CODECHUCKS/123')
            cur=con.cursor()
            x=str(ID.get())
            if(str(PASS.get())=='infosys' and str(ID.get())=='i'):
                top.destroy()
                admin()

            else:
                
                cur.execute("SELECT PASSWORD FROM APPLICANT WHERE ID='%s'"%x)
            
                pasw=cur.fetchall()
               # print(+str(PASS.get())+str(ID.get()))
            
                if(str(pasw[0][0])==str(PASS.get())): 
                   top.destroy()
                   loggedin()
               

            
        L1=Label(top,text="ID") 
        L2=Label(top,text="Password")
        ID=Entry(top,width=20)
        PASS=Entry(top,show="*",width=20)
        
        loginbtn= Button(top,text="LOGIN",command=validate)

        L1.place(relx=0.3, rely=0.4, anchor=CENTER)
        L2.place(relx=0.3, rely=0.5, anchor=CENTER)
        ID.place(relx=0.4, rely=0.4, anchor=CENTER)
        PASS.place(relx=0.4, rely=0.5, anchor=CENTER)
        loginbtn.place(relx=0.35, rely=0.6, anchor=CENTER)

        top.geometry('350x200')
        top.mainloop()

        

