# Final Project: Week 13 (Team) (GUI)
# Coded by Briely Gunn Jacob Goncharenko, and Caleb Harding

import tkinter
import final_db_functions

# Text justification variable for GUI spacing
GUI_text_justification = 20
GUI_email_text_justification = 40


# Functions
# Function to justify all needed strings
def gui_str_justification(string: str):
    return string.ljust(GUI_text_justification, " ")


# Function to format the database table into readable text
def db_str_formatting(string):
    string_formatted = (str(string)
                        .replace("), ", "⌘")
                        .replace("(", "")
                        .replace(")", "")
                        .replace("'", "")
                        .replace("[", "")
                        .replace("]", "")
                        .replace(",", "\t")
                        .replace("⌘", ","))
    return string_formatted


# Intro GUI for when the program first runs
class IntroGUI:

    # Creates the initial GUI window for the user to see
    def __init__(self):
        self.window = tkinter.Tk()

        # Prints the title of the window
        self.window.title("Group 5 Final Project")

        self.image_frame = tkinter.Frame(self.window)
        self.text_frame = tkinter.Frame(self.window)
        self.button_frame = tkinter.Frame(self.window)

        # Image
        # Creates (Group 5) image for the GUI
        self.python_logo = tkinter.PhotoImage(file='python_logo_image.png').subsample(3, 3)

        self.image_real = tkinter.Label(self.image_frame,
                                        image=self.python_logo,
                                        width=600)
        # Adds the image to the GUI
        self.image_real.pack()

        # Text
        # Creates text for the window
        self.intro_text = tkinter.Label(self.text_frame,
                                        text="Coded by Briely Gunn, Jacob Goncharenko, and Caleb Harding\n",
                                        font='Calibri')
        # Adds the text to the GUI
        self.intro_text.pack()

        # Buttons
        # Creates a button to show the database
        self.show_db_button = tkinter.Button(self.button_frame,
                                             text="Show Database",
                                             command=self.open_db_gui)

        # Creates a button to quit the program
        self.exit_button = tkinter.Button(self.button_frame,
                                          text="Exit",
                                          command=self.window.destroy)

        # Adds the buttons to the GUI
        self.show_db_button.pack()
        self.exit_button.pack()

        # Packing
        # Adds the image, text, and button frames to the GUI
        self.image_frame.pack()
        self.text_frame.pack()
        self.button_frame.pack()

        # Mainloop to make the GUI work
        tkinter.mainloop()

    # Function to close the intro GUI and open the one with the database
    def open_db_gui(self):
        self.window.destroy()
        DBGUI()


