import mysql.connector as msql


class connectionProperty:
    #Class that creates a connection to database
    def __init__(self, userName, passw, host, databaseName):
        self.name = userName
        self.password = passw
        self.host = host
        self.database = databaseName
   
    def checkConnectionStatus(self):
        #return -> True or False
        #check if connection is successful
        try:
            self.getConnection()
        except Exception as e:
            print("Connection to MySql has failed. Please check your connection string and try again")
            return False
        return True

    def getConnection(self):
        #return -> connection object
        #Create connection
        conn = msql.connect(
            host=self.host,
            user = self.name,
            passwd = self.password,
            database = self.database
        )
        return conn

    def createTable(self, tableName, data):
        #create table in database with given parameters
        #open connection, try and execute query and then return Boolean
        query = "CREATE TABLE IF NOT EXISTS {} ({})".format(
            tableName, ",".join(data))
        conn = self.getConnection()
        cur = conn.cursor()
        try:
            cur.execute(query)
            return True
        except Exception as e:
            print("Failed to create {} table with schema.\n Detailed Error : {}".format(tableName, str(e)))
            return False
        finally:
            cur.close()
            conn.close()

    def insertData(self, tableName, tableSchema, combinedTables):
        #insert data into give tableName 
        #open connection, try and execute query and then return Boolean
        conn = self.getConnection()
        cur = conn.cursor()
        try:
            for values in combinedTables:
                query = "INSERT INTO {}({}) VALUES {}".format(
                    tableName, tableSchema, values)
                cur.execute(query)
            conn.commit()
            return True
        except Exception as e:
            print("Failed to insert data into {} table.\n Detailed Error : {}".format(tableName, str(e)))
            return False
        finally:
            cur.close()
            conn.close()

    def getTableData(self, tableName):
        #return all data from table
        conn = self.getConnection()
        cur = conn.cursor()
        result = None
        query = "SELECT * FROM {}".format(tableName)
        try:
            cur.execute(query)
            result = cur.fetchall()
        except Exception as e:
            print("Failed to get data from {}\n Detailed Error : ". format(tableName, str(e)))
            return None
        finally:
            cur.close()
            conn.close()
            return result


    def getSchema(self, tableName):
        #get table schema
        conn = self.getConnection()
        cur = conn.cursor()
        result = None
        query = "DESC {}".format(tableName)
        try:
            cur.execute(query)
            result = cur.fetchall()
        except Exception as e:
            print("Failed to get schema from {}\n Detailed Error : {}".format(tableName, str(e)))
            return None
        finally:
            cur.close()
            conn.close()
            return result
