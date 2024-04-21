import sqlite3
from faker import Faker
import random

# Ініціалізуємо Faker
fake = Faker()

# З'єднання з базою даних SQLite
conn = sqlite3.connect('university.db')
cursor = conn.cursor()

# Створення таблиць
cursor.execute('''CREATE TABLE students (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    group_id INTEGER,
                    FOREIGN KEY (group_id) REFERENCES groups(id)
                )''')

cursor.execute('''CREATE TABLE groups (
                    id INTEGER PRIMARY KEY,
                    name TEXT
                )''')

cursor.execute('''CREATE TABLE teachers (
                    id INTEGER PRIMARY KEY,
                    name TEXT
                )''')

cursor.execute('''CREATE TABLE subjects (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    teacher_id INTEGER,
                    FOREIGN KEY (teacher_id) REFERENCES teachers(id)
                )''')

cursor.execute('''CREATE TABLE grades (
                    id INTEGER PRIMARY KEY,
                    student_id INTEGER,
                    subject_id INTEGER,
                    grade INTEGER,
                    date TEXT,
                    FOREIGN KEY (student_id) REFERENCES students(id),
                    FOREIGN KEY (subject_id) REFERENCES subjects(id)
                )''')

# Функція для генерації випадкових даних і наповнення таблиць
def generate_data(num_students, num_groups, num_subjects, num_teachers, max_grades_per_student):
    # Наповнення таблиці груп
    for i in range(num_groups):
        cursor.execute("INSERT INTO groups (name) VALUES (?)", (fake.unique.random_element(("Group A", "Group B", "Group C")),))

    # Наповнення таблиці викладачів
    for i in range(num_teachers):
        cursor.execute("INSERT INTO teachers (name) VALUES (?)", (fake.name(),))

    # Наповнення таблиці предметів
    for i in range(num_subjects):
        cursor.execute("INSERT INTO subjects (name, teacher_id) VALUES (?, ?)", (fake.word(), random.randint(1, num_teachers)))

    # Наповнення таблиці студентів та оцінок
    for i in range(num_students):
        group_id = random.randint(1, num_groups)
        cursor.execute("INSERT INTO students (name, group_id) VALUES (?, ?)", (fake.name(), group_id))
        student_id = cursor.lastrowid
        for j in range(random.randint(1, max_grades_per_student)):
            subject_id = random.randint(1, num_subjects)
            grade = random.randint(60, 100)  # Випадкові оцінки від 60 до 100
            date = fake.date_this_year().strftime('%Y-%m-%d')
            cursor.execute("INSERT INTO grades (student_id, subject_id, grade, date) VALUES (?, ?, ?, ?)", (student_id, subject_id, grade, date))

# Генерація даних
generate_data(50, 3, 8, 5, 20)

# Збереження змін у базі даних
conn.commit()

# Закриваємо з'єднання з базою даних
conn.close()