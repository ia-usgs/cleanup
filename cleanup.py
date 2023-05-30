#This script is made to clean up my downloads folder. 
#You drop the .py file in the dfolder you want to clean. Then run the script 
#First checks if a similar folder has been created before it makes the folder
#if it does have the folder already created, it just moves the files to that folder
#if it does not, it will create the folder and then move the files



import os, os.path
import shutil


if os.path.isdir('downloaded_images/') == False:


    images = [f for f in os.listdir() if '.jpg' in f.lower()]
        
    os.mkdir('downloaded_images')
        
    for image in images:
        new_path = 'downloaded_images/' + image
        shutil.move(image, new_path)
        
    images2 = [f for f in os.listdir() if '.png' in f.lower()]
        
    for image in images2:
        new_path = 'downloaded_images/' + image
        shutil.move(image, new_path)
        
    print('Created Images Directory')
    
if os.path.isdir('exe_files/') == False:

    executables = [f for f in os.listdir() if '.exe' in f.lower()]
    
    os.mkdir('exe_files')
    
    for exe in executables:
        new_path = 'exe_files/' + exe
        shutil.move(exe, new_path)
    print('Created Exe Directory')
    
if os.path.isdir('downloaded_pdfs/') == False:
    
    pdfs = [f for f in os.listdir() if '.pdf' in f.lower()]
    
    os.mkdir('downloaded_pdfs')
    
    for pdf in pdfs:
        new_path = 'downloaded_pdfs/' + pdf
        shutil.move(pdf, new_path)
    print('Created PDFS Directory')
    
if os.path.isdir('word_documents/') == False:
    
    worddocs = [f for f in os.listdir() if '.docx' in f.lower()]
    
    os.mkdir('word_documents')
    
    for doc in worddocs:
        new_path = 'word_documents/' + doc
        shutil.move(doc, new_path)
    
     
    worddocs2 = [f for f in os.listdir() if '.doc' in f.lower()]
    
    for doc in worddocs2:
        new_path = 'word_documents/' + doc
        shutil.move(doc, new_path)
    print('Created WORD DOCS Directory')
    
else:
    
    
    images = [f for f in os.listdir() if '.jpg' in f.lower()]
    
    for image in images:
        new_path = 'downloaded_images/' + image
        shutil.move(image, new_path)
        print("Image is now moved to " + new_path + "\n" )
        
    images2 = [f for f in os.listdir() if '.png' in f.lower()]
        
    for image in images2:
        new_path = 'downloaded_images/' + image
        shutil.move(image, new_path)
        print("Image is now moved to " + new_path + "\n" )

    
    executables = [f for f in os.listdir() if '.exe' in f.lower()]
    
    for exe in executables:
        new_path = 'exe_files/' + exe
        shutil.move(exe, new_path)
        DIR = 'exe_files/'
        print("Exe is now moved to " + new_path + "\n")


        
    pdfs = [f for f in os.listdir() if '.pdf' in f.lower()]
    
    for pdf in pdfs:
        new_path = 'downloaded_pdfs/' + pdf
        shutil.move(pdf, new_path)
        print("PDF is now moved to " + new_path + "\n" )
        
    
    worddocs = [f for f in os.listdir() if '.docx' in f.lower()]
    
    for doc in worddocs:
        new_path = 'word_documents/' + doc
        shutil.move(doc, new_path)
        print("Doc is now moved to " + new_path + "\n" )
    
     
    worddocs2 = [f for f in os.listdir() if '.doc' in f.lower()]
    
    for doc in worddocs2:
        new_path = 'word_documents/' + doc
        shutil.move(doc, new_path)
        print("Doc is now moved to " + new_path + "\n" )