# GUI for displaying all the database information
class DBGUI:
    def __init__(self):
        self.window = tkinter.Tk()

        # Prints the title of the window
        self.window.title("Group 5 Final Project")

        # Initialized Widgets

        # Frames
        self.text_frame = tkinter.Frame(self.window)
        self.db_frame = tkinter.Frame(self.window)
        self.button_frame = tkinter.Frame(self.window)
        self.add_db_entry_frame = tkinter.Frame(self.window)
        self.edit_db_entry_frame = tkinter.Frame(self.window)
        self.remove_db_entry_frame = tkinter.Frame(self.window)
        self.exit_frame = tkinter.Frame(self.window)

        # Text
        self.intro_text = tkinter.Label(self.db_frame, text="Student Information Database\n")

        # Database text
        # Formats the database columns
        self.db_text = ("ID#:".ljust(GUI_text_justification, " ") +
                        "\t Name:".ljust(GUI_text_justification, " ") +
                        "\t Age:" +
                        "\t Gender:" +
                        "\t Country:".ljust(GUI_text_justification, " ") +
                        "\t\t Timezone:".ljust(GUI_text_justification, " ") +
                        "\t Email:\n".ljust(GUI_email_text_justification, " "))

        # Formats the Database info
        self.db_entries = final_db_functions.get_students()

        #
        self.db_scrollbox = tkinter.Listbox(self.db_frame,
                                            justify='left',
                                            height=10,
                                            width=100)
        #
        self.db_scrollbar = tkinter.Scrollbar(self.db_frame,
                                              orient=tkinter.VERTICAL)

        #
        self.db_scrollbar.config(command=self.db_scrollbox.yview)
        self.db_scrollbox.config(yscrollcommand=self.db_scrollbar.set)

        # Adds the database entries to the scrollbox
        self.db_scrollbox.insert(tkinter.END, self.db_text)
        self.db_gui_formatting(self.db_entries)

        # Buttons
        # Creates a button to edit info into the database
        self.edit_db_entry_button = tkinter.Button(self.button_frame,
                                                   text="Edit Database Entry",
                                                   command=self.edit_db_entry)

        # Creates a button to add info into the database
        self.add_db_entry_button = tkinter.Button(self.button_frame,
                                                  text="Add Database Entry",
                                                  command=self.add_db_entry)

        # Creates a button to remove info from the database
        self.remove_db_entry_button = tkinter.Button(self.button_frame,
                                                     text="Remove Database Entry",
                                                     command=self.remove_db_entry)

        # Creates a button to quit the program
        self.exit_button = tkinter.Button(self.exit_frame, text="Exit", command=self.window.destroy)

        # Packing
        # Adds the text to the GUI
        self.intro_text.pack(side='top')

        # Adds the database information to the GUI
        # self.db_entries.pack()
        self.db_scrollbox.pack(side='left')
        self.db_scrollbar.pack(side='right', fill=tkinter.Y)

        # Adds the buttons to the GUI
        self.edit_db_entry_button.pack(side='left')
        self.add_db_entry_button.pack(side='left')
        self.remove_db_entry_button.pack()
        self.exit_button.pack()

        # Frame packing
        # Adds the frames to the GUI
        self.text_frame.pack()
        self.db_frame.pack(padx=20)
        self.button_frame.pack()
        self.exit_frame.pack()

        # Lines 160-260 Coded By: Briely Gunn
        # Widgets for adding a student to the database

        # Widgets for the "add_db_entry" and "add_student" methods
        # Adds the new student's name textbox to the GUI
        self.add_name_textbox = tkinter.Entry(self.add_db_entry_frame,
                                              width=15)

        # Adds the new student's name text to the GUI
        self.add_name_text = tkinter.Label(self.add_db_entry_frame,
                                           text="Student's Name: ")

        # Adds the new student's age textbox to the GUI
        self.add_age_textbox = tkinter.Entry(self.add_db_entry_frame,
                                             width=3)

        # Adds the new student's age text to the GUI
        self.add_age_text = tkinter.Label(self.add_db_entry_frame,
                                          text="Student's Age: ")

        # Creates the variable for the upcoming radiobuttons
        self.radio_button_var = tkinter.IntVar()
        self.radio_button_var.set(1)

        # Adds the new student's gender radiobutton (male) to the GUI
        self.add_gender_male_radiobutton = tkinter.Radiobutton(self.add_db_entry_frame,
                                                               value=1,
                                                               text="Male",
                                                               width=10,
                                                               variable=self.radio_button_var)

        # Adds the new student's gender radiobutton (female) to the GUI
        self.add_gender_female_radiobutton = tkinter.Radiobutton(self.add_db_entry_frame,
                                                                 value=2,
                                                                 text="Female",
                                                                 width=10,
                                                                 variable=self.radio_button_var)

        # Adds the new student's gender text to the GUI
        self.add_gender_text = tkinter.Label(self.add_db_entry_frame,
                                             text="Student's Gender: ")

        # Adds the new student's country textbox to the GUI
        self.add_country_textbox = tkinter.Entry(self.add_db_entry_frame,
                                                 width=15)

        # Adds the new student's country text to the GUI
        self.add_country_text = tkinter.Label(self.add_db_entry_frame,
                                              text="Student's Country: ")

        # Adds the new student's timezone textbox to the GUI
        self.add_timezone_textbox = tkinter.Entry(self.add_db_entry_frame,
                                                  width=15)

        # Adds the new student's timezone text to the GUI
        self.add_timezone_text = tkinter.Label(self.add_db_entry_frame,
                                               text="Student's Timezone: ")

        # Adds the new student's email textbox to the GUI
        self.add_email_textbox = tkinter.Entry(self.add_db_entry_frame,
                                               width=25)

        # Adds the new student's email text to the GUI
        self.add_email_text = tkinter.Label(self.add_db_entry_frame,
                                            text="Student's Email: ")

        # Creates a button to add a student to the database
        self.add_student_button = tkinter.Button(self.add_db_entry_frame,
                                                 text="Add Student",
                                                 command=self.add_student)

        # Packing

        # Adds the text, textboxes, radiobuttons, and standard button for the "add_student" method to the GUI
        # Adds the name text and textbox to the GUI
        self.add_name_text.pack()
        self.add_name_textbox.pack()

        # Adds the age text and textbox to the GUI
        self.add_age_text.pack()
        self.add_age_textbox.pack()

        # Adds the gender text and radiobuttons to the GUI
        self.add_gender_text.pack()
        self.add_gender_male_radiobutton.pack()
        self.add_gender_female_radiobutton.pack()

        # Adds the country text and textbox to the GUI
        self.add_country_text.pack()
        self.add_country_textbox.pack()

        # Adds the timezone text and textbox to the GUI
        self.add_timezone_text.pack()
        self.add_timezone_textbox.pack()

        # Adds the email text and textbox to the GUI
        self.add_email_text.pack()
        self.add_email_textbox.pack()

        # Adds the "Add Student" button to the GUI
        self.add_student_button.pack()

        # Lines ???-??? Coded By:
        # Widgets for editing a student in the database
        # (Jacob you can put your GUI frame for you method here)

        # Lines ???-??? Coded By:
        # Widgets for removing a student from the database
        # (Caleb you can put your GUI frame for your method here)

        # Mainloop to make the GUI work
        tkinter.mainloop()

    # Method to format database entries for the scrollbox
    def db_gui_formatting(self, db_info: list):

        for row in db_info:

            # Gets the fields in the selected row
            db_id = str(row[0])
            db_name = str(row[1])
            db_age = str(row[2])
            db_gender = str(row[3])
            db_state = str(row[4])
            db_timezone = str(row[5])
            db_email = str(row[6])

            db_str_formatting(db_id)
            db_str_formatting(db_name)
            db_str_formatting(db_age)
            db_str_formatting(db_gender)

            db_row = (f"{db_id}".ljust(GUI_text_justification, " ") +
                      f"\t{db_name}".ljust(GUI_text_justification, " ") +
                      f"\t{db_age}".ljust(GUI_text_justification, " ") +
                      f"\t{db_gender}".ljust(GUI_text_justification, " ") +
                      f"\t{db_state}".ljust(GUI_text_justification, " ") +
                      f"\t{db_timezone}".ljust(GUI_text_justification, " ") +
                      f"\t{db_email}")

            self.db_scrollbox.insert(tkinter.END, db_row)

    # Coded by: Briely Gunn
    # Method to add a student to the database and print it to the GUI when the "Add Student" button is clicked
    def add_student(self):
        # Gets the new student's gender before they are added to the database
        if self.radio_button_var.get() == 1:
            self.student_gender = "male"
        else:
            self.student_gender = "female"

        # Calls the add_students function to add a new student to the database
        final_db_functions.add_student(str(self.add_name_textbox.get().ljust(GUI_text_justification, " ")),
                                       int(self.add_age_textbox.get()),
                                       str(self.student_gender),
                                       str(self.add_country_textbox.get().ljust(GUI_text_justification, " ")),
                                       str(self.add_timezone_textbox.get().ljust(GUI_text_justification, " ")),
                                       str(self.add_email_textbox.get().ljust(GUI_email_text_justification, " ")))

        # Gets the updated database info and formats it
        self.db_entries = str(final_db_functions.get_students()[final_db_functions.get_students().__len__() - 1])
        self.db_entries = db_str_formatting(self.db_entries)
        # self.db_info_formatted = self.db_str_formatting(self.db_info)

        # Destroys the erroneous database
        # self.db_entries.destroy()

        # Adds the formatted database info to the GUI
        self.db_gui_formatting(final_db_functions.get_students())

        # Packs the database info to the GUI

        # Unpacks the add_db_entry_frame for a cleaner GUI
        self.add_db_entry_frame.pack_forget()
        self.db_frame.pack_forget()

        # Repacks the exit and button frames
        self.db_frame.pack()
        self.button_frame.pack()
        self.exit_frame.pack()

    # Method to prepare for a new database entry when the "Add Database Entry" button is clicked
    def add_db_entry(self):

        # Unpacks the exit and button frames
        self.button_frame.pack_forget()
        self.exit_frame.pack_forget()

        # Packs the add_db_entry_frame
        self.add_db_entry_frame.pack()

    # This is the method you will be working on, Jacob (You can replace this comment with somthing like "Coded by: Jacob Goncharenko" once you finish it)
    # Method to edit an existing database entry when the "Edit Database Entry" button is clicked
    def edit_db_entry(self):
        self.button_frame.destroy()

    # This is the method you will be working on, Caleb (You can replace this comment with somthing like "Coded by: Caleb Harding" once you finish it)
    def remove_db_entry(self):
        self.button_frame.destroy()


if __name__ == '__main__':
    IntroGUI()
