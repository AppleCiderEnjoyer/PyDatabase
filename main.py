# Final Project (Team)
# Coded by Briely Gunn, Jacob Goncharenko, and Caleb Harding

import final_db_functions

# Connects to and opens the database
final_db_functions.get_connection()

# Creates the student table
final_db_functions.create_student_table()

final_db_functions.add_student(1234, "Briely Gunn")
final_db_functions.add_student(2234, "Jacob Goncharenko")
final_db_functions.add_student(3234, "Caleb Harding")
# student for row 4
# student for row 5
# student for row 6
# student for row 7
# student for row 8
# student for row 9
# student for row 10

# (We still need to add more students to these rows^)
# (You guys can add more rows here with the add_student function)

# Gets the student's information and prints it
final_db_functions.get_students()
