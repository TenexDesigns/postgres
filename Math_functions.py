PostgreSQL provides a variety of built-in mathematical functions that you can use in your SQL queries.
Here are some of the most commonly used mathematical functions in PostgreSQL:

ABS() - returns the absolute value of a number.

CEIL() or CEILING() - rounds a number up to the nearest integer.

FLOOR() - rounds a number down to the nearest integer.

ROUND() - rounds a number to a specified number of decimal places.

TRUNC() - truncates a number to a specified number of decimal places.

EXP() - returns the exponential value of a number.

LN() or LOG() - returns the natural logarithm of a number.

LOG10() - returns the base-10 logarithm of a number.

MOD() - returns the remainder of a division operation.

POWER() - raises a number to a specified power.

SQRT() - returns the square root of a number.

PI() - returns the mathematical constant pi.

RANDOM() - returns a random value between 0 and 1.

GREATEST() - returns the greatest value among a set of input values.

LEAST() - returns the smallest value among a set of input values.

These are just a few of the mathematical functions available in PostgreSQL.
You can find a full list of mathematical functions in the PostgreSQL documentation. 
When using these functions in SQL queries, be sure to check the data types of the input values to ensure that the function can be applied correctly.





HERE ARE CODE SAMPLES

**************************************************************************************************************************************************************

Sure, here are some examples of using mathematical functions in PostgreSQL:

ABS(): Returns the absolute value of a number.
  
  SELECT ABS(-10); -- Output: 10
  SELECT ABS(10); -- Output: 10


CEIL() or CEILING(): Rounds a number up to the nearest integer.

SELECT CEIL(1.5); -- Output: 2
SELECT CEILING(1.5); -- Output: 2



FLOOR(): Rounds a number down to the nearest integer.

SELECT FLOOR(1.5); -- Output: 1



ROUND(): Rounds a number to a specified number of decimal places.

SELECT ROUND(1.23456, 2); -- Output: 1.23



TRUNC(): Truncates a number to a specified number of decimal places.

SELECT TRUNC(1.23456, 2); -- Output: 1.23




EXP(): Returns the exponential value of a number.

SELECT EXP(1); -- Output: 2.71828182845905



LN() or LOG(): Returns the natural logarithm of a number.

SELECT LN(10); -- Output: 2.30258509299405
SELECT LOG(10); -- Output: 1

  
  

LOG10(): Returns the base-10 logarithm of a number.

SELECT LOG10(100); -- Output: 2





MOD(): Returns the remainder of a division operation.

SELECT MOD(10, 3); -- Output: 1




POWER(): Raises a number to a specified power.

SELECT POWER(2, 3); -- Output: 8




SQRT(): Returns the square root of a number.

SELECT SQRT(16); -- Output: 4





PI(): Returns the mathematical constant pi.

SELECT PI(); -- Output: 3.14159265358979




RANDOM(): Returns a random value between 0 and 1.

SELECT RANDOM(); -- Output: Random value between 0 and 1




GREATEST(): Returns the greatest value among a set of input values.

SELECT GREATEST(1, 2, 3, 4); -- Output: 4



LEAST(): Returns the smallest value among a set of input values.

SELECT LEAST(1, 2, 3, 4); -- Output: 1




These are just a few examples of using mathematical functions in PostgreSQL. 
Note that the syntax may vary depending on the version of PostgreSQL you are using,
so be sure to consult the documentation for your specific version for more information.





HERE IS MORE EXPLANATION
************************************************************************************************************************************************************



PostgreSQL provides a wide range of mathematical functions and operators to perform various operations on numeric data types.
These functions and operators are available for standard numeric types such as smallint, integer, bigint, numeric, real, and double precision postgresql.org.
Some of the most commonly used mathematical functions are:





Rounding functions
ceil or ceiling: Returns the nearest integer greater than or equal to the argument postgrespro.com.
round: Rounds to the nearest integer. For numeric, ties are broken by rounding away from zero.
  For double precision, the tie-breaking behavior is platform dependent, but “round to nearest even” is the most common rule postgrespro.com.
round(v, s): Rounds v to s decimal places. Ties are broken by rounding away from zero postgrespro.com.
  
  
  
Division and modulo
Division: For integral types, division truncates the result towards zero postgresql.org.
Modulo: Returns the remainder of the division. Available for smallint, integer, bigint, and numeric postgresql.org.
  
  
  
  
Power and square root
power(a, b): Returns a raised to the power of b. Available for double precision postgrespro.com.
sqrt: Returns the square root of the argument postgrespro.com.
  
  
  
  
Trigonometric functions
PostgreSQL provides various trigonometric functions such as sin, cos, tan, asin, acos, atan, and atan2. 
Each of these functions comes in two variants, one that measures angles in radians and one that measures angles in degrees postgrespro.com.




Greatest common divisor and least common multiple

gcd: Returns the greatest common divisor of the input numbers. Available for integer, bigint, and numeric postgrespro.com.
lcm: Returns the least common multiple of the input numbers. Available for integer, bigint, and numeric postgrespro.com.
  
  
  
Random number generation

random: Generates a random number between 0 and 1 postgrespro.com.
setseed: Sets the seed for subsequent random calls; the argument must be between -1.0 and 1.0, inclusive postgrespro.com.
  
  
  
  
Histogram functions

width_bucket: Returns the number of the bucket in which the operand falls in a histogram.
  Available in different forms, such as for numeric and double precision types postgrespro.com.
These functions are mostly implemented on top of the host systems C library,
so accuracy and behavior in boundary cases can vary depending on the host system postgresql.org.

Examples:





SELECT ceil(4.2) AS ceil_result; -- Result: 5

SELECT round(4.5) AS round_result; -- Result: 5

SELECT power(2, 3) AS power_result; -- Result: 8

SELECT sqrt(9) AS sqrt_result; -- Result: 3

SELECT sin(radians(30)) AS sin_result; -- Result: 0.5

SELECT gcd(12, 8) AS gcd_result; -- Result: 4

SELECT lcm(12, 8) AS lcm_result; -- Result: 24

SELECT random() AS random_result; -- Result: Random number between 0 and 1

SELECT setseed(0.5); -- Sets the seed for random number generation

SELECT width_bucket(15, 0, 100, 10) AS width_bucket_result; -- Result: 2



Keep in mind that the random function uses a deterministic pseudo-random number generator,
which is fast but not suitable for cryptographic applications. For a more secure alternative,
use the pgcrypto module [postgresql.org](https://www.postgresql.org/docs/current/functions-math
















...
