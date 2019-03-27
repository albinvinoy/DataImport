# DataImport
Application to create new MySql tables and import data

# Assumptions
What is interger width?
In schema.csv integer has a width amount. If it follows the patters of Char and Boolean then program assumes the interger should not exceed given width. In MySql Int(k) is only used for zerofill.

What if table name is not provivded?
Since no table name is provided, it should be a user input or set a default value. 

What is there are multiple schemas and data files.
If there are multiple schemas and data file then table name should be part of filename. Ex. author_schema.csv, author_data.csv, bookInfo_schema.csv, bookInfo_data.csv etc. Small change to the code will accept multiple files.

Does data.csv always contain correct datafields associated with the schema.csv.
data.csv contains correct data.

What type of database can I use?
Selected database is MySql. Any database can work with this application with small changes. This is not a web application, but can be imported to Django easily.

What if someone decides to change the schame to add more fields?
Program accounts for additional column values in schama as long as the data.csv also reflects the changes.
Ex. If we decide to add age to schema,(age, 2, INTEGER) then data should also contain age information.

Should it overwrite a table with same name?
No, but it inserts values into the table.

#Run

Application is written in Python 3
1. To run the application first install requirements.txt 
2. python3 run.py --help to see command line help
3. python3 run.py -u username -p password -l hostname/connection -d database [-t tablename]


