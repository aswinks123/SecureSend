import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

# This defines a new class called SecureSendUI
class SecureSendUI:

    #This is the constructor. It runs automatically when you create an object of this class.
    # window is the paramenter we pass from app.py, It is the main application window where all UI elements will appear.
    def __init__(self, window):
        self.window = window  #This stores the window inside the object so other parts of the class can access it.
        self.files = [] #This creates an empty list to store files that the user will select later.




#-----------------creating  Elements--------------------------

    def build_layout(self):  # function that created the UI elements

        # Creates a horizontal box (hbox) that will hold all UI elements.
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=20) 
        hbox.set_margin_top(15)
        hbox.set_margin_bottom(15)
        hbox.set_margin_start(15)
        hbox.set_margin_end(15)
        #puts this box inside the main window.
        self.window.set_child(hbox)
        # What we did is : Create a horizontal container with some space around it and put it inside the window.”





        # Adding a grid inside the box. Gtk.Grid lets you arrange elements in rows and columns.
        # here we are creating left side grid, hold left side elemets of the box.

        left_grid = Gtk.Grid(column_spacing=10, row_spacing=10)
        hbox.append(left_grid)  # places the grid inside the horizontal box.


        #Adding Server IP label and entry
        left_grid.attach(Gtk.Label(label="Server IP:"), 0, 0, 1, 1) #puts label in column 0, row 0, spanning 1 column and 1 row.
        self.ip_entry = Gtk.Entry() #creates a text input box for the user to type the server IP."self.ip_entry " stores it so we can read its value later.
        left_grid.attach(self.ip_entry, 1, 0, 1, 1) # places the entry in column 1, row 0.


        #Same as the previous entry
        left_grid.attach(Gtk.Label(label="Username:"), 0, 1, 1, 1)
        self.user_entry = Gtk.Entry()
        left_grid.attach(self.user_entry, 1, 1, 1, 1)


        #Same as the previous entry
        left_grid.attach(Gtk.Label(label="Password:"), 0, 2, 1, 1)
        self.pass_entry = Gtk.Entry()
        self.pass_entry.set_visibility(False) #hides the text while typing
        left_grid.attach(self.pass_entry, 1, 2, 1, 1)


        #Adding Send button
        self.send_btn = Gtk.Button(label="Send Files") #Creates a button labeled “Send Files”.
        left_grid.attach(self.send_btn, 0, 3, 2, 1)# Placed in row 3, spanning 2 columns, so it’s centered under the entries.


        #Returning the main container
        return hbox  #Returns the main horizontal box so it can be used later if needed.
