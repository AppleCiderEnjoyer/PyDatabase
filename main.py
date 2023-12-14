# Final Project: Week 13 (Team)
# Coded by Briely Gunn Jacob Goncharenko, and Caleb Harding

import final_db_functions
import final_db_gui

# Text justification variable for GUI spacing
GUI_justification = 20
GUI_email_justification = 40

# Connects to and opens the database
final_db_functions.get_connection()

# Creates the student table
final_db_functions.create_student_table()

# Adds the students to the database
final_db_functions.add_student("Briely Gunn".ljust(GUI_justification, " "),
                               16,
                               "male",
                               "United States".ljust(GUI_justification, " "),
                               "America/Chicago".ljust(GUI_justification, " "),
                               "bcgunn@students.unwsp.edu".ljust(GUI_email_justification, " "))

final_db_functions.add_student("Jacob Goncharenko".ljust(GUI_justification, " "),
                               17,
                               "male",
                               "United States".ljust(GUI_justification, " "),
                               "America/Chicago".ljust(GUI_justification, " "),
                               "jdgoncharenko@students.unwsp.edu".ljust(GUI_email_justification, " "))

final_db_functions.add_student("Caleb Harding".ljust(GUI_justification, " "),
                               17,
                               "male",
                               "United States".ljust(GUI_justification, " "),
                               "America/Chicago".ljust(GUI_justification, " "),
                               "crbystrom@students.unwsp.edu".ljust(GUI_email_justification, " "))

final_db_functions.add_student("Jacob Combs".ljust(GUI_justification, " "),
                               17,
                               "male",
                               "United States".ljust(GUI_justification, " "),
                               "America/Chicago".ljust(GUI_justification, " "),
                               "jlcombs2@students.unwsp.edu".ljust(GUI_email_justification, " "))

final_db_functions.add_student("Weston Collins".ljust(GUI_justification, " "),
                               17,
                               "male",
                               "United States".ljust(GUI_justification, " "),
                               "America/Chicago".ljust(GUI_justification, " "),
                               "wtcollins@students.unwsp.edu".ljust(GUI_email_justification, " "))

final_db_functions.add_student("Joshua Bystrom".ljust(GUI_justification, " "),
                               17,
                               "male",
                               "United States".ljust(GUI_justification, " "),
                               "America/Chicago".ljust(GUI_justification, " "),
                               "jrbystrom@students.unwsp.edu".ljust(GUI_email_justification, " "))

final_db_functions.add_student("Mark Swanson".ljust(GUI_justification, " "),
                               17,
                               "male",
                               "United States".ljust(GUI_justification, " "),
                               "America/Chicago".ljust(GUI_justification, " "),
                               "mcswanson2@students.unwsp.edu".ljust(GUI_email_justification, " "))

final_db_functions.add_student("Joseph Steinberg".ljust(GUI_justification, " "),
                               17,
                               "male",
                               "United States".ljust(GUI_justification, " "),
                               "America/Chicago".ljust(GUI_justification, " "),
                               "jhsteinberg@students.unwsp.edu".ljust(GUI_email_justification, " "))

final_db_functions.add_student("Esteban Lozano".ljust(GUI_justification, " "),
                               17,
                               "male",
                               "United States".ljust(GUI_justification, " "),
                               "America/Chicago".ljust(GUI_justification, " "),
                               "enlozano@unwsp.edu".ljust(GUI_email_justification, " "))

final_db_functions.add_student("Dylan Weakly".ljust(GUI_justification, " "),
                               17,
                               "male",
                               "United States".ljust(GUI_justification, " "),
                               "America/Chicago".ljust(GUI_justification, " "),
                               "dcweakly@students.unwsp.edu".ljust(GUI_email_justification, " "))

# Gets the students' information and prints it
final_db_functions.get_students()

final_db_gui.IntroGUI()
