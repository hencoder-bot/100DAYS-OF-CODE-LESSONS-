#group by and order by in mysql
SELECT *
FROM employee_demographics;

SELECT gender#----------has to match
FROM employee_demographics
GROUP BY gender#-----with this
;

#or
SELECT gender, AVG(age)
FROM employee_demographics
GROUP BY gender
;



