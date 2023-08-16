PostgreSQL (or Postgres) is a powerful open-source relational database management system (RDBMS) that is known for its reliability, scalability, 
and extensibility. 
It can handle complex queries and manage large amounts of data, making it a popular choice for many applications.



To work with postgres , you can do so either  by using the graphical user interface ------> pgAdmin 4
                                              by using the command line interface   ------>  SQL Shell(psql)   



HERE WE ARE GOING TO WORK WITH THE SQL SHELL, WHERE WE CA TYPE OUR SQL QUERIIRES

When you connect to the sql shell. The sql shell has a default database called postgress

we will be in this database by default ,
The postgress before the hash means we are in the postgres database, but ,that name before the hash will change to the name of the database we naviage to

postgres=# \c test

but we can create our own database 







TO CREATE YOUR OWN DATABASE
*********************************************************************************************************************************************************
Always end your querries with a semicolon


 ---------> \c database_name;
 
 
 e.g postgres=# \c test
 
 
 TO NAVIAGE OR TO CONNECT TO YOUR CREATED DATABASE
*********************************************************************************************************************************************************
 
 This is the same command we used above, It creates a database if the name given does not exist among the existing databases
 If the name exists among the existing databases , then this command will naviage to that database.
 
 
  ---------> \c database_name;
 
 
 
 To know if you have navigated to your specified data base , the name before the hash will change to your specified database naem 
 
 
 postgres=# \c test
 You are now connected to 
 database "test" as user "postgres".
 
test=#                                                         // The name before the hash has changed to the specified database name, meanin g the change  was succesful
 


TO LSIT ALL DATABASES AVALIABLE IN POSTGRES
*********************************************************************************************************************************************************

RUn this command


----------->  \L


e.g test=# \l   --> In my database ,it lists the following list of databasese. Here , I have 4 databses with names empl_, tet,worker and the default database postgres

                                             List of databases

   Name    |  Owner   | Encoding |          Collate           |           Ctype            |   Access privileges
-----------+----------+----------+----------------------------+----------------------------+-----------------------
 empl_     | postgres | UTF8     | English_United States.1252 | English_United States.1252 |
 worker    | postgres | UTF8     | English_United States.1252 | English_United States.1252 |
 postgres  | postgres | UTF8     | English_United States.1252 | English_United States.1252 |
 test      | postgres | UTF8     | English_United States.1252 | English_United States.1252 |
(4 rows)





TO DELETE OR DROP A DATABASE
*********************************************************************************************************************************************************

run this command


----------------> drop database  database_name:

Here is an exmple
e.g  postgres=# drop database test;
DROP DATABASE                                         // This is a confirmation that the above operation was succesful.





TO CREATE A TABLE IN A DATABSE
*********************************************************************************************************************************************************

------->   create table department(id int primary key not null, dept char(50) not null, emp_id int not null);

This creates a table called department with three columns id, department, employee_id . These columns must have  a value and can not be null,
The id is of integer data type and is the primary key




TO LIST ALL THE TABLES AVAILABEL IN YOUR DATABASE
run this command in your database

-------------------> \d 


for example in my databse ,it list the following


test=# \d

--> My databse has four tables , company ,department, genders and students
           List of relations
 Schema |    Name    | Type  |  Owner
--------+------------+-------+----------
 public | company    | table | postgres
 public | department | table | postgres
 public | genders    | table | postgres
 public | students   | table | postgres
(4 rows)


