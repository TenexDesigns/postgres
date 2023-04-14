In PostgreSQL, the JSON data type is used to store JSON (JavaScript Object Notation) data.
JSON is a lightweight data interchange format that is commonly used for data exchange between client-side and server-side applications.

To create a column with the JSON data type in PostgreSQL, you can use the json data type.
Heres an example of how to create a table with a column of the json data type:
  
  
  
  create table workers(
    
    id integer,
    residence JSON  );
  
  
  
  Json data is within curly braces,
  
  insert into workers(id, residence) values(1, '{
                                            "name":"George",
                                            "address":{
                                              "lane1":"tom boya lane",
                                              "lane2" :"Lithuli lane",
                                              "pincode":"1100024"}
                                            }'                                          
                                           ) 
                                           
  
    insert into workers(id, residence) values(1, '{
                                            "name":"Eliud",
                                            "address":{
                                              "lane1":"nyamakima lane",
                                              "lane2" :"jogoo lane",
                                              "pincode":"3222024"}
                                            }'                                          
                                           ) 




    
    
    TO FETCH DATA FROM THE TABLE 
    
    select * from workers;
    
    This will result in the follwing.
    
    
    
    
     id |                                residence
----+-------------------------------------------------------------------------
  1 | {                                                                      +
    |                                             "name":"George",           +
    |                                             "address":{                +
    |                                               "lane1":"tom boya lane", +
    |                                               "lane2" :"Lithuli lane", +
    |                                               "pincode":"1100024"}     +
    |                                             }
  2 | {                                                                      +
    |                                             "name":"Eliud",            +
    |                                             "address":{                +
    |                                               "lane1":"nyamakima lane",+
    |                                               "lane2" :"jogoo lane",   +
    |                                               "pincode":"3222024"}     +
    |                                             }
    
    
    
    
    
    
    
    
    
    
    
    TO FETCH A PERTICULAR FIELD FROM A JSON DATA
    
    ->> This symbol means to look up the json data in the followinf field name i will enter
    
    
    select residence ->> 'address' from worksers;
    
    This means  that in the residence column look for a field name  called 'address' in the json data type  in the residence column 
    
This will only return the address in our json data type from our object.


                                ?column?
-------------------------------------------------------------------------
 {                                                                      +
                                               "lane1":"tom boya lane", +
                                               "lane2" :"Lithuli lane", +
                                               "pincode":"1100024"}
 {                                                                      +
                                               "lane1":"nyamakima lane",+
                                               "lane2" :"jogoo lane",   +
                                               "pincode":"3222024"}
(2 rows)








TO ACCESSE SOMETHING INSIDE THE ADDRESS 
You have to use -> to access the address and then use this ->> to access that items inside the address


    select residence -> 'address' ->> 'pincode' from worksers;

This pnly gives us the data from pin code in all items in the resident column.

 ?column?
----------
 1100024
 3222024
(2 rows)



WE CAN ALSO USE A DIFFERENT SYNTAX TO GET THE  SAME RESULTS AS ABOVE


select residence #>>'{address,pincode}' from workers;



 ?column?
----------
 1100024
 3222024
(2 rows)

































































































...
