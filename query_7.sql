SELECT s.name AS student_name, g.grade
FROM students AS s
JOIN grades AS g ON s.id = g.student_id
JOIN subjects AS sub ON g.subject_id = sub.id
JOIN groups AS grp ON s.group_id = grp.id
WHERE grp.id = :group_id
  AND sub.id = :subject_id;