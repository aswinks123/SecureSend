# Created by: Aswin KS
# About this file: This file is the main UI of the application.


# gi is the GObject Introspection library. It allows Python to use libraries written in C, like GTK.
import gi

#ensures you are using GTK version 4. GTK 4 is the latest major version.
gi.require_version("Gtk", "4.0")

#imports all GTK classes so you can use
from gi.repository import Gtk

#import the UI_element module that we created that holds the elements like button, label etc. 
# check the file under modules directory.
from modules.ui_elememts import SecureSendUI

#--------------------------------------------------------

# create GTK application class: we are creating a subsclass of "Gtk.Application" . it is the standard way to create GTK applications
# application_id is like a unique name for your app.

class SecureSendGUI(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.aswin.securesend")


#----------------------------------------------------------

# do_activate is a method automatically called when your app starts.

    def do_activate(self):
        # Gtk.ApplicationWindow is a window tied to your app. Always use this with Gtk.Application
        self.window = Gtk.ApplicationWindow(application=self)

        # Sets the text on the title bar.
        self.window.set_title("SecureSend")

        # Window size in pixels.
        self.window.set_default_size(1000, 700)

        # Prevents the user from resizing the window.
        self.window.set_resizable(False)

        self.ui = SecureSendUI(self.window)
        self.ui.build_layout()

        # Shows the window on the screen
        self.window.present()


#--------------------------------------------------------

# Creates an instance of your app.
app = SecureSendGUI()

# Calls run(), which starts the GTK main loop. Everything in GTK runs inside this loop, listening for events like clicks or keypresses.
app.run()
