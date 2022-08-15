import sys
import time
import random

import os
import shutil
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/User/Downloads"

# Event Hanlder Class
class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print("Your file has been created")

    def on_deleted(self, event):
        print("Your file has been deleted")

    def on_modified(self, event):
        print("Your file has been modified")

    def on_moved(self, event):
        print("Your file has been moved")

# Initialize Event Handler Class
event_handler = FileEventHandler()

# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()


#5_Write a exception for keyboardInterrupt

while True:
    time.sleep(2)
    print("running...")






