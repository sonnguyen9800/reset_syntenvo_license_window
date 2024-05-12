import os
import shutil

FolderName  = 'syntevo\\' # Name of the folder you want to remove
appdataPath = os.path.expanduser('~/AppData/Roaming')  # Path to Roaming directory
fullPath    = os.path.join(appdataPath, FolderName).replace('/', '\\')  # Full path to the specified folder
       
# Remove the folder if it exists
if os.path.isdir(fullPath):
    shutil.rmtree(fullPath)   # Use this for delete directories and their contents recursively
else:
    print('The directory does not exist')
