from startingpage_class import startingpage
from registration_class import registration
from loginpage_class import loginpage
from database import database
import cx_Oracle

def db():
     obj=database()

def startup():
    st=startingpage()
    if(st.islogin==1):
        obj1=loginpage()
        if(obj1.valid==1):
            startup()
    elif(st.isregister==1):
        obj=registration()
        if(obj.isclosed==1):
            startup()


db()            
startup()


