SELECT grp.name AS group_name, AVG(g.grade) AS average_grade
FROM students AS s
JOIN groups AS grp ON s.group_id = grp.id
JOIN grades AS g ON s.id = g.student_id
JOIN subjects AS sub ON g.subject_id = sub.id
WHERE sub.id = :subject_id
GROUP BY grp.name;
