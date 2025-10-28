from pathlib import Path
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import shutil 
#from datetime import datetime, timedelta


#DOWNLOADS_PATH = Path.home() / 'Downloads'
WATCH_PATH = Path.home() / 'Downloads'

#DAYS_TO_ARCHIVE = 30


FOLDER_MAPPING = {
    'Images': ['.jpeg', '.jpg', '.png', '.gif', '.bmp', '.svg'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx', '.md'],
    'Audio': ['.mp3', '.wav', '.aac'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Executables': ['.exe', '.msi'],
}

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("organizer.log"),
        logging.StreamHandler()
    ]
)

def get_destination_folder(suffix: str) -> str:
    for folder_name, suffixes in FOLDER_MAPPING.items():
        if suffix.lower() in suffixes:
            return folder_name
    return 'Others' 

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
        
class OrganizationHandler(FileSystemEventHandler):
    """A custom event handler for watchdog that organizes new files."""

    def on_created(self, event):
        """
        This method is called automatically by watchdog when a new file is created.
        'event.src_path' is the full path to the newly created file.
        """
        
        if not event.is_directory:
            time.sleep(1) 
            
            new_file_path = Path(event.src_path)

            
            if new_file_path.name == "watcher.log":
                return
            
            logging.info(f"🚨 New file detected: {new_file_path.name}")
            
            
            dest_folder_name = get_destination_folder(new_file_path.suffix)
            dest_folder_path = WATCH_PATH / dest_folder_name
            dest_folder_path.mkdir(exist_ok=True)
            
            unique_dest_path = get_unique_filepath(dest_folder_path / new_file_path.name)
            
            try:
                shutil.move(str(new_file_path), str(unique_dest_path))
                logging.info(f"✅ Moved '{new_file_path.name}' -> '{dest_folder_name}/'")
            except Exception as e:
                logging.error(f"Failed to move {new_file_path.name}. Reason: {e}")

if __name__ == "__main__":
    logging.info(f"👀 Starting to watch folder: {WATCH_PATH}")
    
    
    event_handler = OrganizationHandler()
    observer = Observer()
    observer.schedule(event_handler, str(WATCH_PATH), recursive=False)
    
    
    observer.start()
    logging.info("🚀 Watchdog is now running in the background. Press Ctrl+C to stop.")
    
    try:
        
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        logging.info("🛑 Watchdog stopped by user.")
        observer.stop()
    
    observer.join() 