'''
Write a Python script that scans a given directory recursively, finds all files larger than 100MB, and 
logs their paths and sizes to a file called large_files.log. Also, ignore files with .log and .tmp extensions.
'''

'''
The os library in Python is a standard library module that provides a way to interact with the operating system.
Working with files:- creating, reading, renaming, deleting & directories. Getting env-var, running system commnds, handling file paths & manage process & permissions.

'''
import os

def find_large_files(directory,log_file = 'large_files.log', max_size_mb = 100 ):
    max_size_bytes = max_size_mb * 1024*1024
     
    with open(log_file, 'w') as log:
       for root,dirs,files in os.walk(directory):
         for file in files:
           if file.endswith('.log', '.tmp'):
             continue
           
           file_path = os.path.join(root,file)
           try:
             size = os.path.getsize(file_path)
             if size > max_size_bytes:
               log.write(f"{file_path} - {round(size/ (1024*1024), 2)} MB\n")
           except FileNotFoundError:
              continue
           
           
find_large_files('/var/log')  
             


             
          
