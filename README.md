# 🧠 Smart Routine Automator

A simple yet powerful Python script to automatically organize your Downloads folder and keep it tidy.

## Features

- **Automatic Categorization**: Sorts files into predefined folders (Images, Documents, Videos, etc.) based on their extension.
- **Smart Folder Creation**: Automatically creates destination folders if they don't exist.
- **Conflict Resolution**: Safely handles duplicate filenames by appending a counter (e.g., `file (1).txt`).
- **Dry Run Mode**: Allows you to preview the changes without actually moving any files, ensuring safety.

## How to Use

1.  **Clone the repository** (or download the `main.py` file).

2.  **Set up the environment**:
    ```bash
    # Navigate to the project folder
    cd smart-routine-automator

    # Create and activate a virtual environment
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Run the script**:
    - To see a preview of the changes (recommended first):
      ```bash
      python main.py
      ```
    - To actually move the files, open `main.py` and change the `IS_DRY_RUN` variable to `False`.

## Customization

You can easily customize the folder mapping by editing the `FOLDER_MAPPING` dictionary at the top of the `main.py` file. Add or remove extensions and folders to fit your needs!