#---Having vs Where(diffference)
#WRONG WAY COZ OF 'WHERE' CLAUSE
SELECT *
FROM employee_demographics
;


-- SELECT gender, AVG(AGE)
-- FROM employee_demographics
-- WHERE AVG(age) > 40
-- GROUP BY gender
-- ;

#WRITE WAY'REMOVE THE WHERE CLAUSE'
SELECT gender, AVG(AGE)
FROM employee_demographicS
GROUP BY gender
HAVING AVG(age) > 40
;
#--how to use both
SELECT * 
FROM employee_salary
;


SELECT occupation, AVG(salary)
FROM employee_salary
WHERE occupation LIKE '%manager%'
GROUP BY occupation
;

SELECT occupation, AVG(salary)
FROM employee_salary
WHERE occupation LIKE '%manager%'
GROUP BY occupation
HAVING AVG(salary) > 75000
;