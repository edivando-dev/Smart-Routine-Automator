from pathlib import Path
import sys 

IMAGE_SUFFIXES = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg']

def get_download_path() -> Path:
    return Path.home() / 'Downloads'

# The complete, updated function

def list_files(folder_path: Path):
    """
    Lists only image files in the given folder_path based on IMAGE_SUFFIXES.
    Exits the script if the path is not a valid directory.
    """
    if not folder_path.exists() or not folder_path.is_dir():
        print(f"❌ Error: The directory '{folder_path}' does not exist or is not a folder.")
        sys.exit(1)

    print(f"🖼️  Searching for images in '{folder_path.name}':")
    print("---" * 10)
    
    found_images = False # A little flag to see if we find anything
    for entry in sorted(folder_path.iterdir()):
        # Check if the entry is a file and if its suffix is in our allowed list
        if entry.is_file() and entry.suffix.lower() in IMAGE_SUFFIXES:
            print(f"- {entry.name}")
            found_images = True # We found at least one!
            
    if not found_images:
        print("No images found with the specified extensions.")
        
    print("---" * 10)


if __name__ == "__main__":
    print("🚀 Smart Routine Automator is running!")
    
    
    downloads_folder = get_download_path()
    
    list_files(downloads_folder)
    
    print("✅ Done!")