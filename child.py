import os
import shutil
import sys
import time
import random
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:"

class FileEventHandler(FileSystemEventHandler):
     def on_created(self, event):
          print(f"Created {event.src_path}")
     def on_deleted(self, event):
          print(f"Deleted {event.src_path}")
     def on_modified(self, event):
          print(f"Modified {event.src_path}")
     def on_moved(self, event):
          print(f"Moved {event.src_path}")
     

observer = Observer()
observer.schedule(FileEventHandler(), from_dir, recursive=True)
observer.start()

try:
     while True:
          time.sleep(2)
          print("Running")
except KeyboardInterrupt:
     print("Ended Observer")
     observer.stop()



# imageFolderPath = "C:\\Users\\aryan\\Downloads\\Documents"
# takeImagesFromPath = "C:\\Users\\aryan\\Downloads"
# extensions = [".pdf", '.docx', '.doc', '.txt']

# for file in os.listdir(takeImagesFromPath):
#      if not os.path.isdir(file):
#           fileName = os.path.splitext(file)[0]
#           fileExtension = os.path.splitext(file)[1]
#           fileNameAndExtension = fileName + fileExtension
#           if fileExtension in extensions:
#                shutil.move(takeImagesFromPath + "\\" + fileNameAndExtension, imageFolderPath)
