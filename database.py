import cx_Oracle

class database:

    def __init__(self):
        con=cx_Oracle.connect('CODECHUCKS/123')
        cur=con.cursor()
        cur.execute("CREATE TABLE APPLICANT(ID VARCHAR(10) ,uname VARCHAR(15),PASSWORD VARCHAR(15),PHONE_NUMBER NUMBER(10))")
        cur.execute("insert into applicant values('1','Aravind','Aravind@11','8870003381')")
        cur.execute("insert into applicant values('2','Ashwin','Ashwin@11','9870003381')")
        cur.execute("insert into applicant values('3','Arun','Arun@11','7870003381')")
        cur.execute("insert into applicant values('4','Arav','Arav@11','9970003381')")
        cur.execute("insert into applicant values('5','ravind','ravind@11','7770003381')")
        cur.execute("CREATE TABLE JOB(NAME VARCHAR(20),DOB VARCHAR(20),DEGREE VARCHAR(20),SK1 VARCHAR(20),SK2 VARCHAR(20),SK3 VARCHAR(30))")
        con.commit()
