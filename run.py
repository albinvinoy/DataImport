import os
import csv
from schemaValide import *
from tableOperations import *


if __name__ == "__main__":

    # initialize schemaFile
    schemaFiles, dataFiles, schemaSave = [], [], {}
    validator = schemaValidate()
    operations = connectionProperty("loca", "234", "localhost", "testdb")
    """
    Get all files from data_drop and seperate schema and data files
    """
    dir_path = os.path.join(os.path.realpath("."), "data_drop")
    for fileName in os.listdir(dir_path):
        realFilePath = os.path.join(dir_path, fileName)
        if 'schema' in fileName:
            schemaFiles.append(realFilePath)
        else:
            dataFiles.append(realFilePath)

    """
    try and create a table in MySql database.
    Need to initialize MySql database and configure get user, pass, host and database before.
    """

    #since no table name is provided create a default one
    table_name = "author"

    #create schema from CSV
    with open(schemaFiles[0] , "r") as file:
        tableInfo = []
        schemaInfo = []
        reader = csv.reader(file)
        #skip header
        next(reader)
        for row in reader:
            """
            save column name and width information into a dictionary 
            so we can access the column name and width information faster
            """
            schemaInfo.append((row[0], int(row[1])))
            #pass the row to validator and it will return a correct validation array.
            tableInfo.append(validator.validate(row))
        #use the table name as a key to save the schema information and returns a string
        schemaSave[table_name] = schemaInfo
        operations.createTable(table_name, tableInfo)

    #insert data 
    with open(dataFiles[0], "r") as file:
        width = [data[1] for data in schemaSave[table_name]]
        tableNames = [data[0] for data in schemaSave[table_name]]
        datas = []
        reader = csv.reader(file)
        for row in reader:
            temp = []
            """
            For each of the row, look at schema width and trim end to match width,
            It follows the same pattern for numeric values.
            """
            for r, w in zip(row, width):
                temp.append(r[:w])
            datas.append(tuple(temp))
        operations.insertData(table_name, ",".join(tableNames), datas)