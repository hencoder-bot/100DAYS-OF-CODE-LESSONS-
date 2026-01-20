SELECT *
FROM employee_demographics
WHERE gender = 'Female'
;
#!= female .....meaning it will show results of male 
#---AND OR NOT --Logical Operators
SELECT *
FROM employee_demographics
WHERE birth_date > '1985-01-01'
AND gender ='male'
;

SELECT *
FROM employee_demographics
WHERE birth_date > '1985-01-01'
OR NOT gender = 'male'
;
SELECT *
FROM employee_demographics
WHERE (first_name = 'Leslie' AND age = 44) OR AGE > 55
;

#--LIKE STATEMENT
#----% MEANS ANYTHING AS ---_MEANS SPECIFIC values
SELECT *
FROM employee_demographics
WHERE first_name LIKE 'a%' # meaning any name which starts with a
;

SELECT *
FROM employee_demographics
WHERE first_name LIKE 'a__' # meaning any name which starts with a and follows 2 letters eg ann
;

SELECT *
FROM employee_demographics
WHERE birth_date LIKE '1989'
;


