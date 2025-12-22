# modules/file_handler.py
import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk


def choose_files_and_update(window, files_label, files_list):
    """
    Opens a file chooser dialog, stores selected files in files_list,
    and updates files_label with selected paths.
    """
    dialog = Gtk.FileDialog()
    dialog.set_title("Select files")

    # Open multiple selection
    dialog.open_multiple(
        window,
        None,
        lambda d, result: on_files_selected(d, result, files_label, files_list)
    )

def on_files_selected(dialog, result, files_label, files_list):
    try:
        files = dialog.open_multiple_finish(result)
        files_list.clear()
        display_text = []

        for f in files:
            path = f.get_path()
            files_list.append(path)
            display_text.append(path)

        files_label.set_text("\n".join(display_text))

    except Exception:
        # User cancelled dialog
        pass