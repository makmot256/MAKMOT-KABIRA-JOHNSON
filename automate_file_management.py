import os
import shutil

# define path to download dir
DOWNLOAD_DIR = os.path.expanduser("~/Downloads")

# define target folders

folders = {
    "Documents": ["pdf", "docx", "txt"],
    "Images": ["jpg", "jpeg", "png", "gif"],
    "Videos": ["mp4", "mkv", "avi"],
    "Music": ["mp3", "wav", "flac"],
    "Archives": ["zip", "rar", "tar", "gz"],
    "Scripts": ["py", "js", "sh", "bat"],
    "Spreadsheets": ["xlsx", "csv"],
    "Presentations": ["pptx", "ppt"],
    "Installers": ["exe", "msi", "dmg"],
    }

# create target folders if they don't exist
for folder in folders.keys():
    target_path = os.path.join(DOWNLOAD_DIR, folder)
    if not os.path.exists(target_path):
        os.makedirs(target_path)
        
# loop through files in the download directory
for filename in os.listdir(DOWNLOAD_DIR):
    # get file extension
    extension = filename.split(".")[-1]
    
    # move file to appropriate folder
    for folder, extensions in folders.items():
        if extension in extensions:
            source_path = os.path.join(DOWNLOAD_DIR, filename)
            target_path = os.path.join(DOWNLOAD_DIR, folder)
            shutil.move(source_path, target_path)
            break
        
