PostgreSQL supports a variety of arithmetic operators that can be used to perform mathematical operations on numeric data types.
Here are the most commonly used arithmetic operators in PostgreSQL:

Addition: +
  
  SELECT 2 + 3;  -- result: 5

Subtraction: -
  
  SELECT 5 - 3;  -- result: 2
    
Multiplication: *
  
  SELECT 2 * 3;  -- result: 6
    
Division: /
  
  SELECT 10 / 2;  -- result: 5

Modulus (remainder): %
  
  SELECT 10 % 3;  -- result: 1

Exponentiation: ^ or **
  
  SELECT 2 ^ 3;    -- result: 8
  SELECT 2 ** 3;   -- result: 8
    
Square root: |/
  
  select |/25;    -- reult: 5
    
cube root : ||\
  
  select ||/27   -- result : 3


These arithmetic operators can be used with numeric data types such as integer, bigint, decimal, numeric, float, real, etc. 
In addition, you can use parentheses to group arithmetic expressions to ensure that they are evaluated in the correct order.






























...
