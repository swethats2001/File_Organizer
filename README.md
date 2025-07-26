# 📁 File Organizer using Python

A simple Python script to automatically organize files in a folder by moving them into categorized subfolders such as **Documents**, **Images**, **Videos**, and **Others** based on file extensions.

---

## 📌 Features

- 📄 Automatically sorts files into folders based on type
- 🛡️ Built-in error handling using `try-except`
- 🧪 Easy to test, modify, and extend
- 🗂️ Creates categorized folders if they don't exist

---

## 🚀 How It Works

1. The user enters the **path of the folder** they want to organize.
2. The script checks all files in the folder (excluding directories).
3. Based on file extension, each file is moved into one of the following:
   - `Documents`
   - `Images`
   - `Videos`
   - `Others`
4. Subfolders are automatically created if they don't exist.
5. Files are moved safely using `shutil`.

---

## 🧠 File Categories

| Category   | File Extensions |
|------------|-----------------|
| Documents  | `.pdf`, `.doc`, `.docx`, `.txt`, `.ppt`, `.pptx`, `.xls`, `.xlsx` |
| Images     | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`, `.avif` |
| Videos     | `.mp4`, `.avi`, `.mov`, `.mkv`, `.flv`, `.wmv`, `.mpg`, `.mpeg` |
| Others     | Anything not listed above |

---

## 🛠️ Requirements

- Python 3.x
- No additional libraries required (uses built-in `os` and `shutil`)

---

## 📂 Folder Structure After Organizing

📁 Target Folder
├── 📁 Documents
├── 📁 Images
├── 📁 Videos
└── 📁 Others

Author
Swetha T S
