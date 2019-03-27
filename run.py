import os
import csv
from schemaValide import *
from tableOperations import *
import argparse

def main():
    
    #Get all files from data_drop and seperate schema and data files
    dir_path = os.path.join(os.path.realpath("."), "data_drop")
    for fileName in os.listdir(dir_path):
        realFilePath = os.path.join(dir_path, fileName)
        if 'schema' in fileName:
            schemaFiles.append(realFilePath)
        else:
            dataFiles.append(realFilePath)

    #try and create a table in MySql database.
    #Need to initialize MySql database and configure get user, pass, host and database before.
    #create schema from CSV
    with open(schemaFiles[0] , "r") as file:
        tableInfo = []
        schemaInfo = []
        reader = csv.reader(file)
        #skip header
        next(reader)
        for row in reader:
            
            #save column name and width information into a dictionary 
            #so we can access the column name and width information faster
            
            schemaInfo.append((row[0], int(row[1])))
            #pass the row to validator and it will return a correct validation array.
            tableInfo.append(validator.validate(row))
        #use the table name as a key to save the schema information and returns a string
        schemaSave[table_name] = schemaInfo
        #if any operation into database fails, then return
        if not operations.createTable(table_name, tableInfo): return

    #insert data 
    with open(dataFiles[0], "r") as file:
        width = [data[1] for data in schemaSave[table_name]]
        tableNames = [data[0] for data in schemaSave[table_name]]
        datas = []
        reader = csv.reader(file)
        for row in reader:
            temp = []
            #For each of the row, look at schema width and trim end to match width,
            #It follows the same pattern for numeric values.
            for r, w in zip(row, width):
                temp.append(r[:w])
            datas.append(tuple(temp))
        #if any operation into database fails, then return
        if not operations.insertData(table_name, ",".join(tableNames), datas): return


if __name__ == "__main__":

    #arguement parser to get usr args for connection details and table name
    parser = argparse.ArgumentParser(description="Enter connection details and table name")
    parser.add_argument('-u', metavar="userName", help="User name associated with MySql datbase", required=True)
    parser.add_argument('-p', metavar="password", help="Password used to connect to MySql database", required=True)
    parser.add_argument('-l', metavar="hostName", help="Name used to connect to MySql database", required=True)
    parser.add_argument('-d', metavar="databaseName", help="Name of the database where table should be created", required=True)
    parser.add_argument('-t', metavar="tableName", help="Name of the database table. Default set to 'author'.", required=False)

    args = vars(parser.parse_args())

    # initialize schemaFile
    schemaFiles, dataFiles, schemaSave = [], [], {}
    validator = schemaValidate()

    #since no table name is provided create a default one
    table_name = args['t'] or "author"

    # operations = connectionProperty("loca", "1234", "localhost", "testdb")
    operations = connectionProperty(args['u'], args['p'], args['l'], args['d'])

    validConnection = operations.checkConnectionStatus()
    # check if connection is successful, if fails then exit display error message and exit the program.
    if validConnection:
        main()
    else:
        print("Closing program")

    