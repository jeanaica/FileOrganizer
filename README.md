# File Organizer by Month

This Python script organizes files in a specified folder by creating subfolders named after the month in which each file was created. The files are then moved into their respective month-named folders.

## Features

- Organizes files based on their creation date.
- Automatically creates folders named after the month (e.g., "January", "February", etc.).
- Moves files into their respective month folders.

## Requirements

- Python 3.x

## Usage

1. **Clone the Repository:**

   Clone this repository to your local machine using:

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd your-repo-name
   ```

3. **Run the Script:**

   Execute the script by running:

   ```bash
   python organize_files_by_month.py
   ```

4. **Provide the Folder Path:**

   When prompted, enter the full path to the folder containing the files you want to organize. The script will handle the rest.

## Example

Suppose you have the following files in a folder:

```
/path/to/your/files/
├── photo1.jpg (created in January)
├── video1.mov (created in February)
├── document1.pdf (created in January)
└── picture.png (created in March)
```

After running the script, the folder will be organized as:

```
/path/to/your/files/
├── January/
│   ├── photo1.jpg
│   └── document1.pdf
├── February/
│   └── video1.mov
└── March/
    └── picture.png
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
