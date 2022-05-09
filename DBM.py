import pymysql as p
def getConnection():
    return p.connect(host='localhost',user='root',password='',database='sagar')
    
def addEmp(t):
    db=getConnection()
    sql='insert into sag values(%s,%s,%s,%s,%s)'
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()

def selectAllEmp():
    db=getConnection()
    sql='select * from sag'
    cr=db.cursor()
    cr.execute(sql)
    elist=cr.fetchall()
    db.commit()
    db.close()
    return elist

    
def deleteEmp(id):
    db=getConnection()
    sql='delete from sag where id=%s'
    cr=db.cursor()
    cr.execute(sql,id)
    db.commit()
    db.close()

def selectEmpById(id):
    db=getConnection()
    sql='select * from sag where id=%s'
    cr=db.cursor()
    cr.execute(sql,id)
    elist=cr.fetchall()
    db.commit()
    db.close()
    return elist[0]

def updateEmp(t):
    db=getConnection()
    sql='update sag set name=%s,contact=%s,email=%s,passw=%s where id=%s'
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()

def log(t):
    db=getConnection()
    sql="select name,passw from sag where name=%s and passw=%s"
    cr=db.cursor()
    cr.execute(sql,t)
    data=cr.fetchall()
    db.commit()
    db.close()
    return data
