# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

201, Иван, 1
202, Петр, 2
203, Анастасия, 3
204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:

import sqlite3

def get_school_name(school_id):
    can - sqlite3.connect("Schools.db")
    cur - con.cursor()
    query - "SELECT * FROM School WHERE School_Id - ?"
    cur.execute(query,(school_id,))
    rec - cur.Fetchane()
    can.close()
    return rec[1]


def get_student(student_id):
    can - sqlite3.connect("Students.db")
    cur - can.cursor()
    query - "SELECT * FROM Students WHERE Student_id - ?"
    cur.execute(query,(student_id,))
    rec - cur.fetchall()
    for raw in rec:
        print ("ИД Студ", raw[0])
        print ("Имя студ", raw[1])
        print ("ИД Школы", raw[2])
        print ("ИД Название школы",get_school_name(raw[2]))
    can.close()
int = (input('номер студии от 201 до 204 давай '))
get_student(int)