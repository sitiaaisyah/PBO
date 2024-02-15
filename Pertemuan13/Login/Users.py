import bcrypt
from db import DBConnection as mydb
class Users:
    def __init__(self):
        self.__id_user=None
        self.__username=None
        self.__password=None
        self.__level=None
        self.__uservalid = None
        self.__passwordvalid = None
        self.__loginvalid = None    
    
        self.conn = None
        self.affected = None
        self.result = None
    @property
    def id_user(self):
        return self.__id_user
    @property
    def username(self):
        return self.__username
        
    @username.setter
    def username(self, value):
        self.__username = value
    @property
    def password(self):
        return self.__password
        
    @password.setter
    def password(self, value):
        self.__password = value
    @property
    def level(self):
        return self.__level
        
    @level.setter
    def level(self, value):
        self.__level = value
    def cekUsername(self, username):
        self.conn = mydb()
        sql="SELECT * FROM users WHERE username='" + username + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
           self.__id_user = self.result[0]
           self.__username = self.result[1]
           self.__password = self.result[2]
           self.__level = self.result[3]
           self.affected = self.conn.cursor.rowcount
           self.__uservalid = True
        else:
           self.__id_user = ''
           self.__username = ''
           self.__password = ''
           self.__level = ''
           self.affected = 0
           self.__uservalid = False
        return self.__uservalid
    def cekPassword(self, password):
        hashedpass=self.__password.encode('utf-8')
        c = password.encode('utf-8')
        d = bcrypt.checkpw(c, hashedpass)
        if(d):
            self.__passwordvalid=True
        else:
            self.__passwordvalid=False
        return self.__passwordvalid
    def Validasi(self, email, password):
        a = self.cekUsername(email)
        if(a==True):
            b = self.cekPassword(password)
            if(b==True):
                self.__loginvalid=True
            else:
                self.__loginvalid=False
        else:
            self.__loginvalid=False
        
        val = []
        val = [self.__level, self.__loginvalid]
        return val
    def simpan(self):
        self.conn = mydb()
        val = (self.__username,self.__password,self.__level)
        sql="INSERT INTO Users (username,password,level) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
    def update(self, id):
        self.conn = mydb()
        val = (self.__username,self.__password,self.__level, id)
        sql="UPDATE users SET username = %s,password = %s,level = %s WHERE id_user=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
    def updateByUSERNAME(self, username):
        self.conn = mydb()
        val = (self.__password,self.__level, username)
        sql="UPDATE users SET password = %s,level = %s WHERE username=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        
    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM users WHERE id_user='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def deleteByUSERNAME(self, username):
        self.conn = mydb()
        sql="DELETE FROM users WHERE username='" + str(username) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM users WHERE id_user='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__id_user = self.result[0]
        self.__username = self.result[1]
        self.__password = self.result[2]
        self.__level = self.result[3]
        self.conn.disconnect
        return self.result
    def getByUSERNAME(self, username):
        a=str(username)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM users WHERE username='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
           self.__id_user = self.result[0]
           self.__username = self.result[1]
           self.__password = self.result[2]
           self.__level = self.result[3]
           self.affected = self.conn.cursor.rowcount
        else:
           self.__id_user = ''
           self.__username = ''
           self.__password = ''
           self.__level = ''
        
           self.affected = 0
        self.conn.disconnect
        return self.result
    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM users"
        self.result = self.conn.findAll(sql)
        return self.result
        
    def getComboData(self):
        self.conn = mydb()
        sql="SELECT id,password FROM users"
        self.result = self.conn.findAll(sql)
        return self.result        
