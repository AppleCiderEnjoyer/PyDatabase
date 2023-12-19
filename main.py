# Final Project: Week 15 (Team)
# Coded by Briely Gunn Jacob Goncharenko, and Caleb Harding

import final_db_functions
import final_db_gui

# Text justification variable for GUI spacing
GUI_text_justification = 20
GUI_email_text_justification = 40

# Connects to and opens the database
final_db_functions.get_connection()

# Creates the student table
final_db_functions.create_student_table()

# Adds the students to the database
final_db_functions.add_student("Briely Gunn",
                               16,
                               "male",
                               "United States",
                               "America/Chicago",
                               "bcgunn@students.unwsp.edu")

final_db_functions.add_student("Jacob Gonch",
                               17,
                               "male",
                               "United States",
                               "America/Chicago",
                               "jdgoncharenko@students.unwsp.edu")

final_db_functions.add_student("Caleb Harding",
                               17,
                               "male",
                               "United States",
                               "America/Chicago",
                               "crbystrom@students.unwsp.edu")

final_db_functions.add_student("Jacob Combs",
                               17,
                               "male",
                               "United States",
                               "America/Chicago",
                               "jlcombs2@students.unwsp.edu")

final_db_functions.add_student("Weston Collins",
                               17,
                               "male",
                               "United States",
                               "America/Chicago",
                               "wtcollins@students.unwsp.edu")

final_db_functions.add_student("Joshua Bystrom",
                               17,
                               "male",
                               "United States",
                               "America/Chicago",
                               "jrbystrom@students.unwsp.edu")

final_db_functions.add_student("Mark Swanson",
                               17,
                               "male",
                               "United States",
                               "America/Chicago",
                               "mcswanson2@students.unwsp.edu")

final_db_functions.add_student("Joseph Steinberg",
                               17,
                               "male",
                               "United States",
                               "America/Chicago",
                               "jhsteinberg@students.unwsp.edu")

final_db_functions.add_student("Esteban Lozano",
                               17,
                               "male",
                               "United States",
                               "America/Chicago",
                               "enlozano@unwsp.edu")

final_db_functions.add_student("Dylan Weakly",
                               17,
                               "male",
                               "United States",
                               "America/Chicago",
                               "dcweakly@students.unwsp.edu")

# Gets the students' information and prints it
final_db_functions.get_students()

final_db_gui.IntroGUI()
