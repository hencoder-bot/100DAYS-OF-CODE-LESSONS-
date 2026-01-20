SELECT *
FROM employee_demographics
;
# average , min,max , count etc
SELECT gender,avg(age), max(age),min(age), count(age)
FROM employee_demographics
GROUP BY gender
;

#----order by ---arranges the data in either ascending or descending form
SELECT *
FROM employee_demographics
ORDER BY first_name ASC;#desc

SELECT *
FROM employee_demographics
ORDER BY age, gender 
;

SELECT *
FROM employee_demographics
ORDER BY age ASC;#desc
SELECT *
FROM employee_demographics
ORDER BY employee_id;#desc