# an automation script that backups files from a folder within 3 mins of modification of that folder
import os
import time
import shutil
# Define the source folder to monitor
SOURCE_FOLDER = os.path.expanduser("~/Downloads")
# Define the backup folder
BACKUP_FOLDER = os.path.expanduser("~/Backup")
# Create the backup folder if it doesn't exist
if not os.path.exists(BACKUP_FOLDER):
    os.makedirs(BACKUP_FOLDER)
# Function to backup files modified within the last 3 minutes
def backup_recent_files():
    current_time = time.time()
    three_minutes_ago = current_time - 180  # 3 minutes in seconds
    for filename in os.listdir(SOURCE_FOLDER):
        source_path = os.path.join(SOURCE_FOLDER, filename)
        if os.path.isfile(source_path):
            modification_time = os.path.getmtime(source_path)
            if modification_time > three_minutes_ago:
                backup_path = os.path.join(BACKUP_FOLDER, filename)
                shutil.copy2(source_path, backup_path)
                print(f"Backed up: {filename}")
# Main loop to monitor the source folder
while True:
    backup_recent_files()
    time.sleep(60)  # Check every minute
# Note: This script runs indefinitely, monitoring the source folder every minute.
# To stop the script, you can use Ctrl+C in the terminal where it's running.