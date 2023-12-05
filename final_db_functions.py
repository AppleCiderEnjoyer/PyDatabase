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

    # Adds the student table to the database
    cursor.execute(str("create table student "
                       "(student_id text primary key, student_name text)"))

    # Commits the table to the database
    connection.commit()


# Function to add a student to the student table

# (You guys can add more columns here to the add_student function)
def add_student(student_id: int, student_name: str):
    # Uses variables to connect to the database
    cursor, connection = get_connection()

    # Creates a list containing the student information
    student_info = [student_id, student_name]

    # Adds the list to the student table
    cursor.execute("insert into student values (?,?,?)", student_info)

    # Commits the list to the database
    connection.commit()

# (Jacob, you can put any of your functions here)

# (Caleb, you can put any of your functions here)


# Function to get the cities in the city table and print them
def get_student():
    # Uses variables to connect to the database
    cursor, connection = get_connection()

    # Selects all the cities in the table and prints them
    for row in cursor.execute("select * from city"):
        print(row)


# Function to close the database
def close():
    # Uses variables to connect to the database
    cursor, connection = get_connection()

    # Closes the database
    connection.close()
