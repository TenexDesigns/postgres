In PostgreSQL, you can specify the behavior that should occur when a row in a parent table is deleted and that row has child rows in a related table. 
There are two options: ON DELETE RESTRICT and ON DELETE CASCADE.
  
  

ON DELETE RESTRICT: This option prevents deletion of a row from the parent table if it has any related rows in the child table. 
  When you specify ON DELETE RESTRICT,
  PostgreSQL will return an error if you try to delete a row from the parent table that has related rows in the child table.

ON DELETE CASCADE: This option deletes all related rows in the child table when a row in the parent table is deleted.
  When you specify ON DELETE CASCADE, PostgreSQL automatically deletes all related rows in the child table when you delete a row from the parent table.




Here's how you can use these options:

For example, if you have a table named "orders" with a foreign key constraint 
on the "customer_id" column that references the "id" column of the "customers" table, 
you can use the following commands to specify the behavior when a customer is deleted:
  
  
ALTER TABLE orders ADD CONSTRAINT orders_customer_fk FOREIGN KEY (customer_id) REFERENCES customers (id) ON DELETE RESTRICT;

ALTER TABLE orders ADD CONSTRAINT orders_customer_fk FOREIGN KEY (customer_id) REFERENCES customers (id) ON DELETE CASCADE;

  

Note that if you dont specify either of these options, PostgreSQL will use the default behavior, which is ON DELETE NO ACTION. 
This means that if you try to delete a row from the parent table that has related rows in the child table, PostgreSQL will return an error.
Since there are tables refencing a foreign key that does'nt exist




































































...
