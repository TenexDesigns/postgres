In PostgreSQL, a primary key is a column or a set of columns that uniquely identifies each row in a table.
A foreign key is a column or a set of columns that refers to the primary key of another table.
Heres how you can create primary keys and foreign keys in PostgreSQL:

Creating a primary key:


ALTER TABLE table_name ADD CONSTRAINT constraint_name PRIMARY KEY (column_name);


For example, if you have a table named "employees" and you want to create a primary key on the "id" column, you can use the following command:

  
  ALTER TABLE employees ADD CONSTRAINT employees_pk PRIMARY KEY (id);

Creating a foreign key:


ALTER TABLE child_table_name ADD CONSTRAINT constraint_name FOREIGN KEY (column_name) REFERENCES parent_table_name (parent_column_name);



For example, if you have a table named "orders" and you want to create a foreign key on the "customer_id" column that references 
the "id" column of the "customers" table, you can use the following command:


  
  ALTER TABLE orders ADD CONSTRAINT orders_customer_fk FOREIGN KEY (customer_id) REFERENCES customers (id);



Note that the data type of the foreign key column must match the data type of the primary key column that it references.
Also, the referenced column must have a unique constraint or be the primary key of the referenced table.

When you create a foreign key, PostgreSQL automatically creates an index on the foreign key column(s) to speed up queries that use the foreign key.













































































..
