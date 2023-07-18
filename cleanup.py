#This script is made to clean up my downloads folder. 
#You drop the .py file in the dfolder you want to clean. Then run the script 
#First checks if a similar folder has been created before it makes the folder
#if it does have the folder already created, it just moves the files to that folder
#if it does not, it will create the folder and then move the files



import os
import shutil
import tkinter as tk


extensions_to_folders = {
    '.jpg': 'Images',
    '.png': 'Images',
    '.exe': 'Executables',
    '.pdf': 'PDFs',
    '.docx': 'WordDocuments',
    '.doc': 'WordDocuments',
    '.html': 'HTML',
    '.zip': 'Archives',
    '.csv': 'CSV',
    '.txt': 'TextFiles',
    '.xlsx': 'Spreadsheets',
    '.pptx': 'Presentations',
    '.mp3': 'Music',
    '.mp4': 'Videos',
    '.py': 'PythonScripts',
    '.java': 'JavaFiles',
    '.cpp': 'C++Files',
    '.js': 'JavaScriptFiles',
    '.css': 'CSSFiles',
    '.php': 'PHPFiles',
    '.json': 'JSONFiles',
    '.xml': 'XMLFiles',
    '.sql': 'SQLFiles',
    '.gif': 'GIFFiles',
    '.ico': 'IconFiles',
    '.svg': 'SVGFiles'
}

excluded_files = ['cleanup.exe', 'cleanup.py']

def move_files_to_folder(folder, extensions):
    files = [f for f in os.listdir() if any(ext in f.lower() for ext in extensions) and f not in excluded_files]

    if not files:
        return

    if not os.path.isdir(folder):
        os.mkdir(folder)
        print(f'Created {folder} directory')

    for file in files:
        new_path = f'{folder}/{file}'
        shutil.move(file, new_path)
        print(f'{file} is now moved to {new_path}')

def letsClean():
    for extension, folder in extensions_to_folders.items():
        move_files_to_folder(folder, [extension])

def clean_files():
    letsClean()
    print('Cleanup complete.')

def create_gui():
    top = tk.Tk()
    top.geometry("200x125")
    button = tk.Button(top, text="Clean", command=clean_files, borderwidth=2)
    button.place(x=80, y=45)
    top.mainloop()

create_gui()
