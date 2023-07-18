#This script is made to clean up my downloads folder. 
#You drop the .py file in the dfolder you want to clean. Then run the script 
#First checks if a similar folder has been created before it makes the folder
#if it does have the folder already created, it just moves the files to that folder
#if it does not, it will create the folder and then move the files



import os
import shutil
import tkinter as tk
from tkinter import messagebox, filedialog


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

def delete_files(files):
    failed_deletions = []
    for file in files:
        try:
            os.remove(file)
            print(f'{file} is deleted')
        except PermissionError:
            print(f'Permission denied: {file}')
            failed_deletions.append(file)
        except OSError:
            print(f'Failed to delete: {file}')
            failed_deletions.append(file)
    
    return failed_deletions

def list_files():
    file_text.delete(0, tk.END)  # Clear previous content
    files = os.listdir()
    for file in files:
        file_text.insert(tk.END, file)

def clean_files():
    letsClean()
    messagebox.showinfo("Cleanup", "Cleanup complete.")

def letsClean():
    for extension, folder in extensions_to_folders.items():
        move_files_to_folder(folder, [extension])

def delete_selected_files():
    selected_files = file_text.curselection()
    files_to_delete = [file_text.get(index) for index in selected_files]
    if files_to_delete:
        confirm = messagebox.askyesno("Confirmation", "Are you sure you want to delete the selected files?")
        if confirm:
            failed_deletions = delete_files(files_to_delete)
            if failed_deletions:
                failed_message = "Failed to delete the following files:\n\n" + "\n".join(failed_deletions)
                messagebox.showwarning("Deletion Failed", failed_message)
            else:
                messagebox.showinfo("Deletion", "Selected files deleted successfully.")
            list_files()

def create_gui():
    global file_text  # Access the global file_text variable
    top = tk.Tk()
    top.geometry("300x300")

    list_button = tk.Button(top, text="List Files", command=list_files)
    list_button.pack(pady=10)

    file_text = tk.Listbox(top, width=40, height=10, selectmode=tk.MULTIPLE)
    file_text.pack()

    delete_button = tk.Button(top, text="Delete Selected Files", command=delete_selected_files)
    delete_button.pack(pady=10)

    clean_button = tk.Button(top, text="Clean", command=clean_files)
    clean_button.pack(pady=10)

    top.mainloop()

create_gui()

