SELECT s.name AS student_name, AVG(g.grade) AS average_grade
FROM students AS s
JOIN grades AS g ON s.id = g.student_id
JOIN subjects AS sub ON g.subject_id = sub.id
WHERE sub.id = :subject_id
GROUP BY s.id
ORDER BY AVG(g.grade) DESC
LIMIT 1;
