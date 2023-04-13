Numeric types
Numeric data types include:

Two-, four-, and eight-byte integers
Four- and eight-byte floating point numbers
Selectable decimals:






Name	Storage Size	Description	Range
smallint	2 bytes	Small-range integer.	-32768 to +32767




Name	                           Storage Size                         	Description                                        	Range
smallint	                       2 bytes	                              Small-range integer.                               	-32768 to +32767
integer                          4 bytes                              	Medium-range integer.                              	-2147483648 to +2147483647
bigint		                       8 bytes	                              Large-range integer.	                              -9223372036854775808 to 9223372036854775807
decimal		                       variable	                              User-specified precision decimal                    Up to 131072 digits before the decimal point. Up to 16383 digits after the decimal point
numeric	                       	 variable	                              User-specified precision decimal.                   up to 131072 digits before the decimal point. Up to 16383 digits after the decimal point
real		                         4 bytes                              	Variable precision decimal.                       	6 decimal digits precision
double precision		             8 bytes	                              Variable precision decimal.	                        15 decimal digits precision
smallserial		                   2 bytes	                              Small autoincrementing integer.	                    1 to 32767
serial		                       4 bytes                              	Medium autoincrementing integer.                    1 to 2147483647
bigserial		                     8 bytes	                              Large autoincrementing integer.	                    1 to 9223372036854775807









HERE IS MORE EXPLANATION


n PostgreSQL, there are several numeric data types that you can use to store numerical 
values with different ranges and precisions. Some of the most commonly used numeric data types in PostgreSQL are:

INTEGER:
The INTEGER data type is used to store whole numbers, such as 1, 2, 3, -4, -5, etc. It can store values from -2,147,483,648 to 2,147,483,647.

BIGINT:
The BIGINT data type is similar to the INTEGER data type, but it can store larger whole numbers. 
It can store values from -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807.

NUMERIC:
The NUMERIC data type is used to store exact numeric values with a user-specified precision and scale.
It can store values from -10^131071 to 10^131071 with up to 131,071 digits before the decimal point and up to 16 digits after the decimal point.

FLOAT and DOUBLE PRECISION:
The FLOAT and DOUBLE PRECISION data types are used to store approximate numeric values with a variable precision.
They can store values from -1.79E+308 to 1.79E+308 (for DOUBLE PRECISION) or from -3.40E+38 to 3.40E+38 (for FLOAT).

DECIMAL:
The DECIMAL data type is similar to the NUMERIC data type, but it is defined in a different way.
It can store values with up to 131,072 digits before the decimal point and up to 16 digits after the decimal point.

When choosing a numeric data type in PostgreSQL, you should consider the range and precision of the values you want to store,
as well as the performance and storage requirements of your database.
If you need to store exact values with a user-specified precision, 
the NUMERIC or DECIMAL data types may be the best option. 
If you need to store approximate values with a variable precision, the FLOAT or DOUBLE PRECISION data types may be more suitable.













































..
