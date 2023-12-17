# Final Project: Week 14 (Team) (GUI)
# Coded by Briely Gunn Jacob Goncharenko, and Caleb Harding

import tkinter
from tkinter import simpledialog, messagebox, END
import final_db_functions

# Text justification variable for GUI spacing
GUI_text_justification_l = 20
GUI_text_justification_r = 20


# Functions
# Function to left justify all needed strings
def gui_str_justification_left(string: str):
    return string.ljust(GUI_text_justification_l, " ")


# Function to right justify all needed strings
def gui_str_justification_right(string: str):
    return string.rjust(GUI_text_justification_r, " ")


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
        self.db_info = []
        self.window = tkinter.Tk()

        # Prints the title of the window
        self.window.title("Group 5 Final Project")

        # Initialized Widgets

        # Frames
        self.text_frame = tkinter.Frame(self.window)
        self.db_frame = tkinter.Frame(self.window)
        self.button_frame = tkinter.Frame(self.window)

        # Creates a frame for entering entries
        self.add_db_entry_frame = tkinter.Frame(self.window)

        # Creates the frames for the different fields within the entry frame
        self.add_name_frame = tkinter.Frame(self.add_db_entry_frame)
        self.add_age_frame = tkinter.Frame(self.add_db_entry_frame)
        self.add_gender_frame = tkinter.Frame(self.add_db_entry_frame)
        self.add_country_frame = tkinter.Frame(self.add_db_entry_frame)
        self.add_timezone_frame = tkinter.Frame(self.add_db_entry_frame)
        self.add_email_frame = tkinter.Frame(self.add_db_entry_frame)
        self.add_student_frame = tkinter.Frame(self.add_db_entry_frame)

        # Creates the frames that go under the add database entry frame
        self.edit_db_entry_frame = tkinter.Frame(self.window)
        self.remove_db_entry_frame = tkinter.Frame(self.window)
        self.exit_frame = tkinter.Frame(self.window)

        # Text
        self.intro_text = tkinter.Label(self.db_frame, text="Student Information Database\n")

        # Database text
        # Formats the database columns
        self.db_text = ("ID#:".ljust(10) +
                        "Name:".ljust(25) +
                        "Age:".ljust(10) +
                        "Gender:".ljust(15) +
                        "Country:".ljust(20) +
                        "Timezone:".ljust(25) +
                        "Email:".ljust(30))

        # Formats the Database info
        self.db_entries = final_db_functions.get_students()

        # Creates the scrollbox (Listbox) for the database
        self.db_scrollbox = tkinter.Listbox(self.db_frame,
                                            justify='left',
                                            height=15,
                                            width=100)
        # Creates the scrollbar for the database
        self.db_scrollbar = tkinter.Scrollbar(self.db_frame,
                                              orient=tkinter.VERTICAL)

        # Configures the scrollbox and scrollbar
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

        # Creates a button to remove info from the database
        self.remove_db_entry_button = tkinter.Button(self.button_frame,
                                                     text="Remove Database Entry",
                                                     command=self.remove_db_entry)

        # Creates a button to quit the program
        self.exit_button = tkinter.Button(self.exit_frame, text="Exit",
                                          command=self.window.destroy)

        # Packing
        # Adds the text to the GUI
        self.intro_text.pack(side='top')

        # Adds the database information to the GUI
        self.db_scrollbox.pack(side='left')
        self.db_scrollbar.pack(side='right', fill=tkinter.Y)

        # Adds the buttons to the GUI
        self.edit_db_entry_button.pack(side='left')
        self.remove_db_entry_button.pack()
        self.exit_button.pack()

        # Frame packing
        # Adds the different frames to the GUI
        self.text_frame.pack()
        self.db_frame.pack(side='right', padx=20, pady=20)

        # Packs the frames for adding an entry to the database
        self.add_db_entry_frame.pack(padx=20, pady=25)
        self.add_name_frame.pack(anchor='w')
        self.add_age_frame.pack(anchor='w')
        self.add_gender_frame.pack(anchor='w')
        self.add_country_frame.pack(anchor='w')
        self.add_timezone_frame.pack(anchor='w')
        self.add_email_frame.pack(anchor='w')
        self.add_student_frame.pack()

        # Packs the rest of the widgets
        self.exit_frame.pack(side='bottom', pady=20)
        self.button_frame.pack(side='bottom', padx=20)

        # Section 1 Coded By: Briely Gunn
        # Widgets for adding a student to the database

        # Widgets for the "add_student" method
        # Adds the new student's name textbox to the GUI
        self.add_name_textbox = tkinter.Entry(self.add_name_frame,
                                              width=15)

        # Adds the new student's name text to the GUI
        self.add_name_text = tkinter.Label(self.add_name_frame,
                                           text=gui_str_justification_right("Student's Name:\t"),
                                           justify='right')

        # Adds the new student's age textbox to the GUI
        self.add_age_textbox = tkinter.Entry(self.add_age_frame,
                                             width=3)

        # Adds the new student's age text to the GUI
        self.add_age_text = tkinter.Label(self.add_age_frame,
                                          text=gui_str_justification_right("Student's Age:\t"),
                                          justify='right')

        # Creates the variable for the upcoming radiobuttons
        self.radio_button_var = tkinter.IntVar()
        self.radio_button_var.set(1)

        # Adds the new student's gender radiobutton (male) to the GUI
        self.add_gender_male_radiobutton = tkinter.Radiobutton(self.add_gender_frame,
                                                               value=1,
                                                               text="Male",
                                                               width=10,
                                                               variable=self.radio_button_var)

        # Adds the new student's gender radiobutton (female) to the GUI
        self.add_gender_female_radiobutton = tkinter.Radiobutton(self.add_gender_frame,
                                                                 value=2,
                                                                 text="Female",
                                                                 width=10,
                                                                 variable=self.radio_button_var)

        # Adds the new student's gender text to the GUI
        self.add_gender_text = tkinter.Label(self.add_gender_frame,
                                             text=gui_str_justification_right(f"Student's Gender:\t"),
                                             justify='right')

        # Adds the new student's country textbox to the GUI
        self.add_country_textbox = tkinter.Entry(self.add_country_frame,
                                                 width=15)

        # Adds the new student's country text to the GUI
        self.add_country_text = tkinter.Label(self.add_country_frame,
                                              text=gui_str_justification_right("Student's Country:\t"),
                                              justify='right')

        # Adds the new student's timezone textbox to the GUI
        self.add_timezone_textbox = tkinter.Entry(self.add_timezone_frame,
                                                  width=15, justify='left')

        # Adds the new student's timezone text to the GUI
        self.add_timezone_text = tkinter.Label(self.add_timezone_frame,
                                               text=gui_str_justification_right("Student's Timezone:\t"),
                                               justify='right')

        # Adds the new student's email textbox to the GUI
        self.add_email_textbox = tkinter.Entry(self.add_email_frame,
                                               width=30, justify='left')

        # Adds the new student's email text to the GUI
        self.add_email_text = tkinter.Label(self.add_email_frame,
                                            text=gui_str_justification_right("Student's Email:\t"),
                                            justify='right')

        # Creates a button to add a student to the database
        self.add_student_button = tkinter.Button(self.add_student_frame,
                                                 text="Add Student",
                                                 command=self.add_student)

        # Packing

        # Adds the text, textboxes, radiobuttons, and standard button for the "add_student" method to the GUI
        # Adds the name text and textbox to the GUI
        self.add_name_text.pack(side='left')
        self.add_name_textbox.pack(anchor='w')

        # Adds the age text and textbox to the GUI
        self.add_age_text.pack(side='left')
        self.add_age_textbox.pack(anchor='w')

        # Adds the gender text and radiobuttons to the GUI
        self.add_gender_text.pack(side='left')
        self.add_gender_male_radiobutton.pack(anchor='w')
        self.add_gender_female_radiobutton.pack(anchor='w')

        # Adds the country text and textbox to the GUI
        self.add_country_text.pack(side='left')
        self.add_country_textbox.pack(anchor='w')

        # Adds the timezone text and textbox to the GUI
        self.add_timezone_text.pack(side='left')
        self.add_timezone_textbox.pack(anchor='w')

        # Adds the email text and textbox to the GUI
        self.add_email_text.pack(side='left')
        self.add_email_textbox.pack(anchor='w')

        # Adds the "Add Student" button to the GUI
        self.add_student_button.pack()

        # Mainloop to make the GUI work
        tkinter.mainloop()

    # Method to format database entries for the scrollbox
    def db_gui_formatting(self, db_info: list):
        # gets each column's width
        column_widths = [10, 25, 10, 15, 20, 20, 30]

        for row in db_info:
            # Get the fields in the selected row
            db_id = str(row[0])
            db_name = str(row[1])
            db_age = str(row[2])
            db_gender = str(row[3])
            db_state = str(row[4])
            db_timezone = str(row[5])
            db_email = str(row[6])

            # Justifies the tuples
            formatted_row = [db_id.ljust(column_widths[0]),
                             db_name.ljust(column_widths[1]),
                             db_age.ljust(column_widths[2]),
                             db_gender.ljust(column_widths[3]),
                             db_state.ljust(column_widths[4]),
                             db_timezone.ljust(column_widths[5]),
                             db_email.ljust(column_widths[6])]

            # Joins the formatted tuples into a single string
            db_row = "".join(formatted_row)

            # Adds the tuples to the scrollbox
            self.db_scrollbox.insert(tkinter.END, db_row)

    # Coded by: Briely Gunn
    # Method to add a student to the database and print it to the GUI when the "Add Student" button is clicked
    def add_student(self):
        # Gets the new student's gender before they are added to the database
        if self.radio_button_var.get() == 1:
            student_gender = "male"
        else:
            student_gender = "female"

        # Calls the add_students function to add a new student to the database
        final_db_functions.add_student(str(self.add_name_textbox.get()),
                                       int(self.add_age_textbox.get()),
                                       str(student_gender),
                                       str(self.add_country_textbox.get().ljust(GUI_text_justification_l, " ")),
                                       str(self.add_timezone_textbox.get().ljust(GUI_text_justification_l, " ")),
                                       str(self.add_email_textbox.get().ljust(GUI_text_justification_l, " ")))

        # Updates the database entry to prevent errors when removing a student
        self.db_info = final_db_functions.get_students()
        self.db_entries = self.db_info

        # Adds the formatted database info to the GUI
        self.db_gui_formatting(final_db_functions.get_students())

        # Refreshes the database scrollbox
        self.refresh_db_info()

    # Method to refresh database
    def refresh_db_info(self):
        self.db_info = final_db_functions.get_students()

        self.db_scrollbox.delete(1, END)
        self.db_gui_formatting(self.db_info)

    # Coded by: Jacob Goncharenko
    # Method to edit an existing database entry when the "Edit Database Entry" button is clicked
    def edit_db_entry(self):
        student_id_to_edit = simpledialog.askinteger("Edit Student", "Enter the student ID to edit:")

        if student_id_to_edit is not None:
            cursor, connection = final_db_functions.get_connection()
            cursor.execute("SELECT * FROM students WHERE student_id=?", (student_id_to_edit,))
            student_info = cursor.fetchone()

            if student_info:
                edit_window = tkinter.Tk()
                edit_window.title("Edit Student Information")

                fields = ["Name", "Age", "Gender", "Country", "Timezone", "Email"]
                entry_widgets = {}
                for i, field in enumerate(fields):
                    label = tkinter.Label(edit_window, text=f"{field}:")
                    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")

                    entry = tkinter.Entry(edit_window, width=30)
                    entry.insert(0, str(student_info[i + 1]))
                    entry.grid(row=i, column=1, padx=10, pady=5, sticky="w")

                    entry_widgets[field.lower()] = entry

                def update_student_info():
                    new_info = {field.lower(): entry.get() for field, entry in entry_widgets.items()}
                    final_db_functions.edit_student(student_id_to_edit, new_info)
                    connection.commit()
                    connection.close()

                    edit_window.destroy()
                    self.refresh_db_info()

                update_button = tkinter.Button(edit_window, text="Update", command=update_student_info)
                update_button.grid(row=len(fields), column=0, columnspan=2, pady=10)

                edit_window.mainloop()
            else:
                messagebox.showinfo("Error", f"No student found with ID: {student_id_to_edit}")

    # Coded by Caleb Harding
    # Method to remove a database entry
    def remove_db_entry(self):
        # Gets the selected database entry from the scrollbox
        indexes = self.db_scrollbox.curselection()

        # Checks to make sure the scrollbox title will not be deleted
        if len(indexes) > 0:

            # Gets the selected row from the user
            for index in reversed(indexes):
                # Gets the student index in the database to remove
                if index > 0:
                    student_id = self.db_entries[index - 1][0]
                # Gets the student index in the database to remove if there is 2 or fewer entries
                else:
                    student_id = self.db_entries[index][0]

                # Removes the selected row
                final_db_functions.remove_student(student_id)

            # Updates the database entries after they are removed
            self.db_info = final_db_functions.get_students()
            self.db_entries = self.db_info

            # refreshes the scrollbox
            self.refresh_db_info()

        # Displays if no database entry is selected
        else:
            tkinter.messagebox.showinfo(message="No entry selected.")


if __name__ == '__main__':
    IntroGUI()
