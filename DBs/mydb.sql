CREATE VIEW emp_view AS
SELECT emp_id , name , salary
FROM employee
WHERE salary > 5000;

SELECT * FROM emp_id