import os
import shutil

# Define path to downloads folder and list all files and directories in this folder
downloads = 'C:/Users/Adaskox/Downloads'
downloads_files = os.listdir(downloads)

# Define paths to folders for specified extensions
pics = 'C:/Users/Adaskox/Downloads/pics'
docs = 'C:/Users/Adaskox/Downloads/docs'
installers = 'C:/Users/Adaskox/Downloads/installers'
zips = 'C:/Users/Adaskox/Downloads/zips'
sounds = 'C:/Users/Adaskox/Downloads/sounds'

# Store unique extensions of files
remaining = set()

# Check downloads folder for files and add their extensions to set
for file in os.listdir(downloads):
    if os.path.isfile(os.path.join(downloads, file)):
        file_name, file_extension = os.path.splitext(file)
        remaining.add(file_extension)

# Add files ending with specified extension to a folder
for file in downloads_files:
    if file.endswith('.png') or file.endswith('.jpg'):
        shutil.move(os.path.join(downloads,file), os.path.join(pics,file))
    elif file.endswith('.pdf') or file.endswith('.xlsx') or file.endswith('.txt'):
        shutil.move(os.path.join(downloads,file), os.path.join(docs,file))
    elif file.endswith('.exe'):
        shutil.move(os.path.join(downloads,file), os.path.join(installers,file))
    elif file.endswith('.zip'):
        shutil.move(os.path.join(downloads,file), os.path.join(zips,file))
    elif file.endswith('.WAV') or file.endswith('.mp4'):
        shutil.move(os.path.join(downloads,file), os.path.join(sounds,file))

# Print all remaining files extensions
for extension in remaining:
    print(extension)