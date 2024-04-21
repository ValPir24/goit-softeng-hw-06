SELECT s.name AS subject_name
FROM subjects AS s
JOIN teachers AS t ON s.teacher_id = t.id
JOIN grades AS g ON s.id = g.subject_id
JOIN students AS st ON g.student_id = st.id
WHERE t.name = (SELECT name FROM teachers WHERE id = :teacher_id)
  AND st.name = (SELECT name FROM students WHERE id = :student_id)