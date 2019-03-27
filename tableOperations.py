import mysql.connector as msql


class connectionProperty:
    """
    Class that creates a connection to database
    """

    def __init__(self, userName, passw, host, databaseName):
        self.name = userName
        self.password = passw
        self.host = host
        self.database = databaseName
   
    def checkConnectionStatus(self):
        try:
            self.getConnection()
            return True
        except:
            print("Connection to MySql has failed. Please check your connection string and try again")
            return False

    def getConnection(self):
        conn = msql.connect(
            host=self.host,
            user = self.name,
            passwd = self.password,
            database = self.database
        )
        return conn

    def createTable(self, tableName, data):
        query = "CREATE TABLE IF NOT EXISTS {} ({})".format(
            tableName, ",".join(data))
        conn = self.getConnection()
        if conn is None:
            print("Failed to connect to database")
            return
        cur = conn.cursor()
        cur.execute(query)
        cur.close()
        conn.close()

    def insertData(self, tableName, tableSchema, combinedTables):
        conn = self.getConnection()
        cur = conn.cursor()
        for values in combinedTables:
            query = "INSERT INTO {}({}) VALUES {}".format(
                tableName, tableSchema, values)
            cur.execute(query)
            conn.commit()
        cur.close()
        conn.close()
