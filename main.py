# main.py

from pathlib import Path
import sys
import time
import shutil # A more powerful tool for file operations

# --- Constants ---
DOWNLOADS_PATH = Path.home() / 'Downloads'

# A dictionary mapping file suffixes to their destination folder
FOLDER_MAPPING = {
    'Images': ['.jpeg', '.jpg', '.png', '.gif', '.bmp', '.svg'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx', '.md'],
    'Audio': ['.mp3', '.wav', '.aac'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Executables': ['.exe', '.msi'],
}

def get_destination_folder(suffix: str) -> str:
    """Finds the destination folder for a given file suffix."""
    for folder_name, suffixes in FOLDER_MAPPING.items():
        if suffix.lower() in suffixes:
            return folder_name
    return 'Others' # Default folder if no match is found

def organize_folder(path: Path):
    """
    Organizes all files in the given path according to FOLDER_MAPPING.
    """
    if not path.exists() or not path.is_dir():
        print(f"❌ Error: The directory '{path}' does not exist.")
        sys.exit(1)
        
    print(f"🚀 Starting organization of '{path.name}'...")
    time.sleep(1) # Give the user a moment to read

    for entry in path.iterdir():
        # We only care about files, not subdirectories
        if entry.is_file():
            # 1. Determine the destination folder name
            dest_folder_name = get_destination_folder(entry.suffix)
            
            # 2. Create the full path for the destination folder
            dest_folder_path = path / dest_folder_name
            
            # 3. Create the folder if it doesn't exist
            dest_folder_path.mkdir(exist_ok=True)
            
            # 4. Construct the full destination file path
            dest_file_path = dest_folder_path / entry.name
            
            # 5. Move the file
            print(f"Moving '{entry.name}' -> '{dest_folder_name}/'")
            shutil.move(str(entry), str(dest_file_path))

    print("\n✅ Organization complete!")


if __name__ == "__main__":
    organize_folder(DOWNLOADS_PATH)