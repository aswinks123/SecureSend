import paramiko
import os

# For threading
import threading
from gi.repository import GLib


def send_files(files, server_ip, username, password, dest_path, progress_callback=None):
    """
    Sends a list of files to a remote server via SCP (using paramiko).
    Returns a tuple (success_list, fail_list)
    """
    success_list = []
    fail_list = []
    total = len(files)

    # Connect to the server
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(server_ip, username=username, password=password)

        sftp = ssh.open_sftp()

        # Ensure destination path exists
        try:
            sftp.chdir(dest_path)
        except IOError:
            sftp.mkdir(dest_path)
            sftp.chdir(dest_path)

        # Send each file
        for idx, f in enumerate(files, start=1):
            filename = os.path.basename(f)
            try:
                sftp.put(f, os.path.join(dest_path, filename))
                success_list.append(f)
            except Exception:
                fail_list.append(f)
             # Call progress callback if provided
            if progress_callback:
                fraction = idx / total
                progress_callback(fraction)           

        sftp.close()
        ssh.close()
    except Exception as e:
        # If connection fails, all files fail
        fail_list = files.copy()

    return success_list, fail_list

