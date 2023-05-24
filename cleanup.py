import os
import shutil

images = [f for f in os.listdir() if '.jpg' in f.lower()]

if images == True:
    os.mkdir('downloaded_images')
else:

    for image in images:
        new_path = 'downloaded_images/' + image
        shutil.move(image, new_path)
    
executables = [f for f in os.listdir() if '.exe' in f.lower()]

if executables == True:
    os.mkdir('exe_files')
else:
        for exe in executables:
            new_path = 'exe_files/' + exe
            shutil.move(exe, new_path)
    
pdfs = [f for f in os.listdir() if '.pdf' in f.lower()]

if pdfs == True:
    os.mkdir('downloaded_pdfs')
else:
    for pdf in pdfs:
        new_path = 'downloaded_pdfs/' + pdf
        shutil.move(pdf, new_path)
    
worddocs = [f for f in os.listdir() if '.docx' in f.lower()]

if worddocs == True:
    os.mkdir('word_documents')
else:
    for doc in worddocs:
        new_path = 'worddocs/' + doc
        shutil.move(doc, new_path)
 
worddocs = [f for f in os.listdir() if '.doc' in f.lower()]

for doc in worddocs:
    new_path = 'worddocs/' + doc
    shutil.move(doc, new_path)
    
    
