import os
import shutil


if os.path.isdir('downloaded_images/') == False:


    images = [f for f in os.listdir() if '.jpg' in f.lower()]
        
    os.mkdir('downloaded_images')
        
    for image in images:
        new_path = 'downloaded_images/' + image
        shutil.move(image, new_path)
    
if os.path.isdir('exe_files/') == False:

    executables = [f for f in os.listdir() if '.exe' in f.lower()]
    
    os.mkdir('exe_files')
    
    for exe in executables:
        new_path = 'exe_files/' + exe
        shutil.move(exe, new_path)
    
if os.path.isdir('downloaded_pdfs/') == False:
    
    pdfs = [f for f in os.listdir() if '.pdf' in f.lower()]
    
    os.mkdir('downloaded_pdfs')
    
    for pdf in pdfs:
        new_path = 'downloaded_pdfs/' + pdf
        shutil.move(pdf, new_path)
    
if os.path.isdir('word_documents/') == False:
    
    worddocs = [f for f in os.listdir() if '.docx' in f.lower()]
    
    os.mkdir('word_documents')
    
    for doc in worddocs:
        new_path = 'worddocs/' + doc
        shutil.move(doc, new_path)
     
    worddocs = [f for f in os.listdir() if '.doc' in f.lower()]
    
    for doc in worddocs:
        new_path = 'worddocs/' + doc
        shutil.move(doc, new_path)
    
    
