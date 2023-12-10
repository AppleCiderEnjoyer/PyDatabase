# Final Project: Week 13 (Team) (GUI)
# Coded by Briely Gunn Jacob Goncharenko, and Caleb Harding

import tkinter
import final_db_functions


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


# GUI containing the database information
class DBGUI:
    def __init__(self):
        self.window = tkinter.Tk()

        # Prints the title of the window
        self.window.title("Group 5 Final Project")

        self.text_frame = tkinter.Frame(self.window)
        self.db_frame = tkinter.Frame(self.window)
        self.button_frame = tkinter.Frame(self.window)
        self.exit_frame = tkinter.Frame(self.window)

        # Text
        self.intro_text = tkinter.Label(self.text_frame,
                                        text="Student Information Database\n")

        # Database text
        # Formats the database columns
        self.db_text = tkinter.Label(self.db_frame,
                                     text=f" ID#:"
                                          "\t Name:"
                                          "\t\t Age:"
                                          "\t Gender:"
                                          "\t Country:"
                                          "\t\t Timezone:"
                                          "\t\t Email:\t\n",
                                     justify='left',
                                     anchor='w', width=100)

        # Formats the Database info
        self.db_info = str(final_db_functions.get_students())
        self.db_info_formatted = self.db_str_formatting(self.db_info)

        # Adds the formatted database information to the label
        self.db_entries = tkinter.Label(self.db_frame,
                                        text=self.db_info_formatted,
                                        justify='left',
                                        anchor='w', width=100)

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
        self.intro_text.pack()

        # Adds the database information to the GUI
        self.db_text.pack()
        self.db_entries.pack()

        # Adds the buttons to the GUI
        self.edit_db_entry_button.pack(side='left')
        self.add_db_entry_button.pack(side='left')
        self.remove_db_entry_button.pack()
        self.exit_button.pack()

        # Adds the frames to the GUI
        self.text_frame.pack()
        self.db_frame.pack()
        self.button_frame.pack()
        self.exit_frame.pack()

        # Mainloop to make the GUI work
        tkinter.mainloop()

    # Method to format the database table into readable text
    def db_str_formatting(self, db_string):
        self.db_info_formatted = (str(db_string)
                                  .replace("),", "\n")
                                  .replace("(", "")
                                  .replace(")", "")
                                  .replace("'", "")
                                  .replace("[", "")
                                  .replace("]", "")
                                  .replace(",", "\t"))
        return self.db_info_formatted

    # Method to organize the database tables
    def db_organizing(self):
        # Temp code
        self.window.destroy()

    # Method to add a new database entry when the "Add Database Entry" button is clicked
    def add_db_entry(self):

        # Calls the add_students function to add a new student to the database
        final_db_functions.add_student(str(), int(), str(), str(), str(), str())

        # Gets the updated database info and formats it
        self.db_info = str(final_db_functions.get_students())
        self.db_info_formatted = self.db_str_formatting(self.db_info)

        # Destroys the erroneous database
        self.db_entries.destroy()

        # Adds the formatted database info to the GUI
        self.db_entries = tkinter.Label(self.db_frame,
                                        text=self.db_info_formatted,
                                        justify='left',
                                        anchor='w', width=100)

        # Packs the database info to the GUI
        self.db_entries.pack()

    # Method to edit an existing database entry when the "Edit Database Entry" button is clicked
    def edit_db_entry(self):
        self.button_frame.destroy()

    def remove_db_entry(self):
        self.button_frame.destroy()


if __name__ == '__main__':
    IntroGUI()
