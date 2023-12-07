# Final Project (Team) (Functions)
# Coded by Briely Gunn, Jacob Goncharenko, and Caleb Harding

import sqlite3

# Lines 6-32 coded by: Briely Gunn


# Function to connect to the final_project database and create a cursor
def get_connection():

    # Connects to the database
    connection = sqlite3.connect('final_project.db')

    # Creates the cursor for SQL executions in other functions
    cursor = connection.cursor()

    # Returns the cursor and connection variables for use in the other functions
    return cursor, connection


# Function to create the student table and add it to the database
def create_student_table():
    # Uses variables to connect to the database
    cursor, connection = get_connection()

    # Removes table if it already exists
    cursor.execute("DROP TABLE IF EXISTS students")

    # Adds the student table to the database
    cursor.execute("CREATE TABLE students "
                   "(student_id INTEGER PRIMARY KEY, "
                   "student_name TEXT, "
                   "student_age INTEGER, "
                   "student_gender TEXT, "
                   "student_country TEXT, "
                   "student_timezone TEXT, "
                   "student_email TEXT)")

    # Commits the table to the database
    connection.commit()

    # Closes the database
    connection.close()


# Function to add a student to the student table

# (You guys can add more columns here to the add_student function)
def add_student(student_id: int, student_name: str, student_age: int, student_gender: str,
                student_country: str, student_timezone: str, student_email: str):
    # Uses variables to connect to the database
    cursor, connection = get_connection()

    # Creates a list containing the student information
    student_info = [student_id, student_name, student_age, student_gender,
                    student_country, student_timezone, student_email]

    # Adds the list to the student table
    cursor.execute("insert into students values (?,?,?,?,?,?,?)", student_info)

    # Commits the list to the database
    connection.commit()

    # Closes the database
    connection.close()

# (Jacob, you can put any of your functions here if we need them in the future)


# (Caleb, you can put any of your functions here if we need them in the future)


# Function to get the students in the student table and print them
def get_students():
    # Uses variables to connect to the database
    cursor, connection = get_connection()

    # Selects all the students in the table and prints them
    for row in cursor.execute("select * from students"):
        print(row)
