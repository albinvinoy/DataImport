# DataImport
Application to create new MySql tables and import data

#Assumptions
In schema.csv integer has a width amount. If it follows the patters of Char and Boolean then program assumes the interger should not exceed given width. In MySql Int(k) is only used for zerofill.

Since no table name is provided, it should be a user input or set a default value. 
If there are multiple schemas and data file then table name should be part of filename. Ex. author_schema.csv, author_data.csv, bookInfo_schema.csv, bookInfo_data.csv etc.

Selected database is MySql. Any database can work with this application with small changes. This is not a web application, but can be imported to Django easily.




