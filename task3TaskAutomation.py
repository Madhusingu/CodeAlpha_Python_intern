import os
import shutil

# Set your source and destination directories here
source_folder = r"c:\Users\madhu\OneDrive\Documents\New folder\OneDrive\Pictures"      
destination_folder = r"C:\Users\madhu\OneDrive\Desktop\codealfa-intern\python development\jpg Automation"  

# Create the destination folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

files_moved = 0

# Loop through all items in the source folder
for filename in os.listdir(source_folder):
    if filename.lower().endswith(".jpg"):
        src_path = os.path.join(source_folder, filename)
        dst_path = os.path.join(destination_folder, filename)
        shutil.move(src_path, dst_path)
        files_moved += 1
        print(f"Moved: {filename}")

print(f"Total .jpg files moved: {files_moved}")
