from pathlib import Path
import sys
import time
import shutil 


DOWNLOADS_PATH = Path.home() / 'Downloads'

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
    return 'Others' 

def organize_folder(path: Path, dry_run: bool = True): 
    """
    Organizes files in the given path.
    If dry_run is True, it will only print the actions it would take.
    """
    if not path.exists() or not path.is_dir():
        print(f"❌ Error: The directory '{path}' does not exist.")
        sys.exit(1)
        
    print(f"🚀 Starting organization of '{path.name}'...")
    if dry_run:
        print("🚨 DRY RUN MODE IS ENABLED. No files will be moved.")
    
    time.sleep(1)

    for entry in path.iterdir():
        if entry.is_file():
            dest_folder_name = get_destination_folder(entry.suffix)
            dest_folder_path = path / dest_folder_name
            unique_dest_path = get_unique_filepath(dest_folder_path / entry.name)
            
            action_message = f"Move '{entry.name}' -> '{unique_dest_path.parent.name}/{unique_dest_path.name}'"

            if dry_run:
                print(f"[DRY RUN] {action_message}")
            else:
                dest_folder_path.mkdir(exist_ok=True)
                print(action_message)
                shutil.move(str(entry), str(unique_dest_path))

    print("\n✅ Organization complete!")

def get_unique_filepath(destination_path: Path) -> Path:
    if not destination_path.exists():
        return destination_path
    
    parent_folder = destination_path.parent
    original_stem = destination_path.stem
    sufffix = destination_path.suffix
    
    counter = 1
    while True:
        new_stem = f"{original_stem} ({counter}{sufffix})"
        new_path = parent_folder / new_stem
        
        if not new_path.exists():
            return new_path
        counter += 1

if __name__ == "__main__":
    IS_DRY_RUN = False
    
    organize_folder(DOWNLOADS_PATH, dry_run=IS_DRY_RUN)