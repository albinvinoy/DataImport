import os
import csv
from tableOperations import *
import argparse

def test(tableName, dataFile):
    #get table schema to get the width of the data
    #get all data from given table => select * from tableName;
    #if failed to get data or schema then return False
    result = operations.getTableData(tableName)
    schemaData = operations.getSchema(tableName)
    if result is None or schemaData is None: return False
    
    #first parse the width from schmea 
    width = []
    for sch in schemaData:
        s = ''.join(x for x in sch[1] if x.isdigit())
        width.append( -1 if s == "" else int(s))
    #open csv file and compare its value with reader and use width to trim the ends
    # if csv and reader does not have same values then return False, else return True
    with open(dataFile, "r") as file:
        reader = csv.reader(file)
        for rdr, rst in zip(reader, result):
            for i in range(len(rdr)):
                if width == -1:
                    if rdr[i][:] != str(rst[i]): return False
                else:
                    if rdr[i][:width[i]] != str(rst[i]): return False
        return True
            
if __name__ == "__main__":
    #command line args to get data
    parser = argparse.ArgumentParser(description="Enter connection details and table name")
    parser.add_argument('-u', metavar="userName", help="User name associated with MySql datbase", required=True)
    parser.add_argument('-p', metavar="password", help="Password used to connect to MySql database", required=True)
    parser.add_argument('-l', metavar="hostName", help="Name used to connect to MySql database", required=True)
    parser.add_argument('-d', metavar="databaseName", help="Name of the database where table should be created", required=True)
    parser.add_argument('-t', metavar="tableName", help="Name of the database table", required=True)
    args = vars(parser.parse_args())

    dataFiles, schemaFiles = [], []
    schemaSave = {}
    operations = connectionProperty(args['u'], args['p'], args['l'], args['d'])

    #check if connection is valid
    validConnection = operations.checkConnectionStatus()
    
    dir_path = os.path.join(os.path.realpath("."), "data_drop")
    for fileName in os.listdir(dir_path):
        realFilePath = os.path.join(dir_path, fileName)
        if 'schema' in fileName:
            schemaFiles.append(realFilePath)
        else:
            dataFiles.append(realFilePath)
    #if connection string is invalid close the program
    if validConnection:
        #pass tablename and data into test function
        valid = test(args['t'], dataFiles[0])
        if valid:
            print("Test case passed")
        else:
            print("Test case failed")
    else:
        print("Closing program")