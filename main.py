# Final Project (Team)
# Coded by Briely Gunn, Jacob Goncharenko, and Caleb Harding

import final_db_functions

# Connects to and opens the database
final_db_functions.get_connection()

# Creates the student table
final_db_functions.create_student_table()
# (NOTE) - Please put in your correct age below, if you know the ages of the other students please fill them in
final_db_functions.add_student(1, "Briely Gunn", 17, "male", "United States", "America/Chicago", "bcgunn@students.unwsp.edu")
final_db_functions.add_student(2, "Jacob Goncharenko", 17, "male", "United States", "America/Chicago", "jdgoncharenko@students.unwsp.edu")
final_db_functions.add_student(3, "Caleb Harding", 17, "male", "United States", "America/Chicago", "crbystrom@students.unwsp.edu")
final_db_functions.add_student(4, "Jacob Combs", 17, "male", "United States", "America/Chicago", "jlcombs2@students.unwsp.edu")
final_db_functions.add_student(5, "Weston Collins", 17, "male", "United States", "America/Chicago", "wtcollins@students.unwsp.edu")
final_db_functions.add_student(6, "Joshua Bystrom", 17, "male", "United States", "America/Chicago", "jrbystrom@students.unwsp.edu")
final_db_functions.add_student(7, "Mark Swanson", 17, "male", "United States", "America/Chicago", "mcswanson2@students.unwsp.edu")
# student for row 8
# student for row 9
# student for row 10

# (We still need to add more students to these rows^)
# (You guys can add more rows here with the add_student function)

# Gets the student's information and prints it
final_db_functions.get_students()