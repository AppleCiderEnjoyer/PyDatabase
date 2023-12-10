# Final Project: Week 13 (Team)
# Coded by Briely Gunn and Jacob Goncharenko

import final_db_functions

# Connects to and opens the database
final_db_functions.get_connection()

# Creates the student table
final_db_functions.create_student_table()

# Adds the students to the database
final_db_functions.add_student(1, "Briely Gunn", 16, "male",
                               "United States", "America/Chicago",
                               "bcgunn@students.unwsp.edu")

final_db_functions.add_student(2, "Jacob Goncharenko", 17, "male",
                               "United States", "America/Chicago",
                               "jdgoncharenko@students.unwsp.edu")

final_db_functions.add_student(3, "Caleb Harding", 17, "male",
                               "United States", "America/Chicago",
                               "crbystrom@students.unwsp.edu")

final_db_functions.add_student(4, "Jacob Combs", 17, "male",
                               "United States", "America/Chicago",
                               "jlcombs2@students.unwsp.edu")

final_db_functions.add_student(5, "Weston Collins", 17, "male",
                               "United States", "America/Chicago",
                               "wtcollins@students.unwsp.edu")

final_db_functions.add_student(6, "Joshua Bystrom", 17, "male",
                               "United States", "America/Chicago",
                               "jrbystrom@students.unwsp.edu")

final_db_functions.add_student(7, "Mark Swanson", 17, "male",
                               "United States", "America/Chicago",
                               "mcswanson2@students.unwsp.edu")

final_db_functions.add_student(8, "Joseph Steinberg", 17, "male",
                               "United States", "America/Chicago",
                               "jhsteinberg@students.unwsp.edu")

final_db_functions.add_student(9, "Esteban Lozano", 17, "male",
                               "United States", "America/Chicago",
                               "enlozano@unwsp.edu")

final_db_functions.add_student(10, "Dylan Weakly", 17, "male",
                               "United States", "America/Chicago",
                               "dcweakly@students.unwsp.edu")

# Gets the students' information and prints it
final_db_functions.get_students()
