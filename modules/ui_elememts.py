import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk
from modules.file_handler import choose_files_and_update
from modules.file_sender import send_files

# This defines a new class called SecureSendUI
class SecureSendUI:

    #This is the constructor. It runs automatically when you create an object of this class.
    # window is the paramenter we pass from app.py, It is the main application window where all UI elements will appear.
    def __init__(self, window):
        self.window = window  #This stores the window inside the object so other parts of the class can access it.
        self.files = [] #This creates an empty list to store files that the user will select later.




#-----------------creating LEFT SIDE Elements--------------------------

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

        left_grid = Gtk.Grid(column_spacing=10, row_spacing=20)
        hbox.append(left_grid)  # places the grid inside the horizontal box.


        #Adding Server IP label and entry
        left_grid.attach(Gtk.Label(label="Server IP:"), 0, 0, 1, 1) #puts label in column 0, row 0, spanning 1 column and 1 row.
        self.ip_entry = Gtk.Entry() #creates a text input box for the user to type the server IP."self.ip_entry " stores it so we can read its value later.
        left_grid.attach(self.ip_entry, 1, 0, 1, 1) # places the entry in column 1, row 0.

        #Add username field
        #Same as the previous entry
        left_grid.attach(Gtk.Label(label="Username:"), 0, 1, 1, 1)
        self.user_entry = Gtk.Entry()
        left_grid.attach(self.user_entry, 1, 1, 1, 1)

        #Add password field
        #Same as the previous entry
        left_grid.attach(Gtk.Label(label="Password:"), 0, 2, 1, 1)
        self.pass_entry = Gtk.Entry()
        self.pass_entry.set_visibility(False) #hides the text while typing
        left_grid.attach(self.pass_entry, 1, 2, 1, 1)

        #Same as the previous entry
        left_grid.attach(Gtk.Label(label="Destination Path:"), 0, 3, 1, 1)
        self.destination_entry = Gtk.Entry()
        self.destination_entry.set_text("/tmp/")  # Set default path
        left_grid.attach(self.destination_entry, 1, 3, 1, 1)

        #Adding Send button
        self.send_btn = Gtk.Button(label="Send Files") #Creates a button labeled “Send Files”.
        left_grid.attach(self.send_btn, 0, 4, 2, 1)# Placed in row 3, spanning 2 columns, so it’s centered under the entries.
        
        # Function that handle sending logic
        self.send_btn.connect("clicked", self.on_send_files_clicked)


        #Adding Clear button
        self.clear_btn = Gtk.Button(label="Clear") #Creates a button labeled “Clear”.
        left_grid.attach(self.clear_btn, 0, 5, 2, 1)# Placed in row 3, spanning 2 columns, so it’s centered under the entries.

        # Feedback label to show the success or failure message
        self.feedback_label = Gtk.Label(label="")
        self.feedback_label.set_wrap(True)
        left_grid.attach(self.feedback_label, 0, 7, 2, 1)  # row 5, spanning 2 columns






#-----------------creating RIGHT SIDE Elements--------------------------


# Right side frame
        right_frame = Gtk.Frame()
        right_frame.set_margin_top(10)
        right_frame.set_margin_bottom(10)
        right_frame.set_margin_start(10)
        right_frame.set_margin_end(10)

        right_frame.set_size_request(600, -1)  

        # Inside the frame, create a vertical box for file labels
        right_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        right_frame.set_child(right_box)

        # Horizontal box for the buttons (side by side)
        buttons_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        right_box.append(buttons_box)

        # Add a choose file button inside the box
        self.choose_files_btn = Gtk.Button(label="Choose Files")
        self.choose_files_btn.set_hexpand(True)          
        self.choose_files_btn.connect("clicked", self.on_choose_files_clicked)
        buttons_box.append(self.choose_files_btn)
       
        # "Clear" button
        self.clear_btn = Gtk.Button(label="Clear Files")
        self.clear_btn.set_hexpand(True)  
        self.clear_btn.connect("clicked", self.on_clear_clicked)
        buttons_box.append(self.clear_btn)







        # By default the no files are selected message is displayed in side the box.
        self.files_label = Gtk.Label(label="(No files selected)")
        right_box.append(self.files_label)

        # Add the frame to the main hbox
        hbox.append(right_frame)

        #Returning the main container
        return hbox  #Returns the main horizontal box 



#----------FUNCTIONS TO HANDLE BUTTON EVENTS--------------------


    # This function is used to open a file picker when choose File button is clicked and display it in the box. its implementation is in modules/file_handler.py
    def on_choose_files_clicked(self, button):
        self.feedback_label.set_text("")        
        choose_files_and_update(self.window, self.files_label, self.files)

    # This function is used to clear the files that ae choosen by select files button sialogue box.
    def on_clear_clicked(self, button):
        self.files.clear()
        self.feedback_label.set_text("")
        self.files_label.set_text("(No files selected)")

        # Reset send feedback label
        self.feedback_label.set_text("")


    # function that handle sending logic
    def on_send_files_clicked(self, button):
        if not self.files:
            #print("No files selected!")
            self.feedback_label.set_text("No files selected!")

            return

        server_ip = self.ip_entry.get_text()
        username = self.user_entry.get_text()
        password = self.pass_entry.get_text()
        dest_path = self.destination_entry.get_text()

        success, fail = send_files(self.files, server_ip, username, password, dest_path)

        if fail:
            result_text = f"✅ Sent: {len(success)} files\n❌ Failed: {len(fail)} files"
        else:
            result_text = f"✅ Sent: {len(success)} files successfully!"

            self.feedback_label.set_text(result_text)























