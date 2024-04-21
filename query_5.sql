SELECT t.name AS teacher_name, sub.name AS subject_name
FROM teachers AS t
JOIN subjects AS sub ON t.id = sub.teacher_id;
