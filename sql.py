import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)

class sqldbconnection:
    ### This class shall be used for mongoDB operation ###
    def __init__(self,host, user, password):
        try:
            self.host=host
            self.user = user
            self.password = password
            self.mydb = mysql.connector.connect(host="localhost",user="abc",password="password")
        except Exception as e:
            raise e

    def Database(self,dbName):
        """
        It creates a Database if does not exist
        """
        try:
            mycursor = self.mydb.cursor()
            query='create database IF NOT EXISTS  '+dbName
            mycursor.execute(query)
            
        except Exception as e:
            raise e

    def Table(self, dbName,TableName):
        """
        It creates a table if does not exist
        """
        try:
            mycursor = self.mydb.cursor()
            query='use '+dbName
            mycursor.execute(query)
            query1='create table IF NOT EXISTS  ' +TableName+ ' (Course_title TEXT  ,Description TEXT  ,Language TEXT ,Pricing TEXT ,Curriculum_data TEXT ,Learn TEXT,Requirements TEXT)'
            mycursor.execute(query1)

        except Exception as e:
            raise e

    

    

  